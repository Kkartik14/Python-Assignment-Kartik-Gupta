# Write a program to convert given seconds into hours, minutes and remaining seconds.

time=int(input("enter the seconds "))
if time>=3600:
    hours=time//3600
    a=time%3600
    if a>60 :
        minss=a//60
        secss=a%60
        print("no of hours: "+str(hours))
        print("no of minss: "+str(minss))
        print("no of secss: "+str(secss))
if time>60 and time<3600 :
    mins=time//60
    secs=time%60
    print("no of mins: "+str(mins))
    if secs<60:
       print("no of secs: "+str(secs))
if time<60:
    print("no of secs: "+str(time))