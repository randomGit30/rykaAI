from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import RecipeForm
from .models import Cuisine, Recipe
from .ai import main
from django.core.mail import send_mail
def landing(request):
    return render(request, 'landing.html')

def publish_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('landing-page')  # Assuming you have a named URL for your landing page
    else:
        form = RecipeForm()
    return render(request, 'publish_recipe.html', {'form': form})

def read_recipes(request):
    recipes = Recipe.objects.all()  # Fetch all recipes from the database
    return render(request, 'read_recipes.html', {'recipes': recipes})


from .emailBase import send_ai_response_email  # Adjust the import path as necessary



def cure_recipes(request):
    res = ""
    try:
        if request.method == "POST":
            age = request.POST.get('age')
            weight = request.POST.get('weight')
            stress = request.POST.get('stress')
            mood = request.POST.get('mood')
            pressure = request.POST.get('pressure')
            # allergies = request.POST.get('allergies')
            email = request.POST.get('email')
            input_dict = {
                'age': age,
                'weight': weight,
                'stress level': stress,
                'mood': mood,
                'pressure': pressure,

            }
            res = main(input_dict)
            print(res)
            send_ai_response_email(email, res)
    except Exception as e:
        res = "Please fill all the fields!"
        print(e)
    return render(request, 'cures.html', {'res': res})