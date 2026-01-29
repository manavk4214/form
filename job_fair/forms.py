from .models import form_m
from django import forms

skill={
    "S&SE":"Software & Systems Expert (O Level/A Level/Programming/Web Development)",
    "AI&ML":"AI & Data Science(AI,ML,Data Science)",
    "DM":"Digital Media (Multimedia Tools,Digital Marketing)",
    "AC":"Accounting",
    "GN":"General Office Automation",
    "O":"Other",
}
class RegisterForm(forms.ModelForm):
    skills=forms.MultipleChoiceField(
        choices=skill.items(),
        widget=forms.CheckboxSelectMultiple,
        label="Technical Skills")
    gender=forms.ChoiceField(
        choices=list(form_m.gender_choices.items()),
        widget=forms.RadioSelect)
    experience=forms.ChoiceField(
        choices=list(form_m.yes_no.items()),
        widget=forms.RadioSelect)
    dec=forms.BooleanField(
        label="I am aware that information provided by me in this form shall be shared by NIELIT with prospective companies, if required.",
        required=False,
        widget=forms.CheckboxInput(attrs={'class':'form-check-input'})
    )
    class Meta:

        model = form_m
        fields = '__all__'
        
            
        widgets={
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your email'}),
            'fullName':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your full name'}),
            
            'fatherName':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your father name'}),
            'phoneNumber':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your phone number'}),
            'highestQualification':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your highest qualification'}),
            'state':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your state'}),
            'nielitStudent':forms.Select(attrs={'class':'form-select'}),
            'trainingCenter':forms.Select(attrs={'class':'form-select'}),
            'passingYear':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your passing year'}),
            'employed':forms.Select(attrs={'class':'form-select'}),
            'experience':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your experience'}),
            
        }
        labels={
            'email':'Email',
            'fullName':'Full Name of Candidate',
            'gender':'Gender',
            'fatherName':'Father/Gaurdian\' Name',
            'phoneNumber':'Mobile Number',
            'highestQualification':'Highest Qualification',
            'state':'State',
            'nielitStudent':'Weather NIELIT/DOEACC Student ?',
            'trainingCenter':'If yes , mention name of Training Center',
            'course':'Mention name of course and duration',
            'passingYear':'Month/Year of passing course',
            
            'employed':'Currently Employed/Self Employed',
            'experience':'Any Working Experience (No. of years)',
            'dec':'DECLARATION BY THE CANDIDATE'
            }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove empty choice from skills field
        self.fields['skills'].empty_label = None