from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from recipes.models import Recipes, Ingredients



class MySignupForm(UserCreationForm):
    # dodajemy do formularza pole e-mail
    email = forms.EmailField(required=True)

    # wyświetalnie pola e-mail w formularzu
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(MySignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']

        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RecipyForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ['title', 'description', 'ingredients', 'category', 'content', 'photo', 'source']
        # ingredients = forms.ModelMultipleChoiceField(
        #     queryset=Ingredients.objects.all(),
        #     widget=forms.CheckboxSelectMultiple
        # )

class IngredientsForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = ['name']




