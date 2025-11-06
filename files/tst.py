import random

#Import all the texts
f = open('Texts', 'r')
sz = []
for line in f:
    line = line.replace("\n", "")
    sz.append(line)

# Get a random line then BUMMM
num = random.randint(0, len(sz))
print(sz[num])
