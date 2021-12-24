
from datetime import datetime, timedelta


#this below function  generates the date in the intervals of 7 and returns the list
def date_generation(startDate,noOfDaysInterval,totNoOfDays):

   print("startDate and Days Interval",startDate,noOfDaysInterval,totNoOfDays)
   i=6
   masterDict={}
   l=[]
   while i <= totNoOfDays:
      newDate=str(startDate + timedelta(days=i))
      l.append(newDate)
      i=i+7
   return l

dates='2021-01-01'
startDate=datetime.strptime(dates,'%Y-%m-%d').date()
noOfDaysInterval=7
totNoOfDays=365
#print((startDate + timedelta(days=3)))
dateDict=date_generation(startDate,noOfDaysInterval,totNoOfDays)

print(dateDict)

#newDate=str(startDate + timedelta(days=7))

inputDates=['2021-01-01','2021-01-02','2021-01-08','2021-02-01','2021-02-02','2021-02-05']

#loop to iterate through 2 list and compare the elements

i=0 # input dates counter
j=0 # interval 7 dates list counter
tempList=[]
outPutList=[]
print("len ",len(inputDates))
while i < len(inputDates):
    print(f" i={i} date value {inputDates[i]},j={j} date values {dateDict[j]}")
    if inputDates[i] <= dateDict[j]: # comparing i element with j element and if ist less then increase the j element and if the templist is not empty then add the templist to original list
        tempList.append(inputDates[i])
       # print("i=",i)
        i=i+1
        print("adter",i)
        print("templist",tempList)
    else:

        j=j+1
        print("j=", j)
        if len(tempList) != 0:
            outPutList.append(tempList)
        tempList=[]
outPutList.append(tempList)

print("output" , outPutList)
