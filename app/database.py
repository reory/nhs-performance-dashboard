import duckdb

# DuckDB path
DB_PATH = 'data/hospital_data.db'

def get_db_connection():
    
    # Open a new connection to the database
    return duckdb.connect(DB_PATH)

def get_all_patients():
    
    # Establish a connection for patient queries
    conn = get_db_connection()
    
    # Fetch as a list of dictionaries so its easier to use in HTML.
    patients = conn.execute(
        "SELECT * FROM patients ORDER BY wait_weeks DESC").pl().to_dicts()
    conn.close()

    return patients