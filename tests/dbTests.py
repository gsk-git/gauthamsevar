import unittest
import mysql.connector
import os

db_pswd = os.environ.get('wip_db_password')

class TestDatabase(unittest.TestCase):

    def setUp(self):
        # Set up a MySQL database connection
        self.connection = mysql.connector.connect(host="localhost",user="root",password=db_pswd,database="wip")
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        # Create tables for testing
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (\
            AID INT NOT NULL AUTO_INCREMENT,\
            UUID varchar(255) NOT NULL,\
            LastName varchar(255),\
            FirstName varchar(255),\
            City varchar(255),\
            Gender varchar(255),\
            Mobile varchar(255),\
            CREATED TIMESTAMP DEFAULT CURRENT_TIMESTAMP,\
            UPDATED TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,\
            PRIMARY KEY (AID, UUID));\
            ALTER TABLE Users AUTO_INCREMENT=100;)
        ''')
        self.connection.commit()

    def test_insert_user(self):
        # Test inserting a user
        self.cursor.execute('''
            INSERT INTO users (name, age) VALUES (%s, %s)
        ''', ("John Doe", 30))
        self.connection.commit()

        self.cursor.execute('SELECT * FROM users WHERE name = %s', ("John Doe",))
        user = self.cursor.fetchone()
        self.assertIsNotNone(user)
        self.assertEqual(user[1], "John Doe")
        self.assertEqual(user[2], 30)

    def test_query_user(self):
        # Insert a user for querying
        self.cursor.execute('''
            INSERT INTO users (name, age) VALUES (%s, %s)
        ''', ("Jane Doe", 25))
        self.connection.commit()

        self.cursor.execute('SELECT * FROM users WHERE name = %s', ("Jane Doe",))
        user = self.cursor.fetchone()
        self.assertIsNotNone(user)
        self.assertEqual(user[1], "Jane Doe")
        self.assertEqual(user[2], 25)

    def tearDown(self):
        # Close the database connection
        self.cursor.execute('DROP TABLE IF EXISTS users')
        self.connection.close()

if __name__ == '__main__':
    unittest.main()