"""Example of a simple class hierarchy"""

class A:
    def foo(self):
        print("A")

class B(A):
    def foo(self):
        print("B")

class C(A):
    pass

a = A()
a.foo()
b = B()
b.foo()
c = C()
c.foo()

print("MRO for class C:", C.__mro__)
