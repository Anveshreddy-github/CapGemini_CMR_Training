class School:
    school_name="ABC school"
    def __init__(self, name):
        self.name=name
    def get_name(self):
        return self.name

p=School("anvesh")
print(p.get_name())
print(p.school_name)
print(School.school_name)
# School.school_name="xyz"
p.school_name="pqr"
print(p.school_name)
print(School.school_name)