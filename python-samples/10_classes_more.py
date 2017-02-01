##############
# Inheritance
##############
class Base1(object):
    def __init__(self):
        self.x = 1
    def Method(self, xint):
        print("Method from A")

class Base2(object):
    def __init__(self):
        self.y = 2
    def Method(self, xint):
        print("Method from B")

class Derived(Base1, Base2):
    def __init__(self):
        # must call init on base to use  their fields (inits dicts)
        # Obs: The calls are from right to left, so Base1 here will overwrite any same-name objects/parameters from Base2
        Base2.__init__(self)
        Base1.__init__(self) 

    def Method(self):
        print("This will override any base method from Base1 or Base2 cause  of dict mode.")
        print("Also, calling the method with params will produce errors, caus it aint having params no more.")
    
    def __str__(self): # toString. call string = str(myDerivedObject)
        return str(self.x)
    
    def __eq__(self, newvalue): # comparing two Derived Objects
        return self.x == newvalue.x
    
    def __contains__(self, value): # the 'in' operator
        return True

    lst = [1, 2, 3, 4]
    def __iter__(self): # init of the iterators (eg in for)
        self.pos = -1
        return self
    def __next__(self): # taking one element
        self.pos += 1
        if self.pos == len(self.lst):
            raise StopIteration # the way to stop
        return self.lst[self.pos]
    
    def __len__(self):
        return 1
    def __getitem__(self, key):
        return self.lst[key]
    def __setitem__(self, key, value):
        self.lst[key] = value
    

d = Derived()
istrue = isinstance(d, Derived)
istrue = isinstance(d, Base1)
istrue = issubclass(Derived, Base1)
isfalse = issubclass(Base1, Base2)
# obs: inheritance is not needed for poly to work (it simply assigns / replaces methods in the dict)


################
# Magic methods
################
# = everything with __namehere__ which are placeholders for others (eg. constructors, operators, tostring etc)

# __init__ = constructor
# __ repr__ / __str__ = toString (every str call)
# __lt__, __eq__ etc = comparison operators
# __add__, __sub__ etc = arith operators
# __bool__ = the truth value


####################
# Context manager
####################
with open("file") as f: # here can add more
    pass # do something with f. it has defined the __exit__ method so it autocloses
# One must define:
# __enter__(self) : define what happens at declaration (eg. open file)
# __exit__(self, exc_type, exc_val) : define what happens after the block is executed (eg. close file). If exception happens, exception params are given.