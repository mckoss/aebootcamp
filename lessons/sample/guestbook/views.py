import reqfilter

from django import forms
from django.shortcuts import render_to_response, redirect
from guestbook.models import Greeting

class GuestbookForm(forms.Form):
    author = forms.CharField(max_length=40)
    website = forms.URLField(required=False)
    content = forms.CharField(widget=forms.Textarea)

def list_entries(request):
    guestbook_form = GuestbookForm(request.POST or None)
    if guestbook_form.is_valid():
        greeting = Greeting(
            author=guestbook_form.cleaned_data['author'],
            website=guestbook_form.cleaned_data['website'],
            content=guestbook_form.cleaned_data['content'])
        greeting.put()
        return redirect(list_entries)
    greetings_list = Greeting.all().order('-date').fetch(10)
    return reqfilter.RenderResponse('guestbook/index.html', locals())
