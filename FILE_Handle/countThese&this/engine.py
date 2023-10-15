def count_word():
    file = open("D:\\Asif\\python\\FILE_Handle\\countThese&this\\articles.txt")
    data = file.read()
    words = data.split()
    count = 0
    for word in words:
        if word == 'this' or word =='these':
            count += 1

    
    print("total This and These word In this article: ", count)


count_word()