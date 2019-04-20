from django import forms
from django.forms.widgets import RadioSelect
from django.forms import extras
from bootstrap_datepicker_plus import DatePickerInput
from multiselectfield import MultiSelectFormField
from django.contrib.admin.widgets import AdminDateWidget


class RegistrationForm(forms.Form):
    name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'First Name'
            }
        )
    )

    mobile = forms.IntegerField(
        label='Mobile Number',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Mobile'
            }
        )
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Email'
            }
        )
    )
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'UserName'
            }
        )
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Password'
            }
        )
    )
    years = range(2000, 1970, -1)
    dob = forms.DateField(
        widget=forms.SelectDateWidget(years=years))


    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = forms.ChoiceField(
        widget=forms.RadioSelect(
        ), choices=GENDER_CHOICES)

    LOCATION_CHOICES = (
        ('Hyd', 'Hyderabad'),
        ('Bang', 'Bangalore'),
        ('Chen', 'Chennai'),
        ('Mum', 'Mumbai')
    )
    location = MultiSelectFormField(choices=LOCATION_CHOICES)



class LoginForm(forms.Form):
    username = forms.CharField(
        label='Enter Your Username',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'UserName'
            }
        )
    )
    password = forms.CharField(
        label='Enter Your pasword',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Password'
            }
        )
    )



from django import  forms

class FeedbackForm(forms.Form):
    name = forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    rating = forms.IntegerField(
        label="Enter Your Rating",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Feedback Rating'
            }
        )
    )

    feedback = forms.CharField(
        label="Enter yout Feedback",
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder':'Enter your feedback here...'

            }
        )
    )


class StudentForm(forms.Form):
    name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }
        )
    )

    mobile = forms.IntegerField(
        label='Mobile Number',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Mobile'
            }
        )
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }
        )
    )
    Shift_Choices = (
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'),
        ('Evening', 'Evening')
    )
    shift = MultiSelectFormField(max_length=100, choices=Shift_Choices)

    Course_Choices = (
        ('Python', 'Python'),
        ('Django', 'Django'),
        ('MySQL', 'MySQL'),
        ('Oracle', 'Oracle'),
        ('MSBI', 'MSBI'),
        ('REST API', 'REST API')
    )
    course = MultiSelectFormField(max_length=400, choices=Course_Choices)

    Faculty_Choices = (
        ('Nani', 'Nani'),
        ('Sai', 'Sai'),
        ('Raju', 'Raju'),
        ('Satya', 'Satya'),
        ('Rajesh', 'Rajesh')
    )
    faculty = MultiSelectFormField(max_length=500, choices=Faculty_Choices)

    Branch_Choices = (
        ('Branch-1', 'Branch-1'),
        ('Branch-2', 'Branch-2'),
        ('Branch-3', 'Branch-3'),
    )
    brance = MultiSelectFormField(max_length=500, choices=Branch_Choices)