# database.py
import mysql.connector
from tkinter import messagebox
import os # Import the os module

class Database:
    def __init__(self, host="localhost", user="root", password=None, database="studentmanagementsystem"):
        """Initializes the database connection."""
        self.host = host
        self.user = user
        self.database = database

        # Get password from environment variable (secure approach)
        # It will default to an empty string if MYSQL_PASSWORD is not set.
        # You *could* put a default like "yes" here for local dev, but it's less secure.
        self.password = os.getenv("MYSQL_PASSWORD", "")

        self.connection = None
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Failed to connect: {err}", icon='error')
            exit() # Exit if connection fails

    def get_cursor(self):
        """Returns a cursor for the established connection."""
        if not self.connection.is_connected():
            # Attempt to reconnect if connection was lost
            self.connection.reconnect()
        return self.connection.cursor()

    def commit(self):
        """Commits the current transaction."""
        self.connection.commit()

    def close(self):
        """Closes the database connection."""
        if self.connection and self.connection.is_connected():
            self.connection.close()

    def fetch_all_students(self):
        """Fetches all records from the information table."""
        cursor = self.get_cursor()
        cursor.execute("SELECT * FROM information")
        records = cursor.fetchall()
        cursor.close()
        return records

    def add_student(self, data_tuple):
        """Inserts a new student record into the database."""
        cursor = self.get_cursor()
        query = "INSERT INTO information (department, course, year, semester, Student_ID, name, section, age, gender, Phone, email, bus) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, data_tuple)
        self.commit()
        cursor.close()

    def update_student(self, data_tuple):
        """Updates an existing student record."""
        cursor = self.get_cursor()
        query = """
            UPDATE information SET department=%s, course=%s, year=%s, semester=%s,
            name=%s, section=%s, age=%s, gender=%s, Phone=%s, email=%s, bus=%s
            WHERE Student_ID=%s
        """
        cursor.execute(query, data_tuple)
        self.commit()
        cursor.close()

    def delete_student(self, student_id):
        """Deletes a student record by student_id."""
        cursor = self.get_cursor()
        query = "DELETE FROM information WHERE student_ID = %s"
        cursor.execute(query, (student_id,))
        self.commit()
        cursor.close()

    def search_student(self, search_by, search_term):
        """Searches for students based on a specific attribute."""
        cursor = self.get_cursor()
        query = f"SELECT * FROM information WHERE {search_by} LIKE %s"
        cursor.execute(query, (f"%{search_term}%",))
        records = cursor.fetchall()
        cursor.close()
        return records