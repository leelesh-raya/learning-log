'''
Design a system where a Company has multiple Employees.
Each employee should be able to display:

“I work at <company_name>”

Constraint:
Employee must get the company name from the outer class, not by storing it independently.'''

class Company:
    def __init__(self):
        self.cname="SpaceX"

    class employee:
        def __init__(self, outer, name):
            self.outer=outer
            self.name=name
        def display(self):
            print(f"I'm {self.name}, I work at {self.outer.cname}")


c=Company()
e1=c.employee(c, "mahi")
e1.display()
