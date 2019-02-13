import datetime 

def main():
    dob = input("enter youre year of birth :")
    yearNow = datetime.datetime.now().year
    myAge = yearNow-int(dob)

    print("youre age is {}".format(myAge))

if __name__ == "__main__":
    main()    