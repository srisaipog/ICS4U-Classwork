# Method overloading (default/optional parameters in Python)

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    @staticmethod
    def speak(times: int=1, message: str="Muffin song time *earth destruction noises*"):
        for i in range(times):
            print(message)


def main():
    s = Person("Sri", 161616)
    s.speak()
    print()
    print()
    s.speak(4)
    s.speak(3, "Bye Hi BYeasdfasdf")
    s.speak(message="we did start the fire lol xD")
    s.speak(message="I am a man of piano", times=2)

if __name__ == "__main__":
    main()