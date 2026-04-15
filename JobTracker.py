import mysql.connector

# ---- Database Connection -----
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="CSK@5cup",  
    database="job_tracker"
)

cursor = conn.cursor()

# ---- OOP Class ---
class JobTracker:

    def add_job(self):
        company = input("Enter company: ")
        role = input("Enter role: ")
        status = input("Enter status: ")
        date = input("Enter date (YYYY-MM-DD): ")

        query = "INSERT INTO jobs (company, role, status, date_applied) VALUES (%s, %s, %s, %s)"
        values = (company, role, status, date)

        cursor.execute(query, values)
        conn.commit()
        print("Job added!")

    def view_jobs(self):
        cursor.execute("SELECT * FROM jobs")
        jobs = cursor.fetchall()

        if not jobs:
            print("No records found")
        else:
            for job in jobs:
                print(job)

    def update_job(self):
        job_id = input("Enter Job ID: ")
        new_status = input("Enter new status: ")

        query = "UPDATE jobs SET status=%s WHERE id=%s"
        cursor.execute(query, (new_status, job_id))
        conn.commit()
        print("Updated successfully!")

    def delete_job(self):
        job_id = input("Enter Job ID: ")

        query = "DELETE FROM jobs WHERE id=%s"
        cursor.execute(query, (job_id))
        conn.commit()
        print("Deleted successfully!")

# ---------- Menu ----------
tracker = JobTracker()

while True:
    print("\n--- Job Application Tracker ---")
    print("1. Add Job")
    print("2. View Jobs")
    print("3. Update Status")
    print("4. Delete Job")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        tracker.add_job()

    elif choice == "2":
        tracker.view_jobs()

    elif choice == "3":
        tracker.update_job()

    elif choice == "4":
        tracker.delete_job()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice")