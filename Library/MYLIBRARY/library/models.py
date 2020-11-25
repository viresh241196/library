from django.db import models
from account.models import CustomUser


class Profile(models.Model):
    user_info = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(blank=True, max_length=30, default='None', null=True)
    email_id = models.EmailField(blank=True, default='None', null=True)
    address = models.TextField(blank=True, default='', null=True)
    town = models.CharField(blank=True, max_length=50, null=True)
    Date_of_Birth = models.CharField(max_length=50,blank=True, default=0, null=True)
    adhar_card = models.IntegerField(blank=True, default=0, null=True)
    book_name = models.CharField(max_length=50, null=True)
    copies_taken = models.IntegerField(null=True)
    book_status = models.BooleanField(default=False, null=True)
    borrow_date = models.CharField(max_length=50,blank=True, default=0, null=True)
    return_date = models.CharField(max_length=50,blank=True, default=0, null=True)

    def __str__(self):
        return self.name


class Store(models.Model):
    book_name = models.CharField(max_length=50)
    Number_of_copies = models.IntegerField()

    def __str__(self):
        return self.book_name


class Records(models.Model):
    name = models.CharField(max_length=30)
    email_id = models.EmailField()
    address = models.TextField()
    book_name = models.CharField(max_length=50, null=True)
    copies_taken = models.IntegerField(null=True)
    borrow_date = models.CharField(max_length=50)
    return_date = models.CharField(max_length=50,default='None')
    expired_date = models.CharField(max_length=50)
