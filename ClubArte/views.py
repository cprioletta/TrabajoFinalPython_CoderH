from django.contrib import messages
from django.shortcuts import render, redirect
from ClubArte.forms import Poesia_Form, Search_Poesia_Form, Cine_Form, Search_Cine_Form, Foto_Forms, Search_Foto_Forms
from ClubArte.models import Poesia, ImgPoesia, Cine, ImgCine, Fotografia, ImgFotograf


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
    username =request.user.username
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
# cinematografia modules
def cine_crear(request):
    cine = Cine_Form(request.POST)
    username = None
    username = request.user.username
    if request.method == "POST":
        if cine.is_valid():
            cine = Cine(
                title_movie=request.POST.get("title_movie"),
                direc_movie=request.POST.get("direc_movie"),
                descr_movie=request.POST.get("descr_movie"),
                user_movie=username,
            )
            cine.save()
            if "img_movie" in request.FILES:
                imagen = request.FILES["img_movie"]
                img = ImgCine(id_movie=cine, img_movie=imagen)
                img.save()
            messages.info(request, "Los datos se cargaron con éxito.")
        else:
            messages.info(request, "Los datos no pudieron ser cargados.")
        contexto = {
            "formulariocine": Cine_Form()
        }
        return render(request, "ClubArte/cinema/cine.html", contexto)

def cine_buscar(request):
    username = None
    username = request.user.username
    c_buscar = []
    if request.method == 'POST':
        title_movie = request.POST.get('title_movie')
        direc_movie = request.POST.get('direc_movie')
        descr_movie = request.POST.get('descr_movie')
        if request.user.is_superuser:
            c_buscar = Cine.objects.filter(title_movie__icontains=title_movie) & \
                       Cine.objects.filter(direc_movie__icontains=direc_movie) & \
                       Cine.objects.filter(descr_movie__contains=descr_movie)
        else:
            c_buscar = Cine.objects.filter(title_movie__icontains=title_movie) & \
                       Cine.objects.filter(direc_movie__icontains=direc_movie) & \
                       Cine.objects.filter(descr_movie__contains=descr_movie) & \
                       Cine.objects.filter(user_movie=username)

    contexto = {
        'buscar_cine': Search_Cine_Form(),
        'cine': c_buscar
    }
    return render(request, 'ClubArte/cinema/search_cine.html', contexto)

def cine_buscar_ver(request):
    c_buscar = []
    if request.method == 'POST':
        title_movie = request.POST.get('title_movie')
        direc_movie = request.POST.get('direc_movie')
        descr_movie = request.POST.get('descr_movie')
        c_buscar = Cine.objects.filter(title_movie__icontains=title_movie) & \
                    Cine.objects.filter(direc_movie__icontains=direc_movie) & \
                    Cine.objects.filter(descr_movie__contains=descr_movie)

    contexto = {
        'buscar_cine': Search_Cine_Form(),
        'cine': c_buscar
    }
    return render(request, 'ClubArte/cinema/obs_cine.html', contexto)

def cine_elim(request, id_movie):
    cine = Cine.objects.get(id_movie=id_movie)
    cine.delete()

    return redirect('EliminarCine')

def cine_modif(request, id_movie):
    cine = Cine.objects.get(id_movie=id_movie)

    if request.method == 'POST':
        cine_t = Cine_Form(request.POST)
        if cine_t.is_valid():
            data = cine_t.cleaned_data
            cine.title_movie = data.get('title_movie')
            cine.direc_movie = data.get('direc_movie')
            cine.descr_movie = data.get('descr_movie')
            cine.save()

            img = ImgCine.objects.filter(id_movie=cine)
            if 'ImgCine' in request.FILES:
                imagen = request.FILES["ImgCine"]
                if img.exists():
                    if imagen:
                        img = img[0]
                        img.ImgCine = imagen
                        img.save()

                else:
                    img = ImgCine(id_movie=cine, ImgCine=imagen)
                    img.save()
            messages.info(request, 'Los datos se actualizaron con exito!')
            return redirect('BuscarCine')

    cine_form = Cine_Form(initial={
        'title_movie': cine.title_movie,
        'direc_movie': cine.direc_movie,
        'descr_movie': cine.descr_movie,
        'user_movie': cine.user_movie,
    }
    )
    contexto = {
        'formulariocine': Cine_Form,
        'cine': cine,
    }

    return render(request, 'ClubArte/cinema/modif_cine.html', contexto)

def cine_ver(request, id_movie):
    cine = Cine.objects.get(id_movie=id_movie)
    cine_form = Cine_Form(initial={
        'title_movie': cine.title_movie,
        'direc_movie': cine.direc_movie,
        'descr_movie': cine.descr_movie,
    }
    )
    contexto = {
        'formulariocine': Cine_Form,
        'cine': cine,
    }

    return render(request, 'ClubArte/cinema/cine_ver.html', contexto)

