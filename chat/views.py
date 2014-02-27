# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.core.cache import cache

from django.views.generic import DateDetailView
from django.views.generic import DetailView, ListView
from django.views.decorators.http import  condition
# ------------------------------------------------------------

def index(request):
    template_name = 'chat/talk.html'
    context = RequestContext(request)
    return render_to_response(template_name,
                              {},
                              context_instance=context)

from buddy.urls import bot

def chat(request, success_url=None,
             form_class=None,
             template_name='blog/blog_post.html',
             extra_context=None):
    

    if request.method == 'POST':
        req = 'Wrong'
    else:
        req = request.GET.get('msg', 'Wrong')
    resp = bot.respond(req)
    resp = resp.replace('"','`')
    #resp.decode('utf-8')
    #print repr(resp)
    #print resp.decode('utf-8')
    return HttpResponse('{"response":"%s","id":24442977,"result":100,"msg":"OK."}'  % resp )


def langinfo(request):
    return HttpResponse('{"result":200,"nctable":[{"dbcnt":5936741,"nc":"ko","vnc":"한국어"},{"dbcnt":5810155,"nc":"en","vnc":"English"},{"dbcnt":2144960,"nc":"zh","vnc":"Chinese – Traditional (繁體)"},{"dbcnt":2040512,"nc":"ch","vnc":"Chinese – Simplified (简体)"},{"dbcnt":1311078,"nc":"ph","vnc":"Filipino"},{"dbcnt":970209,"nc":"he","vnc":"Hebrew"},{"dbcnt":794209,"nc":"th","vnc":"Thai"},{"dbcnt":659139,"nc":"id","vnc":"Bahasa Indonesia"},{"dbcnt":541592,"nc":"ja","vnc":"日本語"},{"dbcnt":286403,"nc":"ms","vnc":"Bahasa Melayu"},{"dbcnt":285839,"nc":"vn","vnc":"tieng viet"},{"dbcnt":246024,"nc":"ar","vnc":"العربية"},{"dbcnt":182343,"nc":"ru","vnc":"Русский<"},{"dbcnt":170209,"nc":"nl","vnc":"Nederlands"},{"dbcnt":162596,"nc":"de","vnc":"Deutsch"},{"dbcnt":144556,"nc":"pt","vnc":"Português"},{"dbcnt":130627,"nc":"es","vnc":"Español"},{"dbcnt":116493,"nc":"it","vnc":"Italiano"},{"dbcnt":89662,"nc":"fr","vnc":"Français"},{"dbcnt":45542,"nc":"sv","vnc":"Svenska"},{"dbcnt":36916,"nc":"da","vnc":"Dansk"},{"dbcnt":30058,"nc":"tr","vnc":"Türkçe"},{"dbcnt":28568,"nc":"nb","vnc":"Norsk (Bokmål)"},{"dbcnt":11407,"nc":"hr","vnc":"Hrvatski"},{"dbcnt":3156,"nc":"kh","vnc":"Khmer"},{"dbcnt":2830,"nc":"pl","vnc":"Polski"},{"dbcnt":2649,"nc":"fi","vnc":"Suomi"},{"dbcnt":2636,"nc":"ml","vnc":"Malayalam"},{"dbcnt":2233,"nc":"hu","vnc":"magyar"},{"dbcnt":2222,"nc":"ro","vnc":"Română"},{"dbcnt":2027,"nc":"hi","vnc":"Hindi"},{"dbcnt":1703,"nc":"bg","vnc":"Български"},{"dbcnt":1518,"nc":"ta","vnc":"Tamil"},{"dbcnt":1472,"nc":"el","vnc":"Ελληνικά"},{"dbcnt":1309,"nc":"lt","vnc":"Lietuvių"},{"dbcnt":845,"nc":"uk","vnc":"українець"},{"dbcnt":824,"nc":"pa","vnc":"Punjabi"},{"dbcnt":810,"nc":"af","vnc":"Afrikaans"},{"dbcnt":756,"nc":"cs","vnc":"čeština"},{"dbcnt":648,"nc":"sk","vnc":"Slovenčina"},{"dbcnt":548,"nc":"rs","vnc":"Српски"},{"dbcnt":479,"nc":"ca","vnc":"catala"},{"dbcnt":441,"nc":"te","vnc":"Telugu"},{"dbcnt":425,"nc":"fa","vnc":"فارسی"},{"dbcnt":421,"nc":"eu","vnc":"Euskara"},{"dbcnt":414,"nc":"cy","vnc":"Cymraeg"},{"dbcnt":145,"nc":"al","vnc":"Shqipëria"},{"dbcnt":64,"nc":"az","vnc":"آذربايجان ديلی"}]}' )
