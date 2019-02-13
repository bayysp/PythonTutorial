def main():
    writeFile = open("testing.txt", "a") #a is for writing on file
    writeFile.write("\nnama : Isan")
    writeFile.write("\nnama : Buddy")
    writeFile.close()

    readFile = open("testing.txt", "r")
    for line in readFile:
        print(line) #make output each line on file

    readFile.close()


if __name__ == '__main__':
    main()