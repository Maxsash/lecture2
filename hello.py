print('Hello, there!')

#f denotes the use of format string
name = input()
print(f"Hey, {name} !")

#conditions
x=21
if x>0:
    print("x is positive")
elif x<0:
    print("x is negative")
else:
    print("x is zero")

#tuple
coordinates = (10.0, 20.0)
#list
names = ['Alice', 'Bob', 'Charlie']
#set  | no item shows up twice | orderless
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(2)
print(s)
#dictionary
ages = {"Alice": 22, "Bob": 42}
ages["Charlie"] = 30
ages["Alice"] += 1
print(ages)

#loops
for i in range(5):
    print(i)
for id, name in enumerate(names):
    print(str(id) + name)