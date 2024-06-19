from django.shortcuts import render, HttpResponse,redirect


from fitapp.models import Contact,Members
from datetime import date, datetime

# to login user
from django.contrib.auth import authenticate,login,logout
# to show message
from django.contrib import messages
# Create your views here.


# Create your views here.
def index(request):
    return render(request,'index.html')
   

def contact(request):
    if request.method=="POST":
        name= request.POST.get("name") 
        email= request.POST.get("email")
        phone= request.POST.get("phone")
        desc= request.POST.get("desc")

        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()

        #to show message sucess
        messages.success(request,"DATA SAVED SUCESSFULLY!")
    
    return render(request,'contact.html')


def pricing(request):
    return render(request,'pricing.html')

def members(request):
        usr = Members.objects.all()
       
        #for i in usr:
           # print(i.Name,"/t",i.Email)
        data = {'usr':usr}
        return render(request,'members.html',data)
    


