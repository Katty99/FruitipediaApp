from django.shortcuts import render, redirect

from FruitipediaApp.account.models import Profile
from FruitipediaApp.fruit.forms import FruitFrom, DeleteFruitFrom, EditFruitFrom
from FruitipediaApp.fruit.models import Fruit


# Create your views here.
def dashboard(request):
    profile = Profile.objects.first()
    fruits = Fruit.objects.all()
    context = {'fruits': fruits, 'profile': profile}
    return render(request, template_name='fruit/dashboard.html', context=context)


def create_fruit(request):
    form = FruitFrom(request.POST or None)
    profile = Profile.objects.first()
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {'form': form, 'profile': profile}
    return render(request, template_name='fruit/create-fruit.html', context=context)


def details_fruit(request, fruitId):
    fruit = Fruit.objects.get(id=fruitId)
    profile = Profile.objects.first()
    context = {'fruit': fruit, 'profile': profile}
    return render(request, template_name='fruit/details-fruit.html', context=context)


def edit_fruit(request, fruitId):
    fruit = Fruit.objects.get(id=fruitId)
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = EditFruitFrom(initial=fruit.__dict__)
        context = {'form': form, 'profile': profile}
        return render(request, template_name='fruit/edit-fruit.html', context=context)
    else:
        form = EditFruitFrom(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            context = {'form': form, 'profile': profile}
            return render(request, template_name='fruit/edit-fruit.html', context=context)


def delete_fruit(request, fruitId):
    fruit = Fruit.objects.get(id=fruitId)
    profile = Profile.objects.first()
    if request.method == 'POST':
        fruit.delete()
        return redirect('dashboard')
    form = DeleteFruitFrom(instance=fruit)
    context = {'form': form, 'profile': profile}
    return render(request, template_name='fruit/delete-fruit.html', context=context)
