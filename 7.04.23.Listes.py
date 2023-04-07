s = []

for i in range (0, 5):
    s.append(int(input('sxoli' + str(i + 1) + ':')))
print (s)

sum = 0

for i in s:
    sum+=i
print (sum)
for i in range (0, 5):
    print ('%d %d' % (i + 1, s[1]))

for i in range (0, 5):
    print ('sxoli %d pairnei %.2f' % (i + 1, 50000/sum*s[i]))