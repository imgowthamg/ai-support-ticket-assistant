import sqlite3

DB_PATH = "app/database/support.db"

conn = sqlite3.connect(DB_PATH)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS support_solutions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    issue TEXT NOT NULL,
    solution TEXT NOT NULL,
    team TEXT NOT NULL
)
""")

sample_data = [
    (
        "Payment",
        "Card Declined",
        "Verify card details and ensure sufficient funds are available.",
        "Payments Support"
    ),
    (
        "Payment",
        "Gateway Timeout",
        "Retry the transaction after a few minutes and check payment gateway status.",
        "Payments Support"
    ),
    (
        "Authentication",
        "Password Reset Failed",
        "Generate a new password reset link and verify the registered email.",
        "Authentication Support"
    ),
    (
        "Authentication",
        "Account Locked",
        "Unlock the account after identity verification.",
        "Authentication Support"
    ),
    (
        "Claims",
        "Document Upload Failure",
        "Verify file format and ensure file size is within allowed limits.",
        "Claims Team"
    ),
    (
        "Claims",
        "Claim Submission Failed",
        "Verify all mandatory fields and resubmit the claim.",
        "Claims Team"
    ),
    (
        "Technical",
        "API Timeout",
        "Check service health and retry the request.",
        "Technical Support"
    ),
    (
        "Technical",
        "Application Error",
        "Review logs and restart affected services if necessary.",
        "Technical Support"
    ),
    (
        "Account Management",
        "Profile Update Failed",
        "Verify input data and retry the update operation.",
        "Account Management Team"
    )
]

cursor.executemany("""
INSERT INTO support_solutions
(category, issue, solution, team)
VALUES (?, ?, ?, ?)
""", sample_data)

conn.commit()
conn.close()

print("Database initialized successfully.")