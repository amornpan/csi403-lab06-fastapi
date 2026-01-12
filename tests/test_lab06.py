"""
Lab 06: FastAPI Search API - Auto-grading Tests
"""

import pytest
import os
import sys

# Add exercise directory to path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'exercise'))


class TestExercise1:
    """Test Exercise 1: Root Endpoint (25 points)"""
    
    def test_root_endpoint_exists(self):
        from fastapi.testclient import TestClient
        try:
            from main import app
            client = TestClient(app)
            response = client.get("/")
            assert response.status_code == 200, "Root endpoint should return 200"
        except ImportError:
            pytest.skip("FastAPI app not properly configured")
    
    def test_root_returns_message(self):
        from fastapi.testclient import TestClient
        try:
            from main import app
            client = TestClient(app)
            response = client.get("/")
            data = response.json()
            assert "message" in data, "Response should contain 'message' key"
        except ImportError:
            pytest.skip("FastAPI app not properly configured")


class TestExercise2:
    """Test Exercise 2: Get All Diseases (25 points)"""
    
    def test_diseases_endpoint_exists(self):
        from fastapi.testclient import TestClient
        try:
            from main import app
            client = TestClient(app)
            response = client.get("/diseases")
            assert response.status_code == 200, "/diseases endpoint should return 200"
        except ImportError:
            pytest.skip("FastAPI app not properly configured")
    
    def test_diseases_returns_list(self):
        from fastapi.testclient import TestClient
        try:
            from main import app
            client = TestClient(app)
            response = client.get("/diseases")
            data = response.json()
            assert isinstance(data, list), "/diseases should return a list"
            assert len(data) >= 1, "/diseases should return at least 1 disease"
        except ImportError:
            pytest.skip("FastAPI app not properly configured")


class TestExercise3:
    """Test Exercise 3: Search Endpoint (25 points)"""
    
    def test_search_endpoint_exists(self):
        from fastapi.testclient import TestClient
        try:
            from main import app
            client = TestClient(app)
            response = client.get("/search?query=fever")
            assert response.status_code == 200, "/search endpoint should return 200"
        except ImportError:
            pytest.skip("FastAPI app not properly configured")
    
    def test_search_returns_results(self):
        from fastapi.testclient import TestClient
        try:
            from main import app
            client = TestClient(app)
            response = client.get("/search?query=fever")
            data = response.json()
            assert isinstance(data, list), "/search should return a list"
        except ImportError:
            pytest.skip("FastAPI app not properly configured")


class TestExercise4:
    """Test Exercise 4: Get Disease by Name (25 points)"""
    
    def test_disease_by_name_exists(self):
        from fastapi.testclient import TestClient
        try:
            from main import app
            client = TestClient(app)
            response = client.get("/disease/Rubella")
            assert response.status_code == 200, "/disease/{name} endpoint should return 200"
        except ImportError:
            pytest.skip("FastAPI app not properly configured")
    
    def test_disease_not_found(self):
        from fastapi.testclient import TestClient
        try:
            from main import app
            client = TestClient(app)
            response = client.get("/disease/Unknown")
            data = response.json()
            assert "error" in data or response.status_code == 404, "Unknown disease should return error"
        except ImportError:
            pytest.skip("FastAPI app not properly configured")


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
