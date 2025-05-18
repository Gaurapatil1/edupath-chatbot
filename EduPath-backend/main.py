from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pymysql


app = FastAPI()

# CORS Middleware Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MySQL Connection Function
def get_connection():
    try:
        return pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="@Gauravpatil123",
            database="edupath_db",
            port=3306,
            cursorclass=pymysql.cursors.DictCursor
        )
    except Exception as e:
        print(f"Connection error: {e}")
        return None


# Root Endpoint
@app.get("/")
def read_root():
    return {"message": "EduPath backend is running!"}

# Test Database Connection
@app.get("/test-db")
def test_db():
    conn = get_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT DATABASE();")
                db_name = cursor.fetchone()['DATABASE()']
            return {"message": "Connected to MySQL", "database": db_name}
        finally:
            conn.close()
    raise HTTPException(status_code=500, detail="Failed to connect to database")


# Homepage Chatbot
@app.post("/homepage-chatbot")
async def homepage_chatbot(request: Request):
    data = await request.json()
    user_input = data.get("message")

    conn = get_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection error")

    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT bot_reply FROM homepage_chatbot 
                WHERE user_input = %s
            """, (user_input.lower(),))
            result = cursor.fetchone()
            return {"reply": result["bot_reply"]} if result else {"reply": "Sorry, I didn't understand that."}
    finally:
        conn.close()

# Predict Colleges Based on Score
@app.get("/")
def read_root():
    return{"message":"Hello,FastAPI!"}