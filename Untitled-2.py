class university:
    def __init__(self,collegename,address):
        self.collegename=collegename
        self.address=address
    def display(self):
        print("collegename",self.collegename)
        print("address",self.address)
class school:
    def __init__(self,schoolof,name):
        self.schoolof=schoolof
        self.name=name
    def display(self):
        print("schoolof",self.schoolof)
        print("Name",self.name)
class department(university):
    def __init__(self,collegename,address,dept,schoolof,name):
        university.__init__(self,collegename,address)
        self.dept=dept
        self.school=school(schoolof,name)
    def display(self):
        university.display(self)
        print("DEPARTMENT",self.dept)
        self.school.display()
d=department("DAYANANDA SAGAR UNIVERSITY","HAROHALLI DEVARAKAGALLAHALLI NEAR RAMNAGARA","SCHOOL OF ENGINEERING","Cyber security","Poorvika")
d.display()