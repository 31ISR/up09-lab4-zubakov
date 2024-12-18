from django.shortcuts import render

# Create your views here.

def communities_list(req):
    return render(req, 'communities/communities_list.html')