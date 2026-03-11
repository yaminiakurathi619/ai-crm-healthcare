# AI CRM Healthcare – HCP Module

AI-powered Customer Relationship Management (CRM) system for Healthcare Professionals (HCPs).  
This application allows field representatives to log interactions with HCPs using either a **structured form** or a **conversational AI chat interface**. It uses AI tools to summarize interactions, extract key entities, and provide actionable insights.

---

## Tech Stack

- Frontend: React + Redux  
- Backend: Python + FastAPI  
- Database: MySQL / PostgreSQL  
- AI Agent Framework: LangGraph  
- LLM: Gemma2-9b-it  
- Font: Google Inter

---

## Features

1. Log Interaction Screen
   - Structured form to record HCP interactions (Name, Specialty, Date, Interaction Type, Notes)  
   - Conversational chat interface using AI

2. LangGraph AI Tools
   - Log Interaction: Logs HCP interactions and summarizes using AI  
   - Edit Interaction: Modify previously logged interactions  
   - View Interaction Summary: See history of HCP interactions  
   - Search Interactions: Search by HCP, specialty, or date  
   - Interaction Insights: Shows trends and analytics

3. Optional: Dashboard to view past interactions

---

## Setup / Running Instructions

### Frontend

cd frontend
npm install
npm start

Open http://localhost:3000
 to view the app.

### Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

### Database Example (MySQL)
CREATE TABLE interactions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    hcp_name VARCHAR(100),
    specialty VARCHAR(50),
    interaction_date DATE,
    interaction_type VARCHAR(50),
    notes TEXT
);

---

## LangGraph AI Tools Overview

1. Log Interaction: Logs new HCP interactions using AI-assisted summarization  
2. Edit Interaction: Allows updating of existing interaction records  
3. View Interaction Summary: Displays summarized HCP interactions  
4. Search Interactions: Search interactions by HCP, specialty, or date  
5. Interaction Insights: Generates trends and analytics

---

## Author

Yamini Akurathi  
GitHub: https://github.com/yaminiakurathi619
