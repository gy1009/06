from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Book,Review
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
def bookdetail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = Review.objects.filter(book=book)
    return render(request, 'bookdetail.html', {'book': book,'reviews':reviews})

def bookhome(request):
    searchTerm = request.GET.get('searchBook')
    if searchTerm:
        book_list = Book.objects.filter(title__contains=searchTerm)
    else:
        book_list = Book.objects.all()
    paginator = Paginator(book_list, 2)
    page_number = request.GET.get('page', 1)
    books = paginator.page(page_number)
    return render(request, 'bookhome.html',
                  {'searchTerm': searchTerm, 'books': books})
@login_required
def createbookreview(request, book_id):
    book= get_object_or_404(Book, pk=book_id)
    if request.method == 'GET' :
        return render(request, 'createbookreview.html' ,
        {'form':ReviewForm , 'book':book})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.book = book
            newReview.save()
            return redirect('bookdetail',newReview.book.id)
        except ValueError:
            return render(request,'createbookreview.html',
                          {'form':ReviewForm, 'error':'非法数据'})
@login_required
def updatebookreview(request, review_id) :
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'updatebookreview.html', {'review':review, 'form':form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('bookdetail', review.book.id)
        except ValueError:
            return render(request, 'updatebookreview.html', {'review':review, 'form':form, 'error':'提交非法数据'})
@login_required
def deletebookreview(request, review_id) :
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('bookdetail', review.book.id)


def home(request):
    return render(request,'home.html',{'name':"LC"})


def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})