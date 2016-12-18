from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from forms import ContactForm
COMPANY_EMAIL = 'alexander.890@hotmail.com'


# Create your views here.
def home_page(request):
    form = ContactForm()
    context = {'my_form': form}
    return render(request, 'sales_app/index.html', context=context)


def handle_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name', None)
            last_name = form.cleaned_data.get('last_name', None)
            email = form.cleaned_data.get('email', None)
            message = form.cleaned_data.get('message', None)

            # Check if the email is valid
            try:
                validate_email(email)
            except ValidationError:
                # If there's an error
                print "Error not valid email"
            else:
                # Proceed with sending an email
                if message:
                    subject = "Nuevo Cliente"

                    # Check if they put their name on the form
                    if first_name and last_name:
                        subject = "%s, %s" % (first_name, last_name)

                    send_mail(
                        subject,
                        message,
                        email,
                        [COMPANY_EMAIL],
                        fail_silently=False
                    )
                        
    return redirect('home_page')
