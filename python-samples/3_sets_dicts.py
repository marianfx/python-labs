
# both sets and dicts are IMMUTABLE and UNORDERED (cannot have index)
# sets keep elements one time only
# cannot apply [], + etc. use .add, .remove/discard/clear
s = set()
s = {} # INCORRECT => IS DICTIONARY. use s = {1, 2, 3}

# x | y = UNION (= .union(), .update() ) 
# x & y = INTERSECT (=.intersection)
# x - y = DIFF (=.difference)
# x ^  y = SYM DIFF (A | B - A&B) (.symmetric_difference(nupoateaveamaimultiparams))
# x <= y = SUBSET (.issubset)
# x >= y = UPPERSET
# .pop() elimina totusi primul element (chiar daca e unordered)
newset = {i for i in range(0, 11)}
x = frozenset({1, 2, 3}) # immutable


x = {} # x = dict()
x = {"abs": 1} # x = dict({"abs": 1}), x = dict(abc=1)
x["abc"] = 2 # seteaza cheia (chiar daca nu exista)
a = x["abc"] # obtine valoarea; daca nu exista cheia, da eroare
# pt. a nu mai da valoare, use .setdefault("abc", 2)
# to delete: del x["abc"] - sterge cheia
newdict = {i:i for i in range(0, 12)}
for key in newdict.keys():
    pass
for value in newdict.values():
    pass
# items to do the basic for, as tuples; and tuples can be sorted
for i in sorted(x.items(), key=lambda x: x[1]):
    pass # sort by value

