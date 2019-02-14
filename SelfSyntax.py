class Val():

    valueX = 3 #first, we declare a variable called valueX

    def printValueX(self):
        print(self.valueX) #because this function was called a valueX who both of which are is in the same function,
                            # so use a self syntax

    def callPrintValueX(self):
        self.printValueX() #same with a printValueX, use a self syntax if you want use a printValueX() func


if __name__ == '__main__':
    Val()

    objectVal = Val() #create object
    objectVal.callPrintValueX() #call a function in class Val using object

#self syntax is uses for call a component which is inside the function itself