from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# User model representing the users of the system
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each user
    username = db.Column(db.String(255), unique=True, nullable=False)  # Username, must be unique
    email = db.Column(db.String(255), unique=True, nullable=False)  # Email, must be unique
    password = db.Column(db.String(255), nullable=False)  # Password
    attempts = db.relationship('Attempt', backref='user', lazy=True)  # Relationship to attempts
    user_chapters = db.relationship('UserChapter', backref='user', lazy=True)  # Relationship to user chapters

# Chapter model representing chapters in the course
class Chapter(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each chapter
    number = db.Column(db.Integer, nullable=False)  # Chapter number
    title = db.Column(db.String(255), nullable=False)  # Chapter title
    sections = db.relationship('Section', backref='chapter', lazy=True)  # Relationship to sections
    quizzes = db.relationship('Quiz', backref='chapter', lazy=True)  # Relationship to quizzes
    user_chapters = db.relationship('UserChapter', backref='chapter', lazy=True)  # Relationship to user chapters

# Section model representing sections within a chapter
class Section(db.Model):
    __tablename__ = 'sections'  # Ensure the table name matches your schema

    id = db.Column('ID', db.Integer, primary_key=True)  # Unique ID for each section
    chapter_id = db.Column('ChapterID', db.Integer, db.ForeignKey('chapter.id'), nullable=False)  # Foreign key to chapter
    title = db.Column('Title', db.String(255), nullable=False)  # Section title
    text_content = db.Column('TextContent', db.Text, nullable=False)  # Section content

# Quiz model representing quizzes in the course
class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each quiz
    percentage_to_pass = db.Column('PercentageToPass', db.Float, nullable=False)  # Passing percentage
    chapter_id = db.Column('ChapterID', db.Integer, db.ForeignKey('chapter.id'), nullable=False)  # Foreign key to chapter
    quiz_questions = db.relationship('QuizQuestion', backref='quiz', lazy=True)  # Relationship to quiz questions
    attempts = db.relationship('Attempt', backref='quiz', lazy=True)  # Relationship to attempts

# QuizQuestion model representing the questions in a quiz
class QuizQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each quiz question
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)  # Foreign key to quiz
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)  # Foreign key to question

# Question model representing the questions in the system
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each question
    text = db.Column(db.Text, nullable=False)  # Question text
    difficulty = db.Column(db.String(50))  # Difficulty level of the question
    answers = db.relationship('Answer', backref='question', lazy=True)  # Relationship to answers
    quiz_questions = db.relationship('QuizQuestion', backref='question', lazy=True)  # Relationship to quiz questions

# Answer model representing possible answers to a question
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each answer
    correct = db.Column(db.Boolean, nullable=False)  # Correct answer flag
    text = db.Column(db.Text, nullable=False)  # Answer text
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)  # Foreign key to question

# Attempt model representing attempts by users to complete quizzes
class Attempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each attempt
    datetime = db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False, name='DateTime')  # Attempt datetime
    percentage_correct = db.Column(db.Float, nullable=False, name='PercentageCorrect')  # Percentage of correct answers
    time_to_complete = db.Column(db.Integer, nullable=False, name='TimeToComplete')  # Time taken to complete the quiz
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, name='UserID')  # Foreign key to user
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False, name='QuizID')  # Foreign key to quiz
    attempt_answers = db.relationship('AttemptAnswer', backref='attempt', lazy=True)  # Relationship to attempt answers

# AttemptAnswer model representing the answers given in an attempt
class AttemptAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each attempt answer
    attempt_id = db.Column(db.Integer, db.ForeignKey('attempt.id'), nullable=False)  # Foreign key to attempt
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)  # Foreign key to question
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id'), nullable=False)  # Foreign key to answer

# UserChapter model representing the chapters visited by users
class UserChapter(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each user-chapter relationship
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, name='UserID')  # Foreign key to user
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapter.id'), nullable=False, name='ChapterID')  # Foreign key to chapter
    times_visited = db.Column(db.Integer, nullable=False, name='TimesVisited')  # Number of times the chapter was visited
