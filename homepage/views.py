from django.shortcuts import redirect, render
from .forms import messageform
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = messageform(request.POST)
        if form.is_valid():
            form.save()
            template_admin = render_to_string('templates/info_email.html')
            email_admin = EmailMessage(
                'Message',
                template_admin,
                settings.EMAIL_HOST_USER,
                ['hantsitaumang@gmail.com']
            )
            email_admin.fail_silently = False
            email_admin.send()
            return redirect('sent')
        else:
            return redirect('/')
    else:
        form = messageform()
    return render(request, "index.html", {'form':form})


def sent(request):
    return render(request, "confirmation.html")