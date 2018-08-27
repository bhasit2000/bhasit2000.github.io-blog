from django.shortcuts import render, redirect, get_object_or_404

from .models import Post

from .forms import PostForm

def index(request):
	posts = Post.objects.order_by('-date')

	context = {'posts': posts}

	return render(request, 'app/index.html', context)

def post(request):

	if request.method == 'POST':
		form = PostForm(request.POST)

		if form.is_valid():
			new_post = Post(name=request.POST['name'], title=request.POST['title'], body=request.POST['body'])
			new_post.save()
			return redirect('index')

	else:	
		form = PostForm()
		context = {'form': form}
		return render(request, 'app/post.html', context)


def contact(request):
	return render(request, 'app/contact.html')

def about(request):
	return render(request, 'app/about.html')

def post_details(request, id): 
	detail = get_object_or_404(Post, id=id)

	context = {
		"detail": detail
	}
	return render(request, "app/details.html", context)


	
