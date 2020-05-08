# pylint:disable=E1101
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.db.models.signals import post_save
from django.dispatch import receiver
from . import compressImage


class MyUserManager(BaseUserManager):

    def create_user(self, roll, password=None):
        if not roll:
            raise ValueError('Users must have an roll number')
        user = self.model(roll=roll)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, roll, password=None):
        user = self.create_user(roll, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    roll = models.IntegerField(verbose_name='Roll Number', primary_key=True)
    #date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_verified = models.IntegerField(default=0)

    objects = MyUserManager()

    USERNAME_FIELD = 'roll'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.roll)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
    # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
    # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
    # Simplest possible answer: All admins are staff
        return self.is_admin


class Profile(models.Model):
    SECTION_CHOICES = [('A', 'A'), ('B', 'B'), ('C', 'C')]
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    CLASS_CHOICES = [('6th', '6th'), ('7th', '7th'), ('8th', '8th'),
                     ('9th', '9th'), ('10th', '10th'), ('11th', '11th'), ('12th', '12th')]
    roll = models.OneToOneField(
        MyUser, on_delete=models.CASCADE, db_column="Roll No")
    fname = models.CharField(max_length=30, null=True,
                             db_column="First Name", verbose_name="First Name")
    lname = models.CharField(max_length=30, null=True,
                             db_column="Last Name", verbose_name="Last Name")
    gender = models.CharField(
        max_length=6, choices=GENDER_CHOICES, null=True, db_column="Gender")
    clss = models.CharField(max_length=4, choices=CLASS_CHOICES,
                            null=True, db_column="Class", verbose_name="Class")
    section = models.CharField(
        max_length=3, choices=SECTION_CHOICES, null=True, db_column="Section")
    img = models.ImageField(
        null=True, db_column="Profile Picture", verbose_name="Profile Picture")
    dob = models.DateField(
        null=True, db_column="Date of Birth", verbose_name="Date of Birth")
    datereg = models.DateTimeField(
        auto_now=True, db_column="Registeration Date", verbose_name="Registeration Date")

    def __str__(self):
        return str(self.roll)

    def save(self, *args, **kwargs):
        if self.img:
            new_image = compressImage.compress(self.img)
            self.img = new_image
        super().save(*args, **kwargs)


@receiver(post_save, sender=MyUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile(roll=instance)
        profile.save()


class Login(models.Model):
    roll = models.IntegerField(verbose_name='Roll Number', primary_key=True)
    password = models.CharField(max_length=50, verbose_name='Password')


class Libook(models.Model):
    bid = models.CharField(max_length=100, db_column="Book Id",
                           verbose_name="Book Id", primary_key=True)
    bname = models.CharField(
        max_length=100, db_column="Book Name", verbose_name="Book Name")
    bno = models.IntegerField(db_column="Total Book",
                              verbose_name="Total Book")
    avlbook = models.IntegerField(
        db_column="Available Book", verbose_name="Available Book")


class Issue(models.Model):
    roll = models.ForeignKey(MyUser, db_column="Roll No",
                             verbose_name="Roll No", on_delete=models.CASCADE)
    bid = models.CharField(max_length=100, db_column="Book Id",
                           verbose_name="Book Id", primary_key=True)
    bname = models.CharField(
        max_length=100, db_column="Book Name", verbose_name="Book Name")
    issuedate = models.DateTimeField(
        auto_now=True, db_column="Issued Date", verbose_name="Issued Date")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['roll', 'bname'], name="one_book")
        ]


class Return(models.Model):
    roll = models.ForeignKey(MyUser, db_column="Roll No",
                             verbose_name="Roll No", on_delete=models.CASCADE)
    bid = models.CharField(max_length=100, db_column="Book Id",
                           verbose_name="Book Id", primary_key=True)
    bname = models.CharField(
        max_length=100, db_column="Book Name", verbose_name="Book Name")
    returndate = models.DateTimeField(
        auto_now=True, db_column="Return Date", verbose_name="Return Date")
