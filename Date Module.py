#DATE module 
import datetime as d
#currunt local date
currunt_date=d.date.today()
print(currunt_date)

result = d.localtime(1545925769)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)