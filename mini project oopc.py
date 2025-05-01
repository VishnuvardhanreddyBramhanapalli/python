from abc import ABC, abstractmethod
class person(ABC):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @abstractmethod
    def show_info(self):
        pass
class student(person):
    def __init__(self, name, age,roll_no):
        super().__init__(name, age)
        self.roll_no=roll_no
        self.marks=[]
    def add_marks(self,mark):
        self.marks.append(mark)
    def get_average(self):
        return sum(self.marks)/len(self.marks)
    def show_info(self):
        print(f"name:{self.name},age:{self.age},roll no:{self.roll_no},average:{self.get_average()}")
class special_student(student):
    def __init__(self, name, age, roll_no,scholarship):
        super().__init__(name, age, roll_no)
        self.scholarship=scholarship
    def show_info(self):
        super().show_info()
        print(f"scholarship for {self.name} is rupees{self.scholarship}")
s1=student("raj",19,1)
s1.add_marks(98)
s1.add_marks(89)
s2=special_student("rakesh",20,2,5000)
s2.add_marks(99)
s2.add_marks(95)
students=[s1,s2]
for student in students:
    student.show_info()