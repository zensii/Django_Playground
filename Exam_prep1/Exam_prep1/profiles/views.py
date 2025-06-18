from django.shortcuts import render, redirect

from Exam_prep1.profiles.forms import ProfileForm
from Exam_prep1.utils import get_usr_obj


# Create your views here.
def profile_details(request):
    profile = get_usr_obj()
    if not profile:
        return redirect('homepage')
    album_count = profile.albums.count()

    context = {
        'profile': profile,
        'album_count': album_count
    }
    return render(request, 'profiles/profile-details.html', context)

def profile_delete(request):
    profile = get_usr_obj()

    if not profile:
        return redirect('homepage')
    if request.method == 'POST':
        profile.delete()
        return redirect('homepage')

    return render(request, 'profiles/profile-delete.html')

def home_page(request):
    profile = get_usr_obj()

    if request.method == 'POST' and not profile:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ProfileForm()

    context = {
        'form': form,
        'profile': profile,
    }

    if profile:
        albums = profile.albums.all()
        context['albums'] = albums
        return render(request, 'profiles/home-with-profile.html', context)

    return render(request, 'profiles/home-no-profile.html', context)
