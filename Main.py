import abc

from Class_Files.Point import Point_Class
from Class_Files.Point import Point_Class_2Dimension
from Class_Files.Point import Point_Class_3Dimension

import Class_Files.PrintOnScreen
from Class_Files.PrintInGraph import plotPoints
from Class_Files.MyInput import MyInput_Class

import random

#from abc import PluginBase

class PluginBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load(self, input):
        """Retrieve data from the input source
        and return an object.
        """

    @abc.abstractmethod
    def save(self, output, data):
        """Save the data object to the output."""

class SubclassImplementation(PluginBase):

    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)

def echo(a):
    print(a)

def AddToVariable(Variable1):
    Variable1 += 2
    Variable1 += 2

class Person:

    def __init__(self, first, last, age):
        self.firstname = first
        self.lastname = last
        self.age = age

    def __str__(self):
        return self.firstname + " " + self.lastname + ", " + str(self.age)

class Employee(Person):

    def __init__(self, first, last, age, staffnum):
        super().__init__(first, last, age)
        self.staffnumber = staffnum

    def __str__(self):
        return super().__str__() + ", " +  self.staffnumber




if __name__ == '__main__':
    a = 5
    print(a)
    print(type(a))
    print(hex(id(a)))

    a = "Lars"
    print(a)
    print(type(a))
    print(hex(id(a)))

    a = 10
    echo(a)

    a = "Thise"
    echo(a)

    a = 15
    print(a)
    AddToVariable(a)
    print(a)

    x = Person("Marge", "Simpson", 36)
    y = Employee("Homer", "Simpson", 28, "1007")

    print(x)
    print(y)

    print('Subclass:', issubclass(SubclassImplementation,
                                  PluginBase))
    print('Instance:', isinstance(SubclassImplementation(),
                                  PluginBase))

    pointList = []

    for counter in range(20):
        dimension = random.randint(2, 3)
        if 2 == dimension:
            pointList.append(Point_Class_2Dimension(random.randint(0, 20), random.randint(0, 20)))
        else:
            pointList.append(Point_Class_3Dimension(random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)))

    Class_Files.PrintOnScreen.PrintOnScreen_Class.PrintList(pointList)
    # Ovenover er vist den helt lange navngivning, hvis man "kun" lavet en import af filen
    # og ikke anvendt from syntaksen. Linje 7 : import Class_Files.PrintOnScreen

    numberOf2DimensionalPoints = [0]
    numberOf3DimensionalPoints = [0]
    # I Python kan vi ikke som i f.eks C# få ændret værdien af en integrr i en funktion.
    # Så vi er nødt til, at bruge en "kunstig" liste med et element i for at opnå
    # denne effekt !!!
    Point_Class.calculate_Number_Of_Poins(pointList, numberOf2DimensionalPoints, numberOf3DimensionalPoints)

    print("Antal 2 dimensionale punkter : %s" % (numberOf2DimensionalPoints))
    print("Antal 3 dimensionale punkter : %s" % (numberOf3DimensionalPoints))

    print("")
    UserInput = MyInput_Class.InputAnything("Tryk på en tast for at punkter i koordinatssystem")
    # Da funktionen InputAnything ligger i klassen MyInput_Class, er vi nødt til at angive dette
    # klassenavn først, før vi kan nå ind til funktionen InputAnything. Vi kan ikke direkte lave en
    # import af en fnktion i en klasse. Vi får kun mulighed for at importe ind til klasse niveau som
    # anvendt i linje 9 : from Class_Files.MyInput import MyInput_Class

    plotPoints(pointList)
    # Da funktionen plotPoints ikke ligger i nogen klasse, kan vi direkte kalde plotpoints
    # ved brug af vores import statement i linje 8 : from Class_Files.PrintInGraph import plotPoints
