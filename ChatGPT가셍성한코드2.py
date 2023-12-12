# Person 클래스 정의
class Person:
    def __init__(self, person_id, name, phone_num):
        # 초기화 메서드: 객체 생성 시 호출되며, 멤버 변수를 초기화합니다.
        self.id = person_id  # ID
        self.name = name     # 이름
        self.phone_num = phone_num  # 전화번호

    def print_info(self):
        # 정보를 출력하는 메서드
        print(f"ID: {self.id}, Name: {self.name}, Phone Number: {self.phone_num}")


# Manager 클래스는 Person 클래스를 상속받음
class Manager(Person):
    def __init__(self, person_id, name, phone_num, skill):
        # 부모 클래스의 초기화 메서드 호출
        super().__init__(person_id, name, phone_num)
        self.skill = skill  # Manager 특유의 스킬 추가

    def print_info(self):
        # 부모 클래스의 print_info 메서드 호출
        super().print_info()
        print(f"Skill: {self.skill}")


# Employee 클래스는 Person 클래스를 상속받음
class Employee(Person):
    def __init__(self, person_id, name, phone_num, title):
        # 부모 클래스의 초기화 메서드 호출
        super().__init__(person_id, name, phone_num)
        self.title = title  # Employee 특유의 직급(Title) 추가

    def print_info(self):
        # 부모 클래스의 print_info 메서드 호출
        super().print_info()
        print(f"Title: {self.title}")


# Alba 클래스는 Person 클래스를 상속받음
class Alba(Person):
    pass  # 추가적인 멤버 변수나 메서드가 없기 때문에 pass 문 사용


# 샘플 코드
people = [
    Manager(1, "John Manager", "123-456-7890", "Leadership"),
    Employee(2, "Jane Employee", "987-654-3210", "Software Engineer"),
    Alba(3, "Bob Alba", "111-222-3333"),
    Manager(4, "Alice Manager", "555-666-7777", "Project Management"),
    Employee(5, "Eva Employee", "888-999-0000", "Data Scientist"),
    Alba(6, "Charlie Alba", "444-555-6666"),
    Manager(7, "David Manager", "777-888-9999", "Communication"),
    Employee(8, "Ellen Employee", "111-222-3333", "Product Manager"),
    Alba(9, "Frank Alba", "222-333-4444"),
    Manager(10, "Grace Manager", "444-555-6666", "Problem Solving"),
]

# 생성된 객체들의 정보 출력
for person in people:
    person.print_info()
    print()
