for x in range(1,10):

    for y in range(2,10):
        #print("%d x %d = %2d" %(y,x,x*y),end='  ')
        print("{} x {} = {:2}".format(y,x,x*y),end='  ')
    print()