from .models import form_m
from django import forms
HIGHEST_QUALIFICATION = [
        ("10+2", "10+2 / ITI / Pursuing Graduation"),
        ("UG", "Graduation (B.Sc / B.Com / BA / BBA)"),
        ("TECH", "Technical (CS / IT / BCA / B.Tech)"),
        ("PG", "Post Graduate"),
        ("MTECH", "MCA / M.Tech"),
        ("O", "Other"),
    ]

skill=[
    ("S&SE","Software & Systems Expert (O Level/A Level/Programming/Web Development)"),
    ("AI&ML","AI & Data Science(AI,ML,Data Science)"),
    ("DM","Digital Media (Multimedia Tools,Digital Marketing)"),
    ("AC","Accounting"),
    ("GN","General Office Automation"),
    ("O","Other"),
]
centers = {
        ("I","Inderlok"),
        ("J", "Janakpuri"),
        ("K", "Karkardooma"),
    }
states=[
        ("AN","Andaman and Nicobar Islands"),
        ("AP","Andhra Pradesh"),
        ("AR","Arunachal Pradesh"),
        ("AS","Assam"),
        ("BR","Bihar"),
        ("CH","Chandigarh"),
        ("CT","Chhattisgarh"),
        ("DL","Delhi"),
        ("DN","Dadra and Nagar Haveli and Daman and Diu"),
        ("GA","Goa"),
        ("GJ","Gujarat"),
        ("HR","Haryana"),
        ("HP","Himachal Pradesh"),
        ("JK","Jammu and Kashmir"),
        ("JH","Jharkhand"),
        ("KA","Karnataka"),
        ("KL","Kerala"),
        ("LA","Ladakh"),
        ("LD","Lakshadweep"),
        ("MP","Madhya Pradesh"),
        ("MH","Maharashtra"),
        ("MN","Manipur"),
        ("ML","Meghalaya"),
        ("MZ","Mizoram"),
        ("NL","Nagaland"),
        ("OR","Odisha"),
        ("PB","Punjab"),
        ("PY","Puducherry"),
        ("RJ","Rajasthan"),
        ("SK","Sikkim"),
        ("TN","Tamil Nadu"),
        ("TG","Telangana"),
        ("TR","Tripura"),
        ("UP","Uttar Pradesh"),
        ("UT","Uttarakhand"),
        ("WB","West Bengal"),
    ]

class RegisterForm(forms.ModelForm):
    skills=forms.MultipleChoiceField(
        choices=skill,
        widget=forms.CheckboxSelectMultiple,
        label="Technical Skills")
    employed=forms.ChoiceField(
        choices=(form_m.yes_no),
        widget=forms.RadioSelect)
    gender=forms.ChoiceField(
        choices=(form_m.gender_choices),
        widget=forms.RadioSelect)
    experience=forms.ChoiceField(
        choices=(form_m.yes_no),
        widget=forms.RadioSelect)
    dec=forms.BooleanField(
        label="DECLARATION BY THE CANDIDATE",
        required=False,
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
    state = forms.ChoiceField(
        choices=[('', 'Choose')] + list(states),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="State"
    )

    class Meta:

        model = form_m
        fields = '__all__'
        
            
        widgets={
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Your answer'}),
            'fullName':forms.TextInput(attrs={'class':'form-control','placeholder':'Your answer'}),
            'fatherName':forms.TextInput(attrs={'class':'form-control','placeholder':'Your answer'}),
            'phoneNumber':forms.TextInput(attrs={'class':'form-control','placeholder':'Your answer'}),
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
            'highestQualification':'Highest Qualification',
            }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove empty choice from skills field
        self.fields['skills'].empty_label = None

    
   