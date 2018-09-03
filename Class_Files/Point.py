import abc
import math
import Class_Files.PrintOnScreen
from Class_Files.PrintOnScreen import PrintOnScreen_Class

"""
Klassen Point er en abstrakt klasse. At en klasse er abstract betyder, at der ikke kan
oprettes objekter af en sådan type klasse. En abstract klasse bliver brugt som skabelon
for andre klasser, der nedarver fra den pågældende "abstracte" klasse.
I eksepmplet her nedarver klassen Point_Class_2Dimension fra klassen Point. 
Klassen Point skal have en implementering af de 3 metoder i klassen Point, som er 
erklæret med attributen @abc.abstractmethod. Det vil i tilfældet her sige metoderne:
1) __init__
2) printPoint
3) lengthToOrigo
"""
class Point_Class(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    # abstract metode som skal nedarves i klasser, der nedarver fra klassen Point
    def __init__(self, x_value = 0, y_value = 0, z_value=0):
        """SubClasses must have a Constructor"""

    @abc.abstractmethod
    # abstract metode som skal nedarves i klasser, der nedarver fra klassen Point
    def printPoint(self, x_value = 0, y_value = 0, z_value = 0):
        """Print Point koordinater"""

    @abc.abstractmethod
    # abstract metode som skal nedarves i klasser, der nedarver fra klassen Point
    def lengthToOrigo(self, x_value = 0, y_value = 0, z_value = 0):
        """Calculate distance from origo to point"""

    @staticmethod
    def calculate_Number_Of_Poins(pointList, numberOf2DimensionalPoints,numberOf3DimensionalPoints):
        for point in pointList:
            if "Point_Class_2Dimension" in str(type(point)):
                numberOf2DimensionalPoints[0] += 1
            else:
                numberOf3DimensionalPoints[0] += 1

class Point_Class_2Dimension(Point_Class):
    """
    Herunder er konstruktor metoden for klassen: Point_Class_2Dimension. Det vil sige den kode,
    der bliver kaldt, når man opretter et objekt af klassen.
    """
    def __init__(self, x_value = 0, y_value = 0):
        self.x_value = x_value
        self.y_value = y_value

    def printPoint(self):
        textToPrint = "Punktets koordinater er : (" + str(self.x_value) + "; " + str(self.y_value) + ")"
        Class_Files.PrintOnScreen.PrintOnScreen_Class.PrintTextOnScreen(textToPrint)
        textToPrint = "Punktets afstand til Origo er : " + str(self.lengthToOrigo())
        PrintOnScreen_Class.PrintTextOnScreen(textToPrint)

    def lengthToOrigo(self):
        length_to_origo = math.sqrt(math.pow(self.x_value, 2) + (math.pow(self.y_value, 2)))
        return length_to_origo

    def GetThisPointCoordinates(self):
        return self

    """
    Herunder laver vi en override af metoden __str__ . Dette bevirker, at når vi laver en 
    print sætning på et objekt af typen Point_Class_2Dimension, vil vi få udført koden i
    metoden herunder. 
    Hvis vi eksempelvis har et objekt My2PointDimenson_Objekt af klassen Point_Class_2Dimension,
    som har x koordinaten 2 og y koordinaten 3, vil sætningen : print(My2PointDimenson_Objekt)
    give teksten her på skærmen: (2; 3)
    """
    def __str__(self):
        #print(type(self))
        stringToReturn = "(" + str(self.x_value) + "; " + str(self.y_value)
        if "Point_Class_2Dimension" in str(type(self)):
            stringToReturn = stringToReturn + ")"
        else:
            stringToReturn = stringToReturn + "; "
        return stringToReturn


class Point_Class_3Dimension(Point_Class_2Dimension):
    """
    Herunder er konstruktor metoden for klassen: Point_Class_3Dimension. Det vil sige den kode,
    der bliver kaldt, når man opretter et objekt af klassen. Læg specielt mærke til, at
    konstruktoren for Point_Class_3Dimension kalder opad til den klasse Point_Claas_2Dimension, som
    den nedarver fra. Dette sker i linje 81 med syntaksen super().__init__. Altså vil man, når man
    opretter et objekt af klassen Point_Class_3Dimension få kaldt samme samme konstruktor kode,
    som når man opretter et objekt af klassen Point_Class_2Dimension. Herudover vil man også få
    udført koden i linje 92.
    """
    def __init__(self, x_value = 0, y_value = 0, z_value = 0):
        super().__init__(x_value, y_value)
        self.z_value = z_value

    def printPoint(self):
        textToPrint = "Punktets koordinater er : (" + str(self.x_value) + "; " + str(self.y_value) + "; " + str(self.z_value) + ")"
        Class_Files.PrintOnScreen.PrintOnScreen_Class.PrintTextOnScreen(textToPrint)
        textToPrint = "Punktets afstand til Origo er : " + str(self.lengthToOrigo())
        PrintOnScreen_Class.PrintTextOnScreen(textToPrint)

    def lengthToOrigo(self):
        length_to_origo = math.sqrt(math.pow(self.x_value, 2) + (math.pow(self.y_value, 2) + (math.pow(self.z_value, 2))))
        return length_to_origo

    def GetThisPointCoordinates(self):
        return self

    def __str__(self):
        if isinstance(Point_Class_3Dimension(), Point_Class):
            return super().__str__() + str(self.z_value) + ")"
        else:
            "Hvad sker der for dig Programmerings Novice i 3 dimensioner !!!"

