x = 9

def func_1(y):
    x = 3 + y
    return x

def func_2(y):
    global x
    x -= y

x = func_1(2)
func_2(5)
print(x)

x = [2, 9, 1, 5]
i = 1
j = 2
i, x[i] = j * 2 - x[j] ** 2, 0
print(i)
print(x)