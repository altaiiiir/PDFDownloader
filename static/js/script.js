document.getElementById("pdfForm").addEventListener("submit", function(event) {
    event.preventDefault();  // Prevent the form from submitting to handle custom validation

    const urlInput = document.getElementById("urlInput");
    const url = urlInput.value.trim();
    const messageContainer = document.getElementById("messageContainer");

    messageContainer.innerHTML = '';
    messageContainer.style.display = 'none';

    // Validate if the URL ends with ".pdf"
    const pdfPattern = /\.pdf$/i;
    if (!pdfPattern.test(url)) {
        showMessage("Invalid URL! Please provide a valid PDF URL.", "error", messageContainer);
        urlInput.value = '';
        return;
    }

    showMessage("Downloading...", "success", messageContainer);
    this.submit();
});

// Function to show the message with pop-up animation
function showMessage(messageText, messageType, messageContainer) {
    const message = document.createElement("div");
    message.classList.add("message", messageType);
    message.innerText = messageText;
    messageContainer.appendChild(message);

    messageContainer.style.display = 'block';
    messageContainer.style.opacity = '1';
    startPopUpAnimation(message, messageContainer);
}

// Function to start the pop-up animation
function startPopUpAnimation(message, messageContainer) {
    messageContainer.style.animation = 'popUpAnimation 0.2s ease-out';

    messageContainer.fadeTimer = setTimeout(() => {
      fadeOutMessage(message, messageContainer);
    }, 1500);
}

// Function to fade out the message
function fadeOutMessage(message, messageContainer) {
    message.style.opacity = '0';

    setTimeout(() => {
        messageContainer.style.display = 'none';
    }, 1500);
}
