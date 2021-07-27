from django.db import models
from django.contrib.auth.models import User
# Create your models here.


#Header

class Headerimage(models.Model):
    image = models.ImageField(upload_to='backgroud/%Y/%m/%d/')

class Headertitel(models.Model):
    titel = models.TextField(max_length=255)

    def __str__(self):
       return self.titel


class Headerparam(models.Model):
    param = models.TextField(max_length=500,blank=True)

    def __str__(self):
       return self.param

# Section

class Section1Part1(models.Model):
    titel = models.TextField(max_length=255,blank=True)

    def __str__(self):
        return self.titel

class Section1Part2(models.Model):
    param = models.TextField(max_length=500)

    def __str__(self):
        return self.param

class Section1Part3(models.Model):
    image = models.ImageField(upload_to='section1/%Y/%m/%d/')

#     Section2*****************

class Section2Part1(models.Model):
    titel = models.TextField(max_length=255,blank=True)


    def __str__(self):
        return self.titel

class Section2Part2(models.Model):
    param = models.TextField(max_length=500)

    def __str__(self):
        return self.param

class Section2Part3(models.Model):
    image = models.ImageField(upload_to='section2/%Y/%m/%d/')

#   section3*********************

class Section3Part1(models.Model):
    titel = models.TextField(max_length=255)

    def __str__(self):
        return self.titel


class Section3Part2(models.Model):
    image = models.ImageField(upload_to='section3/%Y/%m/%d/')
    param = models.TextField(max_length=255)

    def __str__(self):
        return self.param



# Footer

class Footertitel(models.Model):
    titel = models.TextField(max_length=255)

    def __str__(self):
        return self.titel


class Footertitelright(models.Model):
    titel = models.TextField(max_length=255)

    def __str__(self):
        return self.titel


class Footerparamsright(models.Model):
    param = models.TextField(max_length=255)

    def __str__(self):
        return self.param

class Footertitelleft(models.Model):
    titel = models.TextField(max_length=500)

    def __str__(self):
        return self.titel

class Footeraddress(models.Model):
    address = models.TextField(max_length=555)

    def __str__(self):
        return self.address


class Footermobile(models.Model):
    mobile = models.CharField(max_length=255)

    def __str__(self):
        return self.mobile


class Footeremail(models.Model):
    email = models.CharField(max_length=500)

    def __str__(self):
        return self.email


class Footerphone(models.Model):
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.phone

class Footerfax(models.Model):
    fax = models.CharField(max_length=555)

    def __str__(self):
        return self.fax

class Footerimage(models.Model):
    image = models.ImageField(upload_to='footer/%Y/%m/%d/')



# about us


class Aboutus(models.Model):
    titel = models.CharField(max_length=255)
    image = models.ImageField(upload_to='aboutus/%Y/%m/%d/')
    param = models.TextField(max_length=5555)


    def __str__(self):
        return self.titel



# contactus page

class Contactustitel(models.Model):
    param = models.TextField(max_length=555)

    def __str__(self):
        return self.param


class Contactusaddress(models.Model):
    address = models.TextField(max_length=255)

    def __str__(self):
        return self.address

class Contactusphone(models.Model):
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.phone

class Contactusemail(models.Model):
    email = models.TextField(max_length=555)

    def __str__(self):
        return self.email


class Contactusimage(models.Model):
    image = models.ImageField(upload_to='aboutus/%Y/%m/%d/')


class ContactusForm(models.Model):
    name = models.TextField(max_length=555)
    phone = models.CharField(max_length=255)
    subject = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


    # Products



class Productsparam(models.Model):
    param = models.TextField(max_length=10000)

    def __str__(self):
        return  self.param


class Productsbackground(models.Model):
    image = models.ImageField(upload_to='products/%Y/%m/%d/')


class Productsimg(models.Model):
    image = models.ImageField(upload_to='products/%Y/%m/%d/')