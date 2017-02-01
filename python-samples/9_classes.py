# Obs: Classes are behind the scenes dictionaries!

class Example(object): # class example derives from object
    y = 0 # class member. is immutable, so will be specific to each instance
    lst = [1, 2, 3] # member. is mutable, so will have the same reference on all members (it's basically declared global-like)
    def __init__(self): # all must have self (are instance methods). CONSTRUCTOR
        self.x = 1 # now class has member x
        self.newlst = [1, 2, 3] # is mutable, but will be specific to each instance (is declared every time, not globally as above)

    def SomeFunc(self):
        return self.x +  self.y
    
    def OtherFunc(self):
        return "2"

    @staticmethod
    def SomeStaticMethod(): # this is static (no self)
        return 1 + 2 # cant use class members

ex1 = Example()
ex2 = Example()
ex1.newmember = "string" # can dynamically add members. will be instance-specific (ex2 will not have an member 'newmember')
del ex1.x # => from now on, x is deleted from x1 instance (dicts, doh)

# overloading = impossible (methods = keys in dicts, so there can be only one). To simulate it, use params with default values
# private: simple = put '_' in name. superduper = put '__' in name (will be renamed to _ClassName__objname)
# polimorfism = classes with the same method names

# Change stuff inside classes
# can change types
ex1.x = "string"

# can change methods
# cannot assign Example.OtherFunc because it needs to be bound to an 'self' object
ex1.SomeFunc = ex1.OtherFunc

# assignment from other objects
# now 'self' from ex1.SomeFunc will be 'self' from ex2 (only in this method)
# eg. it will actually sort of call ex2.SomeFunc and x will be 69 
# the members are for instance (eg. even iif in x1 x is deleted, now it uses the one from x2)
# can assign outide methods, but will have no self
ex2.x = 69
ex1.SomeFunc = ex2.SomeFunc

# 'self' becomes available only after the 'init' phase (ig in class body or methods)
# outside methods can access self only if assigned directly in the class body!!!

