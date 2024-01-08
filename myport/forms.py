from django import forms


<<<<<<< HEAD
=======

>>>>>>> 2619a3918320ef852ef3d49de35081a6e110ccb9
class EmailContactForm(forms.Form):
    full_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    subject = forms.CharField(max_length=150)
<<<<<<< HEAD
    comments = forms.CharField(required=False, widget=forms.Textarea)
=======
    comments = forms.CharField(required=False, widget=forms.Textarea)
    
    
    
>>>>>>> 2619a3918320ef852ef3d49de35081a6e110ccb9
