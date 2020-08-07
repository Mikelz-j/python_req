f = open('dataset_3363_4.txt', 'r')
stud = [i.strip() for i in f.readlines()]
f.close()
sr_1 = 0
sr_2 = 0
sr_3 = 0
sr_studs = []
for i in stud:
    x = i.split(';')
    sr_st = 0
    for j in range(len(x)):
        if j != 0:
            sr_st += int(x[j])
        if j == 1:
            sr_1 += int(x[j])
        if j == 2:
            sr_2 += int(x[j])
        if j == 3:
            sr_3 += int(x[j])
    sr_studs.append(sr_st/(len(x)-1))
    #print(x[-1]) # средняя оценка студента

r = open("rez.txt", "w")
for i in sr_studs:
    r.write(str(i) + '\n')
r.write(str(sr_1/len(stud)) + ' ')
r.write(str(sr_2/len(stud)) + ' ')
r.write(str(sr_3/len(stud)))
r.close()
print('Ok')