from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# from social.models import Post
from accounts.models import Profile
from social.models import Post


# @login_required(login_url='/login/')
@csrf_exempt
@login_required(login_url='login')
def posts(request):
    # user_object = User.objects.get(username=request.user.username)
    # # user_profile = Post.objects.get(user=user_object)

    posts = Post.objects.all()
    return render(request, 'Html/posts.html', {'posts': posts})


@csrf_exempt
@login_required(login_url='login')
def upload(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image-file')
        write = request.POST['write-post']

        new_post = Post.objects.create(user=user, image=image, write=write)
        new_post.save()
        return redirect('posts')
    else:
        return redirect('posts')


class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts_lists = Post.objects.all().order_by('createdOn')

        context = {
            'post_list': posts_lists,
        }
        return render(request, 'Html/posts.html', context)
