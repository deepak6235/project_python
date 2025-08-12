from django.db import models

class login_table(models.Model):
    username=models.CharField(max_length=90)
    password=models.CharField(max_length=80)
    type=models.CharField(max_length=80)

class hospital_table(models.Model):
    LOGIN=models.ForeignKey(login_table, on_delete=models.CASCADE)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=90)
    website=models.CharField(max_length=90)
    contactno=models.BigIntegerField()
    place=models.CharField(max_length=90)
    pin=models.IntegerField()
    post=models.CharField(max_length=90)
    latitude=models.FloatField()
    longitude=models.FloatField()

class doctor_table(models.Model):
    LOGIN=models.ForeignKey(login_table, on_delete=models.CASCADE)
    HOSPITAL=models.ForeignKey(hospital_table, on_delete=models.CASCADE)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=80)
    phone=models.BigIntegerField()
    image=models.FileField()
    department=models.CharField(max_length=90)
    qualification=models.CharField(max_length=80)
    experience=models.IntegerField()


class user_table(models.Model):
    LOGIN=models.ForeignKey(login_table, on_delete=models.CASCADE)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=80)
    place=models.CharField(max_length=90)
    dob=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    pin=models.IntegerField()
    post=models.CharField(max_length=90)
    image=models.FileField()
    lab = models.CharField(max_length=50, default='none')


class schedule_table(models.Model):
    DOCTOR=models.ForeignKey(doctor_table, on_delete=models.CASCADE)
    date=models.DateField()
    fromtime=models.TimeField()
    totime =models.TimeField()


class booking_table(models.Model):
    USER=models.ForeignKey(user_table, on_delete=models.CASCADE)
    SCHEDULE=models.ForeignKey(schedule_table, on_delete=models.CASCADE)
    status=models.CharField(max_length=90)
    date=models.DateField()
    notificationstatus=models.CharField(max_length=50, default="notopened")


class complaint_table(models.Model):
    USER=models.ForeignKey(user_table, on_delete=models.CASCADE)
    complaint=models.CharField(max_length=90)
    reply=models.CharField(max_length=90)
    date=models.DateField()

class review_table(models.Model):
    USER=models.ForeignKey(user_table, on_delete=models.CASCADE)
    HOSPITAL=models.ForeignKey(hospital_table,on_delete=models.CASCADE)
    review=models.CharField(max_length=90)
    rating=models.CharField(max_length=90)
    date=models.DateField()

class lab_table(models.Model):
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    website = models.CharField(max_length=90)
    contactno = models.BigIntegerField()
    place = models.CharField(max_length=90)
    pin = models.IntegerField()
    post = models.CharField(max_length=90)
    latitude = models.FloatField()
    longitude = models.FloatField()

class test_table(models.Model):
    USER=models.ForeignKey(user_table, on_delete=models.CASCADE)
    LAB=models.ForeignKey(lab_table, on_delete=models.CASCADE)
    test_name=models.CharField(max_length=90)
    result = models.FileField()
    date=models.DateField()

class prescription_table(models.Model):
    BOOKING=models.ForeignKey(booking_table, on_delete=models.CASCADE)
    prescription=models.CharField(max_length=90)
    quantity=models.IntegerField()
    days=models.IntegerField()
    morning=models.CharField(max_length=90)
    afternoon=models.CharField(max_length=90)
    night=models.CharField(max_length=90)
    date=models.DateField()


# class reminder_table(models.Model):
#     PRESCRIPTION=models.ForeignKey(booking_table,on_delete=models.CASCADE)
#     morning = models.CharField(max_length=90)
#     afternoon = models.CharField(max_length=90)
#     night = models.CharField(max_length=90)



class reminder_table(models.Model):
    PRESCRIPTION = models.ForeignKey(prescription_table, on_delete=models.CASCADE)
    morning = models.TimeField(null=True, blank=True)
    afternoon = models.TimeField(null=True, blank=True)
    night = models.TimeField(null=True, blank=True)





class diet_plan_table(models.Model):
    Dietplan=models.FileField()
    Gender = models.CharField(max_length=100)
    Obicity = models.CharField(max_length=100)
    Bloodpressure = models.CharField(max_length=100)
    Diabetes = models.CharField(max_length=100)
    Cholestrol = models.CharField(max_length=100)
    Alcoholabuse = models.CharField(max_length=100)
    Druguse = models.CharField(max_length=100)
    Smoking = models.CharField(max_length=100)
    Headaches = models.CharField(max_length=100)
    Asthma = models.CharField(max_length=100)
    Heartproblem = models.CharField(max_length=100)
    Cancer = models.CharField(max_length=100)
    Stroke = models.CharField(max_length=100)
    Kidney = models.CharField(max_length=100)
    Liver = models.CharField(max_length=100)
    Depression = models.CharField(max_length=100)
    Allergies = models.CharField(max_length=100)
    Arthritis = models.CharField(max_length=100)
    Pregnancy = models.CharField(max_length=100)
    bmi = models.FloatField(max_length=100)












