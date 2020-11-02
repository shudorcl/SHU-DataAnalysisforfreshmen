dic=dict(zhang=180,wang=160,zhao=170,ding=165,li=175)
for i in dic:
    print(i,":",dic[i])
s=input("student name?")
h=dic[s]
for i in dic:
    if dic[i]>h:
        print(i)
