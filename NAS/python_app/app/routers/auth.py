from fastapi import APIRouter, Request, Form, Depends, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import os
import sys

# Add the parent directory to path to allow importing from app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models import mock_users

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# Simple session management with a dictionary
# In a production app, use proper session management/JWT/cookies
active_sessions = {}

@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login", response_class=HTMLResponse)
async def login_submit(request: Request, username: str = Form(...), password: str = Form(...)):
    # Print login attempt to terminal
    print(f"Login attempt: Username: {username}, Password: {password}")
    
    # Check if user exists in mock database
    user = next((user for user in mock_users if user["username"] == username and user["password"] == password), None)
    
    if user:
        # In a real app, you would use secure session/JWT here
        active_sessions[username] = True
        print(f"User {username} logged in successfully")
        return RedirectResponse(url="/dashboard", status_code=status.HTTP_303_SEE_OTHER)
    else:
        print(f"Login failed for user {username}")
        return templates.TemplateResponse(
            "login.html", 
            {"request": request, "error": "Invalid username or password"}
        )

@router.get("/signup", response_class=HTMLResponse)
async def signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@router.post("/signup", response_class=HTMLResponse)
async def signup_submit(
    request: Request, 
    username: str = Form(...), 
    email: str = Form(...),
    password: str = Form(...), 
    confirm_password: str = Form(...)
):
    # Print signup data to terminal
    print(f"Signup attempt: Username: {username}, Email: {email}, Password: {password}")
    
    # Check if passwords match
    if password != confirm_password:
        return templates.TemplateResponse(
            "signup.html", 
            {"request": request, "error": "Passwords do not match"}
        )
    
    # Check if username already exists
    if any(user["username"] == username for user in mock_users):
        return templates.TemplateResponse(
            "signup.html", 
            {"request": request, "error": "Username already exists"}
        )
    
    # Create new user (in a real app, this would add to database)
    new_user = {
        "id": len(mock_users) + 1,
        "username": username,
        "email": email,
        "password": password  # In a real app, you'd hash this password
    }
    mock_users.append(new_user)
    
    print(f"New user registered: {username}, {email}")
    print(f"Current users: {mock_users}")
    
    # Redirect to login page
    return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/logout")
async def logout(request: Request):
    # In a real app, you would clear session/JWT here
    response = RedirectResponse(url="/login")
    print("User logged out")
    return response 