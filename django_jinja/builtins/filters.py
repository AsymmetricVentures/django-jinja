# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse as django_reverse
from jinja2 import Markup


def safe(value):
    return Markup(force_unicode(value))


def reverse(value, *args, **kwargs):
    """
    Shortcut filter for reverse url on templates. Is a alternative to
    django {% url %} tag, but more simple.

    Usage example:
        {{ 'web:timeline'|reverse(userid=2) }}

    This is a equivalent to django:
        {% url 'web:timeline' userid=2 %}

    """
    return django_reverse(value, args=args, kwargs=kwargs)


from django.template.defaultfilters import addslashes
from django.template.defaultfilters import capfirst
from django.utils.html import escapejs as escapejs_filter
from django.utils.html import fix_ampersands as fix_ampersands_filter
from django.template.defaultfilters import floatformat
from django.template.defaultfilters import iriencode
from django.template.defaultfilters import linenumbers
from django.template.defaultfilters import make_list
try:
    from django.utils.text import slugify
except ImportError:
    from django.template.defaultfilters import slugify
from django.template.defaultfilters import stringformat
from django.template.defaultfilters import title
from django.template.defaultfilters import truncatechars
from django.template.defaultfilters import truncatewords
from django.template.defaultfilters import truncatewords_html
from django.template.defaultfilters import upper
from django.template.defaultfilters import lower
from django.template.defaultfilters import urlencode
from django.template.defaultfilters import urlize
from django.template.defaultfilters import urlizetrunc
from django.template.defaultfilters import wordcount
from django.template.defaultfilters import wordwrap
from django.template.defaultfilters import ljust
from django.template.defaultfilters import rjust
from django.template.defaultfilters import center
from django.template.defaultfilters import cut
from django.template.defaultfilters import linebreaks_filter
from django.template.defaultfilters import linebreaksbr
from django.template.defaultfilters import removetags
from django.template.defaultfilters import striptags
from django.template.defaultfilters import join
from django.template.defaultfilters import length
from django.template.defaultfilters import random
from django.template.defaultfilters import add
from django.template.defaultfilters import date
from django.template.defaultfilters import time
from django.template.defaultfilters import timesince_filter
from django.template.defaultfilters import timeuntil_filter
from django.template.defaultfilters import default
from django.template.defaultfilters import default_if_none
from django.template.defaultfilters import divisibleby
from django.template.defaultfilters import yesno
from django.template.defaultfilters import filesizeformat
from django.template.defaultfilters import pprint
from django.template.defaultfilters import pluralize
