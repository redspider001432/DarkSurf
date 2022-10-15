from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from accounts.models import Profile
from social.models import Post, LikePost


# @login_required(login_url='/login/')
@login_required(login_url='login')
def posts(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    posts = Post.objects.all()
    return render(request, 'Html/posts.html',{'user_profile':user_profile ,'posts': posts})

@login_required(login_url='login')
def like_post(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)
    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter is None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes = post.no_of_likes + 1
        post.save()
        return redirect('posts')
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes - 1
        post.save()
        return redirect('posts')
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


# class PostListView(View):
#     def get(self, request, *args, **kwargs):
#         posts_lists = Post.objects.all().order_by('createdOn')
#
#         context = {
#             'post_list': posts_lists,
#         }
#         return render(request, 'Html/posts.html', context)
