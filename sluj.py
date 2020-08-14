lisk = open('url_list.txt', 'r')
l = [i.strip() for i in lisk.readlines()]

n = []
for i in l:
    if i not in n:
        n.append(i)

for i in n:
    print(i)