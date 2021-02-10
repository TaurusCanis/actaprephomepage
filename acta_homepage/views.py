from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from django.template.loader import render_to_string

# Create your views here.

def index(request):
    print("LOADED")
    return render(request, "acta_homepage/index.html")
    
def submit_message(request):
    print("request.POST: ", request.POST)
    parent_name = request.POST.get('parent_name')
    parent_email = request.POST.get('parent_email')
    parent_phone = request.POST.get('parent_phone')
    student_name = request.POST.get('student_name')
    student_grade = request.POST.get('student_grade')
    context = {
        "parent_name": parent_name,
        "parent_email": parent_email,
        "parent_phone": parent_phone,
        "student_name": student_name,
        "student_grade": student_grade,
        "message": request.POST.get('message')
    }
    print("CONTEXT: ", context)
    email_string = render_to_string('acta_homepage/emails/inquiry_email.txt', context)
    print("email_string: ", email_string, " type: ", type(email_string))
    
    try:
        send_mail(
            'Acta Prep - Request from %s' %parent_name,
            email_string,
            parent_email,
            ['actaprepct@gmail.com'],
            fail_silently=False,
        )
        messages.add_message(request, messages.SUCCESS, 'Thank you. Your message has successfully been submitted.')
        return redirect("index")
    except Exception as e:
        print("email_string: ", email_string)
        print("EXCEPTION: ", e)
        messages.add_message(request, messages.ERROR, 'There was an error sending your message. Please try again.')
        
    return redirect("index")
    
    
