def countWord():
    file = open("D:\\Asif\\python\\FILE_Handle\\countTotalWord\\demo.txt", 'r')
    count = 0
    data = file.read()
    words = data.split()
    for word in words:
        count += 1
    
    print("Total words are: ", count)
    file.close()


countWord()