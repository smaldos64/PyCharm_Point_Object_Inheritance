from Class_Files.Point import Point_Class
from Class_Files.Point import Point_Class_2Dimension
from Class_Files.Point import Point_Class_3Dimension

import Class_Files.PrintOnScreen
from Class_Files.PrintInGraph import plotPoints
from Class_Files.MyInput import MyInput_Class

import random


if __name__ == '__main__':
    pointList = []

    for counter in range(20):
        dimension = random.randint(2, 3)
        """"
        Når man opretter et objekt som man gør i linjerne herunder. Linje 26 (et objekt af klassen: 
        Point_Class_2Dimension) og linje 28 (et objekt af klassen: Point_Class_3Dimension). Så vil man
        få kaldt kontruktoren for det pågældende objekt. Denne kode er skrevet under de 2 klasser, vi har i spil
        her. Klassen Point_Class_2Dimension for et 2 dimensionelt punkt og klassen 
        Point_Class_3Dimension for et 3 dimensionelt punkt. Den kode i de 2 klasser, man får kaldt er koden 
        i metoderne der har formen : def __init__(self, og så videre.
        """
        if 2 == dimension:
            pointList.append(Point_Class_2Dimension(random.randint(0, 20), random.randint(0, 20)))
        else:
            pointList.append(Point_Class_3Dimension(random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)))

    Class_Files.PrintOnScreen.PrintOnScreen_Class.PrintList(pointList)
    # Ovenover er vist den helt lange navngivning, hvis man "kun" lavet en import af filen
    # og ikke anvendt from syntaksen. Linje 7 : import Class_Files.PrintOnScreen

    numberOf2DimensionalPoints = [0]
    numberOf3DimensionalPoints = [0]
    # I Python kan vi ikke som i f.eks C# få ændret værdien af en integer i en funktion.
    # Så vi er nødt til, at bruge en "kunstig" liste med et element i for at opnå
    # denne effekt !!!
    Point_Class.calculate_Number_Of_Poins(pointList, numberOf2DimensionalPoints, numberOf3DimensionalPoints)

    print("Antal 2 dimensionale punkter : %s" % (numberOf2DimensionalPoints))
    print("Antal 3 dimensionale punkter : %s" % (numberOf3DimensionalPoints))

    print("")
    UserInput = MyInput_Class.InputAnything("Tryk på en tast for at se punkter i koordinatssystem")
    # Da funktionen InputAnything ligger i klassen MyInput_Class, er vi nødt til at angive dette
    # klassenavn først, før vi kan nå ind til funktionen InputAnything. Vi kan ikke direkte lave en
    # import af en fnktion i en klasse. Vi får kun mulighed for at importe ind til klasse niveau som
    # anvendt i linje 9 : from Class_Files.MyInput import MyInput_Class

    plotPoints(pointList)
    # Da funktionen plotPoints ikke ligger i nogen klasse, kan vi direkte kalde plotpoints
    # ved brug af vores import statement i linje 8 : from Class_Files.PrintInGraph import plotPoints
