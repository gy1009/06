from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.defaultfilters import title
from django.core.paginator import Paginator
from .models import Shop, Review
from django.shortcuts import get_object_or_404
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def shophome(request):
    searchTerm = request.GET.get('searchShop')
    if searchTerm:
        shop_list = Shop.objects.filter(title__contains=searchTerm)
    else:
        shop_list = Shop.objects.all()
    paginator = Paginator(shop_list, 2)
    page_number = request.GET.get('page', 1)
    shops = paginator.page(page_number)
    return render(request, 'shophome.html', {'searchTerm':searchTerm, 'shops':shops})

def home(request):
    return render(request,'home.html',{'name':"LC"})
    # return HttpResponse("项目首页")

def signup(request):
    email=request.GET.get('email')
    return render(request,'signup.html',{'email':email})

def shopdetail(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    reviews = Review.objects.filter(shop=shop)
    return render(request, 'shopdetail.html', {'shop': shop,'reviews':reviews})

@login_required
def createshopreview(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    if request.method == 'GET' :
        return render(request, 'createshopreview.html' ,
        {'form':ReviewForm , 'shop':shop})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.shop = shop
            newReview.save()
            return redirect('shopdetail',newReview.shop.id)
        except ValueError:
            return render(request,'createshopreview.html', {'form':ReviewForm, 'error':'非法数据'})

@login_required
def updateshopreview(request, review_id) :
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'updateshopreview.html', {'review':review, 'form':form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('shopdetail', review.shop.id)
        except ValueError:
            return render(request, 'updateshopreview.html', {'review':review, 'form':form, 'error':'提交非法数据'})

@login_required
def deleteshopreview(request, review_id) :
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('shopdetail', review.shop.id)
