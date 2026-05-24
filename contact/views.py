from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm


def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get("name", "")
            email = request.POST.get("email", "")
            content = request.POST.get("content", "")
            # Enviamos correo y redireccionamos
            # asunto
            # cuerpo
            # email_origen
            # email_destino
            # email al que se respondera el msj
            email = EmailMessage(
                "La Caffetiera: Nuevo mensaje de contacto",
                "De {} <{}> \n\n Escribio: \n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["mirodriguezor@gmail.com"],
                reply_to=[email],
            )
            try:
                email.send()
                return redirect(reverse("contact") + "?ok")
            except:
                return redirect(reverse("contact") + "?fail")
    data = {"form": contact_form}
    return render(request, "contact/contact.html", data)
