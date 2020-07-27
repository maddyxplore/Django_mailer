from django.shortcuts import render,redirect

import smtplib

#set up smtp connecton


# Create your views here.
def mailer(request):
    if request.method == "POST":
        name = request.POST["email"]
        password = request.POST["password"]
        mail = list(request.POST["mail"].split())
        message = request.POST["message"]
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(name,password)

        for i in mail:
            s.sendmail("pypy3blogspot@gmail.com", i , message)

        return render(request, 'mailer.html')
    else:return render(request, 'mailer.html')

def mail(request):
        return render(request, 'mailer.html')
