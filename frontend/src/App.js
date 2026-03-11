import React from "react";
import ChatInterface from "./components/ChatInterface";
import InteractionForm from "./components/InteractionForm";

function App() {
  return (
    <div>
      <h1>AI CRM for Healthcare Professionals</h1>

      <InteractionForm />

      <ChatInterface />
    </div>
  );
}

export default App;
