
###############
# lambdas
###############
func = lambda x, y, z: x + y + z
# func becomes a function with 3 params, returns their sum
# we can also make functions that return lambda (they basically return a function)
def decorate(n):
    return lambda x: x % n == 0
func = decorate(2)
func(4) # checks 4 % 2 == 0

##############
# sequences
##############
# diff between list and tuple is that tuple is immutable
lst = list() # tpl = tuple()
lst = [] # tpl = ()
lst = [1, 2] * 3 # tpl = (1, 2) * 3 => [1, 2, 1, 2, 1, 2] resp. (1, 2, 1, 2, 1, 2)
x, y, z = [1, 2, 3] # x, y, z = 1, 2, 3
lst[1:4:2] # tpl[1:4:2]
newlst = lst + lst # => concatenate. lst + tpl => ERROR

x = [i*j for i  in lst for j in range(0, 10) if i % 2 == 0] # filters lst and gets squares

# .append (add one element); .extend (add more elements). both = '+='
lst.insert(len(lst), "A") # add one element to the end
lst[1:3] = [1, 2, 3] # add if index does not exist, replace if so
lst.remove(1) # => error if does not exisst
del lst[2]
del lst[0:1] # error on invalid indexes
del lst[:] # equiv  lst.clear

# careful on  copying
x = [1, 2, 3]
y = x
y += [4] # => x = y = [1, 2, 3, 4]
y = list(x) # the correct way to do it. equivs: x.copy(), y = x[:]

# count
apparitions = x.count(2) # counts the apparitions

# sort / sorted
# key can be lambda or defined function (the same)
# the arguments must be given by name
x.sort(key = lambda x: x, reverse=False) 
x = [4, 5, 3, 2]
x = sorted(x, key=lambda x: x,reverse=True)
print(x)

# map - modifica toate elementele din iterabil (convert la list ca returneaza iterabil)
z = list(map(lambda x: x**2, lst))

# filter - filtreaza elementele
z = list(filter(lambda x: x > 2, lst))

# max(iterable, key), sum(*iterables), #reversed
# any / all = verifica daca macar unul / toate sunt true (use it with map eg)
x = [1, 2, 3]
y = [4, 5, 6]
zipped = list(zip(x, y))
# zip does x X y => zipped = [(1, 4), (2, 5), (3, 6)]
unzippedx, unzippedy = zip(*zipped)


