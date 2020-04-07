from ticket.models import Date,Ticket
import datetime

# print(Date.objects.all())
# Date.objects.all().delete()
# Ticket.objects.all().delete()
for j in range(4):

    Current_Date = (datetime.date.today()+ datetime.timedelta(days=j)) 
    dateob, datcreated = Date.objects.get_or_create(
        date = Current_Date,
        )
    if datcreated:
        for i in range(1,6):
            tocreate, created = Ticket.objects.get_or_create(
            ticdate = Current_Date,
            ticno = i,
            )
            # if created:
            #     print(tocreate.ticbooked)
            # else:
            #     print("not corrected")
            
            dateob.ticket.add(tocreate)
            # if created:
            #     print("working")
    else:
         print("date already there",Current_Date)
            

        
        


# print(Ticket.objects.all())
# Current_Date = (datetime.datetime.today()+ datetime.timedelta(days=1)).strftime ('%Y-%m-%d') # format the date to ddmmyyyy
# print(Current_Date)



