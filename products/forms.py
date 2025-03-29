from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from products.models import Article

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(label="نام",max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder': 'نام'}))
    last_name = forms.CharField(label="نام خانوادگی",max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی'}))
    email = forms.EmailField(label="ایمیل",max_length=100,required=True,widget=forms.EmailInput(attrs={'placeholder': 'ایمیل'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "last_name", "email")
        widgets = {'username': forms.TextInput(attrs={'placeholder': 'نام کاربری'})}

    password2 = forms.CharField(label="تکرار رمز عبور",widget=forms.PasswordInput(attrs={'placeholder': 'تکرار رمز عبور'}),required=True)

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("رمزهای عبور باید یکسان باشند.")
        return password2



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'cover', 'promote']
