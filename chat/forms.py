from django import forms
from chat.models import Chat


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        