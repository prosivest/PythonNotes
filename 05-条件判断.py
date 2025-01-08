hp=80
if (hp>70):
    # comment: 
    print('you are health')
# end if

mp=50
if (mp>70):
    # comment:
    print('you are health') 
else:
    print('you are out of mp')

at=65
if (at>90):
    # comment: 
    print(1)
elif (at>70):
    # comment: 
    print(2)
else:
    # comment: 
    print('weak')
# end if

# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

height = 1.74
weight = 66

bmi = weight/height/height
print(bmi)

if (bmi>32): 
    print('过于肥胖')
elif (bmi>28):
    print('肥胖')
elif (bmi>25):
    print('过重')
elif (bmi>18.5):
    print('正常')
else:
    print('过轻')
# end if

