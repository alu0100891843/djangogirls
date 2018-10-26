from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #Hacemos el QuerySet
    return render(request, 'blog/post_list.html', {'posts': posts}) #La vista retorna este html, además del QuerySet
    #request es todo lo que recibimos del usuario desde internet
    #posts lo que hará será mostrar los datos según las restricciones que tenga el queryset
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})