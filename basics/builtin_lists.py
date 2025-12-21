#lists []=>
#1.when data like marks (bhot sare diff variables)
#2.they are mutable sequence 
#3.can store differet types of data in a list
#4.slicng is also same as strings
#5. append(value)-> ad the elemnt at end
#6. insert(idx,value)->to insert at idx
#7.sort and revrse f(n) also
#8. remove(value)->dlt first occurance
#9. l.index(value)-> give idx of value and similarly count(value)


marks=[99,89,"abc",12]
print(marks[2])
print(marks[1:4])

nums=[1,23,8,9,4]
idx=0
x=8
for val in nums:
    if(val==x):
        print(f"{x} is at idx={idx}")
        break
    idx+=1

# --------------***-----------***------------******----------------****---------

#tupple() ->immutable
#1.same index(val) and count(val) function as list
#for single value tuple give value then a "," so that its keep atype of tuple 
tup=(1,2,3)
print(type(tup),tup[1])

# --------------***-----------***------------******----------------****---------


#Dictionaries{} --> key:value pairs,mutable,unordered
#1. keys()->give all keys ,same as values() f(n)
#2. d.items()->return all key value pairs
#3. to aces itenm in dict = dict.get(key)->val {if key not exist give none}
#4.dict.update({ ---}) =>we can update a key value pair

# info={
#     "name":"kd",
#     "age":20,
#    "subjects":["sci","sst","eng"],
#    3.14:"PI"
# }
# print(info["subjects"],info[3.14])
# dict_keys=info.keys()
# dict_kvals2=list(info.keys())
# print(dict_keys)
#dict_vals=info.value() 

# --------------***-----------***------------******----------------****---------

#Set--> ye khud to mutable ho skta hai but iske andr ke items imutable hona chaiye
#     (OR)only immutable data types can be put in a set
# implement by {} --> size of set is only no of unique elements
#1. s.remove(value)
#2. s.clear dlt all
#3. s.pop-->removes a random value
#4. s.union(set2)
#5. s.intersection(set2)
# s={1,2,2,2,3}  
# s.add(5)

#for initialisng an empty set -==>
#empty_set={} <--=  ye ek dictionary hai not a set
#empty_set=set() 


#.que-> print all unique subject


# for tup in info:
#     print(tup[0])
# empty_set=set()
# for i in info:
#     empty_set.add(i[1])

# set2=set()

# for name,course in info:
#     (set2.add(course))
    
# print(set2)

#for name,course in info:
    #   if(course=="maths"):
    #     print(name)  
dict={}
#there can be 2 case ,key(name) either can exist orr no
inform=[
 ("a","maths"),
  ("b","sst"),
   ("s","maths"),
    ("d","sci"),
    ("a","english")
]


for name,course in inform:
    # when key not exist initially
    if(dict.get(name)==None):
        dict.update({name:set()})
        dict[name].add(course)
        # when key exist
    else:
        dict[name].add(course)    

print(dict)
