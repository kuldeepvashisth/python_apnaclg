#  in python strings are immutable(not changable)
# slicing==> when we want a specifc part/word in string
#syntax str[st idx(default=0) :endidx(default=str.len) endidx is exclude so give desire idx+1]
#stidx=jha se chaiye;  ,endidx=jha tk chaiye+1;
word="i study from apnacolloege"
print(word[13:24])

# if we traverse from backward then last index is -1 and increase in -ve towards left
letword="kuldeep"
print(letword[-3:-1])

#string formatting --> (a) format function   (b)f-strings
a=5
b=10
sum=a+b
#format function to print the value we use instead of "," de kr
print("sum of {} & {} is {}".format(a,b,sum))
print("language is {}".format("python"))

#normal formatting mai jo phele vo hi phele placeholder ko replace krega
#index fomating mai hum index de skte hai placeholder mai vo hi index ki value ayegi
#index fomat f(n) ke acc. denge
#isme phle b aayega 1 index then A(0 idx)
print("sum of {1} & {0} is {2}".format(a,b,sum))


#value-based formating
print("{a}sum of {a} & {b} is {sum}".format(a=1,b=5,sum=6))


#using f-strings
p=2
q=7
print(f"avg of {p} & {q} is {(p+q)/2}")
