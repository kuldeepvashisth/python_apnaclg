# while loop
# n=int(input("enter n"))
# cnt=1
# while (cnt<=10):
#     print(cnt*n)
#     cnt+=1

# # break and continue also applicable same as here
# n=1
# while(n<=10):
#     if(n%2==0):
#         n+=1
#         continue
#     print(n)
#     n+=1


#for loop mai "in"==> memebership operator hai
s="hello"
# we can use "in" both

# if 'o' in s:
#     print("yes exist")
# for i in s:
#     print(i)

# for i in range(n) ==> it prints from 0 to n-1

word="artificial intelligence"
cnt=0
for ch in word:
    if(ch=='i' or ch=='a'or ch=='e' or ch=='o' or ch=='u'):
        cnt+=1
print(cnt)  

# range f(n)==> range(start,stop,step) {where stop is excluded}
n=int(input("enter n :"))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)    