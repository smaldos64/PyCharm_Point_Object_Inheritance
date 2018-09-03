from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

"""
Her er der vist et eksemepel på, at man i Python (modsat f.eks C#) godt kan have metoder (metoden plotPoints),
der ikke tilhører nogen klasse. 
"""
def plotPoints(plotList):
    Point2DimensionalXCoordinates = []
    Point2DimensionalYCoordinates = []

    Point3DimensionalXCoordinates = []
    Point3DimensionalYCoordinates = []
    Point3DimensionalZCoordinates = []

    for point in plotList:
        if "Point_Class_2Dimension" in str(type(point)):
            Point2DimensionalXCoordinates.append(point.x_value)
            Point2DimensionalYCoordinates.append(point.y_value)
        else:
            Point3DimensionalXCoordinates.append(point.x_value)
            Point3DimensionalYCoordinates.append(point.y_value)
            Point3DimensionalZCoordinates.append(point.z_value)

    plt.plot(Point2DimensionalXCoordinates, Point2DimensionalYCoordinates, color="green")
    plt.title("Punkter i 2 Dimensioner")
    plt.axis([0, 10, 0, 10])
    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(Point3DimensionalXCoordinates, Point3DimensionalYCoordinates, Point3DimensionalZCoordinates, c="red", marker="o")
    ax.set_xlabel("x akse")
    ax.set_ylabel("y akse")
    ax.set_zlabel("z akse")
    plt.show()

    """plt.plot(PointsXCoordinates, PointsXCoordinates, color="green")
    plt.title("Punkter i 2 Dimensioner")
    plt.show()

    plt.plot(PointsXCoordinates, PointsXCoordinates, color="red")
    plt.title("Punkter i 3 Dimensioner")
    plt.show()"""

