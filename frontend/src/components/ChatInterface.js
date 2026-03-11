import React, { useState } from "react";
import axios from "axios";

function ChatInterface() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const sendMessage = async () => {
    const res = await axios.post("http://localhost:8000/chat", {
      message: message,
    });

    setResponse(res.data.reply);
  };

  return (
    <div>
      <h2>AI Interaction Chat</h2>

      <textarea value={message} onChange={(e) => setMessage(e.target.value)} />

      <button onClick={sendMessage}>Send</button>

      <p>
        <b>Agent Response:</b> {response}
      </p>
    </div>
  );
}

export default ChatInterface;
