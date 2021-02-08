from  django import forms
from multiselectfield import MultiSelectFormField
class EnqueryD(forms.Form):
    first_name = forms.CharField(
        label= "Enter Your First_Name",
        widget = forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'your first_name',
            }
        )
    )
    last_name = forms.CharField(
        label= "Enter Your Last_Name",
        widget = forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'your last_name',
            }
        )
    )
    mobile = forms.IntegerField(
        label="Enter Your Mobile No",
        widget = forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your mobile no'
            }
        )
    )
    email_id = forms.EmailField(
        label= "Enter Your EmailID",
        widget= forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Email',
            }
        )
    )
    courses = forms.CharField(
        label="Enter Your Course",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Course Name',
            }
        )
    )
    fee = forms.IntegerField(
        label="Enter Your Fee",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your fee',
            }
        )
    )
    location = forms.CharField(
        label="Enter your location",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Location'
            }
        )
    )
