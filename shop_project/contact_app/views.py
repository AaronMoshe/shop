from django.shortcuts import render, redirect
from contact_app.models import Contact
from contact_app.forms import ContactForm

def contact_form(request):
	if request.method == 'POST':
		contact = Contact.objects.get_or_create(subject=request.POST.get('subject'), email=request.POST.get('email'), text=request.POST.get('text'))
		return redirect('sucess/')

	contact_form = ContactForm()
	return render(request, 'contact_form.html', context={'contact_form': contact_form})

def sucess(request):
	return render(request, 'sucess.html')