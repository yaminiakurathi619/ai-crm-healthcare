import React, { useState } from "react";

function ChatBox({ setResponse }) {
  const [message, setMessage] = useState("");

  const sendMessage = async () => {
    const res = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: message }),
    });

    const data = await res.json();
    setResponse(data.result);
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Type your interaction..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <button onClick={sendMessage}>Send</button>
    </div>
  );
}

export default ChatBox;
