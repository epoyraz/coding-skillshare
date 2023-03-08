a = 5 # integer
b = 5.0 # float
c = "5" # string
d = True # boolean

i = a + b
print(i)
#j = a + c
#print(j)

# conversion
k = str(a) + c
print(k)
l = int(c) + a
print(l)

###### list ######
e = [1, 2, 3] # list
e = ["apple", "orange", "banana"] # list
e.append("cherry") # adds an element to the list
e.remove("apple") # removes an element from the list
e[0] # results in "orange"
e[1] # results in "banana"
e.sort() # sorts the list
e.reverse() # reverses the list  

#### set ####
g = {1, 2, 3} # set
g.add(4) # adds an element to the set
g.remove(2) # removes an element from the set
g.add(3)
g.add(3)
g.add(3)


h = {"a": 1, "b": 2, "c": 3} # dictionary
h["a"] # results in 1
h["b"] # results in 2
h["d"] = 4 # adds a key-value pair to the dictionary
h["a"] = 5 # changes the value of a key-value pair in the dictionary
h.pop("b") # removes a key-value pair from the dictionary
h.values() # results in [1, 3, 4, 5]


### string operations ###
s = "Hello, World!"
s[0] # results in "H"
s[1] # results in "e"
s[2] # results in "l"
s[3] # results in "l"
s[4] # results in "o"

s[0:5] # results in "Hello"
s[7:12] # results in "World"
s.lower() # results in "hello, world!"
s.upper() # results in "HELLO, WORLD!"
s.replace("H", "J") # results in "Jello, World!"
s.split(",") # results in ["Hello", " World!"]