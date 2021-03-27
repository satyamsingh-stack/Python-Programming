class A():
    def feature1(self):
        print("f1 is working")
    def feature2(self):
        print("f2 is working")

class B(A):
    def feature3(self):
        print("f3 is working")
    def feature4(self):
        print("f4 is working")

a1=A()
a1.feature1()
a1.feature2()
b1=B()
b1.feature1()
b1.feature2()

# class A():
#     def greet(self):
#         print("Hello!")
# class B(A):
#         pass
# a1=A()
# a1.greet()
# b1=B()
# b1.greet()