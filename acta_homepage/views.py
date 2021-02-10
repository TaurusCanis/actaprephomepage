from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, "acta_homepage/index.html")
    
def submit_message(request):
    parent_name = request.POST.get('parent_name')
    parent_email = request.POST.get('parent_email')
    parent_phone = request.POST.get('parent_phone')
    student_name = request.POST.get('student_name')
    student_grade = request.POST.get('student_grade')
    message = "Parent Name: ", parent_name, "\nParent Email: ", parent_email, "\nParent Phone: ", parent_phone, "\nStudent Name: ", student_name, "\nStudent Grade: ", student_grade, "\n\nMessage: ", request.POST.get('message')
    
    try:
        send_mail(
            'Acta Prep - Request from %s' %parent_name,
            message,
            parent_email,
            ['actaprepct@gmail.com'],
            fail_silently=False,
        )
        messages.add_message(request, messages.SUCCESS, 'Thank you. Your message has successfully been submitted.')
        return redirect("index")
    except Exception, e:
        print("EXCEPTION: ", e)
        messages.add_message(request, messages.ERROR, 'There was an error sending your message. Please try again.')
        
    return redirect("index")
    
    
