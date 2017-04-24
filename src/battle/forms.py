from datetime import timedelta
from django import forms
from .models import Match, now

current_time = now - timedelta(minutes=2)

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = "__all__"

    def clean(self):
        hashtag_1 = self.cleaned_data.get('hashtag_1')
        hashtag_2 = self.cleaned_data.get('hashtag_2')
        start_time = self.cleaned_data.get('start_time')
        end_time = self.cleaned_data.get('end_time')

        #DateTime Validation
        if start_time >= end_time:
            raise forms.ValidationError("The start time must be less than the end time")
        elif  end_time <= start_time:
            raise forms.ValidationError("The end time must be greater than the start time")
        elif start_time <= current_time:
            raise forms.ValidationError("The start time must be greater than the current time.")


        #hashtag validation    
        if hashtag_1 == hashtag_2 or hashtag_2 == hashtag_1:
             raise forms.ValidationError("You can not put the same hashtags")
        elif not hashtag_1.startswith('#') or not hashtag_2.startswith('#'):
            raise forms.ValidationError("Please include '#' before your hashtags")
        elif ' ' in hashtag_1 or ' ' in hashtag_2:
            raise forms.ValidationError("Please omit spaces in the hashtag search.")

        return self.cleaned_data

