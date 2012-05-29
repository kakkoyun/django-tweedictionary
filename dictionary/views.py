from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.messages.api import get_messages

import random

from dictionary.models import Item, Entry
from dictionary.forms import EntryForm
from django.contrib.auth.models import User

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
    entryform = EntryForm()
    if request.user.is_authenticated():
    	ctx = {
            'item': i,
            'entries': i.entries.all(),
            'hot_items': hot_items(),
            'entryform': entryform
    	}
        return render_to_response('user.html', ctx, RequestContext(request))
    else:
   	 ctx = {
            'item': i,
            'entries': i.entries.all(),
            'hot_items': hot_items()
   	 }
        return render_to_response('index.html', ctx, RequestContext(request))
    
# done
def items(request,item_id):
    """Item page"""
    i = get_object_or_404(Item, id=item_id)
    entryform = EntryForm()
    if request.user.is_authenticated():
 	 ctx = {
		'item': i,
		'entries': i.entries.all(),
		'hot_items': hot_items(),
		'entryform': entryform
  	  }
        return render_to_response('user.html', ctx, RequestContext(request))
    else:
    	ctx = {
     	       'item': i,
     	       'entries': i.entries.all(),
     	       'hot_items': hot_items()
 	   }
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
def edit_entry(request,entry_id):
    """Entry edit page"""
    e = get_object_or_404(Entry, id=entry_id)
    ctx = {
        'entry': e,
        'hot_items': hot_items()
    }
    return render_to_response('edit.html', ctx, RequestContext(request))
    
@login_required
def edit_item(request,item_id):
    """Item edit page"""
    e = get_object_or_404(Entry, id=entry_id)
    ctx = {
        'entry': e,
        'hot_items': hot_items()
    }
    return render_to_response('edit.html', ctx, RequestContext(request))

@login_required
def add_item(request):
    """Add item page"""
    return render_to_response('additem.html', RequestContext(request))

# done
@login_required
def profile(request):
    """profile"""
    return render_to_response('profile.html', {'hot_items': hot_items()}, RequestContext(request))

# done
def public(request, user_id):
    """public profile"""
    if request.user.is_authenticated() and request.user.id == user_id:
    	return render_to_response('profile.html', {'hot_items': hot_items()}, RequestContext(request))
    elif request.user.is_authenticated():
    	public_user = get_object_or_404(User, id=user_id)
    	ctx = {
    		'public_user' : public_user,
    		'hot_items': hot_items()
    	}
	return render_to_response('public_log.html', ctx, RequestContext(request))
    else:
    	public_user = get_object_or_404(User, id=user_id)
    	ctx = {
    		'public_user' : public_user,
    		'hot_items': hot_items()
    	}
	return render_to_response('public.html', ctx, RequestContext(request))

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
       
def login_error(request):
    """Add item page"""
    return render_to_response('login_error.html', RequestContext(request))
    
@login_required
def add_entry(request,item_id):
    """Add entry page"""
    item = get_object_or_404(Item, id=item_id)
    if request.POST:
    	entryform = EntryForm(request.POST)
    	if entryform.is_valid():
    		entryform.save(request,item)
    else:
    	entryform = EntryForm()
    ctx = {
    	    'item': item,
            'entries': item.entries.all(),
            'hot_items': hot_items(),
            'entryform': entryform
    }
    return render_to_response('user.html', ctx, RequestContext(request))
