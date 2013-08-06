# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# Script   Name: urls.py
# Creation Date: 2011-04-23  22:29
# Last Modified: 2011-11-12 17:6:29
# Copyright (c)2011, DDTCMS Project
# Purpose: This file used for DDTCMS Project
# ------------------------------------------------------------

# python.
#import datetime
#import urllib
# ------------------------------------------------------------

# django.
from django.conf.urls.defaults import *
from django.core.paginator import Paginator, InvalidPage
from django.views.generic import DetailView, ListView

from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, \
                                        WeekArchiveView, DayArchiveView, TodayArchiveView, \
                                        DateDetailView

# ------------------------------------------------------------

# 3dpart.
#
# ------------------------------------------------------------

# ddtcms.
#from forms  import AForm,BForm
# ------------------------------------------------------------

# config.
#
# ------------------------------------------------------------
#


urlpatterns = patterns('',



    url(r'^$',     'chat.views.index',name='chat_index'),
    url(r'^func/req/$','chat.views.chat'),
    url(r'^func/langinfo/$','chat.views.langinfo'),

)

