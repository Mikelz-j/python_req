f = open('dataset_3363_3.txt', 'r')
s = f.read()
d = {}
ar = [i.lower() for i in s.split()]
for i in ar:
    d[i] = 0
for i in ar:
    if i in d:
        d[i] += 1
#print(d)
#print(sorted(d, key=lambda x: d.get(x), reverse=True))

list_d = list(d.items())
list_d.sort(key=lambda i: i[1], reverse=True)
#print(list_d)
#print(list_d[0][0], ' ', list_d[0][1])
r = open("rez.txt", "w")
r.write(list_d[0][0] + ' ' + str(list_d[0][1]))
r.close()
print('Ok')