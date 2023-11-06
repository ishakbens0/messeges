function sendMessage() {
    const messageInput = document.getElementById("message");
    const messageText = messageInput.value;
    messageInput.value = "";

    if (messageText.trim() !== "") {
        const chatBox = document.getElementById("chat-box");
        const messageElement = document.createElement("div");
        messageElement.innerText = `USER: ${messageText} (${new Date().toLocaleString()})`;
        chatBox.appendChild(messageElement);
    }
}
