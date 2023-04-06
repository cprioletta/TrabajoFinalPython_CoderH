from django.db import models

# Create your models here.
class Poesia(models.Model):
    id_poesia = models.AutoField(primary_key=True)
    title_poesia = models.CharField(max_length=50)
    author_poesia = models.CharField(max_length=50)
    descr_poesia = models.CharField(max_length=1000)
    user_poesia = models.CharField(max_length=50)
    creationdate_poesia = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"El poema {self.title_poesia}, escrito por {self.author_poesia}"

class ImgPoesia(models.Model):
    id_poesia = models.OneToOneField(Poesia, on_delete=models.CASCADE)
    img_poesia = models.ImageField(upload_to="poesia", null=True, blank=True)

class Cine(models.Model):
    id_movie = models.AutoField(primary_key=True)
    title_movie = models.CharField(max_length=50)
    direc_movie = models.CharField(max_length=50)
    descr_movie = models.CharField(max_length=1000)
    user_movie = models.CharField(max_length=50)
    creationdate_movie = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"La película {self.title_movie}, escrito por {self.direc_movie}"

class ImgCine(models.Model):
    id_movie = models.OneToOneField(Cine, on_delete=models.CASCADE)
    img_movie = models.ImageField(upload_to='cine', null=True, blank=True)

class Fotografia(models.Model):
    id_foto = models.AutoField(primary_key=True)
    title_foto = models.CharField(max_length=50)
    author_foto = models.CharField(max_length=60)
    descr_foto = models.CharField(max_length=1000)
    user_foto = models.CharField(max_length=50)
    creationdate_foto = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"La fotografía {self.title_foto} tomada por {self.author_foto}."

class ImgFotograf(models.Model):
    id_foto = models.OneToOneField(Fotografia, on_delete=models.CASCADE)
    img_foto = models.ImageField(upload_to='fotog', null=True, blank=True)
