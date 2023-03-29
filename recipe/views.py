from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .forms import CommentForm
from django.views.decorators.http import require_POST
from .models import Recipe

def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'recette/home.html', locals())


def detail(request, pk):
    recipe = get_object_or_404(Recipe, id=pk)
    category_name = recipe.get_category_display()
    current_category = recipe.category
    comments = recipe.comments.filter(active=True)
    comment = None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.save()
    else:
        form = CommentForm()
    similar_recipes = Recipe.objects.filter(category=current_category).exclude(id=recipe.id)
    context = {
        'recipe': recipe,
        'similar_recipes': similar_recipes,
        'category_name': category_name,
        'form': form,
        'comments': comments,
    }
    return render(request, 'recette/detail.html', context)


class CategoryView(View):
    def get(self, request, category):
        recipes = Recipe.objects.filter(category=category)
        categorie_choices = Recipe.CATEGORIE_CHOICES
        return render(request, 'recette/category.html', locals())