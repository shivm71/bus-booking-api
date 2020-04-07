# Create your models here.from django.db import models
from django.conf import settings
from django.db import models




class Ticket(models.Model):
     ticdate = models.DateField(blank=True, null=True)
     ticuser = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True, null=True)
     ticno = models.IntegerField(default=0)
     ticbooked = models.BooleanField(default=False)
     ticcancel_time = models.DateTimeField(blank=True, null=True)  
     def __str__(self):
        return (str(self.ticno))    
      

     
class Date(models.Model):
    date = models.DateField(blank=True, null=True) 
    ticket = models.ManyToManyField(Ticket, null=True,blank =True)
    toshow = models.BooleanField(default=False)
    def __str__(self):
        return str(self.date) 
        
class Usertotic(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True, null=True)
    ticket = models.ManyToManyField(Ticket,null=True )             
        

    
            
    


    

# # Create your models here.
# class Item(models.Model):
#     title = models.CharField(max_length=100)
#     price = models.FloatField()
#     discount_price = models.FloatField(blank=True, null=True)
#     category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
#     label = models.CharField(choices=LABEL_CHOICES, max_length=1)
#     def __str__(self):
#         return self.title
# class OrderItem(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True, null=True)
#     ordered = models.BooleanField(default=False)
#     item = models.ForeignKey(Item, on_delete=models.CASCADE,blank=True, null=True)
#     quantity = models.IntegerField(default=1)
#     def __str__(self):
#         return str(self.item.title+" "+self.user.username+" "+str(self.quantity))    
# class Order(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True, null=True)
#     items = models.ManyToManyField(OrderItem,null=True,blank = True)
#     ordered = models.BooleanField(default=False)    
