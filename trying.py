import time
#f = open('hehe.txt','a')
user = 'kajal'
date = time.strftime("%x")
review = """Nice College
Good Infra!!!
Good Placements!!!"""
appending = "#######"

#f.write(user + "\n" + date + "\n" + review + "\n" + appending + "\n")
count = 0
username = []
dates = []
reviews = []
q = []
rev = ''
with open("files/uvce.txt",'r') as k:
    for o in k:
        print(o)
        if o[0] == '#':
            count = -1
            q.append(rev)
            p = ''.join(q)
            reviews.append(p)
            rev = ''
            q = []
        elif count == 0 :
            username.append(o)
        elif count == 1:
            dates.append(o)
        elif count >= 2 :
            rev = rev + o
        count += 1
    
r = zip(username,dates,reviews)

for i in r:
    print(i)