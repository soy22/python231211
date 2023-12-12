# 부모 클래스
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

# 자식 클래스 
class Student(Person):
    # 변수가 추가(덮어쓰기)
    def __init__(self, name, phoneNumber, subject, studentID):
        # 명시적으로 부모 초기화 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
        print("Info(학과:{0}, 학번: {1})".format(self.subject, self.studentID))

# 인스턴스 생성
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
p.printInfo()
s.printInfo()

#print(p.__dict__)
#print(s.__dict__)


