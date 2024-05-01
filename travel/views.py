from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'South Korea, Seoul'
    dest1.img  = 'property-01.jpg'
    dest1.price = 700.17
    dest1.offer = True

    dest2 = Destination()
    dest2.name = 'South Korea, Daegu'
    dest2.img  = 'property-02.jpg'
    dest2.price = 2017.07
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'South Korea, Busan'
    dest3.img  = 'property-03.jpg'
    dest3.price = 1717.07
    dest3.offer = True

    dest4 = Destination()
    dest4.name = 'Japan, Tokyo'
    dest4.img  = 'property-04.jpg'
    dest4.price = 4000.05
    dest4.offer = False

    dest5 = Destination()
    dest5.name = 'America, Washington'
    dest5.img  = 'property-05.jpg'
    dest5.price = 5015.06
    dest5.offer = True

    dest6 = Destination()
    dest6.name = 'South Korea, Incheon'
    dest6.img  = 'property-06.jpg'
    dest6.price = 7017.07
    dest6.offer = True

    dests=[dest1,dest2,dest3,dest4,dest5,dest6]

    return render(request,'index.html', {'dests': dests})
