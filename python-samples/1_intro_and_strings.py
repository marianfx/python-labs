print("Hello world.")

# numeric stuff
x = 1.2j # complex type
x = None # NoneTyope

y = 1 * 1 # => y = 1, int
y = 1 * 1.2 # y = 1.2, float (types alwas cast to the larger type => int to float)
z = 2 ** 3 # pow function

# In Py3 / != //
x = 10 / 3 # = 3.333 (float)
x = 10 // 3 # = 3 (int)
# Mod works just like c++ (Only it applies the 'types always cast to the larger type' rule)
x = 10 % 3 # => 1
x = 10.0 % 2 # => 1.0

# & , | , ^ , <<, >> = bitwise

# comparari
x = 10 < 20 > 15 # check them iteratively, 10 < 20, 20 > 15
# in Py2 '<>' = '!='
# '==' = 'is' ('!=' = 'is not')

#################
# strings
#################
s = r"string is raw escapes do not work"
s = """this can be multiline"""
s = "Python"\
"Line" # this is multiline too (without enter)
s = "A" * 3 # => "AAA"
isin = "A" in "Python" # false, checks if error appears in x = "Python".index("A")

s = "Format: %8s"%("this")
s = "Format: %(nume)8s" % { "nume": "Ion"}
s = "Format: {0}".format("this")

s = "Pythonic"
s[2:-4:2] # starts at 2(including => at 't'), goes to n - 4 (excluded => 'o'), with step 2 => 't'
print(s[2:-4:2])
splitted = s.split(":", 2) # face doua split-uri si dupa, pe ultima pozitie, returneaza restul ramas nesplitat

letter = chr(65) # "A"
asciicode = ord("A") # 65
hexcode = hex(2) # 0x2


##############
# instructions
##############
# switch does not exist
# do-while does not exist
# 'else' on everything executes only if no 'break' or 'throw' appears, at the end ('means success)
# else works if using 'continue'
# for x in list 
for x in range(0, 100, 1): # 100 is excluded, 1 is the step
    print(x)

###########
# meethods
##########
def myMethod(x, y, z=2, *args, **kargs):
    pass
myMethod(x=1, y=3) # good
myMethod(2, 3) # good
# myMethod(z=3, y=2) # wrong, x missing
# all methods return None by default
# the ones with default values must be the last ones in declarations
# *args always comes before **kargs, both at the end (first contains unnamed params, the second named)
# at calling, the ones with no default values must be given (in order, or named)

# to modify value of globals inside methods, use global
x = 2
def modifyX():
    global x
    x = 3

# type check
if type(x) is int:
    pass

# one can define inner private functions
def parentFunc():
    """ Here is comment summary.

    Here is comment description.
    """
    def child1():
        pass
    def child2():
        pass
    # here use child 1 and 2
    print(child1() + child2())
    