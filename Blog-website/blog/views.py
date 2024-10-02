from .form import ProjectForm
from django.shortcuts import render,redirect
from .models import Post,Category,Tag,Comment,Rating
from .utils import check_read_articles,check_select_ratings
# Create your views here.
def hompageview(request):
    categories = Category.objects.all()
    posts = Post.objects.all().order_by('-publish_date')
    last_comments = Comment.objects.all().order_by('-id')[:10]

    data = {
        "categories":categories,
        "posts":posts,
        "last_comments":last_comments
    }
    
    return render(request,'index.html',data)
def detailview(request,pk):
    posts = Post.objects.get(id=pk)
    categories = Category.objects.all()
    post_cat = posts.category.id
    category  = Category.objects.get(id=post_cat)
    related_posts = Post.objects.filter(category=category).exclude(id__in=[0,posts.id]).order_by('?')


    request.session.modified = True
    if posts.id in check_read_articles(request):
        pass
    else:
        check_read_articles(request).append(posts.id)
        posts.views += 1
        posts.save()


    if request.method == "POST":
        name = request.POST.get('comment_author')
        comment = request.POST.get('comment')
        image = request.POST.get('image')
        if image:   
            pass
        else:
            image='https://media.istockphoto.com/id/1337144146/vector/default-avatar-profile-icon-vector.jpg?s=612x612&w=0&k=20&c=BIbFwuv7FxTWvh5S3vB6bkT0Qv8Vn8N5Ffseq84ClGI='
        if all([name,comment]):
            Comment.objects.create(
                author=name,
                image = image,
                comment=comment,
                post=posts
            )


    
    data = {
        "categories":categories,
        "post":posts,
        "related_posts":related_posts
    }

    return render(request,'detail.html',data)


def set_rating(request,value,pk):
    post = Post.objects.get(id=pk)
    value = int(value)
    # print(post,value)
    request.session.modified = True
    if all([post,value]):
        if post.pk in check_select_ratings(request):
            pass
        else:
            check_select_ratings(request).append(post.pk)
            Rating.objects.create(
                post=post,
                value = value)
    return redirect('/',)



def category_list(request,category_slug):
    slug = Category.objects.get(slug=category_slug)
    posts = Post.objects.filter(category=slug)
    return render(request,'index.html',context={"posts":posts})

# Search Option

def search(request):
    query = request.GET.get('query')
    posts = Post.objects.filter(title__icontains=query)
    data = {
        "posts":posts
    }
    return render(request,'index.html',data)

# Post add and edit and delete

def add_post(request):
    
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = ProjectForm()
    
    context = {
        "form":form
    }
    return render(request,'post_add.html',context)    


# Edit post details


def edit_post(request,pk):
    post = Post.objects.get(id=pk)
    form = ProjectForm(instance=post)

    if request.method == "POST":
        form = ProjectForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {
        "form":form
    }
    return render(request,'post_add.html',context)    


def delete_post(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.delete()
        return redirect('/')

    return render(request,'post_delete.html',context={'post':post})