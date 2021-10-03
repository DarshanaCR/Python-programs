flag=1
n=eval(input())
sentence=list(map(str,input().split()))
for i in range (1,n+1):
    if str(i)!=sentence[i-1] and sentence[i-1]!="mumble":
        flag=0
        break
print('makes sense' if flag is 1 else 'something is fishy')
