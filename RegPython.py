import re


def main():
    readFile = open("testing.txt", "r")

    for line in readFile:
        if re.search("(Han|Ba)yu", line):
            print(line)
    readFile.close()


if __name__ == '__main__':
    main()
