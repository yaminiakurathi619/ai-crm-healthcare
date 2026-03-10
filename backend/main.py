from fastapi import FastAPI
from pydantic import BaseModel
from agent import graph
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Interaction(BaseModel):
    doctor_name:str
    notes:str

@app.post("/log")
def log_interaction(data:Interaction):

    print(data)

    return {"message":"saved"}


class ChatMessage(BaseModel):
    message:str


@app.post("/chat")
def chat_with_ai(data:ChatMessage):

    result = graph.invoke({
        "message":data.message
    })

    return {
        "reply": result["result"]
    }