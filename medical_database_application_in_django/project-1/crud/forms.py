#files.py
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import re
from crud import models
import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})
 
class RegistrationForm(forms.Form):
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Lase Name'}))
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={'invalid': _("This value must contain only letters, numbers and underscores.")})
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))
 
    def clean_username(self):
        try:
            User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    def clean_email(self):
        try:
            User.objects.get(email__iexact=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError(_("The email already exists. Please try another one."))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data


# class GeneralDetailsAddForm(forms.Form):
#     user_idsss = forms.IntegerField(required=False, initial=999, widget=forms.HiddenInput())
#     firstname = forms.CharField(label='Firstname')
#     lastname = forms.CharField(label='Lastname')
#     mobile_number = forms.CharField(label='Mobile nos' )
#     location = forms.CharField(label='Locations')
#     description = forms.CharField(label='Description')
#     date = forms.DateField(label='Login Start Date', initial=datetime.date.today)


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('firstname', css_class='form-group col-md-6 mb-0'),
    #             Column('lastname', css_class='form-group col-md-6 mb-0'),
    #             css_class='form-row'
    #         ),
    #         Row(
    #             Column('mobile_number', css_class='form-group col-md-6 mb-0'),
    #             Column('location', css_class='form-group col-md-6 mb-0'),
    #             css_class='form-row'
    #         ),
    #         Row(
    #             Column('description', css_class='form-group col-md-6 mb-0'),
    #             Column('date', css_class='form-group col-md-6 mb-0'),
    #             css_class='form-row'
    #         )

    #     )

MARRITIAL_CHOICE = (
	("UnMarried", "UnMarried"),
	("Married", "Married"))

GENDER_CHOICE = (
	("Male", "Male"),
	("Female", "Female"))

DIET_CHOICE = (
	("Veg", "Veg"),
	("Non-Veg", "Non-Veg"))

ADDICTION_CHOICE = (
	("Smoking", "Smoking"),
	("Drinking","Drinking"),
    ("Tobacco", "Tobacco"))

HABIT_CHOICE = (
	("Regular", "Regular"),
	("Irregular", "Irregular"))

HAZARD_CHOICE = (
	("Dust","Dust"),
    ("Noise","Noise"),
    ("Vibrations","Vibrations"),
    ("Fumes","Fumes")
    )

EXTERNAL_CHOICE = (
	("Normal", "Normal"),
	("Abnormal", "Abnormal"))

SQUINT_CHOICE = (
	("Present", "Present"),
	("Absent", "Absent"))

COLOUR_CHOICE = (
	("Normal", "Normal"),
	("Parhal Colour Deficit", "Parhal Colour Deficit"))

DIST_CHOICE = (
    ("",""),
	("6/6","6/6"),
    ("6/9","6/9"),
    ("6/12","6/12"),
    ("6/18","6/18"),
    ("6/24","6/24"),
    ("6/36","6/36"),
    ("6/60","6/60")

    )


NEAR_CHOICE = (
    ("",""),
	("N6","N6"),
    ("N8","N8"),
    ("N10","N10"),
    ("N12","N12"),
    ("N18","N18"),
    ("N24","N24"),
    ("N36","N36")
    )

BUILT_CHOICE = (
	("Average","Average"),
    ("Strong","Strong"),
    ("Poor","Poor")
    )

TEETH_CHOICE = (
	("Normal","Normal"),
    ("Dental Caries Present","Dental Caries Present")
    )

LUMP_CHOICE = (
	("NAD","NAD"),
    ("Enlarged","Enlarged")
    )

THYROID_CHOICE = (
	("Normal","Normal"),
    ("Enlarged","Enlarged")
    )

class GeneralMedicalDetailsAddForm(forms.Form):
    user_id = forms.IntegerField(required=False,initial=999, widget=forms.HiddenInput())
    fullname = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Patient Name'}), required=False)
    organization = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Organization'}), required=False)
    address = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Address'}) , required=False)
    department = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Department'}), required=False)
    id_mark = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Identification Mark'}), required=False)
    date = forms.DateField(widget=DateInput())
    dob = forms.DateField(widget=DateInput())
    gender = forms.ChoiceField(label='Gender',choices=GENDER_CHOICE, initial="Male", required=False)
    married_stat = forms.ChoiceField(label='Maritial Status',choices=MARRITIAL_CHOICE, initial="UnMarried", required=False)
    desig = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Designation'}), required=False)
    age = forms.CharField(label='Age',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Age'}), required=False)
    present_complains = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Present Complains if any'}), required=False)
    ###
    short_breath     = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    weight_loss = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    fainting_spells = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    freq_headache = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    chest_pain = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    hearing_disturb = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    freq_cold = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    urinary_disturb = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    visual_disturb = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    swelling_ankle = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    vertigo = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    joint_pains = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    ###
    self_hypertension = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    self_diabetes = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    self_heartdisease = forms.BooleanField(label=' ',required=False, widget=forms.CheckboxInput,initial=False)
    self_tuberculosis = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    self_cancer = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    self_asthama = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    self_stroke = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    self_epilepsy = forms.BooleanField(label='',required=False,widget=forms.CheckboxInput,initial=False)
    father_hypertension = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    father_diabetes = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    father_heartdisease = forms.BooleanField(label=' ',required=False, widget=forms.CheckboxInput,initial=False)
    father_tuberculosis = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    father_cancer = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    father_asthama = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    father_stroke = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    father_epilepsy = forms.BooleanField(label='',required=False,widget=forms.CheckboxInput,initial=False)
    mother_hypertension = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    mother_diabetes = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    mother_heartdisease = forms.BooleanField(label=' ',required=False, widget=forms.CheckboxInput,initial=False)
    mother_tuberculosis = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    mother_cancer = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    mother_asthama = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    mother_stroke = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput,initial=False)
    mother_epilepsy = forms.BooleanField(label='',required=False,widget=forms.CheckboxInput,initial=False)
    prev_surgiory                    = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Previous Surgery if any'}), required=False)   
    nos_of_child                        = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'No. of Children:'}), required=False)
    ##Personal History
    diet                             = forms.ChoiceField(label='Diet',choices=DIET_CHOICE, required=False)     
    addictions                          = forms.MultipleChoiceField(label='Addictions',choices=ADDICTION_CHOICE, required=False)
    bowel_habits                        = forms.ChoiceField(label='Bowel Habits',choices=HABIT_CHOICE, required=False)
    exercise                            = forms.ChoiceField(label='Excersice',choices=HABIT_CHOICE, required=False)
    ##Occupational History
    present_comp_name                   = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name of the company'}), required=False)
    present_years_worked                    = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Years'}), required=False)
    present_job_nature                  = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nature of Job'}), required=False)
    previous_comp_name                   = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name of the company'}), required=False)
    previous_years_worked               = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Years'}), required=False)
    previous_job_nature                     = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nature of Job'}), required=False)
    exposed_to_occupational_hazards      = forms.MultipleChoiceField(label='Expose To Hazardous',choices=HAZARD_CHOICE, required=False)
    ##Anthropometry
    height                                  = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Height (cm):'}), required=False)
    chest_inspiration                               = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Chest : Inspiration (cm):'}), required=False)
    abdominal_girth                     = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Abdominal Girth (cm):'}), required=False)
    weight                              = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':' Weight (Kg):'}), required=False)
    expiration                           = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Expiration (cm):'}), required=False)
    bmi                                     = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'BMI:'}), required=False)
    waist              =   forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Waist (cm):'}), required=False)
    hip              =   forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Hip (cm):'}), required=False)
    # waist_hip_ratio              =   forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Waist to Hip ratio:'}), required=False)
    ###Examination of Eyes   
    external_exam                       = forms.ChoiceField(label='External Exam',choices=EXTERNAL_CHOICE,required=False)
    squint_nystagmus                    = forms.ChoiceField(label='Squint Nystagmus', choices=SQUINT_CHOICE, required=False, initial="Absent")
    colour_vision                       = forms.ChoiceField(label='Colour Vision', choices=COLOUR_CHOICE ,required=False)
    ##Distant Vision:   
    without_glasses_re                  = forms.ChoiceField(label='(Without Glasses)R/E',choices=DIST_CHOICE,required=False)
    with_glasses_re                     = forms.ChoiceField(label='(With Glasses) R/E',  choices=DIST_CHOICE,required=False)
    without_glasses_le                  = forms.ChoiceField(label='(Without Glasses)L/E',choices=DIST_CHOICE,required=False)
    with_glasses_le                     = forms.ChoiceField(label='(With Glasses) L/E',  choices=DIST_CHOICE,required=False)
    ##Near Vision:
    without_glasses_re_near             = forms.ChoiceField(label='(Without Glasses)R/E',choices=NEAR_CHOICE, required=False)
    with_glasses_re_near                = forms.ChoiceField(label='(With Glasses) R/E',  choices=NEAR_CHOICE, required=False)
    without_glasses_le_near             = forms.ChoiceField(label='(Without Glasses)L/E',choices=NEAR_CHOICE, required=False)
    with_glasses_le_near                = forms.ChoiceField(label='(With Glasses) L/E',  choices=NEAR_CHOICE, required=False)
    ##General Examination
    built                               = forms.ChoiceField(label='Built',choices=BUILT_CHOICE, required=False)
    teeth                               = forms.ChoiceField(label='Teeth',choices=TEETH_CHOICE, required=False)
    throat                              = forms.CharField(label='Throat',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Throat'}), required=False,initial="Normal")
    tongue                              = forms.CharField(label='Tongue',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Tongue'}), required=False,initial="Normal")
    lymph_nodes                         = forms.ChoiceField(label='Lymph Nodes',choices=LUMP_CHOICE, required=False)
    pallor                              = forms.ChoiceField(label='Pallor',choices=SQUINT_CHOICE, required=False,initial="Absent")
    edema                               = forms.ChoiceField(label='Edema', choices=SQUINT_CHOICE, required=False,initial="Absent")
    thyroid                             = forms.ChoiceField(label='Thyroid',choices=THYROID_CHOICE, required=False)
    tonsils                             = forms.ChoiceField(label='Tonsils', choices=SQUINT_CHOICE, required=False,initial="Absent")
    gums                                = forms.ChoiceField(label='Gums',    choices=EXTERNAL_CHOICE, required=False)
    nails                               = forms.ChoiceField(label='Nails',   choices=EXTERNAL_CHOICE, required=False)
    icterus                             = forms.ChoiceField(label='Icterus', choices=SQUINT_CHOICE, required=False,initial="Absent")
    clubbing                            = forms.ChoiceField(label='Clubbing',choices=SQUINT_CHOICE, required=False,initial="Absent")
    ecg                                 = forms.ChoiceField(label='ECG',choices=EXTERNAL_CHOICE, required=False)

    ##Cardio Vascular system:
    pulse                                = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Pulse'}), required=False)
    pulse_stat                           = forms.ChoiceField(label='',choices=EXTERNAL_CHOICE, required=False)
    blood_pressure                       = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Blood Pressure'}), required=False)
    heart_sounds                         = forms.CharField(label='Heart Sounds',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Heart Sounds'}), required=False, initial="S1 S2 Heard")
    peripheral_pulsations                   = forms.CharField(label='Pheripheral Pulsation',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Pheripheral Pulsation'}), required=False,initial="Felt")
    murmur                                  = forms.ChoiceField(label='Murmur',choices=SQUINT_CHOICE, required=False,initial="Absent")
    ##Respiratory
    chest_shape           =  forms.ChoiceField(label='Chest Shape',choices=EXTERNAL_CHOICE, required=False)
    trachea  =  forms.ChoiceField(label='Trachea',choices=EXTERNAL_CHOICE, required=False)
    chest_movements  =  forms.ChoiceField(label='Chest Movements',choices=EXTERNAL_CHOICE, required=False)
    breath_sounds  =  forms.ChoiceField(label='Breath Sounds',choices=EXTERNAL_CHOICE, required=False)
    adventious_sounds  =  forms.ChoiceField(label='Adventious Sounds',choices=EXTERNAL_CHOICE, required=False)
    # respiratory_system                      = forms.CharField(label='Respiratory System',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Respiratory System'}), initial='Air Entry equal on both sides, No Adventitous sounds heard', required=False)
    ##Gastro - Intestinal System
    liver                                   = forms.CharField(initial='Non Palpable',label='Liver',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Liver'}), required=False)
    abdominal_lumps                         = forms.CharField(initial='Non Palpable',label='Abdominal Lumps',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Abdominal Lumps'}), required=False)
    spleen                                  = forms.CharField(initial='NAD',label='Spleen',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Spleen'}), required=False)
    ##Exam ear
    external_examination    =               forms.ChoiceField(label='External Examination',choices=EXTERNAL_CHOICE, required=False)
    conversational_hearing  =               forms.ChoiceField(label='Conversational Hearing',choices=EXTERNAL_CHOICE, required=False)	

    # examination_ear_nose_throat             = forms.CharField(label='Examination of Ear , Nose & Throat: ',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Examination of Ear , Nose & Throat: '}), initial='Normal External Examination , Normal Conversational Hearing', required=False)
    ##Central nervous system
    higher_function                     = forms.ChoiceField(label='Higher Functions',choices=EXTERNAL_CHOICE, required=False)
    sensory_system                      = forms.ChoiceField(label='Sensory System',choices=EXTERNAL_CHOICE, required=False)
    tendon_reflexes                     = forms.ChoiceField(label='Tendon Reflexes',choices=EXTERNAL_CHOICE, required=False)
    poisture                        = forms.ChoiceField(label='Poisture',choices=EXTERNAL_CHOICE, required=False)
    pshyco_makeup                       = forms.ChoiceField(label='Psychological Make Up',choices=EXTERNAL_CHOICE, required=False)
    cranial_nerves                      = forms.ChoiceField(label='Cranial Nerves',choices=EXTERNAL_CHOICE, required=False)
    motor_function                      = forms.ChoiceField(label='Motor Functions',choices=EXTERNAL_CHOICE, required=False)
    spine                       = forms.ChoiceField(label='Spine',choices=EXTERNAL_CHOICE, required=False)
    gait                        = forms.ChoiceField(label='Gait',choices=EXTERNAL_CHOICE, required=False)
    
    # central_nervous_system                  = forms.CharField(label='Central Nervous System:',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Central Nervous System:' }), initial='Cranial Nerves are Normal , Pshychological Make up Normal', required=False)
    skin                                    = forms.CharField(initial='Normal',label='Skin',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Skin'}), required=False)
    remarks                                 = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Remarks'}), required=False)
    advice                                  = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Advise'}), required=False)


                          




class Form7AddForm(forms.Form):
    form7_id = forms.IntegerField(required=False, initial=999, widget=forms.HiddenInput())
    date = forms.DateField(widget=DateInput())
    patient_name = forms.ModelChoiceField(queryset=models.PatientOverallMedicalDetails.objects.distinct('fullname'), required=False)
    dept_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Department Works'}), required=False )
    hazard = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name of Hazaedous process'}), required=False )
    danger = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Dangerous process'}) , required=False )
    job = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nature of Job'}), required=False )
    raw = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Raw materials, products likely to exposed'}), required=False )
    posting_date = forms.DateField(widget=DateInput())
    leaving_date = forms.DateField(widget=DateInput())
    discharge_reason = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Reason for Discharge or Transfer'}), required=False )
    discahrge_date = forms.DateField(widget=DateInput())
    symptons = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Sign & Symptons observed during examination'}), required=False )
    test_nature = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nature of test'}), required=False )
    results = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Results (Fit/Unfit)'}), required=False )
    temp_withdraw = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Period of temp withdrawl from work'}), required=False )
    reason_withdraw = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Reason for such withdraw'}), required=False )
    unfit_date = forms.DateField(widget=DateInput())
    fitness_date = forms.DateField(widget=DateInput())
    # sign_officer = forms.CharField(label='Sign with date of FActory medical officer',required=False)

URINE_COLOUR = [

    ("Yellow","Yellow"),
    ("Straw Yellow","Straw Yellow"),
    ("Pale Yellow","Pale Yellow"),
    ("Dark Yellow"," Dark Yellow"),
    ("Light Yellow","Light Yellow")
]
URINE_APPEAR = [

    ("Clear","Clear"),
    ("Slightly Hazzy","Slightly Hazzy"),
    ("Hazzy","Hazzy")
    
]

URINE_ODOUR = [

    ("Aromatic","Aromatic"),
    ("Sweet Yellow","Sweet Yellow")
    
    
]


class BloodUrineXRayAddForm(forms.Form):
    xray_id                         = forms.IntegerField(required=False, initial=999, widget=forms.HiddenInput())
    patient_name                        = forms.ModelChoiceField(queryset=models.PatientOverallMedicalDetails.objects.distinct('fullname'), required=False)
    date                             = forms.DateField(widget=DateInput())
    # age                             = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Age'}))
    # gender                          = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Gender'}))

    hb                              = forms.CharField(label='HB',help_text="12 -17 gm/dl",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'HB'}), required=False )
    wbc                             = forms.CharField(label='Total WBC',help_text="4000-10000 cells/cumm",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Total WBC'}), required=False )
    # diff_wb                         = forms.CharField(label='',help_text="",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Differential WBC'}), required=False )
    neutrophils                     = forms.CharField(label='Neutrophils',help_text="40-80 %",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Neutrophils'}), required=False )
    lymphocytes                     = forms.CharField(label='Lymphocytes',help_text="20-40%",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Lymphocytes'}), required=False )
    eosinophils                     = forms.CharField(label='Eosinophils',help_text="0-6%",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Eosinophils'}), required=False )
    monocytes                       = forms.CharField(label='Monocytes',help_text="0-10% ",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Monocytes'}), required=False )
    basophil                        = forms.CharField(label='Basophil',help_text="< 2%",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Basophil'}), required=False )
    total_rbc                       = forms.CharField(label='Total RBC',help_text="M: 4.5-5.5 F: 3.9-4.8 lacs",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Total RBC'}), required=False )
    platelet_count                  = forms.CharField(label='Platelet Count',help_text="1.5-4 lacs",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Platelet Count'}), required=False )
    esr                             = forms.CharField(label='ESR',help_text="M : 0 to 15 & F : 0 to 20 mm at end of 1 hr",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'ESR'}), required=False )
    rbsl                            = forms.CharField(label='RBSL',help_text="Up to 140 mg%",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'RBSL'}), required=False )
    blood_group                     = forms.CharField(label='Blood Group',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Blood Group'}), required=False )
    
    ##kidney
    
    uric_acid =                    forms.CharField(label='Uric Acid',help_text="2.5-7 mg/dl",widget=forms.TextInput(attrs={'class': 'form-control',                                   'placeholder':'Uric Acid:'}), required=False )
    blood_urea  =                  forms.CharField(label='Blood Urea',help_text="10-40 mg/dl",widget=forms.TextInput(attrs={'class': 'form-control',                 'placeholder':'Blood Urea:'}), required=False )
    se_creatinin   =               forms.CharField(label='Se.Creatinin',help_text="0.62-1.5 mg/dl",widget=forms.TextInput(attrs={'class': 'form-control',              'placeholder':'Se.Creatinin'}), required=False )
    
    ##
    ##glucose level
    fbsl                    =  forms.CharField(label='FBSL',help_text="70 - 120 mg/dl",widget=forms.TextInput(attrs={'class': 'form-control',                                 'placeholder':'FBSL'}), required=False)  
    ppbsl                   =  forms.CharField(label='PPBSL',help_text="Upto 140 mg/dl",widget=forms.TextInput(attrs={'class': 'form-control',                                 'placeholder':'PPBSL'}), required=False)  
    ####

    ##Lipid profile
    ldl_hdl_ratio               =  forms.CharField(label='LDL/HDL Ratio',help_text="Upto 3.5",widget=forms.TextInput(attrs={'class': 'form-control',                                 'placeholder':'LDL/HDL Ratio'}), required=False)  
    chol_hdl_ratio              =  forms.CharField(label='Tot Cholestrol/HDL Ratio',help_text="Upto 5.5",widget=forms.TextInput(attrs={'class': 'form-control',                                 'placeholder':'Total Cholesterol/ HDL RAtio'}), required=False)  
    
    total_cholesterol           =  forms.CharField(label='Total Cholestrol',help_text="125-200 mg/dl",widget=forms.TextInput(attrs={'class': 'form-control',                                 'placeholder':'Total Cholesterol'}), required=False)  
    triglycerides               =  forms.CharField(label='Triglycerides',help_text="25-200 mg/dl",widget=forms.TextInput(attrs={'class': 'form-control',                                  'placeholder':'Triglycerides'}), required=False )
    hdl  =                         forms.CharField(label='HDL',help_text="35-80 mg/dl",widget=forms.TextInput(attrs={'class': 'form-control',                                   'placeholder':'HDL'}), required=False )
    ldl  =                         forms.CharField(label='LDL',help_text="85-130 mg/dl",widget=forms.TextInput(attrs={'class': 'form-control',                                  'placeholder':'LDL'}), required=False )
    vldl  =                        forms.CharField(label='VLDL',help_text="5-40 mg/ dl",widget=forms.TextInput(attrs={'class': 'form-control',                                   'placeholder':'VLDL'}), required=False )
    ###s

    ###Liver test
    total_protein               =  forms.CharField(label='Total Protein',help_text="6.0 - 8.3 g/dl",widget=forms.TextInput(attrs={'class': 'form-control',                                   'placeholder':'Total Protein'}), required=False )
    albumin             =  forms.CharField(label='Albumin',help_text="3.5 - 5.5 g/dl",widget=forms.TextInput(attrs={'class': 'form-control',                                   'placeholder':'Albumin'}), required=False )
    globumin                =  forms.CharField(label='Globumin',help_text="2.6 - 4.6 g/dl",widget=forms.TextInput(attrs={'class': 'form-control',                                   'placeholder':'Globumin'}), required=False )
    bilirubin_indierct = forms.CharField(label='Bilrubin Indirect',help_text="0 - 0.9mg/dl",widget=forms.TextInput(attrs={'class': 'form-control',                                   'placeholder':'Bilirubin InDierct'}), required=False )
    
    sgot  =                        forms.CharField(label='SGOT',help_text="Male: 0 to 37 U/l     Female: 0 to 31 U/l ",widget=forms.TextInput(attrs={'class': 'form-control',    'placeholder':'SGOT'}), required=False )
    sgpt  =                        forms.CharField(label='SGPT',help_text="Male: 13 to 40 U/l     Female: 10 to 28 U/l ",widget=forms.TextInput(attrs={'class': 'form-control',  'placeholder':'SGPT'}), required=False )
    bilirubin_total   =            forms.CharField(label='Total Bilrubin',help_text="0.1 - 1.2 mg/dl",widget=forms.TextInput(attrs={'class': 'form-control',                               'placeholder':'Bilirubin Tota'}), required=False )
    bilirubin_dierct   =           forms.CharField(label='Bilrubin Direct',help_text="< 0.3mg/dl",widget=forms.TextInput(attrs={'class': 'form-control',                                   'placeholder':'Bilirubin Dierct'}), required=False )
    alkaline_phosphatase   =       forms.CharField(label='Alkaline Phosphatase',help_text="Male: 53 to 128 U/l     Female:  42 to 98 U/l ",widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Alkaline Phosphatase'}), required=False )
    ####



    
    ##urine exam            
    urine_colour                    = forms.ChoiceField(label='Urine Colour',    choices=URINE_COLOUR, required=False)
    urine_appearance                = forms.ChoiceField(label='Urine Appearance',choices=URINE_APPEAR, required=False)
    urine_odour                     = forms.ChoiceField(label='Urine Odour',  choices=URINE_ODOUR   ,required=False)
    urine_ph                        = forms.CharField(label='PH',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'PH'}), required=False)
    urine_gravity                   = forms.CharField(label='Specific Gravity',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Specific Gravity'}), required=False)
    urine_deposits                  = forms.ChoiceField(label='Deposits',choices=SQUINT_CHOICE, required=False,initial="Absent")
    urine_protein                   = forms.ChoiceField(label='Protein', choices=SQUINT_CHOICE, required=False,initial="Absent")
    urine_sugar                     = forms.ChoiceField(label='Sugar',   choices=SQUINT_CHOICE, required=False,initial="Absent")

    ##Microscop
    microscopic_pus_cell            = forms.CharField(label='Pus Cell',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Pus Cell'}), required=False)    
    microscopic_epithelial_cell     = forms.CharField(label='Epithelial Cell',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Epithelial Cell'}), required=False)
    microscopic_rbc_cells           = forms.CharField(label='RBC Cells',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'RBC Cells'}), required=False, initial="Nil")
    microscopic_crystals            = forms.ChoiceField(label='Crystals',choices=SQUINT_CHOICE, required=False,initial="Absent")
    microscopic_cast                = forms.ChoiceField(label='Cast',    choices=SQUINT_CHOICE, required=False,initial="Absent")
    microscopic_other_findings       = forms.CharField(label='Other Findings',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Other findings'}), required=False, initial="Nil")

                               
    xray_view = forms.CharField( required=False,widget=forms.Textarea(), label='',initial='Bones and soft tissues around the chest appears normal.Both the lungs fields are clear.Both the domes of the diaphragm are at normal level.Heart aorta and the mediastinum are Normal.No profusion seen.')


    opinion                             = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Opinion'}), required=False)


STOOL_COLOR =[
    ("Brownish","Brownish"),
    ("Greenish","Greenish"),
    ("Blackish","Blackish")
]
STOOL_CONST =[
    ("Semi Solid","Semi Solid"),
    ("Solid","Solid"),
    ("Liquid","Liquid")
]

OCCULT =[
    ("Negative","Negative"),
    ("Positive","Positive")
    
]

PH = [
    ("Alkaline","Alkaline"),
    ("Acidic","Acidic")
]

VDRL = [
    ("Reactive","Reactive"),
    ("Non Reactive","Non Reactive")
]
class StoolReportAddForm(forms.Form):
    stool_id                        = forms.IntegerField(required=False, initial=999, widget=forms.HiddenInput())
    patient_name                    = forms.ModelChoiceField(queryset=models.PatientOverallMedicalDetails.objects.distinct('fullname'), required=False)
    date                            = forms.DateField(widget=DateInput())
    # age                             = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Age'}))
    # gender                          = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Gender'}))

    
    ##General exam
    colour                          = forms.ChoiceField(label='Colour',choices=STOOL_COLOR, required=False)
    consistency                     = forms.ChoiceField(label='Consistency',choices=STOOL_CONST, required=False)
    mucus                           = forms.ChoiceField(label='Mucus',choices=SQUINT_CHOICE, required=False, initial="Absent")
    parasites                       = forms.ChoiceField(label='Parasites',choices=SQUINT_CHOICE, required=False, initial="Absent")
    frank_blood                     = forms.ChoiceField(label='Frank Blood',choices=SQUINT_CHOICE, required=False, initial="Absent")
    occult_blood                     = forms.ChoiceField(label='Occult Blood',choices=OCCULT, required=False, initial="Negative")
    # stercobilinogen                   = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Stercobilinogen'}), required=False)
    reaction_pH                    = forms.ChoiceField(label='Reaction (pH)',choices=PH, required=False)

    ##Microscope
    microscope_epithelial_cells         = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Epithelial cells'}), required=False)    
    microscope_pus_cells               = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Pus cells'}), required=False)
    microscope_rbs_cells                = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Red Blood cells'}), required=False)
    microscope_protozoa                 = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Cysts of protozoa'}), required=False)
    microscope_ova                  = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ova'}), required=False)
    microscope_other_findings          = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Other findings'}), required=False)

    ###Widal report

    widal_salmonella_O                = forms.ChoiceField(label="Salmonella Typhi -O",choices=OCCULT, required=False)
    widal_salmonella_H                = forms.ChoiceField(label="Salmonella Typhi -H",choices=OCCULT, required=False)
    widal_salmonella_AH               = forms.ChoiceField(label="Salmonella Paratyphi -AH",choices=OCCULT, required=False)
    widal_salmonella_BH               = forms.ChoiceField(label="Salmonella Paratyphi -BH",choices=OCCULT, required=False)

    hep_A                           =  forms.ChoiceField(label="HEPATITIS A",choices=OCCULT, required=False)
    hep_B                           =  forms.ChoiceField(label="HEPATITIS B",choices=OCCULT, required=False)
    hep_C                           =  forms.ChoiceField(label="HEPATITIS C",choices=OCCULT, required=False)
    vdrl                            =  forms.ChoiceField(label="VDRL",choices=VDRL, required=False)
    hiv1                            =  forms.ChoiceField(label="HIV 1",choices=OCCULT, required=False)
    hiv2                            =  forms.ChoiceField(label="HIV 2",choices=OCCULT, required=False)
    sputum                            =  forms.ChoiceField(label="Sputum AFB",choices=OCCULT, required=False)









class AudiometryAddForm(forms.Form):
    audio_id                         = forms.IntegerField(required=False, initial=999, widget=forms.HiddenInput())
    patient_name                        = forms.ModelChoiceField(queryset=models.PatientOverallMedicalDetails.objects.distinct('fullname'), required=False)
    date                             = forms.DateField(widget=DateInput())
    # age                             = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Age'}))
    # gender                          = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Gender'}))

    le_ear_125                 = forms.CharField(required=False,label='125',widget=forms.TextInput(attrs={'class': 'form-control' }))
    le_ear_250                 = forms.CharField(required=False,label='250',widget=forms.TextInput(attrs={'class': 'form-control' }))
    le_ear_500                 = forms.CharField(required=False,label='500',widget=forms.TextInput(attrs={'class': 'form-control' }))
    le_ear_1K                  = forms.CharField(required=False,label='1K',widget=forms.TextInput(attrs={'class': 'form-control' }))
    le_ear_2K                  = forms.CharField(required=False,label='2K',widget=forms.TextInput(attrs={'class': 'form-control' }))
    le_ear_4K                  = forms.CharField(required=False,label='4K',widget=forms.TextInput(attrs={'class': 'form-control' }))
    le_ear_6K                  = forms.CharField(required=False,label='6K',widget=forms.TextInput(attrs={'class': 'form-control' }))
    le_ear_8K                  = forms.CharField(required=False,label='8K',widget=forms.TextInput(attrs={'class': 'form-control' }))
    re_ear_125                 = forms.CharField(required=False,label='125',widget=forms.TextInput(attrs={'class': 'form-control'}))
    re_ear_250                 = forms.CharField(required=False,label='250',widget=forms.TextInput(attrs={'class': 'form-control'}))
    re_ear_500                 = forms.CharField(required=False,label='500',widget=forms.TextInput(attrs={'class': 'form-control'}))
    re_ear_1K                  = forms.CharField(required=False,label='1K',widget=forms.TextInput(attrs={'class': 'form-control'}))
    re_ear_2K                  = forms.CharField(required=False,label='2K',widget=forms.TextInput(attrs={'class': 'form-control'}))
    re_ear_4K                  = forms.CharField(required=False,label='4K',widget=forms.TextInput(attrs={'class': 'form-control'}))
    re_ear_6K                  = forms.CharField(required=False,label='6K',widget=forms.TextInput(attrs={'class': 'form-control'}))
    re_ear_8K                  = forms.CharField(required=False,label='8K',widget=forms.TextInput(attrs={'class': 'form-control'}))
    bone_le_ear_250            = forms.CharField(required=False,label='250',widget=forms.TextInput(attrs={'class': 'form-control'}))
    bone_le_ear_500            = forms.CharField(required=False,label='500',widget=forms.TextInput(attrs={'class': 'form-control'}))
    bone_le_ear_1K             = forms.CharField(required=False,label='1K',widget=forms.TextInput(attrs={'class': 'form-control'}))
    bone_le_ear_2K             = forms.CharField(required=False,label='2K',widget=forms.TextInput(attrs={'class': 'form-control'}))
    bone_le_ear_4K             = forms.CharField(required=False,label='4K',widget=forms.TextInput(attrs={'class': 'form-control'}))
    bone_re_ear_250            = forms.CharField(required=False,label='250',widget=forms.TextInput(attrs={'class': 'form-control'}))
    bone_re_ear_500            = forms.CharField(required=False,label='500',widget=forms.TextInput(attrs={'class': 'form-control'}))
    bone_re_ear_1K             = forms.CharField(required=False,label='1K',widget=forms.TextInput(attrs={'class': 'form-control'}))
    bone_re_ear_2K             = forms.CharField(required=False,label='2K',widget=forms.TextInput(attrs={'class': 'form-control'}))
    bone_re_ear_4K             = forms.CharField(required=False,label='4K',widget=forms.TextInput(attrs={'class': 'form-control'}))    
    
    
    
class ReportsForm(forms.Form):
    from_date = forms.DateField(widget=DateInput(),required=False)    
    to_date = forms.DateField(widget=DateInput(),required=False)
    company_name = forms.ModelChoiceField(queryset=models.PatientOverallMedicalDetails.objects.values_list('organization',flat=True).distinct(), required=False)







    