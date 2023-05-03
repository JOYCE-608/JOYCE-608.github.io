from django.shortcuts import render
from django.shortcuts import redirect

from .forms import CommentForm

from .models import Comment

# Create your views here.

def home(request):
    
    return render(request, 'index.html')

def comment(request):

    all_comments = Comment.objects.all()

    comment = CommentForm()

    if request.method == "POST":
       user_comment =  CommentForm(request.POST)
       user_comment.save()
       return redirect('comment')
    
    print(all_comments)
    context = {
        'comment': comment,
        'all_comments': all_comments
    }
    



    return render(request, 'index1.html', {'context': context})