from django.db import models
from datetime import datetime
# Create your models here.
#Sports
class Sport(models.Model):
    SpName=models.CharField(max_length=100,verbose_name='Sport Name')
    PricMil=models.DecimalField(max_digits=200,decimal_places=4,verbose_name='Military price')
    PricCivil=models.DecimalField(max_digits=200,decimal_places=4,verbose_name='Civil price')
    MinAge=models.IntegerField(verbose_name='Minimum Age')
    MaxAge=models.IntegerField(verbose_name='Maximum Age')
    Forl=models.BooleanField(default=False,verbose_name='For Ladies')
    def __str__(self):
        return self.SpName  

#Sessions 
class Session(models.Model):
    mus=[('Coral','Coral'),('Guitar','Guitar'),('Violine','Violine'),('Act','Act'),('Piano','Piano')]
    vi=[
        ('Sun','Sun'),('Mon','Mon'),('Tus','Tus'),('Wed','Wed'),('Thu','Thu'),('Fri','Fri'),('Sat','Sat')
    ]
    SName=models.CharField(max_length=100,null=True,blank=True,choices=mus,verbose_name="Music Session Name")
    sport=models.ManyToManyField(Sport,null=True)
    Start=models.TimeField(verbose_name='Begin at')
    End=models.TimeField(verbose_name= 'Ends at')
    Day=models.CharField(max_length=100,null=True,choices=vi)
    def __str__(self):
        return self.Day

#Our players
class Player(models.Model):
    ch=[('Civil','Civil'),('Military','Military')]
    Name=models.CharField(max_length=100,null=True)
    Type=models.CharField(max_length=50,null=True,choices=ch)
    Age=models.IntegerField()
    sport=models.ManyToManyField(Sport)
    sessions=models.ManyToManyField(Session)
    Active=models.BooleanField(default=True)
    Brother=models.BooleanField(default=False,verbose_name='Have a brother')
    Attendant1=models.CharField(max_length=40,null=True,verbose_name='Parent')
    Attendant2=models.CharField(max_length=40,null=True,blank=True,verbose_name='Additional Parent')
    FatherProf=models.CharField(max_length=60,null=True,verbose_name='Fathers profession')
    Email=models.EmailField(verbose_name='Email',null=True)
    PPhone=models.CharField(max_length=14,null=True,verbose_name='Phone number')
    Address=models.TextField(null=True)
    Jan=models.BooleanField(default=False)
    Feb=models.BooleanField(default=False)
    Mar=models.BooleanField(default=False)
    Apr=models.BooleanField(default=False)
    May=models.BooleanField(default=False)
    Jun=models.BooleanField(default=False)
    Jul=models.BooleanField(default=False)
    Aug=models.BooleanField(default=False)
    Sep=models.BooleanField(default=False)
    Oct=models.BooleanField(default=False)
    Nov=models.BooleanField(default=False)
    Dec=models.BooleanField(default=False)
    def __str__(self):
        return self.Name  

#Transactions 
class Transaction(models.Model):
    tran=[('Subscribe','Subscribe'),('Renew','Renew'),('Add Parent','Add Parent')]
    TType=models.CharField(max_length=100,null=True,choices=tran,verbose_name='Transaction Type')
    player=models.ManyToManyField(Player,null=True)
    sport=models.ManyToManyField(Sport,null=True)
    Fees=models.DecimalField(max_digits=13,decimal_places=4)
    TDate=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.TType
#Attendance 
class Attendance(models.Model):
    Date=models.DateTimeField(default=datetime.now)
    sport=models.ManyToManyField(Sport,null=True)
    player=models.ManyToManyField(Player,null=True)
    GroupTitle=models.CharField(max_length=100,null=True,verbose_name='Session Name')
    session=models.ManyToManyField(Session,null=True)
    def __str__(self):
        return self.GroupTitle
#Our Coaches
class Coach(models.Model):
    rh=[
        ('Football','Football'),('Swimming','Swimming'),('Karate','Karate'),('Music','Music'),('Art','Art'),('Ladies Fitness','Ladies Fitness')
    ]
    Name=models.CharField(max_length=100)
    Sport=models.CharField(max_length=50,null=True,choices=rh)
    Sessions=models.ManyToManyField(Session,null=True)
    CPhone=models.CharField(max_length=14,null=True,verbose_name='Phone number')
    def __str__(self):
        return self.Name  

#Renter
class Renter(models.Model):
    choose=[('Stadium Day Full','Stadium Day Full'),('Stadium Day Half','Stadium Day Half'),('Stadium Night','Stadium Night'),('SwPool Lane','SwPool Lane'),('SwPool Half','SwPool Half'),('SwPool Full','SwPool Full')]
    RtName=models.CharField(max_length=100,verbose_name='Renter Name')
    Fees=models.DecimalField(max_digits=30,decimal_places=4,verbose_name='Rent price')
    Location=models.CharField(max_length=100,null=True,blank=True,choices=choose)
    RDuration=models.IntegerField(verbose_name='Rent Duration')
    RDate=models.DateTimeField(verbose_name='Rent Date')
    RPhone=models.CharField(max_length=14,null=True,verbose_name='Phone number')
    def __str__(self):
        return self.RtName  