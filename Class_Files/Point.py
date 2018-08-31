import abc
import math
import Class_Files.PrintOnScreen
from Class_Files.PrintOnScreen import PrintOnScreen_Class

class Point_Class(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def printPoint(self, x_value = 0, y_value = 0, z_value = 0):
        """Print Point koordinater"""

    @abc.abstractmethod
    def lengthToOrigo(self, x_value = 0, y_value = 0, z_value = 0):
        """Calculate distance from origo to point"""

    @abc.abstractmethod
    def __init__(self, x_value = 0, y_value = 0, z_value=0):
        """SubClasses must have a Constructor"""

    @staticmethod
    def calculate_Number_Of_Poins(pointList, numberOf2DimensionalPoints,numberOf3DimensionalPoints):
        for point in pointList:
            if "Point_Class_2Dimension" in str(type(point)):
                numberOf2DimensionalPoints[0] += 1
            else:
                numberOf3DimensionalPoints[0] += 1

class Point_Class_2Dimension(Point_Class):
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

    def __str__(self):
        #print(type(self))
        stringToReturn = "(" + str(self.x_value) + "; " + str(self.y_value)
        if "Point_Class_2Dimension" in str(type(self)):
            stringToReturn = stringToReturn + ")"
        else:
            stringToReturn = stringToReturn + "; "
        return stringToReturn


class Point_Class_3Dimension(Point_Class_2Dimension):
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

