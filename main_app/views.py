from django.shortcuts import render, redirect
from .models import Gift
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from .forms import ContactForm
from django.template.loader import get_template

# Create your views here.
def index(request):
    gifts = Gift.objects.all()
    form_class = ContactForm

    if request.method == 'POST':
        print("JUUUPI")
        form = form_class(data=request.POST)
        if form.is_valid():
            contact_email = request.POST.get('contact_email', '')
            email = EmailMessage('test', 'testteset', to=['jacool92@gmail.com'])
            email.send()

    return render(request, 'index.html', {'gifts': gifts,
                                          'form': form_class})

def occupy(request):
    gift_id = request.GET.get('gift_id', None)

    occupied = 0
    if (gift_id):
        gift = Gift.objects.get(id=int(gift_id))
        if gift is not None and gift.occupied != 0:
            occupied = gift.occupied = 1
            gift.occupied = occupied
            gift.save()
            # send_mail(
            #     'Test',
            #     'testtest',
            #     'jacool92@gmail.com',
            #     ['jacool92@gmail.com'],
            #     fail_silently=False,
            # )
        if form:
            email = EmailMessage('test', 'testteset', to=['jacool92@gmail.com'])
            email.send()
    return HttpResponse(occupied)

def contact(request):
    form_class = ContactForm()

    return render(request, 'index.html', {'form': form_class,
                                            })



# class Gift:
#     def __init__(self, name, link):
#         self.name = name
#         self.link = link
#
# gifts = [
#     Gift('Radio', 'google.com'),
#     Gift('Szafa', 'google.pl'),
#     Gift('Sztućce', 'onet.pl')
# ]