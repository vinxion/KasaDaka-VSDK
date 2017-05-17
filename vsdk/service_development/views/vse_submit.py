from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect

from ..models import *

def submit_get_redirect_url(submit_element,session):
    if not submit_element.final_element:
        return submit_element.redirect.get_absolute_url(session)
    else:
        return None
    


def submit_generate_context(submit_element,session):
    language = session.language
    submit_voice_fragment_url = submit_element.get_voice_fragment_url(language)
    redirect_url = submit_get_redirect_url(submit_element,session) 
    context = {'submit_voice_fragment_url':submit_voice_fragment_url,
            'redirect_url':redirect_url}
    return context


def submit(request, element_id, session_id):
    submit_element = get_object_or_404(submit, pk=element_id)
    session = get_object_or_404(CallSession, pk=session_id)
    session.record_step(submit_element)
    context = submit_generate_context(submit_element, session)
    
    return render(request, 'submit.xml', context, content_type='text/xml')

