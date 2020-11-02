name=[]
for i in range(0,5):
    s=input("stdudent name:")
    name.append(s)
for i in range(0,5):
    print(name[i])
s=input("stdudent name:")
if s in name:
    print("yes")
else:
    print("no")
