score = 72
match score:
    case 100:
        print('满分')
    case x if x<100 and x>=90:
        print('优秀')
    case x if x<90 and x>=75:
        print('合格')
    case 74|73|72|71|70:
        print('一般')
    case _:
        print('不合格')
