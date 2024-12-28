# mylist=[1,2,3,4,5,6,7,8,9,10]
# print("let's calculate the  list")
# c=0
# for i in mylist :
#     print(f"=> {i}")
#     c=+i
#     print(f"The total number is {c}")
# friends=input("Enter the name and the last name of your friends separated by a comaa \n").capitalize()
# friendslist=friends.split(",")
# mylist=[]
# for i in friendslist :
#     s=i.split(" ")
#     print(s)
#     mylist.append(s)
# for rex in mylist :
#     print(f"{rex[0][0].capitalize()}.{rex[1][0].capitalize()}.")    
    
import random
a=random.shuffle([1,2,3])
print(a)

guss=int(input("Guss the number berween 1,10 \n"))
while guss not in range(11):
    print("Invalid Number")
    guss=int(input("Guss the number berween 1,10"))
else:
    print("Accepted Number")
    
    
    
    