from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, session
import datetime
from flask_login import login_required, current_user
from .models import Chapter, Section, Quiz, QuizQuestion, Question, Answer, Attempt, AttemptAnswer, UserChapter
from . import db
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
from scipy.stats import norm

# Blueprint for views
views = Blueprint('views', __name__)

# Function to fetch attempt data for the current user
def fetch_attempt_data():
    attempts = Attempt.query.filter_by(user_id=current_user.id).all()
    times_to_complete = [attempt.time_to_complete for attempt in attempts]
    percentages_correct = [attempt.percentage_correct for attempt in attempts]
    return times_to_complete, percentages_correct

# Route to show user progress
@views.route('/progress')
@login_required
def show_progress():
    times_to_complete, percentages_correct = fetch_attempt_data()

    if len(times_to_complete) == 0 or len(percentages_correct) == 0:
        return "No data available to display progress."

    # Calculate mean and standard deviation
    time_mean = np.mean(times_to_complete)
    time_std = np.std(times_to_complete)
    percentage_mean = np.mean(percentages_correct)
    percentage_std = np.std(percentages_correct)

    # Create figure for plotting
    fig, ax = plt.subplots(2, 1, figsize=(10, 12))

    # Plot Time to Complete
    time_x = np.linspace(min(times_to_complete), max(times_to_complete), 100)
    time_pdf = norm.pdf(time_x, time_mean, time_std)
    ax[0].hist(times_to_complete, bins=10, density=False, alpha=0.6, color='g', edgecolor='black')
    ax[0].plot(time_x, time_pdf * len(times_to_complete) * (max(times_to_complete) - min(times_to_complete)) / 10, 'r', label=f'Normal Distribution\n$\mu={time_mean:.2f}$\n$\sigma={time_std:.2f}$')
    ax[0].set_title('Distribution of Time to Complete')
    ax[0].set_xlabel('Time to Complete (seconds)')
    ax[0].set_ylabel('Count')
    ax[0].legend()

    # Plot Percentage Correct
    percentage_x = np.linspace(min(percentages_correct), max(percentages_correct), 100)
    percentage_pdf = norm.pdf(percentage_x, percentage_mean, percentage_std)
    ax[1].hist(percentages_correct, bins=10, density=False, alpha=0.6, color='b', edgecolor='black')
    ax[1].plot(percentage_x, percentage_pdf * len(percentages_correct) * (max(percentages_correct) - min(percentages_correct)) / 10, 'r', label=f'Normal Distribution\n$\mu={percentage_mean:.2f}$\n$\sigma={percentage_std:.2f}$')
    ax[1].set_title('Distribution of Percentage Correct')
    ax[1].set_xlabel('Percentage Correct')
    ax[1].set_ylabel('Count')
    ax[1].legend()

    plt.tight_layout()

    # Save the plot to a bytes object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template('progress.html', plot_url=plot_url)

# Route to update times visited for a chapter
@views.route('/update_times_visited', methods=['POST'])
@login_required
def update_times_visited():
    data = request.get_json()
    chapter_id = data.get('chapter_id')

    if not chapter_id:
        return jsonify({'success': False, 'message': 'Chapter ID not provided'}), 400

    user_chapter = UserChapter.query.filter_by(user_id=current_user.id, chapter_id=chapter_id).first()

    if user_chapter:
        user_chapter.times_visited += 1
    else:
        user_chapter = UserChapter(user_id=current_user.id, chapter_id=chapter_id, times_visited=1)
        db.session.add(user_chapter)

    db.session.commit()
    return jsonify({'success': True})

# Route to render the home page
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    chapters = Chapter.query.all()  # Query all chapters from the database
    sections = Section.query.all()  # Query all sections from the database
    quizzes = Quiz.query.all()  # Query all quizzes from the database
    return render_template("home.html", user=current_user, chapters=chapters, sections=sections, quizzes=quizzes, check_failed_attempts=check_failed_attempts)

