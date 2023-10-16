def count_letter():
    file = open("D:\\Asif\\python\\FILE_Handle\\UpperCaseCount\\note.txt","r")
    data = file.read()
    count = 0
    for letter in data:
        if letter.isupper():
            count+=1
    print(count)
    file.close()

count_letter()