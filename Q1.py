import psycopg2

from openpyxl.workbook import Workbook
import pandas as pd

class employees:


    def emp(self):
        try:
            conn = psycopg2.connect(

            database="SQL_Assig",
            user="postgres",
            password="Prashant@123")
            cursor = conn.cursor()
            script = """
                    SELECT e1.empno, e1.ename as manager from emp as e1 
                    """

            cursor.execute(script)

            columns = [desc[0] for desc in cursor.description]
            data = cursor.fetchall()
            df = pd.DataFrame(list(data), columns=columns)

            writer = pd.ExcelWriter('Q1.xlsx')
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