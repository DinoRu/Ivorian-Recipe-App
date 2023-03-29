from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field



LEVEL_CHOICES = (
    ('F', 'Facile'),
    ('M', 'Moyenne'),
    ('D', 'Difficile'),
)

class Recipe(models.Model):

    CATEGORIE_CHOICES = (
        ('ACCO', 'Accompagnement'),
        ('PLAT', 'PLat'),
        ('DESS', 'Dessert'),
        ('BOIS', 'Boisson'),
    )


    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250)
    category = models.CharField(max_length=4, choices=CATEGORIE_CHOICES)
    description = CKEditor5Field('Description', config_name='extends')
    recipe_img = models.ImageField(upload_to='Image/')
    ingredient = CKEditor5Field('Ingredient', config_name='extends')
    instruction = CKEditor5Field('Instruction', config_name='extends')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    time_cook = models.CharField(max_length=10)
    temps_cuisson = models.CharField(max_length=10)
    num_people = models.CharField(max_length=10)
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES)
    rate = models.IntegerField()
 

    class Meta:
        ordering = ['-created']
       
    def __str__(self):
        return self.title


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    commentaire = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
    

