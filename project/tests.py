import os
import sqlite3
import subprocess
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


    def test_sqlite_table_content(self):
        # test the content of the tables in the SQLite database.
        print("Testing SQLite database table content...")
        with sqlite3.connect(SQLITE_FILE) as conn:
            parliamentWomen = pd.read_sql("SELECT * FROM parliamentWomen;", conn)
            expectedYears = pd.read_sql("SELECT * FROM ExpectedYearsSchoolWomen;", conn)
            secondarySchool = pd.read_sql("SELECT * FROM SecondarySchoolWomen;", conn)
            tertiarySchool = pd.read_sql("SELECT * FROM TertiarySchoolWomen;", conn)
            self.assertFalse(parliamentWomen.empty, "Table 'parliamentWomen' in SQLite database is empty.")
            self.assertFalse(expectedYears.empty, "Table 'ExpectedYearsSchoolWomen' in SQLite database is empty.")
            self.assertFalse(secondarySchool.empty, "Table 'SecondarySchoolWomen' in SQLite database is empty.")
            self.assertFalse(tertiarySchool.empty, "Table 'TertiarySchoolWomen' in SQLite database is empty.")
            print("SQLite database tables contain valid data.")
            
            # test for the correct columns in the tables
            print("Testing the columns of the tables...")
            expected_columns_parliamentWomen = ['Country Name', 'Year', 'Value']  
            expected_columns_expectedYears = ['Country Name', 'Year', 'Value']   
            expected_columns_secondarySchool = ['Country Name', 'Year', 'Value']  
            expected_columns_tertiarySchool = ['Country Name', 'Year', 'Value']  
            
            self.assertTrue(set(expected_columns_parliamentWomen).issubset(parliamentWomen.columns), "Missing columns in 'parliamentWomen'.")
            self.assertTrue(set(expected_columns_expectedYears).issubset(expectedYears.columns), "Missing columns in 'ExpectedYearsSchoolWomen'.")
            self.assertTrue(set(expected_columns_secondarySchool).issubset(secondarySchool.columns), "Missing columns in 'SecondarySchoolWomen'.")
            self.assertTrue(set(expected_columns_tertiarySchool).issubset(tertiarySchool.columns), "Missing columns in 'TertiarySchoolWomen'.")
            print("SQLite tables contain the correct columns.")
            
            # test for a minimal number of rows, minimum 1 row for each country should be present, so 4 rows minimum for each table
            print("Testing the rows of the tables...")
            self.assertGreater(len(parliamentWomen), 4, "Table 'parliamentWomen' has no rows.")
            self.assertGreater(len(expectedYears), 4, "Table 'ExpectedYearsSchoolWomen' has no rows.")
            self.assertGreater(len(secondarySchool), 4, "Table 'SecondarySchoolWomen' has no rows.")
            self.assertGreater(len(tertiarySchool), 4, "Table 'TertiarySchoolWomen' has no rows.")
            
            print("SQLite tables contain valid rows.")
            
if __name__ == "__main__":
    unittest.main()