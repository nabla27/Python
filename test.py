import matplotlib.pyplot as plt
import numpy as np


print("Enter the degree of the polynomial.")
deg = int(input())

print("Enter the coefficient for each order.")
tmp_num = 0
conf = []
while tmp_num <= deg:
    print("Enter the ",tmp_num,"'s order confficient." )
    conf.append(1)
    conf[tmp_num] = int(input())
    tmp_num += 1

print("The function is ...")
if conf[deg] != 1:
    print("f(x) = ", conf[deg], "x^", deg, end="")
else:
    print("f(x) = ", "x^", deg, end="")
tmp_num = 1
while tmp_num < deg:
    if conf[deg-tmp_num] != 1:
        print(" + ", conf[deg-tmp_num], "x^", deg-tmp_num, end="")
    else:
        print(" + ", "x^", deg-tmp_num, end="")
    tmp_num += 1
print(" + ", conf[0])

x = np.linspace(-5, 5, 50)
def func(var):
    tmp_num = 0
    val = 0
    while tmp_num <= deg:
        val += conf[tmp_num] * var ** tmp_num
        tmp_num += 1
    return val

y = func(x)

plt.plot(x,y)
plt.show()