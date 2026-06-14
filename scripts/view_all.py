# This file lets you see what is in the database by printing a csv file.

import duckdb
from loguru import logger

con = duckdb.connect("data/hospital_data.db")

# This creates a file called 'full_patient_list.csv' in your project folder
con.execute("COPY patients TO 'full_patient_list.csv' (HEADER, DELIMITER ',')")

logger.success("✅ Exported all patients to full_patient_list.csv")
