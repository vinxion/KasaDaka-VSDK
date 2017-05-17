from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect

from ..models import *


def choice_options_resolve_redirect_urls(choice_options, session):
    choice_options_redirection_urls = []
    for choice_option in choice_options:
        redirect_url = choice_option.redirect.get_absolute_url(session)
        choice_options_redirection_urls.append(redirect_url)
    return choice_options_redirection_urls

def choice_options_resolve_voice_labels(choice_options, language):
    """
    Returns a list of voice labels belonging to the provided list of choice_options.
    """
    choice_options_voice_labels = []
    for choice_option in choice_options:
        choice_options_voice_labels.append(choice_option.voice_label.get_voice_fragment_url(language))
    return choice_options_voice_labels

def wr_generate_context(wr_submit, session):
    rain_categories =  RainFall.objects.all()
    wind_categories = WindSpeed.objects.all()
    language = session.language
    redirect = '/vxml/wr_submit/'+str(wr_submit.id)+'/'+str(session.id)
    context = {'wr_submit':wr_submit,
                'wind_voice_label':wr_submit.get_voice_fragment_url(language),
                'rain_voice_label':wr_submit.rain_voice_label.get_voice_fragment_url(language),
                'rain_options': rain_categories,
                'rain_options_voice_labels':choice_options_resolve_voice_labels(rain_categories, language),
                'wind_options': wind_categories,
                'wind_options_voice_labels':choice_options_resolve_voice_labels(wind_categories, language),
                'choice_options_redirect_urls': [],
                'language': language,
				'session_id' : session.id,
				'redirect' : redirect,
                }
    return context

def wr_submit(request, wr_submit_id, session_id):
    if request.POST:
        pass
    wr_submit = get_object_or_404(WeatherReportSubmit, pk=wr_submit_id)
    session = get_object_or_404(CallSession, pk=session_id)
    session.record_step(wr_submit)
    context = wr_generate_context(wr_submit, session)
    
    return render(request, 'submit_wr.xml', context, content_type='text/xml')

