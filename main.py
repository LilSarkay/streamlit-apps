# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from deploy import deploy_app
from dotenv import load_dotenv
import uuid
import os

load_dotenv()  # Load variables from .env

app = FastAPI()

class AppRequest(BaseModel):
    user_request: str
    existing_code: str = None

@app.post("/api/build_app")
async def build_app(req: AppRequest):
    # Step 1: Generate basic Streamlit code
    code = generate_code(req.user_request, req.existing_code)

    # Step 2: Save code to file
    app_id = str(uuid.uuid4())
    os.makedirs("app_storage", exist_ok=True)
    app_path = f"app_storage/{app_id}.py"
    with open(app_path, "w") as f:
        f.write(code)

    # Step 3: Deploy to GitHub and get Streamlit URL
    app_title, live_url = await deploy_app(app_path)

    return {
        "app_title": app_title,
        "live_url": live_url,
        "code": code
    }

def generate_code(user_request, existing_code=None):
    if existing_code:
        # Basic edit append — customize this as needed
        return existing_code + f"\n# User asked to: {user_request}"
    return f"""
import streamlit as st

st.title("{user_request}")
st.write("This app was generated from your request: {user_request}")
"""
