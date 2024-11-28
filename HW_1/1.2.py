class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)

    def __str__(self):
        return f"Employee(name='{self.name}', age={self.age}, position='{self.position}', salary={self.salary:.2f})"

employee1 = Employee("Настя", 22, "Программист", 80000)
employee2 = Employee("Маша", 25, "Бизнес-Аналитик", 60000)

employee1.increase_salary(10)
employee2.increase_salary(15)

print(employee1)
print(employee2)
