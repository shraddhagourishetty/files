def AverageColumn (c):
    f=open(csv,"r")
    average=0
    Sum=0
    column=len(f)
    for i in range(0,column):
        for n in i.split(','):
            n=float(n)
            Sum += n
        average = Sum / len(column)
    return 'The average is:', average

    f.close()

