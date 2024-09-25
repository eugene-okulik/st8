from dataclasses import dataclass


# class Student:
#     def __init__(self, name, last_name, group):
#         self.name = name
#         self.last_name = last_name
#         self.group = group


@dataclass
class Student:
    name: str
    last_name: str
    group: str


student1 = Student('Petia', 'Ivanov', 'ST90')
student2 = Student(name='Kolya', last_name='Petrov', group='ST99')
print(student1.last_name)
