month =  input ("Enter the name of the  month:")
date  =  int (input ("Enter the date:"))

if  month == "January" or month == "February":
   season   =  "Winter"
elif   month == "March":
   if  date  <  20:
     season = "Winter"
   else :
     season = "Spring"
elif   month == "April" or month == "May":
   season   =  "Spring"
elif   month == "June":
   if  date <  21:
     season = "Spring"
   else :
     season = "Summer"
elif   month == "July" or month == "August":
   season   =  "Summer"
elif   month == "September":
   if  date  <  22:
     season = "Summer"
   else :
     season = "Fall"
elif   month == "October"  or month == "November":
   season   =  "Fall"
elif   month == "December":
   if  date <  21:
     season = "Fall"
   else :
     season = "Winter"


print ("summer")
