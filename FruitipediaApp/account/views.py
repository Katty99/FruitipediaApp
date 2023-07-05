from django.shortcuts import render, redirect

from FruitipediaApp.account.forms import ProfileForm, CreateProfileForm, EditProfileForm
from FruitipediaApp.account.models import Profile
from FruitipediaApp.fruit.models import Fruit


# Create your views here.
def create_profile(request):
    form = CreateProfileForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {'form': form}
    return render(request, template_name='account/create-profile.html', context=context)


def details_profile(request):
    profile = Profile.objects.first()
    all_fruits = len(Fruit.objects.all())
    context = {'profile': profile, 'all_fruits': all_fruits}
    return render(request, template_name='account/details-profile.html', context=context)


def edit_profile(request):
    profile = Profile.objects.first()

    if request.method == 'GET':
        form = EditProfileForm(initial=profile.__dict__)
        context = {'form': form, 'profile': profile}
        return render(request, template_name='account/edit-profile.html', context=context)

    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details_profile')
        else:
            context = {'form': form, 'profile': profile}
            return render(request, template_name='account/edit-profile.html', context=context)


def delete_profile(request):
    profile = Profile.objects.first()
    fruits = Fruit.objects.all()
    if request.method == "POST":
        profile.delete()
        fruits.delete()
        return redirect('home')
    context = {'profile': profile}
    return render(request, template_name='account/delete-profile.html', context=context)
