class Demo:

    def check_even(self):
        if 4 % 2 == 0:
            print("it is even")
        else:
            print("it is odd")

    def add(self):
        print(3 + 5)

d = Demo()
d.check_even()
d.add()