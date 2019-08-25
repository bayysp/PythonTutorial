def printPeople(*people): #infinite argument, this variable has more data
    for output in people:
        print(output)


if __name__ == '__main__':
    printPeople("bayu", "ray", "steven", "billy") #send a more string value and will get in function as infiniteArgument