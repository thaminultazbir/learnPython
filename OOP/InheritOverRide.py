class Animal:
    name = ""

    def eat(self):
        print("I can Eat")


class Dog(Animal):
    def eat(self):
        print("I like to eat Bone")



D = Dog()
D.eat()