# Route to get section content via AJAX
@views.route('/get_section_content', methods=['GET'])
def get_section_content():
    section_id = request.args.get('section_id')
    section = Section.query.get(section_id)
    if section:
        return jsonify({
            'title': section.title,
            'text_content': section.text_content
        })
    else:
        return jsonify({'error': 'Section not found'}), 404

# Route to load a quiz for a chapter
@views.route('/chapter/<int:chapter_id>/quiz')
def load_quiz(chapter_id):
    quiz = Quiz.query.filter_by(chapter_id=chapter_id).first()
    if not quiz:
        return "Quiz not found", 404

    first_question = QuizQuestion.query.filter_by(quiz_id=quiz.id).first()
    if not first_question:
        return "No questions found for this quiz", 404

    # Initialize attempt session
    if 'attempt' not in session:
        attempt = Attempt(
            datetime=datetime.datetime.now(),
            percentage_correct=0,
            time_to_complete=0,
            user_id=current_user.id,
            quiz_id=quiz.id
        )
        db.session.add(attempt)
        db.session.commit()
        session['attempt'] = {
            'attempt_id': attempt.id,
            'quiz_id': quiz.id,
            'start_time': datetime.datetime.now().isoformat(),
            'correct_answers': 0,
            'latest_question_index': 1  # Initialize with the first question
        }
    else:
        attempt = Attempt.query.get(session['attempt']['attempt_id'])
        # print(f"Resuming attempt with ID: {attempt.id}")

    return redirect(url_for('views.load_question', quiz_id=quiz.id, question_index=1))

# Route to load a specific question in a quiz
@views.route('/quiz/<int:quiz_id>/question/<int:question_index>')
def load_question(quiz_id, question_index):
    quiz = Quiz.query.get(quiz_id)
    if not quiz:
        return "Quiz not found", 404

    quiz_questions = QuizQuestion.query.filter_by(quiz_id=quiz_id).all()
    if question_index < 1 or question_index > len(quiz_questions):
        return "Question not found", 404

    current_question = quiz_questions[question_index - 1]
    question = Question.query.get(current_question.question_id)
    answers = Answer.query.filter_by(question_id=current_question.question_id).all()

    # Enforce navigation rules
    if 'attempt' in session:
        attempt_id = session['attempt']['attempt_id']
        attempted_questions = AttemptAnswer.query.filter_by(attempt_id=attempt_id).all()
        if len(attempted_questions) >= question_index:
            flash("You cannot go back to a previous question.", "warning")
            return redirect(url_for('views.load_question', quiz_id=quiz_id, question_index=len(attempted_questions) + 1))

    return render_template("quiz_question.html", quiz=quiz, question=question, answers=answers, question_index=question_index, total_questions=len(quiz_questions))

# Route to handle answer submission
import traceback

