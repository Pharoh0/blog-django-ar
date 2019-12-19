from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import NewComment
# Create your views here.

posts = [
    {
        'title': 'التدوينة الاولي',
        'content': 'تفاصيل التدوينة الاولي كنص تجريبي',
        'post_date': '15-11-2019',
        'author': 'Essam Eldin'
    },
    {
        'title': 'التدوينة الثانية',
        'content': 'تفاصيل التدوينة الثانية كنص تجريبي',
        'post_date': '15-11-2019',
        'author': 'Essam Eldin'

    },
    {
        'title': 'التدوينة الثالثة',
        'content': 'تفاصيل التدوينة الثالثة كنص تجريبي',
        'post_date': '15-11-2019',
        'author': 'Essam Eldin'
    },
    {
        'title': 'التدوينة الرابعة',
        'content': 'تفاصيل التدوينة الرابعة كنص تجريبي',
        'post_date': '15-11-2019',
        'author': 'Essam Eldin'
    }

]


def home(request):
    context = {
        'title': "الرئيسية",
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'من انا'})


def post_detail(request, post_id):
    # show post
    post = get_object_or_404(Post, pk=post_id)
    # Show comment
    comments = post.comments.filter(active=True)
    # check before save date from comment form.
    if request.method == 'POST':
        comment_form = NewComment(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form = NewComment()
    else:
        comment_form = NewComment()
    context = {
        'title': post,
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'blog/detail.html', context)
















