def lineCount():
    file = open("D:\\Asif\\python\\FILE_Handle\\NotStartingWithT\\story.txt", "r")
    count = 0
    for line in file:
        if line[0] not in 'T':
            count += 1
            
    file.close()
    print("No of lines not start with 'T'= ", count)


lineCount()