from django.shortcuts import render
from .models import Gift
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def index(request):
    gifts = Gift.objects.all()
    return render(request, 'index.html', {'gifts': gifts})

# def occupy(request):
#     gift_id = request.GET.get('gift_id', None)
#
#     occupied = 0
#     if (gift_id):
#         gift = Gift.objects.get(id=int(gift_id))
#         if gift is not None and gift.occupied != 0:
#             occupied = gift.occupied = 1
#             gift.occupied = occupied
#             gift.save()
#             # send_mail(
#             #     'Test',
#             #     'testtest',
#             #     'jacool92@gmail.com',
#             #     ['jacool92@gmail.com'],
#             #     fail_silently=False,
#             # )
#     form = ContactForm
#     if form:
#         email = EmailMessage('test', 'testteset', to=['jacool92@gmail.com'])
#         email.send()
#     return HttpResponse(occupied)

def occupy(request):
    form = ContactForm()

    return render(request, 'index.html', {'form': form,
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