class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def play(self):
        print("Child is playing")

obj = Child()
obj.greet()  # inherited
obj.play()   # own method
