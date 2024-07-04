document.addEventListener('DOMContentLoaded', function() {
    var loginForm = document.getElementById('loginForm');
    loginForm.addEventListener('submit', function(event) {
        event.preventDefault();  
        var usernameInput = document.getElementById('username');
        var passwordInput = document.getElementById('password');
        var errorMessage = document.getElementById('error-message');
        
        var username = usernameInput.value.trim();
        var password = passwordInput.value.trim();


        
        var usernamePattern = /^[a-zA-Z0-9_]{3,16}$/; 
        var passwordPattern = /^(?=.*\d)(?=.*[a-zA-Z]).{8,}$/; 

    
        if (!usernamePattern.test(username)) {
            errorMessage.textContent = 'Invalid username .';
            return;
        }

    
        if (!passwordPattern.test(password)) {
            errorMessage.textContent = 'Invalid password .';
            return;
        
        }

        errorMessage.textContent = '';

        var formData = new FormData(loginForm);  
        var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;


        $.ajax({
            type: 'POST',
            url: '',  
            data: formData,
            headers: {
                'X-CSRFToken': csrfToken
            },
            processData: false,
            contentType: false,
            success: function(response) {
                if (response.success) {
                   
                    window.location.href = '/dashboard/';
                } else {
               
                    if (response.errors) {
                        $('#error-message').text(response.errors);  
                    } else {
                        $('#error-message').text('Invalid username or password.');
                    }
                }
            },
            error: function(xhr, status, error) {  
                errorMessage.textContent = 'Error occurred .Please try again.';
            }
        });
    });
});