from django.shortcuts import render,redirect
from .forms import SignupForm,UpdateProfileForm
from django.views import View
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import CustomUser,Saved
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from products.models import Product
# Create your views here.


class SignupView(UserPassesTestMixin,View):
    def get(self,request):
        return render(request, 'registration/signup.html',{'form':SignupForm()})
    


    def post(self,request):
        form=SignupForm(data=request.POST)    # inputlarga kiritilgan malumotlarni olish 
        if form.is_valid():   # formamiz yaroqli bo'lsa biz buni saqlaymiz
            form.save()
            messages.success(request, "Your account is succesfully created.")
            return redirect('login')
        return render(request, 'registration/signup.html', {'form':form})   # agar ro'yhatdan o'tish valid bo'lsa xatolikni ko'rsatib beradi
    

    def test_func(self):
        user=self.request.user
        if user.is_authenticated:
            return False
        return True

    

class ProfileView(View):
    def get(self,request,username):    # Hamma odam yaratgan mahsulotimizni ko'rishi uchun ishlatamiz
        user=get_object_or_404(CustomUser,username=username)
        return render(request, 'profile.html', {'customuser':user})




class UpdateProfileView(LoginRequiredMixin,View):
    login_url='login'
    def get(self,request):
        form=UpdateProfileForm(instance=request.user)
        return render(request, 'profile_update.html', {'form':form})
    

    
    def post(self,request):
        form = UpdateProfileForm(instance=request.user, data=request.POST, files=request.FILES)    # inputlarga kiritilgan malumotlarni olish 
        if form.is_valid():   # formamiz yaroqli bo'lsa biz buni saqlaymiz
            form.save()
            messages.success(request, "Your account is succesfully updated.")
            return redirect('users:profile',request.user)
        return render(request, 'registration/signup.html', {'form':form})   # agar ro'yhatdan o'tish valid bo'lsa xatolikni ko'rsatib beradi
    


class AddRemoveSavedView(LoginRequiredMixin,View):
    login_url='login'
    def get(self,requset,product_id):
        product=get_object_or_404(Product, id=product_id)
        saved_product=Saved.objects.filter(author=requset.user, product=product)
        if saved_product:
            saved_product.delete()
            messages.info(requset, 'Rremoved.')

        else:
            Saved.objects.create(author=requset.user, product=product)
            messages.info(requset,'Saved.')
        return redirect(requset.META.get("HTTP_REFERER"))




class SavedView(LoginRequiredMixin,View):
    login_url='login'
    def get(self,request):
        saveds=Saved.objects.filter(author=request.user)
        q=request.GET.get('q','')
        if q:   
            products=Product.objects.filter(title__icontains=q)
            saveds=Saved.objects.filter(product_in=products, author=request.user)
        return render(request, 'saveds.html',{"saveds":saveds})
    



class RecentlyViewedView(View):
    def get(self,request):
        products=[]
        if not "recently_viewed" in request.session:
            pass
        else:
            r_viewed=request.session["recently_viewed"]
            for i in Product.objects.all():
                if i.id in r_viewed:
                    products.append(i)
            q=request.GET.get('q','')
            if q:
              products=Product.objects.filter(title__icontains=q)
        return render(request, "recently_viewed.html",{"products":products})