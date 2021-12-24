
from datetime import datetime, timedelta

def date_generation(startDate,noOfDaysInterval,totNoOfDays):

   print("startDate and Days Interval",startDate,noOfDaysInterval,totNoOfDays)
   i=0
   j=1
   masterDict={}
   l=[]
   while i < totNoOfDays:
      newDate=str(startDate + timedelta(days=i))
      aggDates=i//noOfDaysInterval
      l.append({aggDates:newDate})
      i=i+1
   return l

dates='2021-01-01'
startDate=datetime.strptime(dates,'%Y-%m-%d').date()
noOfDaysInterval=7
totNoOfDays=365
#print((startDate + timedelta(days=3)))
dateDict=date_generation(startDate,noOfDaysInterval,totNoOfDays)

inputDates=['2021-01-01','2021-01-02','2021-01-08','2021-02-01','2021-02-02','2021-02-05']

#print(dateDict[0])
print(dateDict[2].values())

for i in range(0,len(dateDict)):
    #print(i)
    for j in inputDates:
      if j in dateDict[i].values():
        print(dateDict[i].keys(),dateDict[i].values())
        #print("true")


#print(len(dateDict))
#print(dateDict)