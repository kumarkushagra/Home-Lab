from fastapi import APIRouter, Request, Depends, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import os
import sys

# Add the parent directory to path to allow importing from app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models import mock_users, mock_files

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# Simple middleware to check if user is authenticated
# In a real app, you would use proper auth middleware
def authenticated(request: Request):
    # For simplicity, we're just checking if a user is passed in the request
    # In a real app, check sessions, JWT, etc.
    # This is just for demonstration
    print("Checking if user is authenticated...")
    return True

@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request, authorized: bool = Depends(authenticated)):
    # Print database contents to terminal
    print("\n--- Dashboard Access ---")
    print("Users in database:", mock_users)
    print("Files in database:", [(f["id"], f["filename"], f["size"]) for f in mock_files])
    
    # Calculate storage metrics
    total_files = len(mock_files)
    total_size = sum(file["size"] for file in mock_files)
    total_size_mb = total_size / (1024 * 1024)
    
    # In a real app, you would fetch this data from a database
    storage_info = {
        "total_files": total_files,
        "total_size_mb": round(total_size_mb, 2),
        "free_space_mb": 1000.0,  # Mock value
        "used_percent": round((total_size_mb / 1000.0) * 100, 2)  # Mock calculation
    }
    
    # Recent activity - would be from real logs in a production app
    recent_activity = [
        {"action": "Upload", "filename": "document.pdf", "time": "2 minutes ago"},
        {"action": "Download", "filename": "image.jpg", "time": "5 hours ago"},
        {"action": "Delete", "filename": "old_file.txt", "time": "Yesterday"}
    ]
    
    return templates.TemplateResponse(
        "dashboard.html", 
        {
            "request": request,
            "username": "User",  # Would be actual username in real app
            "storage_info": storage_info,
            "files": mock_files,
            "recent_activity": recent_activity
        }
    ) 