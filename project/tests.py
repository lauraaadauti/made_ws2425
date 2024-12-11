import os
import sqlite3
import unittest
import pandas as pd

DATA_DIR = "../data"
SQLITE_FILE = os.path.join(DATA_DIR, "project.sqlite")

class TestPipeline(unittest.TestCase):    
    def test_pipeline_execution(self):
        os.system("jv pipeline.jv")
        print("\t\tPipeline executed successfully.")
    
    def test_sqlite_file_exists(self):
        # test if the sqlite file exists
        print("Testing if SQLite database exists...")
        self.assertTrue(os.path.exists(SQLITE_FILE), "The SQLite file was not created.")
        print("SQLite file exists.")
        
        
    def test_sqlite_tables(self):
        # test if the expected tables exist in the SQLite database.
        print("Testing SQLite database tables...")
        with sqlite3.connect(SQLITE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = [row[0] for row in cursor.fetchall()]
            self.assertIn("parliamentWomen", tables, "Table 'parliamentWomen' not found in SQLite database.")
            self.assertIn("ExpectedYearsSchoolWomen", tables, "Table 'ExpectedYearsSchoolWomen' not found in SQLite database.")
            self.assertIn("SecondarySchoolWomen", tables, "Table 'SecondarySchoolWomen' not found in SQLite database.")
            self.assertIn("TertiarySchoolWomen", tables, "Table 'TertiarySchoolWomen' not found in SQLite database.")
            print("Expected tables found in SQLite database.")    
    
    def test_sqlite_table_not_empty(self):
        # test the content of the tables in the SQLite database.
        print("Testing if SQLite database tables are not empty...")
        with sqlite3.connect(SQLITE_FILE) as conn:
            tables = {
                "parliamentWomen": "Table 'parliamentWomen' is empty.",
                "ExpectedYearsSchoolWomen": "Table 'ExpectedYearsSchoolWomen' is empty.",
                "SecondarySchoolWomen": "Table 'SecondarySchoolWomen' is empty.",
                "TertiarySchoolWomen": "Table 'TertiarySchoolWomen' is empty.",
            }
            for table, error_message in tables.items():
                data = pd.read_sql(f"SELECT * FROM {table};", conn)
                self.assertFalse(data.empty, error_message)
        print("All SQLite tables are non-empty.")
    
    def test_sqlite_table_columns(self):        
        # test for the correct columns in the tables
        print("Testing if SQLite database tables have the correct columns...")
        expected_columns = {
            "parliamentWomen": ['Country Name', 'Year', 'Value'],
            "ExpectedYearsSchoolWomen": ['Country Name', 'Year', 'Value'],
            "SecondarySchoolWomen": ['Country Name', 'Year', 'Value'],
            "TertiarySchoolWomen": ['Country Name', 'Year', 'Value'],
        }
        with sqlite3.connect(SQLITE_FILE) as conn:
            for table, expected in expected_columns.items():
                data = pd.read_sql(f"SELECT * FROM {table};", conn)
                self.assertTrue(set(expected).issubset(data.columns), f"Missing columns in table '{table}'.")
        print("All SQLite tables have the correct columns.")
     
    def test_sqlite_table_minimum_rows(self):        
        # test for a minimal number of rows, minimum 1 row for each country should be present, so 4 rows minimum for each table
        print("Testing if SQLite database tables have a minimum number of rows...")
        with sqlite3.connect(SQLITE_FILE) as conn:
            tables = {
                "parliamentWomen": "Table 'parliamentWomen' has less than 4 rows.",
                "ExpectedYearsSchoolWomen": "Table 'ExpectedYearsSchoolWomen' has less than 4 rows.",
                "SecondarySchoolWomen": "Table 'SecondarySchoolWomen' has less than 4 rows.",
                "TertiarySchoolWomen": "Table 'TertiarySchoolWomen' has less than 4 rows.",
            }
            for table, error_message in tables.items():
                data = pd.read_sql(f"SELECT * FROM {table};", conn)
                self.assertGreater(len(data), 4, error_message)
        print("All SQLite tables have minimum 4 rows.")
        
if __name__ == "__main__":
    unittest.main()