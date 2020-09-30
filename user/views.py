from django.shortcuts import render,redirect
from . forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages



def register(request):
  
  if request.method == "POST":
      form = RegisterForm(request.POST)
      if form.is_valid():
          username = form.cleaned_data.get("username")
          password = form.cleaned_data.get("password")

          newUser12 = User(username = username)
          newUser12.set_password(password)

          newUser12.save()
          login(request,newUser12)
          messages.success(request,"Başarıyla kayıt oldunuz")
          return redirect("index")
      context = {
          "form" : form
      }
      return render(request,"register.html",context)

  else:
      form = RegisterForm()
      context = {
          "form" : form
      }
      return render(request,"register.html",context)
  
  
  """ form = RegisterForm()
    context = {
        "form" : form
    }


   return render(request,"register.html",context)"""

def loginUser(request):

    form = LoginForm(request.POST or None)
    
    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user =  authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"login.html",context)
        
        messages.success(request,"Başarıyla Giriş Yaptınız")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yaptınız")
    return redirect("index")

