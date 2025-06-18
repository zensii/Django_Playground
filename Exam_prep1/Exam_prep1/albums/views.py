from django.shortcuts import render, redirect

from Exam_prep1.albums.forms import AlbumBaseForm, AlbumForm
from Exam_prep1.albums.models import Album
from Exam_prep1.utils import get_usr_obj


# Create your views here.
def add_album(request):
    profile = get_usr_obj()
    if not profile:
        return redirect('homepage')

    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.owner = profile
            album.save()
            return redirect('homepage')
    else:
        form = AlbumForm()

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'albums/album-add.html', context)

def edit_album(request, pk):
        album = Album.objects.get(pk=pk)
        if request.method == 'POST':
            form = AlbumForm(request.POST, instance=album)
            if form.is_valid():
                form.save()
                return redirect('homepage')
        else:
            form = AlbumForm(instance=album)
        context = {
            'form': form,
            'album': album,
        }
        return render(request, 'albums/album-edit.html', context)

def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    form = AlbumForm(instance=album)

    for name, field in form.fields.items():
        if name == "genre":
            field.widget.attrs["disabled"] = True
        else:
            field.widget.attrs["readonly"] = True

    if request.method == 'POST':
        album.delete()
        return redirect('homepage')

    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'albums/album-delete.html', context)

def album_details(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'album': album,
    }
    return render(request, 'albums/album-details.html', context)