from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseForbidden
from django import shortcuts
from django.shortcuts import render_to_response
from google.appengine.ext import db
import logging
import random
import cgi

import util
import reqfilter

def add_numbers(req):
    x = int(req.mParams.get('x', 1))
    y = int(req.mParams.get('y', 2))
    req.SetCacheTime(0)
    return render_to_response('numbers.html', {'x':x, 'y':y, 'z':x+y})
