def concat(*args,sep = "/"):
    return sep.join(args)

print(concat('earth','mars','venus'))


args = [3,10]
list(range(*args))

def parrot(voltage,state = 'a stiff',action = 'voom'):
    print("--This parrot would't",action,end = ' ')
    print("if you put",voltage,"volts through it.",end = ' ')
    print("E's",state,"!")

d = {"voltage":"four million","state":"bleedin' demised","action":"voom"}

parrot(**d)

def make_incrementor(n):
    return lambda x: x+n

f = make_incrementor(42)

f(0)
f(1)

pairs = [(1,'one'),(2,'two'),(3,'three'),(4,'four')]
pairs.sort(key = lambda pair:pair[1])
print(pairs)

def my_function():
    """Do nothing,but document it.

    No,really,it doesn't do anything.
    """
    pass

print(my_function.__doc__)
help(my_function)

def f(ham:42,eggs: int = 'spam') ->"nothing to see here":
    print("Annotations:",f.__annotations__)
    print("arguments:",ham,eggs)

f('wonderful')

a = [66.25,333,333,1,123,5]
print(a.count(333),a.count(66.25),a.count('x'))
a.insert(2,-1)
print(a)
a.append(333)
print(a)
a.index(333)
a.remove(333)
a.sort()
a.pop

stack = [3,4,5]
stack.append(6)
for i in range(6,100):
    stack.append(i)
stack
