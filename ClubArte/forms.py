from django import forms

class Date(forms.DateInput):
    input_type = "date"

class Poesia_Form(forms.Form):
    title_poesia = forms.CharField(max_length=50)
    author_poesia = forms.CharField(max_length=50)
    descr_poesia = forms.CharField(max_length=1000)
    img_poesia = forms.ImageField(required=False)

class Search_Poesia_Form(forms.Form):
    title_poesia = forms.CharField(max_length=50)
    author_poesia = forms.CharField(max_length=50)
    descr_poesia = forms.CharField(max_length=1000)

class Foto_Forms(forms.Form):
    title_foto = forms.CharField(max_length=50)
    descr_foto = forms.CharField(max_length=1000)
    img_foto = forms.ImageField(required=True)

class Search_Foto_Forms(forms.Form):
    title_foto = forms.CharField(max_length=50)
    descr_foto = forms.CharField(max_length=1000)
    img_foto = forms.ImageField(required=True)

class Cine_Form(forms.Form):
    title_movie = forms.CharField(max_length=50)
    direc_movie = forms.CharField(max_length=50)
    descr_movie = forms.CharField(max_length=1000)
    img_movie = forms.ImageField(required=False)

class Search_Cine_Form(forms.Form):
    title_movie = forms.CharField(max_length=50)
    direc_movie = forms.CharField(max_length=50)
    descr_movie = forms.CharField(max_length=1000)