lisk = open('ya_url_list.txt', 'r')
l = [i.strip() for i in lisk.readlines()]

n = []
for i in l:
    if '.PDF' not in i:
        n.append(i)
for i in n:
    print(i)