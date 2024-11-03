$(document).ready(function() {
    $('.list-group-item').click(function() {
        var sectionId = $(this).data('id');
        var isLocked = $(this).data('locked');

        if (isLocked) {
            alert('This section is locked.');
            return;
        }

        $.ajax({
            url: '/get_section_content',
            type: 'GET',
            data: { section_id: sectionId },
            success: function(response) {
                $('#main-content').html(`
                    <h2>${response.title}</h2>
                    <div class="card">
                        <div class="card-body">
                            <p>${response.text_content}</p>
                        </div>
                    </div>
                `);
            },
            error: function(error) {
                console.log('Error:', error);
            }
        });
    });
});

// Function to submit an answer for the current quiz question
function submitAnswer() {
    let selectedAnswer = document.querySelector('input[name="answer"]:checked'); // Get the selected answer
    if (!selectedAnswer) {
        alert("Please select an answer."); // If no answer is selected, show an alert
        return;
    }

    let form = document.getElementById("quiz-form"); // Get the quiz form element
    let formData = new FormData(form); // Create a FormData object from the form

    // Create a data object with the necessary information to submit
    let data = {
        question_id: formData.get("question_id"),
        selected_answer_id: selectedAnswer.value,
        quiz_id: formData.get("quiz_id"),
        question_index: formData.get("question_index"),
        total_questions: formData.get("total_questions")
    };

    console.log("Data to be sent:", data); // Log the data to be sent for debugging

    // Use the fetch API to send the data to the server
    fetch("/submit_answer", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data) // Send the data as a JSON string
    })
    .then(response => {
        console.log("Raw response received:", response); // Log the raw response for debugging
        return response.json(); // Parse the response as JSON
    })
    .then(data => {
        console.log("JSON response received:", data); // Log the JSON response for debugging
        if (data.redirect_url) {
            console.log("Redirecting to:", data.redirect_url); // Log the redirect URL
            alert(data.message); // Show an alert with the message before redirecting
            window.location.href = data.redirect_url; // Redirect to the provided URL
        } else if (data.next_question_url) {
            console.log("Loading next question:", data.next_question_url); // Log the next question URL
            window.location.href = data.next_question_url; // Redirect to the next question
        } else {
            console.error("No redirect or next question URL in response."); // Log an error if no URLs are provided
        }
    })
    .catch(error => console.error("Error:", error)); // Catch and log any errors
}



$(document).ready(function() {
    setTimeout(function() {
        $(".flash-message").alert('close');
    }, 5000);
});

document.addEventListener('DOMContentLoaded', function() {
    const chapterButtons = document.querySelectorAll('.chapter-button');

    chapterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const chapterId = this.getAttribute('data-chapter-id');
            fetch('/update_times_visited', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ chapter_id: chapterId })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    console.log('TimesVisited updated successfully');
                } else {
                    console.error('Failed to update TimesVisited');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });
});
