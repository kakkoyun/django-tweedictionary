from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.messages.api import get_messages
from dictionary.operations import send

import random

from dictionary.models import Item, Entry
from dictionary.forms import EntryForm, ItemForm
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
    i = get_object_or_404(Item, id=e.belong.id)
    if request.POST:
        entryform = EntryForm(request.POST)
        if entryform.is_valid():
            e = entryform.saveAs(request, e)
            entryform = EntryForm()
            ctx = {
                'item': i,
                'entries': i.entries.all(),
                'hot_items': hot_items(),
                'entryform': entryform
                }
        return render_to_response('user.html', ctx, RequestContext(request))
    else:
        entryform = EntryForm({'content' : e.content})
    ctx = {
        'entry' : e,
        'hot_items' : hot_items(),
        'entryform' : entryform
       }
    return render_to_response('edit_entry.html', ctx, RequestContext(request))

@login_required
def edit_item(request,item_id):
    """Item edit page"""
    i = get_object_or_404(Item, id=item_id)
    if request.POST:
        itemform = ItemForm(request.POST)
        if itemform.is_valid():
            i = itemform.saveAs(request, i)
            entryform = EntryForm()
            ctx = {
                'item': i,
                'entries': i.entries.all(),
                'hot_items': hot_items(),
                'entryform': entryform
                }
        return render_to_response('user.html', ctx, RequestContext(request))
    else:
        itemform = ItemForm({'name' : i.name})
    ctx = {
        'item' : i,
        'hot_items' : hot_items(),
        'itemform' : itemform
       }
    return render_to_response('edit_item.html', ctx, RequestContext(request))

# done
@login_required
def add_item(request):
    """Add item page"""
    if request.POST:
        itemform = ItemForm(request.POST)
        if itemform.is_valid():
            i = itemform.save(request)
            entryform = EntryForm()
            ctx = {
                'item': i,
                'entries': i.entries.all(),
                'hot_items': hot_items(),
                'entryform': entryform
                }
        return render_to_response('user.html', ctx, RequestContext(request))
    else:
        itemform = ItemForm()
    ctx = {
       'hot_items' : hot_items(),
       'itemform' : itemform
       }
    return render_to_response('additem.html', ctx, RequestContext(request))

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
    """Login error page"""
    ctx = {
    	'hot_items': hot_items(),
    	'error_name': "Some error appeared on login, please try again. If this problem continues contact with the admin on gmail@grgizem "
    }
    return render_to_response('error.html', ctx, RequestContext(request))

# done
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

# done
def entry(request, entry_id):
    """entry show page"""
    entry = get_object_or_404(Entry, id=entry_id)
    if request.user.is_authenticated():
    	ctx = {
    		'entry' : entry,
    		'hot_items': hot_items()
    	}
	return render_to_response('entry_log.html', ctx, RequestContext(request))
    else:
    	ctx = {
    		'entry' : entry,
    		'hot_items': hot_items()
    	}
	return render_to_response('entry.html', ctx, RequestContext(request))

# done
@login_required
def delete(request,entry_id):
	"""Delete entry function"""
	entry = get_object_or_404(Entry, id=entry_id)
	entry.delete()
	entryform = EntryForm()
	ctx = {
		'item': entry.belong,
		'entries': entry.belong.entries.all(),
		'hot_items': hot_items(),
		'entryform': entryform
	}
	return render_to_response('user.html', ctx, RequestContext(request))

# done
@login_required
def retweet(request,entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    if (request.user.id== entry.author.id) :
        send(request,entry_id)
        ctx = {
                'item': entry.belong,
                'entries': entry.belong.entries.all(),
                'hot_items': hot_items(),
                'entryform': EntryForm()
        }
        return render_to_response('user.html', ctx, RequestContext(request))
    else:
        ctx = {
                'error_name': "This is not your entry, you can not tweet it!",
                'hot_items': hot_items()
        }
        return render_to_response('error_log.html', ctx, RequestContext(request))
        
def git(request):
    return redirect('http://www.github.com', permanent=True)
 #   return HttpResponseRedirect("http://www.github.com")

