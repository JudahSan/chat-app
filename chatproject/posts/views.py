from django.shortcuts import render, get_object_or_404
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views here.

@login_required
def post_create(request):
  if request.method == 'POST':
    form = PostCreateForm(data=request.POST, files=request.FILES)
    if form.is_valid():
      new_item = form.save(commit=False)
      new_item.user = request.user
      new_item.save()
  else:
    form = PostCreateForm(data=request.GET)
  return render(request,'posts/create.html', {'form': form})

def feed(request):
  posts = Post.objects.all()
  return render(request, 'posts/feed.html', {'posts':posts})

# like view and check the liked post
def like_post(request):
  liked_post = request.POST.get('post_id')
  post = get_object_or_404(Post, id=post_id)
  # check if post is already liked
  if post.liked_by.filter(id=request.user.id).exists():
    post.liked_by.remove(request.user)
  else: 
    post.liked_by.add(request.user)