
# coding: utf-8

# In[8]:

from tkinter import *
from tkinter import messagebox
import pymysql as sql

class Employee():
    def __init__(self,company='XYZ'):
        self.company=company
         
class HourlyEmployee(Employee):
    def __init__(self,name,hour=8,emptype='Hourly',salary=200):
        Employee.__init__(self)
        self.emptype=emptype
        self.name=name
        self.salary=salary
        self.hour=hour
        self.salary=(self.salary)*(self.hour)
        
class SalariedEmployee(Employee):
    def __init__(self,name,hour=8,emptype='Salaried',salary=30000):
        Employee.__init__(self)
        self.emptype=emptype
        self.name=name
        self.hour=hour
        self.salary=salary

class Manager(Employee):
    def __init__(self,name,hour=8,emptype='Manager',salary=500000):
        Employee.__init__(self)
        self.emptype=emptype
        self.name=name
        self.hour=hour
        self.salary=salary
        
class Executive(Employee):
    def __init__(self,name,hour=8,emptype='Executive',salary=1000000):
        Employee.__init__(self)
        self.emptype=emptype
        self.name=name
        self.hour=hour
        self.salary=salary
        
class company():
    def __init__(self, parent):
       
        self.parent=parent
        self.user_interface()
  
    def getDBConnection(ip = "localhost", usern = "root",passn = "",dbname = "company"):
        try:
            import pymysql as sql
            db = sql.connect(ip,usern,passn,dbname)
            cursor=db.cursor()
       
        except BaseException as e:
            print(e)        
        else:
            print("Connected..")
            return db,cursor
   
    
    def add(self,p,id0):
        try:
            db=sql.connect("localhost","root","","company")
            cursor=db.cursor()
            n=p
            s=id0
            if n==2:                
                a=HourlyEmployee(name=s)    
            elif n==1: 
                a=SalariedEmployee(name=s)   
            elif n==3:  
                a=Manager(name=s)
            else:
                a=Executive(name=s)    
            a1=a.name
            a2=a.hour
            a3=a.emptype
            a4=a.salary
            sql_cmd="insert into employees2(NAME,Hour,EmpType,Salary) values('{}','{}','{}','{}')".format(a1,a2,a3,a4)
            cursor.execute(sql_cmd)       
        except BaseException as e:
            print(e)
            db.rollback()      
            msg=messagebox.showinfo("Info","Error in hiring employee!")
        else:
            db.commit()   
            if(cursor.rowcount>0):
                message=messagebox.showinfo("Info","Employee hired!")
        finally:
            db.close()
            
    def getEntry(self):
        p=self.entry1.get()
        id0=self.entry2.get()
        self.add(p,id0)

    def delete(self,id1):
        try:
            uname=id1
            db=sql.connect("localhost","root","","company")
            cursor=db.cursor()
            sql_cmd = "delete from employees2 where id like '%{}%'".format(uname)
            cursor.execute(sql_cmd)                    
        except BaseException as e:
            print(e)
            db.rollback()     
        else:
            db.commit()
            if(cursor.rowcount>0):
                message=messagebox.showinfo("Info","Employee has been fired.")
            else:
                message=messagebox.showinfo("Info","Employe Not Found!")
                        
        finally:
            db.close()  
            
    def getExit(self):
        user =self.entry3.get()
        self.delete(id1 = user)
        
    def update(self,id2,id3,id4):
        try:
            a8=id2
            a6=id3
            a7=id4
            db=sql.connect("localhost","root","","company")
            cursor=db.cursor()
            sql_cmd = "update employees2 set EmpType='{}',salary='{}' where id like '%{}%'".format(a6,a7,a8)
            cursor.execute(sql_cmd)                    
        except BaseException as e:
            print(e)
            db.rollback() 
            msg=messagebox.showinfo("Info","Error in promoting Employee!")
        else:
            db.commit()
            if(cursor.rowcount>0):
                message=messagebox.showinfo("Info","Employee Promoted!")    
                           
        finally:
            db.close()
    
    def getEntry1(self):
        user3 = self.entry4.get()
        user1=self.entry5.get()
        user2=self.entry6.get()
        
        self.update(id2 = user3,id3=user1,id4=user2)
        
    
    
    def user_interface(self):
        self.parent.geometry("500x500")
        self.parent.title("Employee management system")
        self.parent.iconbitmap('favicon.ico')
        self.parent.label1=Label(self.parent,text='Company Manager')
        self.parent.label1.pack()
        self.parent.label1.config(justify = CENTER)
        #Adding the employee
        self.label2=Label(self.parent,text='Enter 1.To hire Salaried employee 2.To hire hourly employee 3.To hire Manager 4.To hire Executive:')
        self.label2.pack()
        self.label2.config(justify = CENTER)
        self.entry1 = Entry(self.parent,width=10)
        self.entry1.pack()
        self.label3=Label(self.parent,text='Enter Name of the new employee:')
        self.label3.pack()
        self.label3.config(justify = CENTER)
        self.entry2 = Entry(self.parent,width=20)
        self.entry2.pack()
        self.button1=Button(self.parent,text='Hire',activebackground="Blue",activeforeground="Red")
        self.button1.pack()

        self.button1.config(command=self.getEntry)

        #Adding the employee
        #Removing the Employee

        self.label4=Label(self.parent,text='Enter ID of the Employee to be Fired:')

        self.label4.pack()

        self.label4.config(justify = CENTER)

        self.entry3 = Entry(self.parent,width=10)

        self.entry3.pack()

        self.button2=Button(self.parent,text='Fire',activebackground="Blue",activeforeground="Red")

        self.button2.pack()

        self.button2.config(command=self.getExit)
        #update

        self.label5=Label(self.parent,text='Enter ID of Employee who is to be Raised:')

        self.label5.pack()

        self.label5.config(justify = CENTER)

        self.entry4 = Entry(self.parent,width=10)

        self.entry4.pack()
        self.label6=Label(self.parent,text='Enter the postion to which the employee is being raised: ')

        self.label6.pack()

        self.label6.config(justify = CENTER)

        self.entry5 = Entry(self.parent,width=20)

        self.entry5.pack()
        self.label7=Label(self.parent,text='Enter new salary for that employee:')

        self.label7.pack()

        self.label7.config(justify = CENTER)

        self.entry6 = Entry(self.parent,width=20)

        self.entry6.pack()
        self.button3=Button(self.parent,text='Update',activebackground="Blue",activeforeground="Red")

        self.button3.pack()

        self.button3.config(command=self.getEntry1)
   


def main():
    root=Tk()
    d=company(root)
    root.mainloop()

if __name__=="__main__":
    main()         
            


# In[ ]:



