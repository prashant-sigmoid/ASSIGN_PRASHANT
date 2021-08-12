import psycopg2
from openpyxl.workbook import Workbook
import pandas as pd



##Should have given some comments about the code and it's solution such as 
##"Solution for Problem Statement2 and connecting the database"




class Total_compensation:
    
    
    def compensation(self):
        try:
            conn = psycopg2.connect(
                host="localhost",
                database="SQL_Assig",
                user="postgres",
                password="Prashant@123")
            cur = conn.cursor()
            script = """select emp.ename, emp.empno, dept.dname, (case when enddate is not null then ((enddate-startdate+1)/30)*(jobhist.sal) else ((current_date-startdate+1)/30)*(jobhist.sal) end)as Total_Compensation,
                        (case when enddate is not null then ((enddate-startdate+1)/30) else ((current_date-startdate+1)/30) end)as Months_Spent from jobhist, dept, emp 
                        where jobhist.deptno=dept.deptno and jobhist.empno=emp.empno"""

            cur.execute(script)
            #cur.execute('select empno from jobhist')


## below 3 lines of code can be done in a single line of code so to remove extra lines of code 
## like   ----- df = pd.DataFrame(cur.fetchall())


            columns = [desc[0] for desc in cur.description]
            data = cur.fetchall()
            df = pd.DataFrame(list(data), columns=columns)

            writer = pd.ExcelWriter('Q2.xlsx')
            df.to_excel(writer, sheet_name='bar')
            writer.save()

        except Exception as e:
            print("Error", e)
        finally:

            if conn is not None:
                cur.close()
                conn.close()


if __name__=='__main__':
    conn = None
    cur = None
    comp = Total_compensation()
    comp.compensation()
    
    
    
    
    
    ## you should have written test cases for unit testing ....
