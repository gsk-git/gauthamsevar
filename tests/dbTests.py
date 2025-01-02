import unittest
import sqlite3

class TestDatabase(unittest.TestCase):
    def setUp(self):
        # Connect to a test database (in-memory database for testing)
        self.connection = sqlite3.connect(":memory:")
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        # Create a sample table
        self.cursor.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        ''')
        self.connection.commit()

    def test_insert_user(self):
        # Insert a sample user
        self.cursor.execute('''
            INSERT INTO users (name, age) VALUES (?, ?)
        ''', ("John Doe", 30))
        self.connection.commit()

        # Verify the user was inserted
        self.cursor.execute('SELECT * FROM users WHERE name = ?', ("John Doe",))
        user = self.cursor.fetchone()
        self.assertIsNotNone(user)
        self.assertEqual(user[1], "John Doe")
        self.assertEqual(user[2], 30)

    def test_query_user(self):
        # Insert a sample user
        self.cursor.execute('''
            INSERT INTO users (name, age) VALUES (?, ?)
        ''', ("Jane Doe", 25))
        self.connection.commit()

        # Query the user
        self.cursor.execute('SELECT * FROM users WHERE name = ?', ("Jane Doe",))
        user = self.cursor.fetchone()
        self.assertIsNotNone(user)
        self.assertEqual(user[1], "Jane Doe")
        self.assertEqual(user[2], 25)

    def tearDown(self):
        # Close the database connection
        self.connection.close()

if __name__ == '__main__':
    unittest.main()