from django.shortcuts import render
from .models import Gift

# Create your views here.
def index(request):
    gifts = Gift.objects.all()
    return render(request, 'index.html', {'gifts': gifts})


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