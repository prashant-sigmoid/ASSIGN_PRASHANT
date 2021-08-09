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

