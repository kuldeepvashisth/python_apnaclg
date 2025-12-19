'''age=int(input("enter age : "))

 tab ka space de kr likhna hai -->indentation
those which have same indentain are in 1 block

if (age<13):
    print("child")
elif( age>13 and age <18):
        print("mid")
else:
    print("adult")

username=input("enter username ")
passcode=int(input("enter pass"))
if(username == "admin" and passcode==123):
    print("logged in")
else:
    if(username!="admin"):
        print("wrong username")
    else:
        print('wrong username')
''' 
# ---> MATCH -CASE <---
# jise match krna hai condirtion se vo match mai then cases 

color=input("enter color")
match color:
    case "green":
        print("go")
    case "yellow":
        print("ready")
     #default case
    case _:  
        print("wrong color")


