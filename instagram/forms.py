from django import forms

from . models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["photo", "caption", "location"]
        widgets = {
            "caption": forms.Textarea
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["message"]



"""
myapp/models.py

class GameUser(model.Model):
    server = models.CharField(max_lenght=10)
    username = models.charfIedl(())
    
    
class GameUserSingupForm(form.Modelform):
    class MetaL
        model = GameUser
        fields = ['server', 'username']
        
    def clean_username(self)
        username = self.cleaned_data.get('username','').strip()
        return username
        
    def clean(self)
        cleaned_data = super().clean()
        if self.check_exist(cleaned_data['server'], cleaned_data['username']):
            raise forms.ValidationError("서버에 이미등록된 이름입니다")
        
        retrun cleaned_data
        
    def check_exist(self, server, username)
        return GameUser.object.filter(server=server, username=username) exists()








"""
