#TASK_1

class Employee:
    def __init__(self, salary, hours_per_day):
        self.salary = salary
        self.hours_per_day = hours_per_day

    def getInfo(self):
        print("Salary: ", self.salary)
        print("Hours per day: ", self.hours_per_day)

    def addSal(self):
        if self.salary < 500:
            self.salary += 10

    def addWork(self):
        if self.hours_per_day > 6:
            self.salary += 5


employee = Employee(450, 7)
employee.getInfo()
employee.addSal()
employee.addWork()
print("Final Paycheck: ", employee.salary)

#TASK_2

class Pizza:
    def __init__(self, size, cheese, pepperoni, ham):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.ham = ham


#TASK_3

class Pizza:
    def __init__(self, size, cheese, pepperoni, ham):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.ham = ham

    def calcCost(self):
        cost = 0
        if self.size == "small":
            cost = 10 + 2 * (self.cheese + self.pepperoni + self.ham)
        elif self.size == "medium":
            cost = 12 + 2 * (self.cheese + self.pepperoni + self.ham)
        elif self.size == "large":
            cost = 14 + 2 * (self.cheese + self.pepperoni + self.ham)
        return float(cost)


#TASK_4

class Pizza:
    def __init__(self, size, cheese, pepperoni, ham):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.ham = ham

    def getDescription(self):
        return f"{self.size} pizza with {self.cheese} cheese, {self.pepperoni} pepperoni, and {self.ham} ham toppings"

class PizzaOrder:
    def __init__(self, pizzas):
        self.pizzas = pizzas

    def getDescriptions(self):
        descriptions = []
        for pizza in self.pizzas:
            descriptions.append(pizza.getDescription())
        return descriptions

pizza1 = Pizza("Large", 1, 1, 2)
pizza2 = Pizza("Small", 2, 0, 1)
pizza3 = Pizza("Medium", 1, 2, 1)

order = PizzaOrder([pizza1, pizza2, pizza3])

print(order.getDescriptions())


#Bonus_TASK

class Matrix:
    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns
        self.__matrix = [[0 for j in range(columns)] for i in range(rows)]

    def get_rows(self):
        return self.__rows

    def get_columns(self):
        return self.__columns

    def set_element(self, i, j, value):
        self.__matrix[i][j] = value

    def add_matrix(self, other_matrix):
        if self.__rows != other_matrix.__rows or self.__columns != other_matrix.__columns:
            print("Matrices cannot be added")
            return
        result = Matrix(self.__rows, self.__columns)
        for i in range(self.__rows):
            for j in range(self.__columns):
                result.__matrix[i][j] = self.__matrix[i][j] + other_matrix.__matrix[i][j]
        return result

    def multiply_matrix(self, other_matrix):
        if self.__columns != other_matrix.__rows:
            print("Matrices cannot be multiplied")
            return
        result = Matrix(self.__rows, other_matrix.__columns)
        for i in range(self.__rows):
            for j in range(other_matrix.__columns):
                sum = 0
                for k in range(self.__columns):
                    sum += self.__matrix[i][k] * other_matrix.__matrix[k][j]
                result.__matrix[i][j] = sum
        return result
