from .models import form_m
from django import forms


class RegisterForm(forms.ModelForm):
   
    skills=forms.MultipleChoiceField(
        choices=form_m.skill,
        widget=forms.CheckboxSelectMultiple,
        label="Technical Skills")
    employed=forms.ChoiceField(
        choices=form_m.yes_no,
        widget=forms.RadioSelect)
    gender=forms.ChoiceField(
        choices=form_m.gender_choices,
        widget=forms.RadioSelect)
    experience=forms.ChoiceField(
        choices=form_m.yes_no,
        widget=forms.RadioSelect)
    dec=forms.BooleanField(
        label="DECLARATION BY THE CANDIDATE",
        required=True,
        widget=forms.CheckboxInput(attrs={'class':'form-check-input'})
    )
    nielitStudent = forms.ChoiceField(
        choices=[('', 'Choose')] + list(form_m.yes_no),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Weather a NIELIT/DOEACC Student?"
    )
    trainingCenter = forms.ChoiceField(
        choices=[('', 'Choose')] + list(form_m.centers),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="If yes, mention name of Training Center"
    )
    highestQualification = forms.ChoiceField(
        choices=[('', 'Choose')] + list(form_m.HIGHEST_QUALIFICATION),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Highest Qualification"
    )
    state = forms.ChoiceField(
        choices=[('', 'Choose')] + list(form_m.states),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="State"
    )
    class Meta:

        model = form_m
        fields = '__all__'
        
            
        widgets={
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Your answer'}),
            'fullName':forms.TextInput(attrs={'class':'form-control','placeholder':'Your answer'}),
            'phoneNumber':forms.TextInput(attrs={'class':'form-control','placeholder':'Your answer'}),
            'fatherName':forms.TextInput(attrs={'class':'form-control','placeholder':'Your answer'}),
            'course':forms.TextInput(attrs={'class':'form-control','placeholder':'Your answer'}),
            'passingYear':forms.TextInput(attrs={'class':'form-control','placeholder':'Your answer'}),
            'experience':forms.TextInput(attrs={'class':'form-control','placeholder':'Your answer'}),
            'highestQualification':forms.Select(attrs={'class':'form-select'}),
            
        }
        labels={
            'email':'Email',
            'fullName':'Full Name of Candidate',
            'gender':'Gender',
            'fatherName':'Father/Gaurdian\' Name',
            'phoneNumber':'Mobile Number',
            'state':'State',
            'nielitStudent':'Weather NIELIT/DOEACC Student ?',
            'trainingCenter':'If yes , mention name of Training Center',
            'course':'Mention name of course and duration',
            'passingYear':'Month/Year of passing course',
            'employed':'Currently Employed/Self Employed',
            'experience':'Any Working Experience (No. of years)',
            'dec':'DECLARATION BY THE CANDIDATE',
            }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove empty choice from skills field
        self.fields['skills'].empty_label = None

    
   