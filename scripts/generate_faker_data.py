import duckdb
import nhs_number
from faker import Faker
import random
from datetime import datetime
from tqdm import tqdm

# Locales list
locales = ['en_GB', 'en_IN', 'pl_PL', 'tr_TR', 'ro_RO',
              'es_ES', 'pt_PT', 'en_NG',
]

# Initialise Faker and DuckDB
fake = Faker(locales)
con = duckdb.connect('data/hospital_data.db')

# Define NHS specific data
specialties = ['Cardiology', 'Orthopaedic', 'Neurology', 'Pediatrics',
               'Oncology', 'Gastroenterology', 'Haematology', 'Rheumatology',
               'Pulmonolgy', 'Infectious Diseases']

priorities = ['Routine', 'Urgent', 'Two Week Wait (Cancer)',]

gp_practices = ['Health Centre Beeston', 'Leeds Medical Practice', 
                'Oakwood Surgery', 'Highfield Roundhay Doctors', 
                "St. Armley's Medical Group", 'Meadow View Alwoodley Surgery',
                'The Village Medical Centre', 'Beacon Health Partnership', 
                'Bankside GP Partners Bramley','Bluefield Farsley Health Centre']

def generate_pilot_data(n=1000):
    """Create the table if it dosen't exist."""

    con.execute("""
        CREATE OR REPLACE TABLE patients (
                gp_practice VARCHAR,
                nhs_id VARCHAR,
                name VARCHAR,
                dob DATE,
                specialty VARCHAR,
                priority VARCHAR,
                referral_date DATE,
                wait_weeks INTEGER
        )
    """)

    patients = []

    # Wrap the range in tqdm() to show the progress bar.
    print(f"Generating {n} clinical records....")
    for _ in tqdm(range(n), desc="Buidling Patient Data", unit="patient"):

        # Generate a valid nhs number
        valid_nhs = nhs_number.generate(
            quantity=1, for_region=nhs_number.REGION_ENGLAND)[0]

        # Date logic: Referrals in the last 6 months
        ref_date = fake.date_between(start_date='-180d', end_date='today')
        wait_weeks = (datetime.now().date() - ref_date).days // 7

        patient = (
            random.choice(gp_practices),
            valid_nhs,
            fake.name(),
            fake.date_of_birth(minimum_age=0, maximum_age=105),
            random.choice(specialties),
            random.choice(priorities),
            ref_date,
            wait_weeks
        )

        patients.append(patient)

    # Bulk insert into DuckDB
    con.executemany(
        "INSERT INTO patients VALUES (?, ?, ?, ?, ?, ?, ?, ?)", patients)
    print(f"😁 Successfully injected {n} patient records into DuckDB!")

if __name__ == "__main__":
    generate_pilot_data(1000)