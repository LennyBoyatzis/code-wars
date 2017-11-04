# Any
print(any([0,0,0,1])) # True
print(any([0,0,0,False])) # False

# Enumerate
# Ever needed to loop over a list and also know where in the list you were at?
my_string = 'abcdefg'
for pos, letter in enumerate(my_string):
    print(pos, letter)

# Eval
var = 10
source = 'var * 2'
print(eval(source))

# Filter
def less_than_ten(x):
    return x < 10

my_list = [1, 2, 3, 10, 11, 12]
for item in filter(less_than_ten, my_list):
    print(item)

# Map
def doubler(x):
    return x * 2

my_list = [1, 2, 3, 4, 5]
for item in map(doubler, my_list):
    print(item)

# Zip
# Zip Objects can be converted to either arrays of tuples or dicts of key val
# pairs 
keys = ['x', 'y', 'z']
values = [5, 6, 7]
print(zip(keys, values))
