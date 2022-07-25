from .models import Comment,House,Blog,Agent
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ('blog',)
        widgets = {
            'content': forms.Textarea(
                attrs={'class': "form-control"}
            ),
        }

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = "__all__"

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = "__all__"