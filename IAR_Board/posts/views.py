from django.shortcuts import render, redirect
from .forms import AddPostForm
from django.contrib import messages

def addPost(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'The post has been created!')
            return redirect('home_page')
    else:
        form = AddPostForm()
        return render(request, "posts/add_posts.html", {'form': form})