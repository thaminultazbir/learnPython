def count_words():
    file = open("D:\\Asif\\python\\FILE_Handle\\EndWithE\\article.txt","r")
    count = 0
    data = file.read()
    words = data.split()
    for word in words:
        if word[-1] == 'w':
            count+=1
    print(count)
    file.close()

count_words()