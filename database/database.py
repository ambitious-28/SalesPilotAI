import sqlite3

conn = sqlite3.connect("leads.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT,
    lead_score TEXT,
    email TEXT
)
""")

conn.commit()

def save_lead(company_name, lead_score, email):

    cursor.execute("""
    INSERT INTO leads (
        company_name,
        lead_score,
        email
    )
    VALUES (?, ?, ?)
    """, (company_name, lead_score, email))

    conn.commit()