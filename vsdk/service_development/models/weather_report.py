from django.db import models

from .vs_element import VoiceServiceElement
from .voicelabel import VoiceLabel
from .vse_choice import Choice

class WeatherReport(models.Model):
    """
    An user-generated weather report, including wind speed and rainfall
    """
    session = models.ForeignKey(
        'CallSession',
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        )
    wind = models.ForeignKey(
        'WindSpeed',
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        )
    rain = models.ForeignKey(
        'RainFall',
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        )
    start = models.DateTimeField(auto_now_add = True)
    _urls_name = 'service-development:weather-report'


    def __str__(self):
        return "Weather report: "
		
		
class WindSpeed(models.Model):
    name = models.CharField('name', max_length=100)
    voice_label = models.ForeignKey(
            VoiceLabel,
            on_delete = models.SET_NULL,
            null = True,
            blank = True,
            )
			
    def __str__(self):
        return "WindSpeed: " + self.name

class RainFall(models.Model):
    name = models.CharField('name', max_length=100)
    voice_label = models.ForeignKey(
            VoiceLabel,
            on_delete = models.SET_NULL,
            null = True,
            blank = True,
            )
	
    def __str__(self):
        return "Rainfall: " + self.name
		
		
class WeatherReportSubmit(Choice):
    _urls_name = 'service-development:wr_submit'
    rain_voice_label = models.ForeignKey(
            VoiceLabel,
            on_delete = models.SET_NULL,
            null = True,
            blank = True,
            )
	
	
    def __str__(self):
        return self.name

    def is_valid(self):
        return True
    is_valid.boolean = True

    def validator(self):
        errors = []
        return errors
			
			