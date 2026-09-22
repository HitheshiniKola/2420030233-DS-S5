a = 200
b = 90
c = 2

if a >= b and a >= c:
    print("a is greater")
elif b >= a and b >= c:
    print("b is greater")
else:
    print("c is greater")


import pandas as pd

data = {
    'St.NO': [101, 102, 103, 104, 105],
    'Name': ['Ram', 'Sita', 'Madhav', 'Radha', 'Sindhu'],
    'Age': [18, 19, 17, 18, 19],
    'Section': [4, 7, 2, 8, 3],
    'Branch': ['CSE', 'ECE', 'CSIT', 'CSE', 'ECE']
}

df = pd.DataFrame(data)
print(df)

df.to_csv('Student.csv')
df.to_json('Student.json')

df = pd.read_csv('Iris.csv')
print(df)

df2 = pd.read_csv('Iris.csv', index_col=0)
print(df2)

df3 = pd.read_json('sample1.json', typ='series')
print(df3)

print("Head:", df.head())
print("Head10:", df.head(10))
print("Tail:", df.tail())
print("Tail 10:", df.tail(10))
print("Info:", df.info())
print("Shape:", df.shape)
print("Describe:", df.describe)


a, b, c = 4, 5.6, 45 + 34j

print(type(a))
print(type(b))
print(type(c))


f = ["apple", "orange", "banana"]

for x in f:
    print(x)

for x in range(5):
    print(x)

for x in range(40, 4, -4):
    print(x)


def find_square(n):
    return n * n


num_to_sq = int(input())
square = find_square(num_to_sq)
print(square)


def even_odd(a):
    if a % 2 == 0:
        return "Even"
    else:
        return "Odd"


num = int(input())
print(even_odd(num))


import numpy as np

N = np.array([10, 12, 13, 14])

print(type(N))

n = np.array([23])
print(n.ndim)

p = np.array([[1, 2, 3], [4, 5, 6]])

print(p)
print(p.ndim)

h = np.ones([1])
i = np.zeros([3, 4])

print(h)
print(i)
print(type(i))

print(p[0, 2])
print(p[0, -1])

print(N[4:])
print(N[:5])


data = {
    'app': [3, 2, 0, 1],
    'orange': [0, 3, 7, 2],
    'mangoes': [4, 5, 7, 8]
}

df = pd.DataFrame(data)
print(df)

df['Guava'] = pd.Series([10, 4, 8, 2], index=[0, 1, 2, 3])
print(df)

df['Four'] = df['app'] + df['orange']
print(df)

del df['app']
df.pop('orange')

print(df)


str = "hi am hitheshini and iam stydying at KL"

s2 = """My name is Hitheshini Kola

I am currently doing my b-tech in KL University, Hyderabad

Iam from CSE dept

"""

print(str, s2, sep="!!!")

s2 = "JRNTGBRJEN"
s3 = "thbghjv rhvbytv irughbtv iurghtnh"

print(str[-6:-18])
print(str[:17])
print(str[43:])

print(s2.lower())
print(s2.find('N'))
print(len(s2))

print(str.capitalize())
print(str.title())
print(str.upper())
print(s3.swapcase())

s4 = "Hitheshini"
s5 = "Kola"

print(s4 + s5)
print(s4 + " " + s5)

txt1 = "My name is {fname},I'm {age}".format(fname="Hitheshini", age=18)
txt2 = "My name is {0},I'm {1}".format("Hitheshini", 18)
txt3 = "My name is {},I'm {}".format("Hitheshini", 18)

print(txt1, txt2, txt3, sep=" && ")


x = int(1)
y = int(4.56)
z = int("453")

a = float(3)
p = float()

g = str("honey")
h = str(5)

print(x, y, z, a, g, h, sep=",")

h = 9.456
print(int(h))


i = 1

while i < 5:
    print(i)
    i += 1


j = 1

while j < 6:
    print(j)

    if j == 3:
        break

    j += 1


k = 0

while k < 5:
    k += 1

    if k == 3:
        continue

    print(k)
