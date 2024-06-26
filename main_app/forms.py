# queuetube/main_app/forms.py

from .models import Video
from django import forms

# class VideoForm(forms.ModelForm):
#     class Meta:
#         model = Video 
#         fields = ['title', 'url', 'youtube_id']
#         labels = {'youtube_id':'YouTube ID' }

#for youtubeAPI
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video 
        fields = ['url']
        labels = {'url':'YouTube URL' }
        
class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=255, label='Search for Videos:')