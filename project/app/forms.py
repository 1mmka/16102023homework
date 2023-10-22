from django.forms import forms,CharField,Textarea
from captcha.fields import CaptchaField

class CreateProduct(forms.Form):
    name = CharField(max_length=64)
    body = CharField(max_length=256)
    captcha = CaptchaField(label='Введите текст с картинки', error_messages={'invalid':'Неправильный текст'})