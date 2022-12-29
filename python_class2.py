'''

    1. 상속(inheritance)
        1) class 자식 클래스 이름(부모 클래스 이름)
                pass
        2) super()
            - 부모 클래스의 속성 및 매서드를 가져와야할 때 사용한다
            super.init()
            - 부모 클래스에서 정의되어 있던 생성자로 사용한다는 의미



'''


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_human(self):
        print("==== 인적 사항====")
        print(f"이름 : {self.name}")
        print(f"나이 : {self.age}")


class Teacher(Human):
    def __init__(self, name, age, teacher_id, subject, salary):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.subject = subject
        self.salary = salary

    def show_teacher(self):
        print("====교직원 카드====")
        print(f" 교직원 번호 : {self.teacher_id}")
        print(f" 담당 과목 : {self.subject}")
        print(f" 급여 : {self.salary}")


teacher = Teacher("이순신", 40, 1, "컴퓨터", 300)
teacher.show_human()
teacher.show_teacher()

# student_id, grade, score
print()

class Student(Human):
    def __init__(self, name, age, Student_id, grade, score):
        super().__init__(name, age)
        self.Student_id = Student_id
        self.grade = grade
        self.score = score

    def show_student(self):
        print("====학생 카드====")
        print(f" 학생 번호 : {self.Student_id}")
        print(f" 학생 등급 : {self.grade}")
        print(f" 학생 점수 : {self.score}")

student = Student("이경빈", 27, 20221229, 1, 100)
student.show_human()
student.show_student()