from django.contrib import messages
from django.shortcuts import render, redirect
from ClubArte.forms import Poesia_Form, Search_Poesia_Form
from ClubArte.models import Poesia, ImgPoesia


# Create your views here.
def Main(request):
    return render (request, "ClubArte/main.html")

# poesia modules
def poesia_crear(request):
    poesia = Poesia_Form(request.POST or None, request.FILES or None)
    username = None
    username = request.user.username
    if request.method == "POST":
        if poesia.is_valid():
            poesia = Poesia(
                title_poesia = request.POST.get("title_poesia"),
                author_poesia = request.POST.get("author_poesia"),
                descr_poesia = request.POST.get("descr_poesia"),
                user_poesia = request.POST.get("user_poesia"),
            )
            poesia.save()
            if "img_poesia" in request.FILES:
                imagen = request.FILES["img_poesia"]
                img = ImgPoesia(id_poesia=poesia, img_poesia=imagen)
                img.save()
            messages.info(request, "Los datos se cargaron con éxito.")
        else:
            messages.info(request, "Los datos no pudieron ser cargados.")

    contexto ={
        "formCargarPoesia": Poesia_Form(),
    }
    return render (request, "ClubArte/poesia/poesia.html", contexto)

def poesia_buscar(request):
    username = None
    username =request.user.usename
    p_buscar = []
    if request.method == "POST":
        title_poesia = request.POST.get("title_posia")
        autor_poesia = request.POST.get("autor_poesia")
        descr_poesia = request.POST.get("descr_poesia")
    if request.user.is_superuser:
        p_buscar = Poesia.objects.filter(title_poesia__icontains=title_poesia) & \
                   Poesia.objects.filter(autor_poesia__icontains=autor_poesia) & \
                   Poesia.objects.filter(descr_poesia__icontains=descr_poesia)
    else:
        p_buscar = Poesia.objects.filter(title_poesia__icontains=title_poesia) & \
                   Poesia.objects.filter(autor_poesia__icontains=autor_poesia) & \
                   Poesia.objects.filter(descr_poesia__icontains=descr_poesia) & \
                   Poesia.objects.filter(user_poesia__icontains=username)

    contexto={
        "buscar_poesia": Search_Poesia_Form,
        "poesia": p_buscar
    }
    return render(request, "ClubArte/poesia/search_poesia.html", contexto)

def poesia_buscar_ver(request):
    p_buscar = []
    if request.method == "POST":
        title_poesia = request.POST.get("title_poesia")
        author_poesia = request.POST.get("author_poesia")
        descr_poesia = request.POST.get("descr_poesia")
        p_buscar = Poesia.objects.filter(title_poesia__icontains=title_poesia) & \
                   Poesia.objects.filter(author_poesia__icontains=author_poesia) & \
                   Poesia.objects.filter(descr_poesia__icontains=descr_poesia)

    contexto = {
        "buscar_poesia": Search_Poesia_Form(),
        "poesia": p_buscar
    }
    return render(request, "ClubArte/poesia/obs_poesia.html", contexto)

def poesia_elim(request, id_poesia):
    poesia = Poesia.objects.get(id_poesia=id_poesia)
    poesia.delete()

    return redirect("BuscarPoesia")

def poesia_modif(request, id_poesia):
    poesia = Poesia.objects.get(id_poesia=id_poesia)
    if request.method == "POST":
        Poe = Poesia_Form(request.POST)
        if Poe.is_valid():
            data = Poe.cleaned_data
            poesia.title_poesia = data.get("title_poesia")
            poesia.author_poesia = data.get("author_poesia")
            poesia.descr_poesia = data.get("descr_poesia")
            poesia.save()

            img = ImgPoesia.objects.filter(id_poesia=poesia)
            if "img_poesia" in request.FILES:
                imagen = request.FILES["imgpoesia"]
                if img.exists():
                    if imagen:
                        img = img[0]
                        img.img_poesia = imagen
                        img.save()

                else:
                    img = ImgPoesia(id_poesia=poesia, img_poesia=imagen)
                    img.save()
                messages.info(request, 'Los datos se actualizaron con exito!')
                return redirect('PoesiaBuscar')

        poesia_form = Search_Poesia_Form(initial={
            'title_poesia': poesia.title_poesia,
            'author_poesia': poesia.author_poesia,
            'descr_poesia': poesia.descr_poesia,
            'user_poesia': poesia.user_poesia,
        }
        )
        contexto = {
            'buscar_poesia': poesia_form,
            'poesia': poesia,
        }

        return render(request, 'ClubArte/poesia/modif_poesia.html', contexto)

def poesia_ver(request, id_poesia):
    poesia = Poesia.objects.get(id_poesia=id_poesia)
    poesia_form = Poesia_Form(initial={
        'title_poesia': poesia.title_poesia,
        'author_poesia': poesia.author_poesia,
        'descr_poesia': poesia.descr_poesia,
    }
    )
    contexto = {
        'buscar_poesia': poesia_form,
        'poesia': poesia,
    }

    return render(request, 'ClubArte/poesia/ver_poesia.html', contexto)

# ------------------------------------------------------------------------------------
