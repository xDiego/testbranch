from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(
        label='first_name',
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control',
                                      'placeholder':'Nombre'})
    )
    last_name = forms.CharField(
        label='last_name',
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control',
                                      'placeholder': 'Apellido'})
    )
    email = forms.EmailField(
        label='email',
        widget=forms.EmailInput(attrs={'class':'form-control',
                                       'placeholder':'Correo electronico'})
    )
    message = forms.CharField(
        label='message',
        widget=forms.Textarea(attrs={'class':'form-control',
                                      'placeholder':'Tu Mensaje'})
    )
