def countWord():
    file = open("D:\\Asif\\python\\FILE_Handle\\find&Display\\notes.txt")
    data = file.read()

    words = data.split()
    count = 0
    for word in words:
        if (word == 'the' or word == 'The' or word == "THE"):
            count += 1
    

    print("Total number of THE in this note file: ", count)


countWord()