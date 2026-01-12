# Lab 06 Exercise: Create a FastAPI Search API
# Save this as main.py and run: uvicorn main:app --reload

from fastapi import FastAPI

app = FastAPI(title="Disease Search API")

# Sample disease data
diseases = [
    {"name": "Rubella", "symptoms": "fever, rash", "treatment": "rest"},
    {"name": "Cholera", "symptoms": "diarrhea, vomiting", "treatment": "rehydration"},
    {"name": "GERD", "symptoms": "heartburn, acid reflux", "treatment": "antacids"},
    {"name": "Dengue", "symptoms": "high fever, headache", "treatment": "rest, fluids"}
]

# Exercise 1: Create root endpoint (25 pts)
# YOUR CODE HERE - Create GET "/" that returns {"message": "Welcome to Disease API"}



# Exercise 2: Get all diseases (25 pts)  
# YOUR CODE HERE - Create GET "/diseases" that returns all diseases



# Exercise 3: Search endpoint (25 pts)
# YOUR CODE HERE - Create GET "/search" with query parameter
# Return diseases where query appears in symptoms



# Exercise 4: Get disease by name (25 pts)
# YOUR CODE HERE - Create GET "/disease/{name}" 
# Return the disease with matching name, or {"error": "Not found"}



# Run with: uvicorn main:app --reload
# Test at: http://localhost:8000/docs