@views.route('/submit_answer', methods=['POST'])
def submit_answer():
    try:
        data = request.get_json()
        print("Data received:", data)

        question_id = int(data['question_id'])
        selected_answer_id = int(data['selected_answer_id'])
        quiz_id = int(data['quiz_id'])
        question_index = int(data['question_index'])
        total_questions = int(data['total_questions'])

        print(f"Question ID: {question_id}, Selected Answer ID: {selected_answer_id}, Quiz ID: {quiz_id}, Question Index: {question_index}")

        answer = Answer.query.get(selected_answer_id)
        if not answer:
            raise Exception("Answer not found")
        correct = answer.correct
        print(f"Is Correct: {correct}")

        # Increment correct answers if the selected answer is correct
        if correct:
            session['attempt']['correct_answers'] += 1
            # Reassign the session to ensure it updates correctly
            session.modified = True

        attempt = Attempt.query.get(session['attempt']['attempt_id'])
        if attempt is None:
            raise Exception("Attempt not found in session")
        print(f"Existing attempt found with ID: {attempt.id}")

        attempt_answer = AttemptAnswer(
            attempt_id=attempt.id,
            question_id=question_id,
            answer_id=selected_answer_id  # Use the selected answer ID
        )
        db.session.add(attempt_answer)
        db.session.commit()
        print(f"Attempt answer recorded with ID: {attempt_answer.id}")

        if question_index == total_questions:
            # Calculate the score and time to complete
            correct_percentage = (session['attempt']['correct_answers'] / total_questions) * 100
            print(f"Correct answers: {session['attempt']['correct_answers']}")
            print(f"Total questions: {total_questions}")
            start_time = datetime.datetime.fromisoformat(session['attempt']['start_time'])
            time_to_complete = (datetime.datetime.now() - start_time).total_seconds()

            attempt.percentage_correct = correct_percentage
            attempt.time_to_complete = int(time_to_complete)
            db.session.commit()
            print(f"Quiz completed with {correct_percentage}% correct and {time_to_complete} seconds to complete")

            # Clear the attempt session
            session.pop('attempt', None)

            if correct_percentage >= 75:
                print("User passed the quiz")
                return jsonify({"redirect_url": url_for('views.home'), "message": "You passed the quiz!"})
            else:
                print("User did not pass the quiz")
                return jsonify({"redirect_url": url_for('views.home'), "message": "You did not pass the quiz."})

        # Ensure the next question URL is correctly generated
        next_question_url = url_for('views.load_question', quiz_id=quiz_id, question_index=question_index + 1)
        print(f"Next question URL: {next_question_url}")
        return jsonify({"next_question_url": next_question_url})

    except Exception as e:
        print("Error:", str(e))
        traceback.print_exc()  # Print the full traceback for debugging
        return jsonify({"message": "An error occurred", "error": str(e)}), 500


# Function to check the number of failed attempts by a user
def check_failed_attempts(user_id):
    failed_attempts = Attempt.query.filter_by(user_id=user_id).filter(Attempt.percentage_correct < 75).count()
    return failed_attempts >= 4

# Route to load the general quiz
@views.route('/general_quiz')
@login_required
def general_quiz():
    # Get the last quiz ID and calculate the general quiz ID
    last_quiz = Quiz.query.order_by(Quiz.id.desc()).first()
    general_quiz_id = last_quiz.id + 10 if last_quiz else 10

    # Insert the general quiz into the database if it doesn't already exist
    general_quiz = Quiz.query.get(general_quiz_id)
    if not general_quiz:
        general_quiz = Quiz(
            id=general_quiz_id,
            percentage_to_pass=75,
            chapter_id=6  # Assuming chapter ID 6 is for the general quiz
        )
        db.session.add(general_quiz)
        db.session.commit()

    if check_failed_attempts(current_user.id):
        questions = Question.query.filter(Question.difficulty.in_(['Easy', 'Medium'])).order_by(db.func.random()).limit(8).all()
    else:
        questions = Question.query.order_by(db.func.random()).limit(8).all()

    # Insert quiz questions into the database
    for question in questions:
        quiz_question = QuizQuestion(
            quiz_id=general_quiz_id,
            question_id=question.id
        )
        db.session.add(quiz_question)
    db.session.commit()

    # Initialize attempt session for the general quiz
    if 'attempt' not in session:
        attempt = Attempt(
            datetime=datetime.datetime.now(),
            percentage_correct=0,
            time_to_complete=0,
            user_id=current_user.id,
            quiz_id=general_quiz_id
        )
        db.session.add(attempt)
        db.session.commit()
        session['attempt'] = {
            'attempt_id': attempt.id,
            'start_time': datetime.datetime.now().isoformat(),
            'correct_answers': 0
        }
    else:
        attempt = Attempt.query.get(session['attempt']['attempt_id'])
        # print(f"Resuming general attempt with ID: {attempt.id}")

    return redirect(url_for('views.load_question', quiz_id=general_quiz_id, question_index=1))
