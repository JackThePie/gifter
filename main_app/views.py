from django.shortcuts import render, redirect, get_object_or_404
from .models import Gift
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from .forms import ContactForm
from django.template.loader import get_template
import pprint as pp

# Create your views here.
def index(request):
    print('test1')

    gifts = Gift.objects.all()

    form_class = ContactForm

    if request.method == 'POST':
        print('lolex')
        # print(request)
        # form = ContactForm(request.POST)
        # if(form.is_valid()):
            # print(request.POST)
        # occupy(request)

    return render(request, 'index.html', {'gifts': gifts,
                                          'form': form_class})
    # return render(request, 'index.html', {'gifts': gifts})


def occupy(request):
    print('hrj')
    gift_id = request.GET.get('gift_id', None)
    print(gift_id)
    # print(type(request))
    test = dict(request.GET.lists())
    email = test['form_data[1][value]']
    print(email)

    occupied = 0
    if (gift_id) and '@' in email[0]:
        print("blah")
        gift = Gift.objects.get(id=int(gift_id))
        print('identified')

        print(gift.name)
        print(gift.link)
        if gift is not None and gift.occupied == 0 and gift.email == '':
            print('Its working!')
            occupied = gift.occupied = 1
            gift.occupied = occupied

            gift.save()

            send_mail(
                'Prezent dla Klary i Jacka, który zarezerwowałeś, to: {}'.format(gift.name),
                'Gratulacje! \n'
                'Wybrałeś prezent: {}\n'
                'Przykładowy link: {}\n'
                'Do zobaczenia ma Ślubie!'.format(gift.name, gift.link),
                'jacool92@gmail.com',
                email,
                fail_silently = False,
            )
            # email = EmailMessage('Prezent dla Klary i Jacka, który zarezerwowałeś, to: {}'.format(gift.name),
            #                      'Gratulacje! \n Wybrałeś prezent: {}'
            #                      'Przykładowy link: {}'
            #                      'Do zobaczenia ma Ślubie!'.format(gift.name, gift.link), to=[email])
            # email.send()
        else:
            print('Bad email adress')
    return HttpResponse(occupied)