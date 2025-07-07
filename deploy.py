# deploy.py

import os
import base64
import requests
from datetime import datetime
import re
from dotenv import load_dotenv

load_dotenv()

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = "streamlit-apps"
GITHUB_API = "https://api.github.com"

def extract_app_title(code: str):
    match = re.search(r'st\.title\(["\'](.+?)["\']\)', code)
    return match.group(1).strip() if match else "Streamlit App"

def generate_branch_name(app_title):
    slug = app_title.lower().replace(" ", "-")
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    return f"{slug}-{timestamp}"

async def deploy_app(app_file_path: str):
    with open(app_file_path, "r") as f:
        code = f.read()

    app_title = extract_app_title(code)
    branch_name = generate_branch_name(app_title)

    # Step 1: Get SHA of main
    sha_resp = requests.get(
        f"{GITHUB_API}/repos/{GITHUB_USERNAME}/{REPO_NAME}/git/refs/heads/main",
        auth=(GITHUB_USERNAME, GITHUB_TOKEN)
    )
    sha = sha_resp.json()["object"]["sha"]

    # Step 2: Create new branch from main
    requests.post(
        f"{GITHUB_API}/repos/{GITHUB_USERNAME}/{REPO_NAME}/git/refs",
        auth=(GITHUB_USERNAME, GITHUB_TOKEN),
        json={"ref": f"refs/heads/{branch_name}", "sha": sha}
    )

    # Step 3: Upload file to new branch
    upload_url = f"{GITHUB_API}/repos/{GITHUB_USERNAME}/{REPO_NAME}/contents/streamlit_app.py"
    encoded = base64.b64encode(code.encode()).decode()

    requests.put(
        upload_url,
        auth=(GITHUB_USERNAME, GITHUB_TOKEN),
        json={
            "message": f"Add {app_title}",
            "content": encoded,
            "branch": branch_name
        }
    )

    # Step 4: Return Streamlit URL
    streamlit_url = f"https://streamlit.app/{GITHUB_USERNAME}/{REPO_NAME}/{branch_name}"
    return app_title, streamlit_url
