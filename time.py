import datetime
s=input("please input a time")
format="%H:%M:%S"
t=datetime.datetime.strptime(s,format)
t=t+datetime.timedelta(minutes=5)
t=t+datetime.timedelta(seconds=30)
print (t.strftime(format))