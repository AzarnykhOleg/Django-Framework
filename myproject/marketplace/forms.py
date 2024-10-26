from django import forms
from .models import Product


class UploadImmage(forms.ModelForm):
    # title = forms.CharField(max_length=20)
    # description = forms.TextField()
    # price = forms.DecimalField(max_digits=8, decimal_places=2)
    # quantity = forms.IntegerField()
    # image = forms.ImageField(upload_to='images/', default='1')
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'quantity', 'image']
