from django.shortcuts import render

from FruitipediaApp.account.models import Profile


# Create your views here.
def home(request):
    profile = Profile.objects.first()
    context = {'profile': profile}
    return render(request, template_name='common/index.html', context=context)
