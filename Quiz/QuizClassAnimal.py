class Animal:

    def __init__(self, sound):
        self.sound = sound

    def eat(self):
        print('Eating')

    def bark(self):
        print(self.sound + " 짖는다. (Animal)")


class Dog(Animal):
    def __init__(self, sound, name):
        super().__init__(sound)
        self.name = name

    def bark(self):
        print(self.sound + " 짖는다. (Dog)")

dog = Dog("멍멍", "Joy")
dog.eat()
dog.bark()