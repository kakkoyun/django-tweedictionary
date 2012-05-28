from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.messages.api import get_messages

from dictionary.models import Item, Entry

from social_auth.utils import setting

def home(request):
    """Home view"""
    """random choose item content """
    if request.user.is_authenticated():
        return HttpResponseRedirect('user')
    else:
    	i = get_object_or_404(Item, id=item_id)
        return render_to_response('index.html', {'item': i}, RequestContext(request))

@login_required
def user(request):
    """Login complete view"""
    """ random choose item content """
    i = get_object_or_404(Item, id=item_id)
    return render_to_response('user.html', {'item': i}, RequestContext(request))

def credits(request):
    """Credits page"""
    if request.user.is_authenticated():
        return HttpResponseRedirect('credits_log')
    else:
        return render_to_response('credits.html', RequestContext(request))
                 
@login_required
def credits_log(request):
    """Login complete view"""
    return render_to_response('credits_log.html', RequestContext(request))

@login_required
def edit(request,entry_id):
    """Edit page"""
    e = get_object_or_404(Entry, id=entry_id)
    return render_to_response('edit.html', {'entry': e}, RequestContext(request))

def items(request,item_id):
    """Item page"""
    if request.user.is_authenticated():
        return HttpResponseRedirect('item_log')
    else:
    	i = get_object_or_404(Item, id=item_id)
        return render_to_response('index.html', {'item': i}, RequestContext(request))

@login_required
def item_log(request,item_id):
    """Item page"""
    i = get_object_or_404(Item, id=item_id)
    return render_to_response('user.html', {'item': i}, RequestContext(request))

@login_required
def additem(request):
    """Add item page"""
    return render_to_response('additem.html', RequestContext(request))

@login_required
def profile(request):
    """profile"""
    return render_to_response('profile.html', RequestContext(request))

def alphabet(request,char):
    """alphabet"""
    """search items"""
    if request.user.is_authenticated():
    	return HttpResponseRedirect('alphabet_log')
    else:
    	listofitems
        return render_to_response('list.html', {'item_list': listofitems}, RequestContext(request))

@login_required
def alphabet_log(request,char):
    """alphabet"""
    """search items"""
    listofitems
    return render_to_response('list_log.html', {'item_list': listofitems}, RequestContext(request))
