from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.timezone import now

from codebase import settings

    
# Create your models here.



class Batch(models.Model):
    id = models.AutoField(primary_key=True)
    start_date = models.DateField(default=now)
    end_date = models.DateField(default=now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100, default='', blank=False)
    short_name = models.CharField(max_length=20, default='', blank=True)
    hod = models.CharField(max_length=100, default='', blank=False)
    batch = models.ForeignKey(Batch, on_delete=models.PROTECT, default='', blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()





class CustomUser(AbstractUser):
    user_type_choices = ((1,'Dean'),(2,'Staff'),(3,'Student'),(4,'Developers'),(5,'Cells'),(6,'Admin'))
    user_type = models.CharField(default=6, max_length=20, choices=user_type_choices)



class DeanUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.PROTECT, blank=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()



class StaffUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.PROTECT, blank=False)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, default='', blank=False)
    joined_at = models.DateField(default=now)
    is_active = models.BooleanField(default=True)
    is_permanent = models.BooleanField(default=False)
    is_hod = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class StudentUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.PROTECT, blank=False)
    college = models.CharField(max_length=100, default='', blank=False)
    department = models.ForeignKey(Department, on_delete=models.PROTECT,default='', blank=False)
    batch_starting = models.DateField(default=now)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class DevelopersUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.PROTECT, blank=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class CellsUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.PROTECT, blank=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class AdminUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.PROTECT, blank=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    regulation = models.DateField(default=now)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, default='', blank=False)
    subject_name = models.CharField(max_length=100, default='', blank=False)
    subject_code = models.CharField(max_length=10, default='', blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    upated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()



class ClassRoom(models.Model):
    id = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, default='', blank=False)
    batch = models.ForeignKey(Batch, on_delete=models.PROTECT, default='', blank=False)
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    upated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class StudyMaterials(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, default='', blank=False)
    material_title = models.CharField(max_length=200, default='', blank=False)
    material = models.URLField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    upated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    






@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if not created:
        return
    if instance.user_type == 1:
        DeanUser.objects.create(admin=instance)
    if instance.user_type == 2:
        StaffUser.objects.create(admin=instance)
    if instance.user_type == 3:
        StudentUser.objects.create(admin=instance)
    if instance.user_type == 4:
        DevelopersUser.objects.create(admin=instance)
    if instance.user_type == 5:
        CellsUser.objects.create(admin=instance)
    if instance.user_type == 6:
        AdminUser.objects.create(admin=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.deanuser.save()
    if instance.user_type == 2:
        instance.staffser.save()
    if instance.user_type == 3:
        instance.studentuser.save()
    if instance.user_type == 4:
        instance.developersuser.save()
    if instance.user_type == 5:
        instance.cellsuser.save()
    if instance.user_type == 6:
        instance.adminuser.save()

















