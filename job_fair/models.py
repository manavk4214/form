from django.db import models



class form_m(models.Model):
    declare=[
    ("Declared","I am aware that information provided bt me in this form shall be shared by NIELIT with prospective companies,if required."),
]
    gender_choices = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    HIGHEST_QUALIFICATION = [
        ("10+2 / ITI / Pursuing Graduation", "10+2 / ITI / Pursuing Graduation"),
        ("Graduation (B.Sc / B.Com / BA / BBA)", "Graduation (B.Sc / B.Com / BA / BBA)"),
        ("Technical (CS / IT / BCA / B.Tech)", "Technical (CS / IT / BCA / B.Tech)"),
        ("Post Graduate", "Post Graduate"),
        ("MCA / M.Tech", "MCA / M.Tech"),
        ("Other", "Other"),
    ]

    yes_no = [
        ("Yes", "Yes"),
        ("No", "No"),
    ]

    centers = [
        ("Inderlok", "Inderlok"),
        ("Janakpuri", "Janakpuri"),
        ("Karkardooma", "Karkardooma"),
    ]

    skill = [
        ("Software & Systems Expert (O Level/A Level/Programming/Web Development)",
        "Software & Systems Expert (O Level/A Level/Programming/Web Development)"),
        ("AI & Data Science (AI, ML, Data Science)",
        "AI & Data Science (AI, ML, Data Science)"),
        ("Accounting", "Accounting"),
        ("Digital Media (Multimedia Tools, Digital Marketing)",
        "Digital Media (Multimedia Tools, Digital Marketing)"),
        ("General Office Automation", "General Office Automation"),
        ("Other", "Other"),
    ]

    states = [
        ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"),
        ("Andhra Pradesh", "Andhra Pradesh"),
        ("Arunachal Pradesh", "Arunachal Pradesh"),
        ("Assam", "Assam"),
        ("Bihar", "Bihar"),
        ("Chandigarh", "Chandigarh"),
        ("Chhattisgarh", "Chhattisgarh"),
        ("Delhi", "Delhi"),
        ("Dadra and Nagar Haveli and Daman and Diu", "Dadra and Nagar Haveli and Daman and Diu"),
        ("Goa", "Goa"),
        ("Gujarat", "Gujarat"),
        ("Haryana", "Haryana"),
        ("Himachal Pradesh", "Himachal Pradesh"),
        ("Jammu and Kashmir", "Jammu and Kashmir"),
        ("Jharkhand", "Jharkhand"),
        ("Karnataka", "Karnataka"),
        ("Kerala", "Kerala"),
        ("Ladakh", "Ladakh"),
        ("Lakshadweep", "Lakshadweep"),
        ("Madhya Pradesh", "Madhya Pradesh"),
        ("Maharashtra", "Maharashtra"),
        ("Manipur", "Manipur"),
        ("Meghalaya", "Meghalaya"),
        ("Mizoram", "Mizoram"),
        ("Nagaland", "Nagaland"),
        ("Odisha", "Odisha"),
        ("Punjab", "Punjab"),
        ("Puducherry", "Puducherry"),
        ("Rajasthan", "Rajasthan"),
        ("Sikkim", "Sikkim"),
        ("Tamil Nadu", "Tamil Nadu"),
        ("Telangana", "Telangana"),
        ("Tripura", "Tripura"),
        ("Uttar Pradesh", "Uttar Pradesh"),
        ("Uttarakhand", "Uttarakhand"),
        ("West Bengal", "West Bengal")
    ]

    email= models.EmailField(max_length=100,blank=True, null=True)
    fullName= models.CharField(max_length=100,blank=True, null=True)
    gender=models.CharField(max_length=100,choices=gender_choices,blank=False)
    fatherName=models.CharField(max_length=100,blank=True, null=True)
    phoneNumber=models.CharField(max_length=10,blank=True, null=True)
    highestQualification=models.CharField(max_length=100,blank=False,choices=HIGHEST_QUALIFICATION)
    state= models.CharField(max_length=100,choices=states, null=True)
    nielitStudent= models.CharField(max_length=100,choices=yes_no,blank=True, null=True)
    trainingCenter=models.CharField(max_length=100,choices=centers,blank=True, null=True)
    course=models.CharField(max_length=100,blank=True, null=True)
    passingYear=models.CharField(max_length=100,blank=True, null=True)
    skills=models.JSONField(default=list,blank=True)
    employed= models.CharField(max_length=100,choices=yes_no,blank=True, null=True)
    experience=models.CharField(max_length=10,blank=True, null=True)
    dec=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email} -- {self.fullName}"
    
    def get_skill_display_list(self):
        skill_dict = dict(self.skill)
        return [skill_dict.get(s, s) for s in self.skills]


