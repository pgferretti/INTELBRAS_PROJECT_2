from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from chat.models import Chat
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def home(request):
    if request.method == "POST":        
        username = request.POST['loginname']
        password = request.POST['password']
        print username
        print password
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'index.html')                            
            else:
                return render(request, 'form.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    
def form(request):
    if request.method == "POST":          
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        user.last_name = username
        user.save()
        return render(request, 'index.html')
    else:           
        return render(request, 'form.html')
    
        
class ChatForm(CreateView):
    template_name = 'form.html'
    model = Chat
    success_url = reverse_lazy('chat')

    
    
