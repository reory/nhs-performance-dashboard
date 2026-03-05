# This file create a fixture. The goal is to mimic the DuckDB in memory only 
# so as to not interfere with the real DuckDB

import pytest
import duckdb
from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db_connection

# Set up the Database fixture
@pytest.fixture(scope="session")
def test_db_connection():
    """
    Creates an in-memory DuckDB instance for testing.
    This ensures we dont touch the production .db file.
    """

    conn = duckdb.connect(':memory:')

    conn.execute("""
        CREATE TABLE patients (
            id INTEGER,
            nhs_number VARCHAR,
            name VARCHAR,
            specialty VARCHAR,
            referral_date DATE,
            priority VARCHAR,
            is_breach BOOLEAN
        )
    """)

    yield conn

    conn.close()

# Fast API client fixture.
@pytest.fixture(scope="module")
def client(test_db_connection):
    """Provides a TestClient for FastAPI."""

    def _get_test_db_connection():

        return test_db_connection
    
    app.dependency_overrides[get_db_connection] = _get_test_db_connection
    with TestClient(app) as c:
        yield c

    app.dependency_overrides.clear()
    