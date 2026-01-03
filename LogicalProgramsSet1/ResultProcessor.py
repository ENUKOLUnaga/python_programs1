m1,m2,m3,m4,m5=list(map(int,input().split()))
avg=(m1+m2+m3+m4+m5)/5
if m1<=35 or m2<=35 or m3<=35 or m4<=35 or m5<=35:
    print("Fail!")
elif avg>=75:
    print("Distinction")
else:
    print("Pass")