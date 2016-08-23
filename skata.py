f = open('alex.py', 'r')
count = 0
for line in f.readlines():
    stripe = line.strip()
    count += 1
    print(line)
    print(stripe)
    if stripe == '' or stripe[0] == '#':
        count -=1
f.close()
print(count)
