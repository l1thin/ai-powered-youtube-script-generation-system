"""
Main entry point for the FastAPI application.
"""

from fastapi import FastAPI

app = FastAPI(title="YouTube-Scripting-Agent API")

@app.get("/")
def root():
    return {"message": "Welcome to YouTube-Scripting-Agent API"}
