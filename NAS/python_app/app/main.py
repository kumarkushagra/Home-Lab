from fastapi import FastAPI, Request, Form, File, UploadFile, Depends, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
import uvicorn
from typing import List, Optional
import os

# Import routers
from routers import auth, dashboard, files

app = FastAPI(title="NAS Web Interface")

# Mount static files directory
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Set up templates
templates = Jinja2Templates(directory="app/templates")

# Include routers
app.include_router(auth.router)
app.include_router(dashboard.router)
app.include_router(files.router)

# Root redirect to login
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return RedirectResponse(url="/login")

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True) 