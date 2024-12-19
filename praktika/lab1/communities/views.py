from django.shortcuts import render
from .models import communities

def communities_list(request):
    Communities = communities.objects.all() 
    return render(request, 'communities/communities_list.html', {'communities': Communities})
