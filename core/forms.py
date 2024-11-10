from django import forms
from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'headline', 'company', 'website', 'resume', 'subscribe_to_jobs']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'subscribe_to_jobs': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        } 