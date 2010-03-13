from django.shortcuts import render_to_response
from django.template import RequestContext
from guestbook.models import Greeting

def list_entries(request):
    return render_to_response('guestbook/index.html', locals(),
                              context_instance=RequestContext(request))

def create_entry(request):
    request.POST = request.POST.copy()
    request.POST['author'] = str(request.user.key())
    return create_object(request, Greeting, post_save_redirect='/guestbook')
