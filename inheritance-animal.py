class Animal:
    def __init__(self, name, sleep_duration):
        self.name = name
        self.sleep_duration = sleep_duration
    def sleep(self):
        print("{} sleeps for {} hours".format(self.name, self.sleep_duration))

class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

if __name__ == "__main__":
    dog = Dog("Beagle", 12)
    dog.sleep()
    dog.bark()
