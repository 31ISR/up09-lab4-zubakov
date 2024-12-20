from django.shortcuts import render, redirect
from .models import community
from django.contrib.auth.decorators import login_required

from . import forms 

def communities(req):
    communities = community.objects.all().order_by('-date')
    return render(req, 'communities/communities_list.html', {'communities':communities})
def community_page(request, slug):
    _community = community.objects.get(slug=slug)
    return render(request, 'communities/communities_page.html', {'community': _community})
@login_required(login_url="/users/login/")
def community_new(request):
    if request.method == 'POST': 
        form = forms.CreateCommunity(request.POST, request.FILES) 
        if form.is_valid():
            newpost = form.save(commit=False) 
            newpost.author = request.user 
            newpost.save()
        return redirect('community:list')
    else:
        form = forms.CreateCommunity()
    return render(request, 'communities/community_new.html', { 'form': form })