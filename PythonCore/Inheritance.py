class A:
    def print(self):
        print('A')
class B:
    def print(self):
        print('B')
class C(A):
    def print(self):
        print('C')
class D(A):
    def print(self):
        print('D')
class E(B):
    def print(self):
        print('E')
class F(B):
    def print(self):
        print('F')
class G(C,D,F,E):
    pass
g1=G()
print(g1.print())
help(g1)