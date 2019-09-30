from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

from .models import Post

from django.views import View

from .forms import PostForm, ExtendedUserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class HomeView(View):

	template_name = 'socialupdate/home.html'	

	def get(self, request):

		if 'is_logout' in request.GET:
			logout(request)
			return redirect('socialupdate-login')
		
		posts = Post.objects.order_by('-posted_at')
		form = PostForm()
		context = {'posts': posts, 'form': form}

		return render(request, self.template_name, context)
	
	def post(self, request):

		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			postCreated = form.save(commit=False)
			postCreated.posted_by = request.user
			postCreated.save()

		posts = Post.objects.order_by('-posted_at')
		form = PostForm()
		context = {'posts': posts, 'form': form}

		return render(request, self.template_name, context)

'''
@login_required
def HomeView(request):

	#is_logout = True

	# login required manual implementation
	#if not request.user.is_authenticated:
	#	 return redirect('socialupdate-login')

	if 'is_logout' in request.GET:
		logout(request)
		return redirect('socialupdate-login')

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			#print("VALID")
			postCreated = form.save(commit=False)
			postCreated.posted_by = request.user
			#print(postCreated)
			#print(form)
			postCreated.save()

	form = PostForm()
	posts = Post.objects.order_by('-posted_at')
	content = {'posts': posts, 'form': form}
	return render(request, 'socialupdate/home.html', content)
'''

#Function based Custom LoginView
'''
@csrf_protect
def LoginView(request):

	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				if 'next' in request.GET:
					return redirect(request.GET['next'])
				else:
					return redirect('socialupdate-home')
	form = AuthenticationForm()
	content = {'form': form}
	return render(request, 'socialupdate/loginPage.html', content)
'''

@login_required
def CreatePostView(request):

	if request.method == 'POST':
		form = request.POST

	return render(request, 'socialupdate/createPost.html')

#Vannilla class based User Creation View :
class UserCreationView(View):

	template_name = 'socialupdate/userCreationPage.html'

	def get(self, request):

		form = ExtendedUserCreationForm()
		return render(request, self.template_name, {'form': form})

	def post(self, request):

		form = ExtendedUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Account has been created successfully!, Please login')
			return redirect('socialupdate-login')

#Function Based User Creation View:
'''
def UserCreationView(request):

	if request.method == 'POST':
		form = ExtendedUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Account has been created successfully!, Please login')
			return redirect('socialupdate-login')
	else:
		form = ExtendedUserCreationForm()

	content = {
		'form': form,
	}

	return render(request, 'socialupdate/userCreationPage.html', content)
'''

@login_required
def ProfileView(request):

	return render(request, 'socialupdate/profile.html')