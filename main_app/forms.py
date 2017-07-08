from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.admin.widgets import AdminDateWidget

class RegForm(UserCreationForm):
    username = forms.CharField(label='Логин *', help_text='только буквы, цифры и символы @.+-_')
    password1 = forms.CharField(label='Пароль *', help_text='не короче 8 символов', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Опять пароль *', help_text='не короче 8 символов', widget=forms.PasswordInput)
    email = forms.EmailField(label='E-mail *')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class UserChangeForm(forms.ModelForm):

    """
    Форма для обновления данных пользователей в админке. Нужна только для того, чтобы не
    видеть постоянных ошибок "Не заполнено поле password" при обновлении данных
    пользователя.
    """

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class UserForm(UserCreationForm):
    username = forms.CharField(label='Логин', help_text='только буквы, цифры и символы @.+-_',)
    password1 = forms.CharField(label='Пароль', help_text='не короче 8 символов', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Опять пароль', help_text='не короче 8 символов', widget=forms.PasswordInput)
    email = forms.EmailField(label='E-mail')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)

class ProfileForm(forms.ModelForm):
    middle_name = forms.CharField(label="Отчество")
    sex = forms.ChoiceField(label='Пол', widget=forms.RadioSelect, choices=(('1', 'М'), ('2', 'Ж')))
    birthday = forms.DateField(label='Дата рождения', widget=forms.SelectDateWidget)
    userpic = forms.ImageField(label='Аватарка', widget=forms.FileInput)
    class Meta:
        model = Profile
        exclude = ('userpic', 'user', 'userpic')