#s = "x20G14W3h6q18O5Q5W19G18Z7o11z16j18S3W19m8W14o16B16j20d10o12F5"
f = open('dataset_3363_2.txt', 'r')
s = f.read()
ar = []
srez = ''
# for i in ar:
#     if i.isdigit():
#         x = int(i)
#         print(x, end=' - ')
#         print(type(x))
#     else:
#         print(i, end=' - ')
#         print(type(i))
integ = []
streg = []
l = len(s)
i = 0
while i < l:
    s_int = ''
    a = s[i]
    while a.isdigit():
        s_int += a
        i += 1
        if i < l:
            a = s[i]
        else:
            break
    i += 1
    if s_int != '':
        integ.append(int(s_int))
    if not a.isdigit():
        streg.append(a)
for i in range(len(streg)):
    srez += (streg[i] * integ[i])
#print(srez)
r = open("rez.txt", "w")
r.write(srez)
r.close()
print('Ok')