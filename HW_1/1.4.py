class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.__age = age
        self.__course = course

    def introduce(self):
        print(f"Привет, меня зовут {self.name}. Мне {self.__age} лет, и я учусь на {self.__course} курсе.")

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Ошибка: возраст должен быть больше 0!")

    def get_course(self):
        return self.__course

    def set_course(self, course):
        if 1 <= course <= 6:
            self.__course = course
        else:
            print("Ошибка: курс должен быть в диапазоне от 1 до 6!")

student = Student("Анастасия", 22, 4)

student.introduce()

student.set_age(21)
student.set_course(4)

student.introduce()
