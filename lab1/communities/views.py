from django.shortcuts import render, redirect
from .models import community

def communities(req):
    communities = community.objects.all().order_by('-date')
    return render(req, 'communities/communities_list.html', {'communities':communities})
def community_page(request, slug):
    _community = community.objects.get(slug=slug)
    return render(request, 'communities/communities_page.html', {'community': _community})