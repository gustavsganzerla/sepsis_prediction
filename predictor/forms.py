from django import forms
#/content/drive/MyDrive/DISP/Programming/models/('IFNg', 'IL-10', 'TNF-a', 'G-CSF').model
class Model1Form(forms.Form):#IFNg,IL-6,IL-17A,IL-1b
    IFNg = forms.FloatField(required=True)
    IL10 = forms.FloatField(required=True)
    TNFa = forms.FloatField(required=True)
    GCSF = forms.FloatField(required=True)

    


class Model2Form(forms.Form):#
    IL6 = forms.FloatField(required=True)
    IL4 = forms.FloatField(required=True)
    IL1b = forms.FloatField(required=True)
    TNFa = forms.FloatField(required=True)
    GCSF = forms.FloatField(required=True)

class Model3Form(forms.Form):#
    IL6 = forms.FloatField(required=True)
    IL2 = forms.FloatField(required=True)
    IL17A = forms.FloatField(required=True)
    IL1b = forms.FloatField(required=True)
    GCSF = forms.FloatField(required=True)
    

