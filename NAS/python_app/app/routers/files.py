from fastapi import APIRouter, Request, Form, File, UploadFile, Depends, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
import os
import sys
from datetime import datetime
from typing import List

# Add the parent directory to path to allow importing from app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models import mock_files

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# Simple middleware to check if user is authenticated
# In a real app, you would use proper auth middleware
def authenticated(request: Request):
    # For demonstration purposes only
    print("Checking if user is authenticated...")
    return True

@router.get("/upload", response_class=HTMLResponse)
async def upload_page(request: Request, authorized: bool = Depends(authenticated)):
    return templates.TemplateResponse("upload.html", {"request": request})

@router.post("/upload", response_class=HTMLResponse)
async def upload_file(
    request: Request, 
    file: UploadFile = File(...),
    description: str = Form(""),
    authorized: bool = Depends(authenticated)
):
    # Print upload information to terminal
    print(f"\n--- File Upload ---")
    print(f"Filename: {file.filename}")
    print(f"Content type: {file.content_type}")
    print(f"Description: {description}")
    
    try:
        # In a real app, you would save the file to disk/cloud storage
        contents = await file.read()
        file_size = len(contents)
        print(f"File size: {file_size} bytes")
        
        # Add file to mock database
        new_file = {
            "id": len(mock_files) + 1,
            "filename": file.filename,
            "size": file_size,
            "upload_date": datetime.now(),
            "owner_id": 1  # Assuming user ID 1 for now
        }
        mock_files.append(new_file)
        
        print(f"File added to mock database: {new_file}")
        
        return templates.TemplateResponse(
            "upload.html", 
            {"request": request, "success": True, "filename": file.filename}
        )
    except Exception as e:
        print(f"Error uploading file: {str(e)}")
        return templates.TemplateResponse(
            "upload.html", 
            {"request": request, "error": f"Failed to upload file: {str(e)}"}
        )

@router.get("/download", response_class=HTMLResponse)
async def download_page(request: Request, authorized: bool = Depends(authenticated)):
    # Print download page access to terminal
    print("\n--- Download Page Access ---")
    print(f"Available files: {[(f['id'], f['filename']) for f in mock_files]}")
    
    return templates.TemplateResponse(
        "download.html", 
        {"request": request, "files": mock_files}
    )

@router.get("/download/{file_id}")
async def download_file(file_id: int, authorized: bool = Depends(authenticated)):
    # Print download attempt to terminal
    print(f"\n--- Download Attempt ---")
    print(f"File ID: {file_id}")
    
    # Find file in mock database
    file = next((f for f in mock_files if f["id"] == file_id), None)
    
    if not file:
        print(f"File with ID {file_id} not found")
        raise HTTPException(status_code=404, detail="File not found")
    
    print(f"Download requested for file: {file['filename']}")
    
    # In a real app, you would return the actual file
    # For this prototype, we'll just redirect back to download page
    return RedirectResponse(url="/download", status_code=status.HTTP_303_SEE_OTHER) 