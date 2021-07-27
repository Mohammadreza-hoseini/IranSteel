from django.contrib import admin
from .models import Headertitel , Headerparam , Headerimage , Section1Part1 , Section1Part2 ,\
    Section1Part3 ,Section2Part1 , Section2Part2 ,\
    Section2Part3 , Section3Part1 , Section3Part2 , Footertitel \
    , Footertitelright , Footerparamsright ,\
    Footertitelleft , Footeraddress ,\
    Footermobile , Footeremail , Footerphone ,\
    Footerfax , Footerimage ,\
    Aboutus , Contactustitel , Contactusaddress ,\
    Contactusphone , Contactusemail , Contactusimage , ContactusForm , Productsparam , Productsbackground , Productsimg


# Register your models here.


admin.site.register(Headerimage)

admin.site.register(Headertitel)

admin.site.register(Headerparam)

admin.site.register(Section1Part1)

admin.site.register(Section1Part2)

admin.site.register(Section1Part3)

# section2******
admin.site.register(Section2Part1)

admin.site.register(Section2Part2)

admin.site.register(Section2Part3)

admin.site.register(Section3Part1)

admin.site.register(Section3Part2)

# Footer
admin.site.register(Footertitel)

admin.site.register(Footertitelright)

admin.site.register(Footerparamsright)

admin.site.register(Footertitelleft)

admin.site.register(Footeraddress)

admin.site.register(Footermobile)

admin.site.register(Footeremail)

admin.site.register(Footerphone)

admin.site.register(Footerfax)

admin.site.register(Footerimage)

# Aboutus

admin.site.register(Aboutus)

# contactus

admin.site.register(Contactustitel)


admin.site.register(Contactusaddress)

admin.site.register(Contactusphone)

admin.site.register(Contactusemail)

admin.site.register(Contactusimage)

admin.site.register(ContactusForm)


# Products


admin.site.register(Productsparam)
admin.site.register(Productsbackground)
admin.site.register(Productsimg)
