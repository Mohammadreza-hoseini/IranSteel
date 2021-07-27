from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Headertitel , Headerparam , Headerimage , Section1Part1 , Section1Part2 ,\
    Section1Part3 ,Section2Part1 \
    , Section2Part2 , Section2Part3 \
    , Section3Part1 , Section3Part2 ,  Footertitel ,\
    Footertitelright , Footerparamsright \
    , Footertitelleft , Footeraddress \
    , Footermobile , Footeremail ,\
    Footerphone , Footerfax ,\
    Footerimage , Aboutus , Contactustitel ,\
    Contactusaddress , Contactusphone , Contactusemail , Contactusimage , ContactusForm, Productsparam ,  Productsbackground ,Productsimg
# Create your views here.

class Dry():
    def footertitelright(self):
        return Footertitelright.objects.all()
    def footertitel(self):
        return Footertitel.objects.all()

    def footerparamsright(self):
        return Footerparamsright.objects.all()
    def footertitelleft(self):
        return Footertitelleft.objects.all()
    def footeraddress(self):
        return Footeraddress.objects.all()
    def footermobile(self):
        return Footermobile.objects.all()
    def footeremail(self):
        return Footeremail.objects.all()
    def footerphone(self):
        return Footerphone.objects.all()
    def footerfax(self):
        return Footerfax.objects.all()
    def footerimage(self):
        return Footerimage.objects.all()

class Pages(View):
    def get(self,request,*args,**kwargs):
        headerimage = Headerimage.objects.all()
        headertitel = Headertitel.objects.all()
        headerparam = Headerparam.objects.all()
        section1Part1 = Section1Part1.objects.all()
        section1Part2 = Section1Part2.objects.all()
        section1Part3 = Section1Part3.objects.all()
        section2Part1 = Section2Part1.objects.all()
        section2Part2 = Section2Part2.objects.all()
        section2Part3 = Section2Part3.objects.all()
        section3Part1 = Section3Part1.objects.all()
        section3Part2 = Section3Part2.objects.all()

        dry = Dry()
        footertitelright = dry.footertitelright()
        footertitel = dry.footertitel()
        footerparamsright = dry.footerparamsright()
        footertitelleft = dry.footertitelleft()
        footeraddress = dry.footeraddress()
        footermobile = dry.footermobile()
        footeremail = dry.footeremail()
        footerphone = dry.footerphone()
        footerfax = dry.footerfax()
        footerimage = dry.footerimage()
        return render(request,'pages/home.html',{'headerimage':headerimage,'headertitel':headertitel,'headerparam':headerparam,'section1Part1':section1Part1,
                                                'section1Part2':section1Part2,'section1Part3':section1Part3,
                                                'section2Part1': section2Part1,'section2Part2': section2Part2,
                                                'section2Part3': section2Part3,
                                                'section3Part1':section3Part1,'section3Part2':section3Part2,
                                                'footertitel':footertitel,'footertitelright':footertitelright,
                                                'footerparamsright':footerparamsright,
                                                'footertitelleft':footertitelleft,
                                                'footeraddress':footeraddress,
                                                'footermobile':footermobile,
                                                'footeremail':footeremail,
                                                'footerphone':footerphone,'footerfax':footerfax,'footerimage':footerimage})




class Aboutuss(View):
    def get(self,request,*args,**kwargs):
        dry = Dry()
        footertitelright = dry.footertitelright()
        footertitel = dry.footertitel()
        footerparamsright = dry.footerparamsright()
        footertitelleft = dry.footertitelleft()
        footeraddress = dry.footeraddress()
        footermobile = dry.footermobile()
        footeremail = dry.footeremail()
        footerphone = dry.footerphone()
        footerfax = dry.footerfax()
        footerimage = dry.footerimage()
        aboutus = Aboutus.objects.all()
        return render(request,'pages/aboutus.html' , {'footertitel':footertitel,'footertitelright':footertitelright,
                                                'footerparamsright':footerparamsright,
                                                'footertitelleft':footertitelleft,
                                                'footeraddress':footeraddress,
                                                'footermobile':footermobile,
                                                'footeremail':footeremail,
                                                'footerphone':footerphone,
                                                    'footerfax':footerfax,
                                                    'footerimage':footerimage,
                                                    'aboutus':aboutus})

class Contactus(View):
    def get(self,request,*args,**kwargs):
            dry = Dry()
            footertitelright = dry.footertitelright()
            footertitel = dry.footertitel()
            footerparamsright = dry.footerparamsright()
            footertitelleft = dry.footertitelleft()
            footeraddress = dry.footeraddress()
            footermobile = dry.footermobile()
            footeremail = dry.footeremail()
            footerphone = dry.footerphone()
            footerfax = dry.footerfax()
            footerimage = dry.footerimage()
            contactustitel = Contactustitel.objects.all()
            contactusaddress = Contactusaddress.objects.all()
            contactusphone = Contactusphone.objects.all()
            contactusemail = Contactusemail.objects.all()
            contactusimage = Contactusimage.objects.all()
            if request.method == 'POST':
               contact = ContactusForm()
               name = request.POST.get('name')
               phone = request.POST.get('phone')
               subject = request.POST.get('subject')
               contact.name = name
               contact.phone = phone
               contact.subject = subject
               contact.save()
            return render(request, 'pages/contactus.html', {'footertitel': footertitel, 'footertitelright': footertitelright,
                                                           'footerparamsright': footerparamsright,
                                                           'footertitelleft': footertitelleft,
                                                           'footeraddress': footeraddress,
                                                           'footermobile': footermobile,
                                                           'footeremail': footeremail,
                                                           'footerphone': footerphone,
                                                           'footerfax': footerfax,
                                                           'footerimage': footerimage,
                                                           'contactustitel': contactustitel,
                                                           'contactusaddress': contactusaddress,
                                                           'contactusphone': contactusphone,
                                                           'contactusemail': contactusemail,
                                                           'contactusimage': contactusimage})



class Products(View):
    def get(self,request,*args,**kwargs):
        dry = Dry()
        footertitelright = dry.footertitelright()
        footertitel = dry.footertitel()
        footerparamsright = dry.footerparamsright()
        footertitelleft = dry.footertitelleft()
        footeraddress = dry.footeraddress()
        footermobile = dry.footermobile()
        footeremail = dry.footeremail()
        footerphone = dry.footerphone()
        footerfax = dry.footerfax()
        footerimage = dry.footerimage()
        productsparam = Productsparam.objects.all()
        productsbackground = Productsbackground.objects.all()
        productsimg = Productsimg.objects.all()


        return render(request,'pages/products.html',{'footertitel': footertitel, 'footertitelright': footertitelright,
                                                        'footerparamsright': footerparamsright,
                                                        'footertitelleft': footertitelleft,
                                                        'footeraddress': footeraddress,
                                                        'footermobile': footermobile,
                                                        'footeremail': footeremail,
                                                        'footerphone': footerphone,
                                                        'footerfax': footerfax,
                                                        'footerimage': footerimage,
                                                    'productsparam':productsparam,'productsbackground':productsbackground,
                                                    'productsimg':productsimg})