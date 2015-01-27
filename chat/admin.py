from django.contrib import admin
from .models import Chat

class ChatAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()
        
    def query_set(self, request):
        qs = super(ChatAdmin, self).queryset(request)   
        return qs.filter(usuario=request.user)
    
admin.site.register(Chat, ChatAdmin)