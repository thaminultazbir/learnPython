def Display_word():
    file = open("D:\\Asif\\python\\FILE_Handle\\displayLessThan 4char\\note.txt")
    data = file.read()
    words = data.split()

    for word in words:
        if (len(word) < 4):
            print(word)
    


Display_word()