while True:
    try:
        y=int(input('year:'))
        m=int(input('month:'))
        d=int(input('date:'))
        import datetime
        d1=datetime.datetime(1970,1,1)
        d2=datetime.datetime(y,m,d)
        print((d2-d1).days+1)       
    except ValueError:
        print(0)