# ------------------------------------------------------------------------------------
# fotografia modules

def foto_crear(request):
    foto = Foto_Forms(request.POST)
    username = None
    username = request.user.username
    if request.method == 'POST':
        if foto.is_valid():
            foto = Fotografia(
                title_foto=request.POST.get('title_foto'),
                author_foto=request.POST.get('author_foto'),
                descr_foto=request.POST.get('descr_foto'),
                user_foto=username,
            )
            foto.save()
            if 'img_foto' in request.FILES:
                imagen = request.FILES["imgmus"]
                img = ImgFotograf(id_musica=foto, imgmus=imagen)
                img.save()
            messages.info(request, 'Los datos se han cargado con exito!')
        else:
            messages.info(request, 'Los datos no se han cargado con exito!')

    contexto = {
        'formulariomusica': Foto_Forms()
    }
    return render(request, 'ClubArte/photo/photo.html', contexto)

def foto_buscar(request):
    username = None
    username = request.user.username
    f_buscar = []
    if request.method == 'POST':
        title_foto = request.POST.get('title_foto')
        author_foto = request.POST.get('author_foto')
        descr_foto = request.POST.get('descr_foto')
        if request.user.is_superuser:
            f_buscar = Fotografia.objects.filter(title_foto__icontains=title_foto) & \
                       Fotografia.objects.filter(author_foto__icontains=author_foto) & \
                       Fotografia.objects.filter(descr_foto__icontains=descr_foto)
        else:
            f_buscar = Fotografia.objects.filter(title_foto__icontains=title_foto) & \
                       Fotografia.objects.filter(author_foto__icontains=author_foto) & \
                       Fotografia.objects.filter(descr_foto__icontains=descr_foto) & \
                       Fotografia.objects.filter(user_foto=username)
    contexto = {
        'buscar_foto': Search_Foto_Forms,
        'musica': f_buscar
    }
    return render(request, 'ClubArte/photo/foto_buscar.html', contexto)

def foto_buscar_ver(request):
    f_buscar = []
    if request.method == 'POST':
        title_foto = request.POST.get('title_foto')
        author_foto = request.POST.get('author_foto')
        descr_foto = request.POST.get('descr_foto')
        f_buscar = Fotografia.objects.filter(title_foto__icontains=title_foto) & \
                    Fotografia.objects.filter(author_foto__icontains=author_foto) & \
                    Fotografia.objects.filter(descr_foto__icontains=descr_foto)
        contexto = {
        'buscar_foto': Search_Foto_Forms(),
        'foto': f_buscar
    }
    return render(request, 'ClubArte/photo/buscar_ver_foto.html', contexto)

def foto_eliminar(request, id_foto):
    foto = Fotografia.objects.get(id_foto=id_foto)
    foto.delete()

    return redirect('BuscarFoto')

def foto_modificar(request, id_foto):
    foto = Fotografia.objects.get(id_foto=id_foto)

    if request.method == 'POST':
        fot = Foto_Forms(request.POST)
        if fot.is_valid():
            data = fot.cleaned_data
            fot.title_foto = data.get('title_foto')
            fot.author_foto = data.get('author_foto')
            fot.descr_foto = data.get('descr_foto')
            fot.save()

            img = ImgFotograf.objects.filter(id_foto=fot)
            if 'imgfot' in request.FILES:
                imagen = request.FILES["imgfot"]
                if img.exists():
                    if imagen:
                        img = img[0]
                        img.ImgFotograf = imagen
                        img.save()

                else:
                    img = ImgFotograf(id_foto=fot, imgfot=imagen)
                    img.save()
            messages.info(request, 'Los datos se han actualizado con exito!')

            return redirect('BuscarFoto')

    foto_form = Foto_Forms(initial={
        'title_foto': fot.title_foto,
        'author_foto': fot.author_foto,
        'descr_foto': fot.descr_foto,
        'user_foto': fot.user_foto,
    }
    )
    contexto = {
        'formulariofoto': foto_form,
        'foto': fot,
    }

    return render(request, 'ClubArte/photo/modif_foto.html', contexto)

def foto_ver(request, id_foto):
    fot = Fotografia.objects.get(id_foto=id_foto)
    foto_form = Foto_Forms(initial={
        'title_foto': fot.title_foto,
        'author_foto': fot.author_foto,
        'descr_foto': fot.descr_foto,
    }
    )
    contexto = {
        'formulariofoto': foto_form,
        'foto': fot,
    }

    return render(request, 'ClubArte/photo/ver_foto.html', contexto)
