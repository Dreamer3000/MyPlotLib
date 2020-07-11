import bar

n = input("Insert a list of numbers, followed by spaces: ")
x = n.split()
for i in range(len(x)):
    x[i] = int(x[i])
bar.mybar(x)