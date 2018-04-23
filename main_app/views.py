from django.shortcuts import render
from .models import Gift
from django.http import HttpResponse

# Create your views here.
def index(request):
    gifts = Gift.objects.all()
    return render(request, 'index.html', {'gifts': gifts})

def occupy(request):
    gift_id = request.GET.get('gift_id', None)

    occupied = 0
    if (gift_id):
        gift = Gift.objects.get(id=int(gift_id))
        if gift is not None:
            occupied = gift.occupied = 1
            gift.occupied = occupied
            gift.save()
    return HttpResponse(occupied)

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