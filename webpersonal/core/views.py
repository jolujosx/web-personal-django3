from django.shortcuts import render,HttpResponse

html_base="""
    "<h1>Mi web personal</h1>
    <ul>
        <li><a href="{% url 'home' %}">Portada</a></li>
        <li><a href="{% url 'about' %}">Acerca de...</a></li>
        <li><a href="{% url 'potafolio' %}">Portafolio</a></li>
        <li><a href="{% url 'contact' %}">Contactos</a></li>
    </ul>
"""

# Create your views here.
def home(request):
    return render(request,"core/home.html")


def about(request):
   return render(request,"core/about.html")



def contact(request):
   return render(request,"core/contact.html")
