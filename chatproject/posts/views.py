from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostCreateForm, CommentForm
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
  return render(request,'posts/create.html', {'form': form},)

def feed(request):
  # Comment form
  if request.method == 'POST':
    comment_form = CommentForm(data=request.POST)
    # get new comment object and save it, but don't commit
    new_comment = comment_form.save(commit=False)
    # get post id and associate it with a comment
    post_id = request.POST.get('post_id')
    post = get_object_or_404(Post, id=post_id)
    # Attach post to the new comment
    new_comment.post = post
    new_comment.save()
  else:
    comment_form = CommentForm()

    # Save Comment to db

  posts = Post.objects.all()
  # Get access to user for like functionality
  logged_user = request.user
  return render(request, 'posts/feed.html', {'posts':posts,'logged_user':logged_user, 'comment_form':comment_form},)

# like view and check the liked post
def like_post(request):
  liked_post = request.POST.get('post_id')
  post = get_object_or_404(Post, id=liked_post)
  # check if post is already liked
  if post.liked_by.filter(id=request.user.id).exists():
    post.liked_by.remove(request.user)
  else: 
    post.liked_by.add(request.user)
  return redirect('feed')

