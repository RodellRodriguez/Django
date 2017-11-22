from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.views.generic import RedirectView, View
from .models import Post
from .forms import PostForm, UserForm, UserLoginForm

def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog:post_list')


class UserFormView(View):
    form_class = UserForm
    template_name = 'blog/registration_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            # creates an object from the form locally but doesn't save it to DB yet
            user = form.save(commit=False)

            # cleaned (normalized) data for DB
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)

            # save data to DB
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                # user account is not banned or disabled
                if user.is_active:
                    login(request, user)
                    return redirect('blog:post_list')

        return render(request, self.template_name, {'form':form})

# similar set up to UserFormView class
class UserLoginFormView(View):
    form_class = UserLoginForm
    template_name = 'blog/login_form.html'
 
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        print(user.is_active())
        if user is not None:
            print(user.is_active())
            if user.is_active:
                login(request,user)
                return redirect('blog:post_list')
        return render(request, self.template_name, {'form':form})

def logout_view(request):
    logout(request)
    return redirect('blog:post_list')