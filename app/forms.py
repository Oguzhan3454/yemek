from django import forms
from app.models import Post

class UserSearchForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserSearchForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control mb-3'}

    class Meta:
        model = Post
        fields = [
            'city' 
            ]