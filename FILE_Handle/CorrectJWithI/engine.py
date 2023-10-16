def JTOI():
    file = open("D:\\Asif\\python\\FILE_Handle\\CorrectJWithI\\WORD.txt")
    data = file.read()

    for letter in data:
        if letter == 'J':
            print("I", end="")
        
        else:
            print(letter, end="")
    
    file.close()

JTOI()
