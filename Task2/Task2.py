print("\n")
print("Swallow Speed Analysis: Version 1.0")
print("\n")
count=0
sum=0
mph=[]
kph=[]
Reading1=input("Enter the Next Reading ")
if Reading1:
    if Reading1[0]=="U":
        print("Reading Saved")
        acceleration=float(Reading1[1:])
        mph.append(acceleration)
        sum=sum+acceleration
        acceleration=acceleration*1.6
        kph.append(acceleration)
        count=+1
        while True:
            Reading2=input("Enter the Next Reading ")
            if Reading2=="":
                break
            speed=float(Reading2[1:])
            if Reading2[0]=="U":
                print("Reading Saved")
                mph.append(speed)
                sum=sum+speed
                speed=speed*1.6
                kph.append(speed)
                count+=1
            
            if Reading2[0]=="E":
                print("Reading Saved")
                kph.append(speed)
                speed=speed/1.6
                sum=sum+speed
                mph.append(speed)
                count+=1
        print("Result Summary")
        print(count,"Reading Analysed") if count==1 else print(count,"Readings Analysed") 
        print(sum)
        average=sum/count
        KPH=average*1.6
        print("Max Speed: {:.2f} MPH , {:.2f} KPH".format(max(mph),max(kph)))
        print("Min Speed: {:.2f} MPH , {:.2f} KPH".format(min(mph),min(kph)))
        print("Avg speed: {:.2f} MPH , {:.2f} KPH".format(average,KPH))

    if Reading1[0]=="E":
        print("Reading Saved")
        acceleration=float(Reading1[1:])
        kph.append(acceleration)
        sum=+acceleration
        acceleration=acceleration/1.6
        mph.append(acceleration)
        count=+1
        while True:
            Reading2=input("Enter the Next Reading ")
            if Reading2=="":
                break
            speed=float(Reading2[1:])
            if Reading2[0]=="U":
                print("Reading Saved")
                mph.append(speed)
                speed=speed*1.6
                sum=sum+speed
                kph.append(speed)
                count+=1
            
            if Reading2[0]=="E":
                print("Reading Saved")
                kph.append(speed)
                sum=sum+speed
                speed=speed/1.6
                mph.append(speed)
                count+=1
        print("Result Summary")
        print(count,"Reading Analysed") if count==1 else print(count,"Readings Analysed") 
        average=sum/count
        MPH=average/1.6
        print("Max Speed: {:.2f} MPH , {:.2f} KPH".format(max(mph),max(kph)))
        print("Min Speed: {:.2f} MPH , {:.2f} KPH".format(min(mph),min(kph)))
        print("Avg speed: {:.2f} MPH , {:.2f} KPH".format(MPH,average))    
else:
    print("No readings entered. Nothing to do.")