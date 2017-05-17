from django.conf.urls import url, include

from . import views

app_name= 'service-development'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^choice/(?P<element_id>[0-9]+)/(?P<session_id>[0-9]+)$', views.choice, name='choice'),
	url(r'^wr_submit/(?P<wr_submit_id>[0-9]+)/(?P<session_id>[0-9]+)$', views.wr_submit, name='wr_submit'),
    url(r'^message/(?P<element_id>[0-9]+)/(?P<session_id>[0-9]+)$', views.message_presentation, name='message-presentation'),
    url(r'^start/(?P<voice_service_id>[0-9]+)$', views.voice_service_start, name='voice-service'),
    url(r'^start/(?P<voice_service_id>[0-9]+)/(?P<session_id>[0-9]+)$', views.voice_service_start, name='voice-service'),
    url(r'^user/register/$', views.user_registration, name = 'user-registration'),
    url(r'^language_select/(?P<voice_service_id>[0-9]+)/(?P<session_id>[0-9]+)$', views.language_selection, name = 'language-selection'),
]

