import React, { useState } from "react";
import axios from "axios";

function InteractionForm() {
  const [doctorName, setDoctorName] = useState("");
  const [notes, setNotes] = useState("");

  const submitInteraction = async () => {
    await axios.post("http://localhost:8000/log", {
      doctor_name: doctorName,
      notes: notes,
    });

    alert("Interaction saved");
  };

  return (
    <div>
      <h2>Log Interaction</h2>

      <input
        placeholder="Doctor Name"
        value={doctorName}
        onChange={(e) => setDoctorName(e.target.value)}
      />

      <textarea
        placeholder="Interaction Notes"
        value={notes}
        onChange={(e) => setNotes(e.target.value)}
      />

      <button onClick={submitInteraction}>Submit</button>
    </div>
  );
}

export default InteractionForm;
