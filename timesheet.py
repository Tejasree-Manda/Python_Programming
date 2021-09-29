class Employee:
    def __init__(self, empname, empid, empsal, empdept):
        self.name = empname
        self.name = empid
        self.name = empsal
        self.name = empdept
    def timesheet(self,hrs,date,activity,description):
        self.hrs = hrs
        self.date = date
        self.activity = activity
        self.description = description
    def display(self, empname, empid, empsal, empdept):
        print("name :", empname, " ,id :", empid, " ,salary :", empsal, " ,department :", empdept,)
    def displaytime(self,hrs,date,activity,description):
        print("hrs :", hrs, ",date :",date, ",activity:", activity, ",description:", description)
e1 = Employee("ada", 20998, 20000, "do")
e1.display("ada", 20998, 20000, "do")
Employee("aradhya", 20898, 20700, "do").display("aradhya", 20898, 20700, "do")
d1=Employee(8,'05-09-2010','explaining the solution','about solving skills')
d1.displaytime(8,'05-09-2010','explaining the solution','about solving skills')

