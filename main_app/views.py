# I used this resource from stackoverflow in add_image: https://stackoverflow.com/questions/68725696/django-upload-image-from-form 

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Keychain, Tag
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from .forms import KeychainImageForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def welcome(request):
    return render(request, "welcome_page.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('welcome')
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

class KeychainListView(LoginRequiredMixin, ListView):
    model = Keychain
    template_name = "keychain_collection.html"
    context_object_name = "keychains"
    
    # retrieves the keychains belong to the logged in user
    def get_queryset(self):
        return Keychain.objects.filter(user= self.request.user)
    
    
@login_required
def add_tag_to_keychain(request, keychain_id, tag_id):
    Keychain.objects.get(id=keychain_id).tags.add(tag_id)
    return redirect('keychain_detail', keychain_id=keychain_id)

@login_required
def remove_tag_from_keychain(request, keychain_id, tag_id):
    Keychain.objects.get(id=keychain_id).tags.remove(tag_id)
    return redirect('keychain_detail', keychain_id=keychain_id)

@login_required
def keychain_detail_view(request,keychain_id):
    keychain = Keychain.objects.get(id=keychain_id)
    keychain_form=KeychainImageForm()
    
    tags_keychain_does_not_have = Tag.objects.exclude(id__in=keychain.tags.all().values_list("id"))
    return render(request,"keychain_detail.html",{"keychain":keychain,"keychain_form":keychain_form, "tags_keychain_does_not_have":tags_keychain_does_not_have})
    
    
@login_required
def add_image(request,keychain_id):
    form= KeychainImageForm(request.POST, request.FILES)
    if form.is_valid(): 
        new_feeding=form.save(commit=False) 
        new_feeding.keychain_id=keychain_id
        new_feeding.save()
    return redirect("keychain_detail",keychain_id=keychain_id)
    
    
class CreateKeychainView(LoginRequiredMixin,CreateView):
    model=Keychain 
    fields=["name","acquired_in","year_acquired","material","theme","story","is_gift"] 
    template_name="keychain_create_update.html"
    success_url=reverse_lazy("keychain_list")
    
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    

class UpdateKeychainView(LoginRequiredMixin,UpdateView):
    model=Keychain 
    fields=["name","acquired_in","year_acquired","material","theme","story","is_gift"] 
    template_name="keychain_create_update.html" 
    success_url=reverse_lazy("keychain_list")
    
class DeleteKeychainView(LoginRequiredMixin,DeleteView):
    model=Keychain 
    template_name="confirm_keychain_removal.html"
    success_url=reverse_lazy("keychain_list")

    