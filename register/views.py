
from django.shortcuts import render, redirect

from .forms import RegisterForm, patientform
from django.views.generic import TemplateView


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})


def HomeView(request):
    context = {}
    # create object of form
    form = patientform(request.POST or None, request.FILES or None)
    # check if form data is valid
    if form.is_valid():

        #Blood Eosinophilis =patientform.cleaned_data['patient_name']
        # save the form data to model
        form.save()

    context['form'] = patientform()
    return render(request, "register/home.html", context)
