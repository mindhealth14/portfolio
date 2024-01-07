from django import forms



class EmailContactForm(forms.Form):
    full_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    subject = forms.CharField(max_length=150)
    comments = forms.CharField(required=False, widget=forms.Textarea)
    
    
    
