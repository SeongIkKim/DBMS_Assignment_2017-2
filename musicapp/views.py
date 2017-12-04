from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Album, Song
from django.views import generic
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

'''
def index(request):
    all_album = Album.objects.all()
    template = loader.get_template('musicapp/index.html')
    context = {
        'albums' : all_album,
    }
    return render(request, "musicapp/index.html",context)

def detail(request, album_id):
    try:
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")

    context = {
        'album' : album,
    }
    return render(request, 'musicapp/detail.html', context)

'''

class IndexView(generic.ListView):
    template_name = 'musicapp/index.html'
    context_object_name = 'albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'musicapp/detail.html'



def favorite(request,album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        select_song=album.song_set.get(pk = request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'musicapp/detail.html', {
            'album' : album,
            'error_message' : "You did not select a valid song.",
        })
    else:
        if (select_song.is_favorite == False) :
            select_song.is_favorite = True
            select_song.save()
            return render(request, 'musicapp/detail.html', {'album': album})
        else :
            select_song.is_favorite = False
            select_song.save()
            return render(request, 'musicapp/detail.html', {'album': album})
# Create your views here.
