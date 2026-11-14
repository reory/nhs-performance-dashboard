# This file create a fixture. The goal is to mimic the DuckDB in memory only
# so as to not interfere with the real DuckDB

import duckdb
import pytest
from fastapi.testclient import TestClient

from app.database import get_db_connection
from app.main import app


# Set up the Database fixture
@pytest.fixture(scope="session")
def test_db_connection():
    """
    Creates an in-memory DuckDB instance for testing.
    This ensures production .db files are not touched.
    """

    conn = duckdb.connect(":memory:")

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
