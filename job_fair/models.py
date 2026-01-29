from django.db import models



class form_m(models.Model):
    declare={
    "Declared":"I am aware that information provided bt me in this form shall be shared by NIELIT with prospective companies,if required."
}
    gender_choices={
        "M":"Male",
        "F":"Female",
        "O":"other",
    }
    highestQualification={
        "10+2/ITI/Pursuing Graduation":"10+2/ITI/Pursuing Graduation",
        "Graduation (B.SC/B.COM/BA/BBA)":"Graduation (B.SC/B.COM/BA/BBA)",
        "Technical(CS/IT/Electronics/Electrical/Mechinical/B.tech/BCA)":"Technical(CS/IT/Electronics/Electrical/Mechinical/B.tech/BCA)",
        "Post Graduate":"Post Graduate",
        "Master in Tech":"Master in Tech(MCA/M.Tech)",
        "Other":"Other"
    }
    yes_no={
        "Y":"Yes",
        "N":"No",
    }
    centers={
        "I":"Inderlok",
        "J":"janakpuri",
        "K":"Karakrdooma",
    }
    skill={
        "S&SE":"Software & Systems Expert (O Level/A Level/Programming/Web Development)",
        "AI&ML":"AI & Data Science(AI,ML,Data Science)",
        "DM":"Digital Media (Multimedia Tools,Digital Marketing)",
        "AC":"Accounting",
        "GN":"General Office Automation",
        "O":"Other"
    }
    email= models.EmailField(max_length=100,blank=True, null=True)
    fullName= models.CharField(max_length=100,blank=True, null=True)
    gender=models.CharField(max_length=1,choices=gender_choices,blank=False)
    fatherName=models.CharField(max_length=100,blank=True, null=True)
    phoneNumber=models.CharField(max_length=10,blank=True, null=True)
    highestQualification=models.CharField(max_length=100,blank=True,null=True)
    state= models.CharField(max_length=50,blank=True, null=True)
    nielitStudent= models.CharField(max_length=1,choices=yes_no,blank=True, null=True)
    trainingCenter=models.CharField(max_length=1,choices=centers,blank=True, null=True)
    course=models.CharField(max_length=100,blank=True, null=True)
    passingYear=models.CharField(max_length=4,blank=True, null=True)
    skills=models.JSONField(default=list,blank=True)
    employed= models.CharField(max_length=1,choices=yes_no,blank=True, null=True)
    experience=models.CharField(max_length=10,blank=True, null=True)
    dec=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email} -- {self.fullName}"

