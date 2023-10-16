def count_hash():
    file = open("D:\\Asif\\python\\FILE_Handle\\HashDisplay\\matter.txt","r")
    data = file.read()
    for letter in data:
        print(letter, end="#")

    file.close()

count_hash()