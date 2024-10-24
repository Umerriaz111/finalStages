function sendMessage() {
    const messageBox = document.getElementById('message-box');
    const message = messageBox.value.trim();

    if (message === "") return;

    // Add the user's message to the chat window
    const chatWindow = document.getElementById('chat-window');

    // Create a container for user message and YOU circle
    const userContainer = document.createElement('div');
    userContainer.classList.add('user-container');

    // Create the user message div
    const userMessageDiv = document.createElement('div');
    userMessageDiv.classList.add('user-message');

    const messageText = document.createElement('p');
    messageText.innerText = message;
    // Apply the scrollable box for long responses to the p element
    messageText.style.maxHeight = '200px';  // Set the max height for the response text
    messageText.style.overflowY = 'auto';
    userMessageDiv.appendChild(messageText);

    // Create the time element
    const currentTime = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    const userTimeSpan = document.createElement('span');
    userTimeSpan.classList.add('time');
    userTimeSpan.innerText = currentTime;

    // Append time to the message div
    userMessageDiv.appendChild(userTimeSpan);

    // Create the YOU circle
    const youCircle = document.createElement('div');
    youCircle.classList.add('you-circle');
    youCircle.innerText = 'YOU';

    // Add the message and YOU circle to the container
    userContainer.appendChild(userMessageDiv);
    userContainer.appendChild(youCircle);

    // Append the entire container to the chat window
    chatWindow.appendChild(userContainer);
    chatWindow.scrollTop = chatWindow.scrollHeight;

    // Send the user's message to the Flask backend
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: message })
    })
        .then(response => response.json())
        .then(data => {
            // Create the support message container
            const supportMessageDiv = document.createElement('div');
            supportMessageDiv.classList.add('chat-message', 'support');

            // Create a div for the response content (scrollable)
            const supportMessageText = document.createElement('p');
            supportMessageText.innerText = data.response; // Backend response

            // Apply the scrollable box for long responses to the p element
            supportMessageText.style.maxHeight = '200px';  // Set the max height for the response text
            supportMessageText.style.overflowY = 'auto';   // Add vertical scrolling

            supportMessageDiv.appendChild(supportMessageText);

            const supportTimeSpan = document.createElement('span');
            supportTimeSpan.classList.add('time');
            supportTimeSpan.innerText = currentTime; // Using the same time for both
            supportMessageDiv.appendChild(supportTimeSpan);

            chatWindow.appendChild(supportMessageDiv);
            chatWindow.scrollTop = chatWindow.scrollHeight;
        })
        .catch(error => console.error('Error:', error));

    // Clear the input box
    messageBox.value = '';
}

function toggleSubscriptionForm() {
    const form = document.getElementById('subscription-form');
    form.style.display = form.style.display === 'none' ? 'block' : 'none';
}

function submitSubscription() {
    const name = document.getElementById('sub-name').value.trim();
    const email = document.getElementById('sub-email').value.trim();
    const phone = document.getElementById('sub-phone').value.trim();

    // Name validation: Should not start with a number and must start with characters
    const nameRegex = /^[A-Za-z]{4,}\s?[A-Za-z0-9]*$/;
    if (!nameRegex.test(name)) {
        alert("Invalid name. Name should start with letters and may contain numbers.");
        return;
    }

    // Email validation: Must start with letters, minimum 5 characters before @
    // Allows letters, numbers, periods, and underscores, and specific domains
    const emailRegex = /^[a-zA-Z][a-zA-Z0-9._-]{4,}@(gmail|hotmail|yahoo)\.com$/;
    if (!emailRegex.test(email)) {
        alert("Invalid email format. Email should start with a letter and have at least 5 characters before '@'. Only @gmail.com, @hotmail.com, or @yahoo.com domains are allowed.");
        return;
    }



    // Phone number validation: Should start with a valid country code followed by 10-14 digits, allowing optional spaces
    const phoneRegex = /^\+([0-9]{1,3})\s?[0-9]{3}\s?[0-9]{7}$/;
    if (!phoneRegex.test(phone)) {
        alert("Invalid phone number. Please enter a valid phone number starting with a country code (e.g., +92, +91) and the correct number of digits.");
        return;
    }


    // Send subscription data to the Flask backend
    fetch('/subscribe', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: name, email: email, phone: phone })
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log("Subscription response:", data); // Log the response from the backend
            alert("Thank you for subscribing!");

            // Clear the form
            document.getElementById('subscription-form').style.display = 'none';
            document.getElementById('sub-name').value = '';
            document.getElementById('sub-email').value = '';
            document.getElementById('sub-phone').value = '';
        })
        .catch(error => {
            console.error('Error:', error);
            alert("There was an issue with your subscription. Please try again later.");
        });
}

function toggleSubscriptionForm2() {
    const form = document.getElementById('subscription-form2');
    form.style.display = form.style.display === 'none' ? 'block' : 'none';
}

function submitSubscription2() {
    const name = document.getElementById('sub-name2').value;
    const email = document.getElementById('sub-email2').value;
    const phone = document.getElementById('sub-phone2').value;

    // Name validation: Should not start with a number and must start with characters
    const nameRegex = /^[A-Za-z]{4,}\s?[A-Za-z0-9]*$/;
    if (!nameRegex.test(name)) {
        alert("Invalid name. Name should start with letters and may contain numbers.");
        return;
    }

    // Email validation: Must start with letters, minimum 5 characters before @
    // Allows letters, numbers, periods, and underscores, and specific domains
    const emailRegex = /^[a-zA-Z][a-zA-Z0-9._-]{4,}@(gmail|hotmail|yahoo)\.com$/;
    if (!emailRegex.test(email)) {
        alert("Invalid email format. Email should start with a letter and have at least 5 characters before '@'. Only @gmail.com, @hotmail.com, or @yahoo.com domains are allowed.");
        return;
    }



    // Phone number validation: Should start with a valid country code followed by 10-14 digits, allowing optional spaces
    const phoneRegex = /^\+([0-9]{1,3})\s?[0-9]{3}\s?[0-9]{7}$/;
    if (!phoneRegex.test(phone)) {
        alert("Invalid phone number. Please enter a valid phone number starting with a country code (e.g., +92, +91) and the correct number of digits.");
        return;
    }

    // Send subscription data to the Flask backend
    fetch('/subscribe2', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: name, email: email, phone: phone })
    })
        .then(response => response.url) // Get the redirect URL from the response
        .then(url => window.location.href = url); // Redirect the user to the new URL

    // Clear the form after sending the request
    document.getElementById('subscription-form2').style.display = 'none';
    document.getElementById('sub-name2').value = '';
    document.getElementById('sub-email2').value = '';
    document.getElementById('sub-phone2').value = '';
}