from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.messages.api import get_messages

import random

from dictionary.models import Item, Entry

from social_auth.utils import setting
# done
def random_item():
    return Item.objects.order_by('?')[0]

# done
def hot_items():
    """hot-items filter"""
    obj_list = Item.objects.all().order_by("-last_modified")
    return obj_list[:30]
    
# done
@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect("/")
    
# done
def home(request):
    """Home view"""
    """random choose item content """
    i = random_item()
    ctx = {
            'item': i,
            'entries': i.entries.all(),
            'hot_items': hot_items()
    }
    if request.user.is_authenticated():
        return render_to_response('user.html', ctx, RequestContext(request))
    else:
        return render_to_response('index.html', ctx, RequestContext(request))
    
# done
def items(request,item_id):
    """Item page"""
    i = get_object_or_404(Item, id=item_id)
    ctx = {
            'item': i,
            'entries': i.entries.all(),
            'hot_items': hot_items()
    }
    if request.user.is_authenticated():
        return render_to_response('user.html', ctx, RequestContext(request))
    else:
        return render_to_response('index.html', ctx, RequestContext(request))

# done
def credits(request):
    """Credits page"""
    if request.user.is_authenticated():
        """Login complete credits"""
        return render_to_response('credits_log.html', {'hot_items' : hot_items()}, RequestContext(request))
    else:
        return render_to_response('credits.html', {'hot_items' : hot_items()}, RequestContext(request))

@login_required
def edit(request,entry_id):
    """Edit page"""
    e = get_object_or_404(Entry, id=entry_id)
    ctx = {
        'entry': e,
        'hot_items': hot_items()
    }
    return render_to_response('edit.html', ctx, RequestContext(request))

@login_required
def additem(request):
    """Add item page"""
    return render_to_response('additem.html', RequestContext(request))

@login_required
def profile(request):
    """profile"""
    return render_to_response('profile.html', RequestContext(request))

# done
def alphabet(request,char):
    """alphabet"""
    """search items"""
    items = Item.objects.filter(name__startswith=char.lower())
    ctx = {
        'items': items,
        'hot_items': hot_items(),
        'char': char.lower()
    }
    if request.user.is_authenticated():
    	return render_to_response('list_log.html', ctx, RequestContext(request))
    else:
        return render_to_response('list.html', ctx, RequestContext(request))
