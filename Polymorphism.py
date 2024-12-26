class A:
    def print_hello_class(self): #the function must be overriden
        print("Hello A")

        raise NotImplementedError("This function must be override in its subclasses") # == Abstraction
    #by this line this method must be override (must do Polymorphism)

class B(A):
    def print_hello_class(self):  #the function in another place and do another job (that is Polymorphism)
        print("Hello B")

class C(A):
    def print_hello_class(self): #the function in another place and do another job (that is Polymorphism)
        print("Hello C")

var =C()
var.print_hello_class()
var2 =B()
var2.print_hello_class()