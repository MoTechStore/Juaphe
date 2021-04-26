from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth import get_user_model
from django.db import transaction
from django.forms.utils import ValidationError
from django.contrib.auth.models import User
from classroom.models import User
#User = get_user_model()


from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Customer, Truck, User

from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin




class CustomUserCreationForm(PopRequestMixin, CreateUpdateAjaxMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']



from django.contrib.auth.forms import UserCreationForm
from classroom.models import User
from django.apps import apps
from django.contrib.auth import get_user_model
from django.core.signals import setting_changed
from django.dispatch import receiver

@receiver(setting_changed)
def user_model_swapped(**kwargs):
    if kwargs['setting'] == 'AUTH_USER_MODEL':
        apps.clear_cache()
        from classroom import some_module
        some_module.UserModel = get_user_model()



# -*- coding: utf-8 -*-
from django import forms

from .models import Customer

class BookModelForm(BSModalModelForm):
    reg_date = forms.DateField(
        error_messages={'invalid': 'Enter a valid date in YYYY-MM-DD format.'}
    )

    class Meta:
        model = Customer
        exclude = ['timestamp']

class CustomerForm(BSModalModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['customer_name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['vehicle_number'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['first_name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['last_name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['id_type'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['id_number'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['car_model'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['car_color'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['chases_number'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['cost_per_day'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['contact_number'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['description'].widget.attrs = {
            'class': 'form-control col-md-6'
        } 
        self.fields['is_payed'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
    class Meta:
        model = Customer
        fields = ('customer_name', 'vehicle_number', 'first_name', 'last_name', 'id_type', 'id_number', 'car_model', 'car_color', 'chases_number', 'cost_per_day', 'contact_number', 'description', 'is_payed')




class TruckForm(BSModalModelForm):
    def __init__(self, *args, **kwargs):
        super(TruckForm, self).__init__(*args, **kwargs)
        self.fields['truck_plate_number'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['first_name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['last_name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['id_type'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['id_number'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['type_of_truck'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['truck_company'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['card_number'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['cost_per_day'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['contact_number'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['remark'].widget.attrs = {
            'class': 'form-control col-md-6'
        } 
        self.fields['is_payed'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
    class Meta:
        model = Truck
        fields = ('truck_plate_number', 'first_name', 'last_name', 'id_type', 'id_number', 'type_of_truck', 'truck_company', 'card_number', 'cost_per_day', 'contact_number', 'remark', 'is_payed')




class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = True
        if commit:
            user.save()
        return use




class UserForm(BSModalModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['first_name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['last_name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['email'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['password'].widget.attrs = {
            'class': 'form-control col-md-6'
        }


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
