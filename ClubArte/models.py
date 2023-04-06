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

