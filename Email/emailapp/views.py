from django.shortcuts import render
from django.views import View 
from .models import Reg
from django.http import HttpResponse
from django.conf import settings 
from django.core.mail import send_mail
class Home(View):
    def get(self,r):
        return render(r,template_name='home.html')
class InputView(View):
    def get(self,r):
        return render(r,template_name='reginput.html')
class Input(View):
    def post(self,r):
        p1=Reg(
        fn=r.POST["t1"],
        ln=r.POST["t2"],
        g=r.POST["t3"],
        dob=r.POST["t4"],
        hgra=r.POST["t5"],
        course=r.POST["t6"],
        year=r.POST["t7"],
        mob=r.POST["t8"],
        ename=r.POST["t9"],
        p=r.POST["t10"],
        cp=r.POST["t11"]
        )
        p1.save()
        sub="Thank You For Contacting Us!"
        msg="we get in few moments"
        From_email=settings.EMAIL_HOST_USER
        email=r.POST['t9']
        to_list=[email]
        send_mail(sub , msg, From_email,to_list,fail_silently=True)
        return HttpResponse("<html><body bgcolor=yellow><h1>Registration is Successful!</h1></body></html>")
class OutputView(View):
    def get(self,r):
        return render(r,template_name='login.html')
class Output(View):
    def post(self,r):

        a1=r.POST['t9']
        a2=r.POST['t10']
        p2=Reg.objects.filter(ename=a1,p=a2)
        p2.exists()
        if p2:
            return HttpResponse("<html><body bgcolor=yellow><h1>Login is Successful!</h1></body></html>")
        else:
            return HttpResponse("<html><body bgcolor=yellow><h1>Login Failed Please enter valid email and password </h1></body></html>")