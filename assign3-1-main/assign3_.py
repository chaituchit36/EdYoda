def juk():
    sum=0
    for ele in lst:
        sum+=ele
    print("the sum is",sum)
lst=[]
num=int(input("enter list size:"))
for i in range(num):
    ele=int(input("enter the value:"))
    lst.append(ele)
print(lst)
juk()            