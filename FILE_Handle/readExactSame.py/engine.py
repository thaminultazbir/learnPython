def read_file():
    file = open("D:\\Asif\\python\\FILE_Handle\\readExactSame.py\\demo.txt","r")
    for line in file:
        print(line, end="")
    file.close()

read_file()