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



