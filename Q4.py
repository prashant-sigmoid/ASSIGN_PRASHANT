import psycopg2
from openpyxl.workbook import Workbook
import pandas as pd


## you should have done question 3 by writing some python lines of code instead of using pg admin tool to read and upload the .xlsx file in the database..
## like
##cur.execute("COPY comp FROM '/Users/rahul/PycharmProjects/pythonProject1/sqlassignment/compensation.csv' " "DELIMITER ',' CSV HEADER;")




# Should have given some comments about the and it's solution 
# such as "Solution for Problem Statement2 and connecting the database"...

class employees:

    def emp(self):
        
        
        
        ## create a sepearare database connection file....to avoid writing same lines of code again and again in every file for db connection ..
        try:
            conn = psycopg2.connect(

                database="SQL_Assig",
                user="postgres",
                password="Prashant@123")
            cursor = conn.cursor()
            script = """
                     select dept.deptno, dept_name, sum(total_compensation) from Compensation, dept
                    where Compensation.dept_name=dept.dname
                    group by dept_name, dept.deptno
                    """

            cursor.execute(script)

            columns = [desc[0] for desc in cursor.description]
            data = cursor.fetchall()
            df = pd.DataFrame(list(data), columns=columns)

            writer = pd.ExcelWriter('Q4.xlsx')
            df.to_excel(writer, sheet_name='bar')
            writer.save()

        except Exception as e:
            print("Error", e)

        finally:

            if conn is not None:
                cursor.close()
                conn.close()


if __name__ == '__main__':
    conn = None
    cur = None
    employee = employees()
    employee.emp()

    
    ##should have written sone test cases for unit testing ...
