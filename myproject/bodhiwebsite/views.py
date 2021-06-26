from bodhiwebsite.forms import ContactForm
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.contrib import messages
from django.shortcuts import HttpResponse

from socket import gaierror
from smtplib import SMTPAuthenticationError, SMTPDataError
from django.conf import settings as sname 
from bodhiwebsite.models import carousel,features,client,about



from bodhiwebsite.forms import ContactForm
from django.conf import settings as conf_set


# Create your views here.


obj=sname.CNAME



def web_contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            person_name=form.cleaned_data['name']
            
            subject = form.cleaned_data['subject']
            user_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            message_send="\n Name : "+person_name+" \n Message : "+message+"\n User Email : "+user_email
            from_email=conf_set.EMAIL_HOST_USER
            try:
                send_mail(subject,message_send,from_email, ['gaikwadkomal48@gmail.com'])
            except (BadHeaderError,gaierror,SMTPAuthenticationError,SMTPDataError):
                messages.error(request,"Check your Internet connection... Try again")
                return redirect('web_contact')
            messages.success(request,"Thank you for contacting school! Your form successfully submited")
            return redirect('web_contact')
            
    context = {
        'form': form,
        
    }        
    return render(request, "webpages/contact.html",context)





def home_page(request):

    ccarousel=carousel.objects.all()
    ffeatures=features.objects.all()
    sclient=features.objects.all()
    aabout=about.objects.all()
    context={'ccarousel':ccarousel,'ffeatures':ffeatures,'sclient':sclient,'aabout':aabout}

    return render(request,'webpages/index.html',context)

    # return render(request,'layout/layout.html')






def webapp_homepage(request):
    # page_title = "index page"
    # text = "abc"
    # about="Why you choose-Us?"
    # client="Our Clients "
    # abouts="About Us"
    aabout="aabout"
    

    # context = {'title':page_title,'text':text,'client':client,'about':about,'pname':obj,'aabout':aabout}
    context={'aabout':aabout}

    return render(request,'webpages/index.html',context)

















    

