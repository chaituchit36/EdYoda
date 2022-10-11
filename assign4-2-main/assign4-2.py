lst=[]
num=int(input("enter list size:"))
for i in range(num):
    ele=int(input("enter the value:"))
    lst.append(ele)
result=map(lambda x:x+x+x,lst)
print(list(result))