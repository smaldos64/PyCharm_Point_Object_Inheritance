class PrintOnScreen_Class():
    def PrintTextOnScreen(stringToPrintOnScreen):
        print(stringToPrintOnScreen)

    def PrintList(ListToPrint):
        counter = 1
        for point in ListToPrint:
            print("Punkt nummer %d : %s" % (counter, point))
            counter += 1
