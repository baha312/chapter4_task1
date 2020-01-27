# 1)Student #
# Создайте класс Student, конструктор которого имеет параметры name,lastname,
# department, year_of_entrance. 
# Добавьте метод get_student_info, 
# который возвращает имя, фамилию, год поступления и факультет 
# в отформатированном виде: “Вася Иванов поступил в 2017 г. на факультет:Программирование.”

class Student():
    def __init__(self, name, last_name, department, year_of_entrance):
        self.name = name
        self.last_name = last_name
        self.department = department
        self.year_of_entrance = year_of_entrance

    def get_student_info(self):
        return f"{self.name} {self.last_name} поступил в {self.year_of_entrance} г. на факультет: {self.department}."

student1 = Student(
    'Аскар',
    'Акаев',
    'Механика и Оптика',
    1961
)
print(student1.get_student_info())

student2 = Student(
    'Donald',
    'Trump',
    'Экономика',
    1964
)
print(student2.get_student_info())
