from django import forms
from .models import Notes
from datetime import datetime


class AddNewNoteForm(forms.ModelForm):
    title =  forms.CharField(widget=forms.TextInput(attrs={'name':'title'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'name':'body', 'rows':3, 'cols':5}))

    class Meta:
        model = Notes
        fields = ('title', 'body')
        
        
        
    def save(self, commit=True):
        note = Notes.objects.create(
            title = self.cleaned_data['title'],
            body = self.cleaned_data['body'],
            created_at = datetime.now(),
        )
        return note
    
    
    
class UpdateNoteForm(forms.ModelForm):
            
    title =  forms.CharField(widget=forms.TextInput(attrs={'name':'title'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'name':'body', 'rows':3, 'cols':5}))

    
    
    class Meta:
        model = Notes
        fields = ('title', 'body')
        
        
        
    def save(self, commit=True):
        note = Notes.objects.update(
            title = self.cleaned_data['title'],
            body = self.cleaned_data['body'],
            created_at = datetime.now()
        )
        return note