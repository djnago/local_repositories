from django.shortcuts import render, redirect
from .models import RegistrationData,Feedbackdata,StudentData
from .forms import RegistrationForm, LoginForm,FeedbackForm,StudentForm
from django.http import HttpResponse
import datetime as dt

dt1 = dt.datetime.now()

def registrationview(request):
    if request.method =='POST':
        rform = RegistrationForm(request.POST)
        if rform.is_valid():
            name = request.POST.get('name','')
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            mobile = request.POST.get('mobile','')
            email = request.POST.get('email','')
            location = request.POST.get('location','')
            dob = rform.cleaned_data.get('dob','')

            rd = RegistrationData(
                name=name,
                username=username,
                password=password,
                mobile=mobile,
                email=email,
                locations=location,
                dob = dob
            )
            rd.save()
            return HttpResponse("Data  insetred")

    rform = RegistrationForm()
    return render(request,'institute_registration.html',{'rform':rform})


def loginview(request):
    if request.method=='POST':
        lform = LoginForm(request.POST)
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        user = RegistrationData.objects.filter(username=username)
        pwd = RegistrationData.objects.filter(password=password)
        if user and pwd:
            return redirect('/home/')
        else:
            return redirect('/home/')
    else:
        lform = LoginForm()
        return render(request,'institute_login.html',{'lform':lform})


def home(request):
    return render(request,'institute_home.html')


def about(request):
    return render(request,'institute_about.html')

#
# def contact(request):
#     return render(request,'institute_contact.html')


def services(request):
    return render(request,'institute_services.html')


def gallery(request):
    return render(request,'institute_gallery.html')





def feedback(request):
    if request.method =='POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name','')
            rating = request.POST.get('rating','')
            feedback = request.POST.get('feedback','')

            data = Feedbackdata(name=name,
                         rating=rating,
                         time=dt1,
                         feedback=feedback)
            data.save()
            return redirect('/feedback/')
    else:
        data1 = Feedbackdata.objects.all()
        form = FeedbackForm()
        return render(request, 'institute_feedback.html', {'form':form, 'data1':data1})

def contact(request):
    if request.method=='POST':
        sform = StudentForm(request.POST)
        if sform.is_valid():
            name = sform.cleaned_data.get('name','')
            mobile = sform.cleaned_data.get('mobile','')
            email = sform.cleaned_data.get('email','')
            shift = sform.cleaned_data.get('shift','')
            course = sform.cleaned_data.get('course','')
            faculty = sform.cleaned_data.get('faculty','')
            brance = sform.cleaned_data.get('brance','')

            sd = StudentData(
                name=name,
                mobile=mobile,
                email=email,
                shift=shift,
                course=course,
                faculty=faculty,
                brance=brance
            )
            sd.save()
            return redirect('/contact/')
        else:
            return HttpResponse('Invalid Data')



    else:
        sform = StudentForm()
        return render(request,'institute_contact.html',{'sform':sform})
