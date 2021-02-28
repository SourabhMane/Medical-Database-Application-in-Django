from django.shortcuts import render, redirect
from .models import Member, Document, Ajax, CsvUpload
import datetime
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from crud.forms import *
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import FormView, ListView
from django.template.context_processors import csrf

from django.db.models import Q



from django.http import HttpResponse
from django.views.generic import View

from crud.utils import render_to_pdf #created in step 4

class GenerateMedicalPdf(View):
    def get(self, request, *args, **kwargs):
        if self.kwargs['patient_id']:
            patient_obj = models.PatientOverallMedicalDetails.objects.get(id = self.kwargs['patient_id'] )

            data = {
                    

                    'user_id':patient_obj.id,
                    'fullname':patient_obj.fullname,
                    'organization':patient_obj.organization,
                    'address':patient_obj.address,
                    'department':patient_obj.department,
                    'id_mark':patient_obj.id_mark,
                    'date':patient_obj.date,
                    'dob':patient_obj.dob,
                    'gender':patient_obj.gender,
                    'married_stat':patient_obj.married_stat,
                    'desig':patient_obj.desig,
                    'age':patient_obj.age,
                    'present_complains':patient_obj.present_complains,
                    'self_hypertension':patient_obj.self_hypertension,
                    'self_diabetes':patient_obj.self_diabetes,
                    'self_heartdisease':patient_obj.self_heartdisease,
                    'self_tuberculosis':patient_obj.self_tuberculosis,
                    'self_cancer':patient_obj.self_cancer,
                    'self_asthama':patient_obj.self_asthama,
                    'self_stroke':patient_obj.self_stroke,
                    'self_epilepsy':patient_obj.self_epilepsy,
                    'father_hypertension':patient_obj.father_hypertension,
                    'father_diabetes':patient_obj.father_diabetes,
                    'father_heartdisease':patient_obj.father_heartdisease,
                    'father_tuberculosis':patient_obj.father_tuberculosis,
                    'father_cancer':patient_obj.father_cancer,
                    'father_asthama':patient_obj.father_asthama,
                    'father_stroke':patient_obj.father_stroke,
                    'father_epilepsy':patient_obj.father_epilepsy,
                    'mother_hypertension':patient_obj.mother_hypertension,
                    'mother_diabetes':patient_obj.mother_diabetes,
                    'mother_heartdisease':patient_obj.mother_heartdisease,
                    'mother_tuberculosis':patient_obj.mother_tuberculosis,
                    'mother_cancer':patient_obj.mother_cancer,
                    'mother_asthama':patient_obj.mother_asthama,
                    'mother_stroke':patient_obj.mother_stroke,
                    'mother_epilepsy':patient_obj.mother_epilepsy,
                    'prev_surgiory':patient_obj.prev_surgiory,
                    'nos_of_child':patient_obj.nos_of_child,
                    'diet':patient_obj.diet,
                    'addictions':patient_obj.addictions,
                    'bowel_habits':patient_obj.bowel_habits,
                    'exercise':patient_obj.exercise,
                    'present_comp_name':patient_obj.present_comp_name,
                    'present_years_worked':patient_obj.present_years_worked,
                    'present_job_nature':patient_obj.present_job_nature,
                    'previous_comp_name':patient_obj.previous_comp_name,
                    'previous_years_worked':patient_obj.previous_years_worked,
                    'previous_job_nature':patient_obj.previous_job_nature,
                    'exposed_to_occupational_hazards':patient_obj.exposed_to_occupational_hazards,
                    'height':patient_obj.height,
                    'chest_inspiration':patient_obj.chest_inspiration,
                    'abdominal_girth':patient_obj.abdominal_girth,
                    'weight':patient_obj.weight,
                    'expiration':patient_obj.expiration,
                    'bmi':patient_obj.bmi,
                    'external_exam':patient_obj.external_exam,
                    'squint_nystagmus':patient_obj.squint_nystagmus,
                    'colour_vision':patient_obj.colour_vision,
                    'without_glasses_re':patient_obj.without_glasses_re,
                    'with_glasses_re':patient_obj.with_glasses_re,
                    'without_glasses_le':patient_obj.without_glasses_le,
                    'with_glasses_le':patient_obj.with_glasses_le,
                    'without_glasses_re_near':patient_obj.without_glasses_re_near,
                    'with_glasses_re_near':patient_obj.with_glasses_re_near,
                    'without_glasses_le_near':patient_obj.without_glasses_le_near,
                    'with_glasses_le_near':patient_obj.with_glasses_le_near,
                    'built':patient_obj.built,
                    'teeth':patient_obj.teeth,
                    'throat':patient_obj.throat,
                    'tongue':patient_obj.tongue,
                    'lymph_nodes':patient_obj.lymph_nodes,
                    'pallor':patient_obj.pallor,
                    'edema':patient_obj.edema,
                    'thyroid':patient_obj.thyroid,
                    'tonsils':patient_obj.tonsils,
                    'gums':patient_obj.gums,
                    'nails':patient_obj.nails,
                    'icterus':patient_obj.icterus,
                    'pulse':patient_obj.pulse,
                    'blood_pressure':patient_obj.blood_pressure,
                    'heart_sounds':patient_obj.heart_sounds,
                    'peripheral_pulsations':patient_obj.peripheral_pulsations,
                    'murmur':patient_obj.murmur,
                    'liver':patient_obj.liver,
                    'abdominal_lumps':patient_obj.abdominal_lumps,
                    'spleen':patient_obj.spleen,                                      
                    'skin':patient_obj.skin,
                    'remarks':patient_obj.remarks,
                    'advice':patient_obj.advice,
                    'clubbing':patient_obj.clubbing,
                    'ecg':patient_obj.ecg,
                    'pulse_stat':patient_obj.pulse_stat,
                    'higher_function':patient_obj.higher_function,
                    'sensory_system':patient_obj.sensory_system,
                    'tendon_reflexes':patient_obj.tendon_reflexes,
                    'poisture':patient_obj.poisture,
                    'pshyco_makeup':patient_obj.pshyco_makeup,
                    'cranial_nerves':patient_obj.cranial_nerves,
                    'motor_function':patient_obj.motor_function,
                    'spine':patient_obj.spine,
                    'gait':patient_obj.gait,
                    'external_examination':patient_obj.external_examination,
                    'conversational_hearing':patient_obj.conversational_hearing,
                    'chest_shape':patient_obj.chest_shape,
                    'trachea':patient_obj.trachea,
                    'chest_movements':patient_obj.chest_movements,
                    'breath_sounds':patient_obj.breath_sounds,
                    'adventious_sounds':patient_obj.adventious_sounds,
                    'waist':patient_obj.waist,
                    'hip':patient_obj.hip,
                    # 'waist_hip_ratio':patient_obj.waist_hip_ratio,
                    # 'short_breath':patient_obj.short_breath,
                    # 'weight_loss':patient_obj.weight_loss,
                    # 'fainting_spells':patient_obj.fainting_spells,
                    # 'freq_headache':patient_obj.freq_headache,
                    # 'chest_pain':patient_obj.chest_pain,
                    # 'hearing_disturb':patient_obj.hearing_disturb,
                    # 'freq_cold':patient_obj.freq_cold,
                    # 'urinary_disturb':patient_obj.urinary_disturb,
                    # 'visual_disturb':patient_obj.visual_disturb,
                    # 'swelling_ankle':patient_obj.swelling_ankle,
                    # 'vertigo':patient_obj.vertigo,
                    # 'joint_pains':patient_obj.joint_pains,
            }
            
            pdf = render_to_pdf('patient_pdf.html', data)
            response = HttpResponse(pdf, content_type='application/pdf')
            name = patient_obj.fullname
            filename = "Patient_%s.pdf"%(name)
            content = "inline;filename=%s"%(filename)
            response['Content-Disposition'] = content
            return response



class GenerateBloodPdf(View):
    def get(self, request, *args, **kwargs):
        if self.kwargs['blood_id']:
            patient_obj = models.BloodUrineXRay.objects.get(id = self.kwargs['blood_id'] )
            patient_obj_info = models.PatientOverallMedicalDetails.objects.filter(id=patient_obj.patient_id_id).values('gender','age','fullname')

            data = {
                
                'date':patient_obj.date,      
                'hb':patient_obj.hb,
                'wbc':patient_obj.wbc,
                'diff_wb':patient_obj.diff_wb,
                'neutrophils':patient_obj.neutrophils,
                'lymphocytes':patient_obj.lymphocytes,
                'eosinophils':patient_obj.eosinophils,
                'monocytes':patient_obj.monocytes,
                'basophil':patient_obj.basophil,
                'total_rbc':patient_obj.total_rbc,
                'platelet_count':patient_obj.platelet_count,
                'esr':patient_obj.esr,
                'rbsl':patient_obj.rbsl,
                'blood_group':patient_obj.blood_group,
                'urine_colour':patient_obj.urine_colour,
                'urine_appearance':patient_obj.urine_appearance,
                'urine_odour':patient_obj.urine_odour,
                'urine_ph':patient_obj.urine_ph,
                'urine_gravity':patient_obj.urine_gravity,
                'urine_deposits':patient_obj.urine_deposits,
                'urine_protein':patient_obj.urine_protein,
                'urine_sugar':patient_obj.urine_sugar,
                'microscopic_pus_cell':patient_obj.microscopic_pus_cell,
                'microscopic_epithelial_cell':patient_obj.microscopic_epithelial_cell,
                'microscopic_rbc_cells':patient_obj.microscopic_rbc_cells,
                'microscopic_crystals':patient_obj.microscopic_crystals,
                'microscopic_cast':patient_obj.microscopic_cast,
                'microscopic_other_findings':patient_obj.microscopic_other_findings,
                'xray_view':patient_obj.xray_view,
                'opinion':patient_obj.opinion,
                'age' : patient_obj_info[0]['age'],
                'gender' : patient_obj_info[0]['gender'],
                'fullname' : patient_obj_info[0]['fullname'],
                'total_cholesterol':patient_obj.total_cholesterol,
                'triglycerides':patient_obj.triglycerides,
                'hdl':patient_obj.hdl,
                'ldl':patient_obj.ldl,
                'vldl':patient_obj.vldl,
                'sgot':patient_obj.sgot,
                'sgpt':patient_obj.sgpt,
                'blood_urea':patient_obj.blood_urea,
                'se_creatinin':patient_obj.se_creatinin,
                'bilirubin_total':patient_obj.bilirubin_total,
                'bilirubin_dierct':patient_obj.bilirubin_dierct,
                'alkaline_phosphatase':patient_obj.alkaline_phosphatase,
                'uric_acid': patient_obj.uric_acid,
                'fbsl': patient_obj.fbsl,
                'ppbsl': patient_obj.ppbsl,
                'ldl_hdl_ratio': patient_obj.ldl_hdl_ratio,
                'chol_hdl_ratio': patient_obj.chol_hdl_ratio,
                'total_protein': patient_obj.total_protein,
                'albumin': patient_obj.albumin,
                'globumin': patient_obj.globumin,
                'bilirubin_indierct': patient_obj.bilirubin_indierct,

            }
            pdf = render_to_pdf('blood_urine_pdf.html', data)
            response = HttpResponse(pdf, content_type='application/pdf')
            name = patient_obj_info[0]['fullname']
            filename = "BloodUrineReport_%s.pdf"%(name)
            content = "inline;filename=%s"%(filename)
            response['Content-Disposition'] = content
            return response

class GenerateStoolPdf(View):
    def get(self, request, *args, **kwargs):
        if self.kwargs['stool_id']:
            patient_obj = models.StoolReport.objects.get(id = self.kwargs['stool_id'] )
            patient_obj_info = models.PatientOverallMedicalDetails.objects.filter(id=patient_obj.patient_id_id).values('gender','age','fullname')

            data = {
                    'age' : patient_obj_info[0]['age'],
                    'gender' : patient_obj_info[0]['gender'],
                    'fullname' : patient_obj_info[0]['fullname'],
                    'date':patient_obj.date,
                    'colour':patient_obj.colour,
                    'consistency':patient_obj.consistency,
                    'mucus':patient_obj.mucus,
                    'parasites':patient_obj.parasites,
                    'frank_blood':patient_obj.frank_blood,
                    'occult_blood':patient_obj.occult_blood,
                    # 'stercobilinogen':patient_obj.stercobilinogen,
                    'reaction_pH':patient_obj.reaction_pH,
                    'microscope_epithelial_cells':patient_obj.microscope_epithelial_cells,
                    'microscope_pus_cells':patient_obj.microscope_pus_cells,
                    'microscope_rbs_cells':patient_obj.microscope_rbs_cells,
                    'microscope_protozoa':patient_obj.microscope_protozoa,
                    'microscope_ova':patient_obj.microscope_ova,
                    'microscope_other_findings':patient_obj.microscope_other_findings,
                    'widal_salmonella_O':patient_obj.widal_salmonella_O,
                    'widal_salmonella_H':patient_obj.widal_salmonella_H,
                    'widal_salmonella_AH':patient_obj.widal_salmonella_AH,
                    'widal_salmonella_BH':patient_obj.widal_salmonella_BH,
                    'hep_A':patient_obj.hep_A,
                    'hep_B':patient_obj.hep_B,
                    'hep_C':patient_obj.hep_C,
                    'vdrl':patient_obj.vdrl,
                    'hiv1':patient_obj.hiv1,
                    'hiv2':patient_obj.hiv2,
                    'sputum':patient_obj.sputum,
            }
            
            pdf = render_to_pdf('stool_pdf.html', data)
            response = HttpResponse(pdf, content_type='application/pdf')
            name = patient_obj_info[0]['fullname']
            filename = "StoolReport_%s.pdf"%(name)
            content = "inline;filename=%s"%(filename)
            response['Content-Disposition'] = content
            return response



class GenerateForm7Pdf(View):
    def get(self, request, *args, **kwargs):
               
        if self.kwargs['form7_id']:
            patient_obj = models.Form7Details.objects.get(id = self.kwargs['form7_id'] )
            patient_obj_info = models.PatientOverallMedicalDetails.objects.filter(id=patient_obj.patient_id_id).values('gender','dob')
            print(patient_obj_info[0]['gender'])
            data = {
                'dept_name':   patient_obj.dept_name,
                'hazard':   patient_obj.hazard,   
                'danger':   patient_obj.danger,
                'job':   patient_obj.job,
                'raw':   patient_obj.raw,
                'posting_date':   patient_obj.posting_date,
                'leaving_date':   patient_obj.leaving_date,
                'discharge_reason':   patient_obj.discharge_reason,
                'discahrge_date':   patient_obj.discahrge_date,
                'symptons':   patient_obj.symptons,
                'test_nature':   patient_obj.test_nature,
                'results':   patient_obj.results,
                'temp_withdraw':   patient_obj.temp_withdraw,
                'reason_withdraw':   patient_obj.reason_withdraw,
                'unfit_date':   patient_obj.unfit_date,
                'fitness_date':   patient_obj.fitness_date,
                'pt_name':   patient_obj.patient_name,
                'gender': patient_obj_info[0]['gender'],
                'dob': patient_obj_info[0]['dob']
            }
            
            pdf = render_to_pdf('form7_pdf.html', data)
            response = HttpResponse(pdf, content_type='application/pdf')
            name = patient_obj.patient_name
            filename = "Form7_%s.pdf"%(name)
            content = "inline;filename=%s"%(filename)
            response['Content-Disposition'] = content
            return response
        

    def get_initial(self):
        print("inside initial")
        initial = super(GenerateMedicalPdf, self).get_initial()
        try:
            if self.kwargs['user_id']:
                print("id inside initial",self.kwargs['user_id'] )
                patient_obj = models.PatientOverallMedicalDetails.objects.get(id = self.kwargs['user_id'] )
                initial['user_id'] = patient_obj.id
                print("patient name",initial['user_id'])
                initial['fullname']= patient_obj.fullname
                print("patient name",patient_obj.fullname)
                initial['organization']= patient_obj.organization
                initial['address']= patient_obj.address
                initial['department']= patient_obj.department
                initial['id_mark']= patient_obj.id_mark
                initial['date']= patient_obj.date
                initial['dob']= patient_obj.dob
                initial['gender']= patient_obj.gender
                initial['married_stat']= patient_obj.married_stat
                initial['desig']= patient_obj.desig
                initial['age']= patient_obj.age
                initial['present_complains']= patient_obj.present_complains

        
        
        except Exception:
            print()
        return initial


class GenerateGraph(FormView):
    template_name = 'charts.html'
    


    def get(self, request, *args, **kwargs):
        # if self.kwargs['id']
        print(self.kwargs['id'])
        context = {}
        mean_le = []
        mean_re = []
        mean_bone_le = []
        mean_bone_re = []
        import statistics
        graph_data = models.Audiometry.objects.filter(id=self.kwargs['id'])
        patient_info = models.PatientOverallMedicalDetails.objects.get(id=graph_data[0].patient_name_id)
        sum = graph_data[0].le_ear_500 + graph_data[0].le_ear_1K + graph_data[0].le_ear_2K
        mean_le.append(graph_data[0].le_ear_500)
        mean_le.append(graph_data[0].le_ear_1K)
        mean_le.append(graph_data[0].le_ear_2K)
        
        mean_re.append(graph_data[0].re_ear_500)
        mean_re.append(graph_data[0].re_ear_1K)
        mean_re.append(graph_data[0].re_ear_2K)

        mean_bone_le.append(graph_data[0].bone_le_ear_500)
        mean_bone_le.append(graph_data[0].bone_le_ear_1K)
        mean_bone_le.append(graph_data[0].bone_le_ear_2K)

        mean_bone_re.append(graph_data[0].bone_re_ear_500)
        mean_bone_re.append(graph_data[0].bone_re_ear_1K)
        mean_bone_re.append(graph_data[0].bone_re_ear_2K)

        print("mean",statistics.mean(mean_bone_le))
        print("mean",statistics.mean(mean_bone_re))
        print("mean",statistics.mean(mean_le))
        print("mean",statistics.mean(mean_re))

        return render(request, self.template_name, {'graph_data': graph_data, 'mean_le_data':statistics.mean(mean_le), 'mean_re_data':statistics.mean(mean_re), 'mean_bone_re_data':statistics.mean(mean_bone_re), 'mean_bone_le_data':statistics.mean(mean_bone_le), 'patient_info':patient_info})
        
        
        

@login_required
def index(request):
    return render(request, 'index.html')

def get_pglist_from_obj_list(obj_list):
    if not obj_list:
        return []

    _ids = []
    for obj in obj_list:
        _ids.append(str(obj.id))
    return  ",".join(_ids) 


class AddGeneralDetailsView(FormView):
    template_name = 'member_info.html'
    form_class = GeneralMedicalDetailsAddForm


    def post(self, request, *args, **kwargs):
        
        # try:
            c = {}
            c.update(csrf(request))
            fw_nw_form = GeneralMedicalDetailsAddForm(request.POST)
            if not fw_nw_form.is_valid():
                variables = {'form': fw_nw_form }
                messages.error(request, 'Invalid data in form')
                return render(request, self.template_name, variables )

            user_id             = fw_nw_form.cleaned_data['user_id']
            fullname            = fw_nw_form.cleaned_data['fullname']
            organization        = fw_nw_form.cleaned_data['organization']
            address             = fw_nw_form.cleaned_data['address']
            department           = fw_nw_form.cleaned_data['department']
            id_mark             = fw_nw_form.cleaned_data['id_mark']
            date                 = fw_nw_form.cleaned_data['date']
            dob                 = fw_nw_form.cleaned_data['dob']
            gender              = fw_nw_form.cleaned_data['gender']
            married_stat        = fw_nw_form.cleaned_data['married_stat']
            desig               = fw_nw_form.cleaned_data['desig']
            age                 = fw_nw_form.cleaned_data['age']
            present_complains   = fw_nw_form.cleaned_data['present_complains']
            self_hypertension   = fw_nw_form.cleaned_data['self_hypertension']
            self_diabetes       = fw_nw_form.cleaned_data['self_diabetes']
            self_heartdisease   = fw_nw_form.cleaned_data['self_heartdisease']
            self_tuberculosis   = fw_nw_form.cleaned_data['self_tuberculosis']
            self_cancer         = fw_nw_form.cleaned_data['self_cancer']
            self_asthama        = fw_nw_form.cleaned_data['self_asthama']
            self_stroke         = fw_nw_form.cleaned_data['self_stroke']
            self_epilepsy         = fw_nw_form.cleaned_data['self_epilepsy']
            father_hypertension = fw_nw_form.cleaned_data['father_hypertension']
            father_diabetes     = fw_nw_form.cleaned_data['father_diabetes']
            father_heartdisease = fw_nw_form.cleaned_data['father_heartdisease']
            father_tuberculosis = fw_nw_form.cleaned_data['father_tuberculosis']
            father_cancer       = fw_nw_form.cleaned_data['father_cancer']
            father_asthama      = fw_nw_form.cleaned_data['father_asthama']
            father_stroke       = fw_nw_form.cleaned_data['father_stroke']
            father_epilepsy         = fw_nw_form.cleaned_data['father_epilepsy']
            mother_hypertension = fw_nw_form.cleaned_data['mother_hypertension']
            mother_diabetes     = fw_nw_form.cleaned_data['mother_diabetes']
            mother_heartdisease = fw_nw_form.cleaned_data['mother_heartdisease']
            mother_tuberculosis = fw_nw_form.cleaned_data['mother_tuberculosis']
            mother_cancer       = fw_nw_form.cleaned_data['mother_cancer']
            mother_asthama      = fw_nw_form.cleaned_data['mother_asthama']
            mother_stroke       = fw_nw_form.cleaned_data['mother_stroke']
            mother_epilepsy         = fw_nw_form.cleaned_data['mother_epilepsy']
            prev_surgiory       = fw_nw_form.cleaned_data['prev_surgiory']
            nos_of_child        = fw_nw_form.cleaned_data['nos_of_child']
            diet        = fw_nw_form.cleaned_data['diet']
            addictions      = fw_nw_form.cleaned_data['addictions']
            bowel_habits        = fw_nw_form.cleaned_data['bowel_habits']
            exercise        = fw_nw_form.cleaned_data['exercise']
            present_comp_name       = fw_nw_form.cleaned_data['present_comp_name']
            present_years_worked        = fw_nw_form.cleaned_data['present_years_worked']
            present_job_nature      = fw_nw_form.cleaned_data['present_job_nature']
            previous_comp_name      = fw_nw_form.cleaned_data['previous_comp_name']
            previous_years_worked       = fw_nw_form.cleaned_data['previous_years_worked']
            previous_job_nature     = fw_nw_form.cleaned_data['previous_job_nature']
            exposed_to_occupational_hazards     = fw_nw_form.cleaned_data['exposed_to_occupational_hazards']
            height      = fw_nw_form.cleaned_data['height']
            chest_inspiration       = fw_nw_form.cleaned_data['chest_inspiration']
            abdominal_girth     = fw_nw_form.cleaned_data['abdominal_girth']
            weight      = fw_nw_form.cleaned_data['weight']
            expiration      = fw_nw_form.cleaned_data['expiration']
            bmi     = fw_nw_form.cleaned_data['bmi']
            external_exam       = fw_nw_form.cleaned_data['external_exam']
            squint_nystagmus        = fw_nw_form.cleaned_data['squint_nystagmus']
            colour_vision       = fw_nw_form.cleaned_data['colour_vision']
            without_glasses_re      = fw_nw_form.cleaned_data['without_glasses_re']
            with_glasses_re     = fw_nw_form.cleaned_data['with_glasses_re']
            without_glasses_le      = fw_nw_form.cleaned_data['without_glasses_le']
            with_glasses_le     = fw_nw_form.cleaned_data['with_glasses_le']
            without_glasses_re_near     = fw_nw_form.cleaned_data['without_glasses_re_near']
            with_glasses_re_near        = fw_nw_form.cleaned_data['with_glasses_re_near']
            without_glasses_le_near     = fw_nw_form.cleaned_data['without_glasses_le_near']
            with_glasses_le_near        = fw_nw_form.cleaned_data['with_glasses_le_near']
            built       = fw_nw_form.cleaned_data['built']
            teeth       = fw_nw_form.cleaned_data['teeth']
            throat      = fw_nw_form.cleaned_data['throat']
            tongue      = fw_nw_form.cleaned_data['tongue']
            lymph_nodes     = fw_nw_form.cleaned_data['lymph_nodes']
            pallor      = fw_nw_form.cleaned_data['pallor']
            edema       = fw_nw_form.cleaned_data['edema']
            thyroid     = fw_nw_form.cleaned_data['thyroid']
            tonsils     = fw_nw_form.cleaned_data['tonsils']
            gums        = fw_nw_form.cleaned_data['gums']
            nails       = fw_nw_form.cleaned_data['nails']
            icterus     = fw_nw_form.cleaned_data['icterus']
            pulse       = fw_nw_form.cleaned_data['pulse']
            blood_pressure      = fw_nw_form.cleaned_data['blood_pressure']
            heart_sounds        = fw_nw_form.cleaned_data['heart_sounds']
            peripheral_pulsations       = fw_nw_form.cleaned_data['peripheral_pulsations']
            murmur      = fw_nw_form.cleaned_data['murmur']
            # respiratory_system      = fw_nw_form.cleaned_data['respiratory_system']
            liver       = fw_nw_form.cleaned_data['liver']
            abdominal_lumps     = fw_nw_form.cleaned_data['abdominal_lumps']
            spleen      = fw_nw_form.cleaned_data['spleen']
            # examination_ear_nose_throat     = fw_nw_form.cleaned_data['examination_ear_nose_throat']
            # central_nervous_system      = fw_nw_form.cleaned_data['central_nervous_system']
            skin        = fw_nw_form.cleaned_data['skin']
            remarks     = fw_nw_form.cleaned_data['remarks']
            advice      = fw_nw_form.cleaned_data['advice']
            clubbing      = fw_nw_form.cleaned_data['clubbing']
            ecg      = fw_nw_form.cleaned_data['ecg']
            pulse_stat = fw_nw_form.cleaned_data['pulse_stat']
            higher_function = fw_nw_form.cleaned_data['higher_function']
            sensory_system = fw_nw_form.cleaned_data['sensory_system']
            tendon_reflexes = fw_nw_form.cleaned_data['tendon_reflexes']
            poisture = fw_nw_form.cleaned_data['poisture']
            pshyco_makeup = fw_nw_form.cleaned_data['pshyco_makeup']
            cranial_nerves = fw_nw_form.cleaned_data['cranial_nerves']
            motor_function = fw_nw_form.cleaned_data['motor_function']
            spine = fw_nw_form.cleaned_data['spine']
            gait = fw_nw_form.cleaned_data['gait']
            external_examination = fw_nw_form.cleaned_data['external_examination']
            conversational_hearing = fw_nw_form.cleaned_data['conversational_hearing']
            chest_shape = fw_nw_form.cleaned_data['chest_shape']
            trachea = fw_nw_form.cleaned_data['trachea']
            chest_movements = fw_nw_form.cleaned_data['chest_movements']
            breath_sounds = fw_nw_form.cleaned_data['breath_sounds']
            adventious_sounds = fw_nw_form.cleaned_data['adventious_sounds']
            waist = fw_nw_form.cleaned_data['waist']
            hip = fw_nw_form.cleaned_data['hip']
            # waist_hip_ratio = fw_nw_form.cleaned_data['waist_hip_ratio']
            # short_breath = fw_nw_form.cleaned_data['short_breath']
            # weight_loss = fw_nw_form.cleaned_data['weight_loss']
            # fainting_spells = fw_nw_form.cleaned_data['fainting_spells']
            # freq_headache = fw_nw_form.cleaned_data['freq_headache']
            # chest_pain = fw_nw_form.cleaned_data['chest_pain']
            # hearing_disturb = fw_nw_form.cleaned_data['hearing_disturb']
            # freq_cold = fw_nw_form.cleaned_data['freq_cold']
            # urinary_disturb = fw_nw_form.cleaned_data['urinary_disturb']
            # visual_disturb = fw_nw_form.cleaned_data['visual_disturb']
            # swelling_ankle = fw_nw_form.cleaned_data['swelling_ankle']
            # vertigo = fw_nw_form.cleaned_data['vertigo']
            # joint_pains = fw_nw_form.cleaned_data['joint_pains']

            print("User id from form", self_heartdisease)
       
            if user_id == 999:
                print("New user created")
                (user_obj, created) = models.PatientOverallMedicalDetails.objects.update_or_create(
                    fullname = fullname, 
                    organization= organization, 
                    address=address, 
                    department=department,
                    date=date, 
                    id_mark=id_mark, 
                    gender=gender, 
                    married_stat=married_stat, 
                    desig=desig, 
                    age=age, 
                    dob=dob,  
                    present_complains=present_complains,
                    self_hypertension   = self_hypertension,
                    self_diabetes       = self_diabetes,
                    self_heartdisease   = self_heartdisease,
                    self_tuberculosis   = self_tuberculosis,
                    self_cancer         = self_cancer,
                    self_asthama        = self_asthama,   
                    self_stroke         = self_stroke,
                    self_epilepsy       =   self_epilepsy,
                    father_hypertension = father_hypertension,
                    father_diabetes     =father_diabetes,
                    father_heartdisease =father_heartdisease,
                    father_tuberculosis =father_tuberculosis,
                    father_cancer       =father_cancer,
                    father_asthama      =father_asthama,
                    father_stroke       =father_stroke,
                    father_epilepsy     = father_epilepsy,
                    mother_hypertension =mother_hypertension,
                    mother_diabetes     =mother_diabetes,
                    mother_heartdisease =mother_heartdisease,
                    mother_tuberculosis = mother_tuberculosis,
                    mother_cancer       =mother_cancer,
                    mother_asthama      =mother_asthama,
                    mother_stroke       =mother_stroke,
                    mother_epilepsy     =mother_epilepsy,
                    prev_surgiory   = prev_surgiory,
                    nos_of_child    = nos_of_child,
                    diet    = diet,
                    addictions  = addictions,
                    bowel_habits    = bowel_habits,
                    exercise    = exercise,
                    present_comp_name   = present_comp_name,
                    present_years_worked    = present_years_worked,
                    present_job_nature  = present_job_nature,
                    previous_comp_name  = previous_comp_name,
                    previous_years_worked   = previous_years_worked,
                    previous_job_nature = previous_job_nature,
                    exposed_to_occupational_hazards = exposed_to_occupational_hazards,
                    height  = height,
                    chest_inspiration   = chest_inspiration,
                    abdominal_girth = abdominal_girth,
                    weight  = weight,
                    expiration  = expiration,
                    bmi = bmi,
                    external_exam   = external_exam,
                    squint_nystagmus    = squint_nystagmus,
                    colour_vision   = colour_vision,
                    without_glasses_re  = without_glasses_re,
                    with_glasses_re = with_glasses_re,
                    without_glasses_le  = without_glasses_le,
                    with_glasses_le = with_glasses_le,
                    without_glasses_re_near = without_glasses_re_near,
                    with_glasses_re_near    = with_glasses_re_near,
                    without_glasses_le_near = without_glasses_le_near,
                    with_glasses_le_near    = with_glasses_le_near,
                    built   = built,
                    teeth   = teeth,
                    throat  = throat,
                    tongue  = tongue,
                    lymph_nodes = lymph_nodes,
                    pallor  = pallor,
                    edema   = edema,
                    thyroid = thyroid,
                    tonsils = tonsils,
                    gums    = gums,
                    nails   = nails,
                    icterus = icterus,
                    clubbing = clubbing,
                    ecg = ecg,
                    pulse   = pulse,
                    pulse_stat=pulse_stat,
                    blood_pressure  = blood_pressure,
                    heart_sounds    = heart_sounds,
                    peripheral_pulsations   = peripheral_pulsations,
                    murmur  = murmur,
                    # respiratory_system  = respiratory_system,
                    liver   = liver,
                    abdominal_lumps = abdominal_lumps,
                    spleen  = spleen,
                    # examination_ear_nose_throat = examination_ear_nose_throat,
                    # central_nervous_system  = central_nervous_system,
                    skin    = skin,
                    remarks = remarks,
                    advice  = advice,
                    higher_function = higher_function,
                    sensory_system = sensory_system,
                    tendon_reflexes = tendon_reflexes,
                    poisture = poisture,
                    pshyco_makeup = pshyco_makeup,
                    cranial_nerves = cranial_nerves,
                    motor_function = motor_function,
                    spine = spine,
                    gait = gait,
                    external_examination = external_examination,
                    conversational_hearing = conversational_hearing,
                    chest_shape = chest_shape,
                    trachea = trachea,
                    chest_movements = chest_movements,
                    breath_sounds = breath_sounds,
                    adventious_sounds = adventious_sounds,
                    waist = waist,
                    hip = hip
                    # waist_hip_ratio = waist_hip_ratio,
                    # short_breath = short_breath,
                    # weight_loss = weight_loss,
                    # fainting_spells = fainting_spells,
                    # freq_headache = freq_headache,
                    # chest_pain = chest_pain,
                    # hearing_disturb = hearing_disturb,
                    # freq_cold = freq_cold,
                    # urinary_disturb = urinary_disturb,
                    # visual_disturb = visual_disturb,
                    # swelling_ankle = swelling_ankle,
                    # vertigo = vertigo,
                    # joint_pains = joint_pains

                    )
            else:
                print(" user updated")
                print(user_id)
                (user_obj, created) = models.PatientOverallMedicalDetails.objects.update_or_create(
                    id = user_id, 
                    defaults = 
                    {
                        'fullname' : fullname, 
                        'organization' : organization, 
                        'address':address, 
                        'department':department , 
                        'date':date, 
                        'id_mark':id_mark, 
                        'gender':gender, 
                        'married_stat':married_stat, 
                        'desig':desig, 
                        'age':age, 
                        'dob':dob, 
                        'present_complains':present_complains,
                        'self_hypertension' : self_hypertension,
                        'self_diabetes' : self_diabetes,
                        'self_heartdisease' : self_heartdisease,
                        'self_tuberculosis' : self_tuberculosis,
                        'self_cancer' : self_cancer,
                        'self_asthama' : self_asthama,
                        'self_stroke' : self_stroke,
                        'self_epilepsy'        :self_epilepsy,
                        'father_hypertension' : father_hypertension,
                        'father_diabetes' :father_diabetes,
                        'father_heartdisease' :father_heartdisease,
                        'father_tuberculosis' :father_tuberculosis,
                        'father_cancer' :father_cancer,
                        'father_asthama' :father_asthama,
                        'father_stroke' :father_stroke,
                        'father_epilepsy'      :father_epilepsy,
                        'mother_hypertension' :mother_hypertension,
                        'mother_diabetes' :mother_diabetes,
                        'mother_heartdisease' :mother_heartdisease,
                        'mother_tuberculosis' : mother_tuberculosis,
                        'mother_cancer' :mother_cancer,
                        'mother_asthama' :mother_asthama,
                        'mother_stroke' :mother_stroke,
                        'mother_epilepsy'   :mother_epilepsy,
                        'prev_surgiory' :prev_surgiory,
                        'nos_of_child': nos_of_child,
                        'diet': diet,
                        'addictions': addictions,
                        'bowel_habits': bowel_habits,
                        'exercise': exercise,
                        'present_comp_name': present_comp_name,
                        'present_years_worked': present_years_worked,
                        'present_job_nature': present_job_nature,
                        'previous_comp_name': previous_comp_name,
                        'previous_years_worked': previous_years_worked,
                        'previous_job_nature': previous_job_nature,
                        'exposed_to_occupational_hazards': exposed_to_occupational_hazards,
                        'height': height,
                        'chest_inspiration': chest_inspiration,
                        'abdominal_girth': abdominal_girth,
                        'weight': weight,
                        'expiration': expiration,
                        'bmi': bmi,
                        'external_exam': external_exam,
                        'squint_nystagmus': squint_nystagmus,
                        'colour_vision': colour_vision,
                        'without_glasses_re': without_glasses_re,
                        'with_glasses_re': with_glasses_re,
                        'without_glasses_le': without_glasses_le,
                        'with_glasses_le': with_glasses_le,
                        'without_glasses_re_near': without_glasses_re_near,
                        'with_glasses_re_near': with_glasses_re_near,
                        'without_glasses_le_near': without_glasses_le_near,
                        'with_glasses_le_near': with_glasses_le_near,
                        'built': built,
                        'teeth': teeth,
                        'throat': throat,
                        'tongue': tongue,
                        'lymph_nodes': lymph_nodes,
                        'pallor': pallor,
                        'edema': edema,
                        'thyroid': thyroid,
                        'tonsils': tonsils,
                        'gums': gums,
                        'nails': nails,
                        'icterus': icterus,
                        'clubbing':clubbing,
                        'ecg':ecg,
                        'pulse': pulse,
                        'pulse_stat':pulse_stat,
                        'blood_pressure': blood_pressure,
                        'heart_sounds': heart_sounds,
                        'peripheral_pulsations': peripheral_pulsations,
                        'murmur': murmur,
                        # 'respiratory_system': respiratory_system,
                        'liver': liver,
                        'abdominal_lumps': abdominal_lumps,
                        'spleen': spleen,
                        # 'examination_ear_nose_throat': examination_ear_nose_throat,
                        # 'central_nervous_system': central_nervous_system,
                        'skin': skin,
                        'remarks': remarks,
                        'advice': advice,
                        'higher_function':higher_function,
                        'sensory_system':sensory_system,
                        'tendon_reflexes':tendon_reflexes,
                        'poisture':poisture,
                        'pshyco_makeup':pshyco_makeup,
                        'cranial_nerves':cranial_nerves,
                        'motor_function':motor_function,
                        'spine':spine,
                        'gait':gait,
                        'external_examination':external_examination,
                        'conversational_hearing':conversational_hearing,
                        'chest_shape': chest_shape,
                        'trachea': trachea,
                        'chest_movements': chest_movements,
                        'breath_sounds': breath_sounds,
                        'adventious_sounds': adventious_sounds,
                        'waist':waist,
                        'hip':hip,
                        # 'waist_hip_ratio':waist_hip_ratio,
                        # 'short_breath':short_breath,
                        # 'weight_loss':weight_loss,
                        # 'fainting_spells':fainting_spells,
                        # 'freq_headache':freq_headache,
                        # 'chest_pain':chest_pain,
                        # 'hearing_disturb':hearing_disturb,
                        # 'freq_cold':freq_cold,
                        # 'urinary_disturb':urinary_disturb,
                        # 'visual_disturb':visual_disturb,
                        # 'swelling_ankle':swelling_ankle,
                        # 'vertigo':vertigo,
                        # 'joint_pains':joint_pains
                
                
                        })

            if created:
                messages.success(request, "Users  %s added" % user_obj)
            else:
                messages.success(request, "Users  %s updated" % user_obj)




            return HttpResponseRedirect('/memberinfo/')
        # except Exception,exp:
        #     print("exception")

    def get_initial(self):
        print("inside initial")
        initial = super(AddGeneralDetailsView, self).get_initial()
        try:
            if self.kwargs['user_id']:
                print("id inside initial",self.kwargs['user_id'] )
                patient_obj = models.PatientOverallMedicalDetails.objects.get(id = self.kwargs['user_id'] )
                initial['user_id'] = patient_obj.id
                initial['fullname'] = patient_obj.fullname
                initial['organization'] = patient_obj.organization
                initial['address'] = patient_obj.address
                initial['department'] = patient_obj.department
                initial['date'] = patient_obj.date
                initial['id_mark'] = patient_obj.id_mark
                initial['gender'] = patient_obj.gender
                initial['married_stat'] = patient_obj.married_stat
                initial['desig'] = patient_obj.desig
                initial['age'] = patient_obj.age
                initial['dob'] = patient_obj.dob
                initial['present_complains'] = patient_obj.present_complains
                initial['self_hypertension'] = patient_obj.self_hypertension
                initial['self_diabetes'] = patient_obj.self_diabetes
                initial['self_heartdisease'] = patient_obj.self_heartdisease
                initial['self_tuberculosis'] = patient_obj.self_tuberculosis
                initial['self_cancer'] = patient_obj.self_cancer
                initial['self_asthama'] = patient_obj.self_asthama
                initial['self_stroke'] = patient_obj.self_stroke
                initial['self_epilepsy'] = patient_obj.self_epilepsy
                initial['father_hypertension'] = patient_obj.father_hypertension
                initial['father_diabetes'] = patient_obj.father_diabetes
                initial['father_heartdisease'] = patient_obj.father_heartdisease
                initial['father_tuberculosis'] = patient_obj.father_tuberculosis
                initial['father_cancer'] = patient_obj.father_cancer
                initial['father_asthama'] = patient_obj.father_asthama
                initial['father_stroke'] = patient_obj.father_stroke
                initial['father_epilepsy'] = patient_obj.father_epilepsy
                initial['mother_hypertension'] = patient_obj.mother_hypertension
                initial['mother_diabetes'] = patient_obj.mother_diabetes
                initial['mother_heartdisease'] = patient_obj.mother_heartdisease
                initial['mother_tuberculosis'] = patient_obj.mother_tuberculosis
                initial['mother_cancer'] = patient_obj.mother_cancer
                initial['mother_asthama'] = patient_obj.mother_asthama
                initial['mother_stroke'] = patient_obj.mother_stroke
                initial['mother_epilepsy'] = patient_obj.mother_epilepsy
                initial['prev_surgiory'] = patient_obj.prev_surgiory
                initial['nos_of_child'] = patient_obj.nos_of_child
                initial['diet'] = patient_obj.diet
                print ("Addicct",patient_obj.addictions)
                initial['addictions'] = patient_obj.addictions
                initial['bowel_habits'] = patient_obj.bowel_habits
                initial['exercise'] = patient_obj.exercise
                initial['present_comp_name'] = patient_obj.present_comp_name
                initial['present_years_worked'] = patient_obj.present_years_worked
                initial['present_job_nature'] = patient_obj.present_job_nature
                initial['previous_comp_name'] = patient_obj.previous_comp_name
                initial['previous_years_worked'] = patient_obj.previous_years_worked
                initial['previous_job_nature'] = patient_obj.previous_job_nature
                initial['exposed_to_occupational_hazards'] = patient_obj.exposed_to_occupational_hazards
                initial['height'] = patient_obj.height
                initial['chest_inspiration'] = patient_obj.chest_inspiration
                initial['abdominal_girth'] = patient_obj.abdominal_girth
                initial['weight'] = patient_obj.weight
                initial['expiration'] = patient_obj.expiration
                initial['bmi'] = patient_obj.bmi
                initial['external_exam'] = patient_obj.external_exam
                initial['squint_nystagmus'] = patient_obj.squint_nystagmus
                initial['colour_vision'] = patient_obj.colour_vision
                initial['without_glasses_re'] = patient_obj.without_glasses_re
                initial['with_glasses_re'] = patient_obj.with_glasses_re
                initial['without_glasses_le'] = patient_obj.without_glasses_le
                initial['with_glasses_le'] = patient_obj.with_glasses_le
                initial['without_glasses_re_near'] = patient_obj.without_glasses_re_near
                initial['with_glasses_re_near'] = patient_obj.with_glasses_re_near
                initial['without_glasses_le_near'] = patient_obj.without_glasses_le_near
                initial['with_glasses_le_near'] = patient_obj.with_glasses_le_near
                initial['built'] = patient_obj.built
                initial['teeth'] = patient_obj.teeth
                initial['throat'] = patient_obj.throat
                initial['tongue'] = patient_obj.tongue
                initial['lymph_nodes'] = patient_obj.lymph_nodes
                initial['pallor'] = patient_obj.pallor
                initial['edema'] = patient_obj.edema
                initial['thyroid'] = patient_obj.thyroid
                initial['tonsils'] = patient_obj.tonsils
                initial['gums'] = patient_obj.gums
                initial['nails'] = patient_obj.nails
                initial['icterus'] = patient_obj.icterus
                initial['clubbing'] = patient_obj.clubbing
                initial['ecg'] = patient_obj.ecg
                initial['pulse'] = patient_obj.pulse
                initial['pulse_stat'] = patient_obj.pulse_stat
                initial['blood_pressure'] = patient_obj.blood_pressure
                initial['heart_sounds'] = patient_obj.heart_sounds
                initial['peripheral_pulsations'] = patient_obj.peripheral_pulsations
                initial['murmur'] = patient_obj.murmur
                # initial['respiratory_system'] = patient_obj.respiratory_system
                initial['liver'] = patient_obj.liver
                initial['abdominal_lumps'] = patient_obj.abdominal_lumps
                initial['spleen'] = patient_obj.spleen
                initial['examination_ear_nose_throat'] = patient_obj.examination_ear_nose_throat
                # initial['central_nervous_system'] = patient_obj.central_nervous_system
                initial['skin'] = patient_obj.skin
                initial['remarks'] = patient_obj.remarks
                initial['advice'] = patient_obj.advice
                initial['higher_function'] = patient_obj.higher_function
                initial['sensory_system'] = patient_obj.sensory_system
                initial['tendon_reflexes'] = patient_obj.tendon_reflexes
                initial['poisture'] = patient_obj.poisture
                initial['pshyco_makeup'] = patient_obj.pshyco_makeup
                initial['cranial_nerves'] = patient_obj.cranial_nerves
                initial['motor_function'] = patient_obj.motor_function
                initial['spine'] = patient_obj.spine
                initial['gait'] = patient_obj.gait
                initial['external_examination'] = patient_obj.external_examination
                initial['conversational_hearing'] = patient_obj.conversational_hearing
                initial['chest_shape'] = patient_obj.chest_shape                
                initial['trachea'] = patient_obj.trachea                
                initial['chest_movements'] = patient_obj.chest_movements
                initial['breath_sounds'] = patient_obj.breath_sounds
                initial['adventious_sounds'] = patient_obj.adventious_sounds
                initial['waist'] = patient_obj.waist
                initial['hip'] = patient_obj.hip
                # initial['waist_hip_ratio'] = patient_obj.waist_hip_ratio
                # initial['short_breath'] = patient_obj.short_breath
                # initial['weight_loss'] = patient_obj.weight_loss
                # initial['fainting_spells'] = patient_obj.fainting_spells
                # initial['freq_headache'] = patient_obj.freq_headache
                # initial['chest_pain'] = patient_obj.chest_pain
                # initial['hearing_disturb'] = patient_obj.hearing_disturb
                # initial['freq_cold'] = patient_obj.freq_cold
                # initial['urinary_disturb'] = patient_obj.urinary_disturb
                # initial['visual_disturb'] = patient_obj.visual_disturb
                # initial['swelling_ankle'] = patient_obj.swelling_ankle
                # initial['vertigo'] = patient_obj.vertigo
                # initial['joint_pains'] = patient_obj.joint_pains
                
                
                
                

        
        
        except Exception:
            print()
        return initial

    

    def get_context_data(self, **kwargs):
        print("Inside getcontext")
       
        context = super(AddGeneralDetailsView, self).get_context_data(**kwargs)
        context['member_info'] = models.PatientOverallMedicalDetails.objects.all()
        return context



class Form7View(FormView):
    template_name = 'form7_info.html'
    form_class = Form7AddForm


    def post(self, request, *args, **kwargs):
        
        try:
            c = {}
            c.update(csrf(request))
            forms7 = Form7AddForm(request.POST)
            if not forms7.is_valid():
                variables = {'form': forms7 }
                messages.error(request, 'Invalid data in form')
                return render(request, self.template_name, variables )

            
            form7_id         = forms7.cleaned_data['form7_id']
            patient_name         = forms7.cleaned_data['patient_name']
            
            dept_name        = forms7.cleaned_data['dept_name']
            hazard           = forms7.cleaned_data['hazard']
            danger           = forms7.cleaned_data['danger']
            job              = forms7.cleaned_data['job']
            raw              = forms7.cleaned_data['raw']
            posting_date     = forms7.cleaned_data['posting_date']
            leaving_date     = forms7.cleaned_data['leaving_date']
            discharge_reason = forms7.cleaned_data['discharge_reason']
            discahrge_date   = forms7.cleaned_data['discahrge_date']
            symptons         = forms7.cleaned_data['symptons']
            test_nature      = forms7.cleaned_data['test_nature']
            results          = forms7.cleaned_data['results']
            temp_withdraw    = forms7.cleaned_data['temp_withdraw']
            reason_withdraw  = forms7.cleaned_data['reason_withdraw']
            unfit_date       = forms7.cleaned_data['unfit_date']
            fitness_date     = forms7.cleaned_data['fitness_date']
            date     = forms7.cleaned_data['date']
            # pt_name = forms7.cleaned_data['patient_name'][0]
                   
            if form7_id == 999:
                (form7_obj, created) = models.Form7Details.objects.update_or_create(
                    
                    
                    dept_name=dept_name,
                    hazard=hazard,
                    danger=danger,
                    job=job,
                    raw=raw,
                    posting_date=posting_date,
                    leaving_date=leaving_date,
                    discharge_reason=discharge_reason,
                    discahrge_date=discahrge_date,
                    symptons=symptons,
                    test_nature=test_nature,
                    results=results,
                    temp_withdraw=temp_withdraw,
                    reason_withdraw=reason_withdraw,
                    unfit_date=unfit_date,
                    fitness_date=fitness_date,
                    patient_id_id=patient_name.id,
                    patient_name = patient_name.fullname,
                    date=date
                     

                    )
            else:
                (form7_obj, created) = models.Form7Details.objects.update_or_create(
                    id = form7_id, defaults = 
                {
                    
                    'dept_name':dept_name,
                    'hazard':hazard,
                    'danger':danger,
                    'job':job,
                    'raw':raw,
                    'posting_date':posting_date,
                    'leaving_date':leaving_date,
                    'discharge_reason':discharge_reason,
                    'discahrge_date':discahrge_date,
                    'symptons':symptons,
                    'test_nature':test_nature,
                    'results':results,
                    'temp_withdraw':temp_withdraw,
                    'reason_withdraw':reason_withdraw,
                    'unfit_date':unfit_date,
                    'fitness_date':fitness_date,
                    'patient_id_id':patient_name.id,
                    'patient_name' : patient_name.fullname,
                    'date': date
                
                
                
                 })

            if created:
                messages.success(request, "Users  %s added" % form7_obj.patient_name)
            else:
                messages.success(request, "Users  %s updated" % form7_obj.patient_name)




            return HttpResponseRedirect('/form7/')
        except Exception:
            print("exception")

    def get_initial(self):
        print("inside initial")
        initial = super(Form7View, self).get_initial()
        try:
            if self.kwargs['id']:
                form7_obj = models.Form7Details.objects.get(id = self.kwargs['id'] )
                initial['form7_id']         =form7_obj.id
                initial['dept_name']=form7_obj.dept_name
                initial['hazard']=form7_obj.hazard
                initial['danger']=form7_obj.danger
                initial['job']=form7_obj.job
                initial['raw']=form7_obj.raw
                initial['posting_date']=form7_obj.posting_date
                initial['leaving_date']=form7_obj.leaving_date
                initial['discharge_reason']=form7_obj.discharge_reason
                initial['discahrge_date']=form7_obj.discahrge_date
                initial['symptons']=form7_obj.symptons
                initial['test_nature']=form7_obj.test_nature
                initial['results']=form7_obj.results
                initial['temp_withdraw']=form7_obj.temp_withdraw
                initial['reason_withdraw']=form7_obj.reason_withdraw
                initial['unfit_date']=form7_obj.unfit_date
                initial['fitness_date']=form7_obj.fitness_date
                # initial['patient_id_id'] = form7_obj.patient_id_id
                initial['patient_name']=form7_obj.patient_id_id
                initial['date'] = form7_obj.date


        except Exception:
            print()
        return initial

    

    def get_context_data(self, **kwargs):
        print("Inside getcontext")
       
        context = super(Form7View, self).get_context_data(**kwargs)
        context['form7_info'] = models.Form7Details.objects.all()
        return context


# @login_required
# def edit(request, id):
#     members = models.PatientOverallMedicalDetails.objects.get(id=id)
#     context = {'members': members}
#     return render(request, 'edit.html', context)


class UrineBloodView(FormView):
    template_name = 'urine_blood.html'
    form_class = BloodUrineXRayAddForm


    def post(self, request, *args, **kwargs):
        
        # try:
            c = {}
            c.update(csrf(request))
            blood_uri = BloodUrineXRayAddForm(request.POST)
            if not blood_uri.is_valid():
                variables = {'form': blood_uri }
                messages.error(request, 'Invalid data in form')
                return render(request, self.template_name, variables )

            
            xray_id                      = blood_uri.cleaned_data["xray_id"]  
            patient_name               = blood_uri.cleaned_data["patient_name"]
            date                       = blood_uri.cleaned_data["date"]
            # age                        = blood_uri.cleaned_data["age"]
            # gender                       = blood_uri.cleaned_data["gender"]  
            hb                         = blood_uri.cleaned_data["hb"]
            wbc                        = blood_uri.cleaned_data["wbc"]
            # diff_wb                    = blood_uri.cleaned_data["diff_wb"]
            neutrophils                = blood_uri.cleaned_data["neutrophils"]
            lymphocytes                = blood_uri.cleaned_data["lymphocytes"]
            eosinophils                = blood_uri.cleaned_data["eosinophils"]
            monocytes                  = blood_uri.cleaned_data["monocytes"]
            basophil                   = blood_uri.cleaned_data["basophil"]
            total_rbc                  = blood_uri.cleaned_data["total_rbc"]
            platelet_count             = blood_uri.cleaned_data["platelet_count"]
            esr                        = blood_uri.cleaned_data["esr"]
            rbsl                       = blood_uri.cleaned_data["rbsl"]
            blood_group                  = blood_uri.cleaned_data["blood_group"]          
            urine_colour               = blood_uri.cleaned_data["urine_colour"]
            urine_appearance           = blood_uri.cleaned_data["urine_appearance"]
            urine_odour                = blood_uri.cleaned_data["urine_odour"]
            urine_ph                   = blood_uri.cleaned_data["urine_ph"]
            urine_gravity              = blood_uri.cleaned_data["urine_gravity"]
            urine_deposits             = blood_uri.cleaned_data["urine_deposits"]
            urine_protein              = blood_uri.cleaned_data["urine_protein"]
            urine_sugar                = blood_uri.cleaned_data["urine_sugar"]
            microscopic_pus_cell        = blood_uri.cleaned_data["microscopic_pus_cell"]
            microscopic_epithelial_cell = blood_uri.cleaned_data["microscopic_epithelial_cell"]
            microscopic_rbc_cells       = blood_uri.cleaned_data["microscopic_rbc_cells"]
            microscopic_crystals        = blood_uri.cleaned_data["microscopic_crystals"]
            microscopic_cast            = blood_uri.cleaned_data["microscopic_cast"]
            microscopic_other_findings  = blood_uri.cleaned_data["microscopic_other_findings"]
            xray_view                  = blood_uri.cleaned_data["xray_view"]
            opinion                    = blood_uri.cleaned_data["opinion"]
            # pt_name = blood_uri.cleaned_data['patient_name'][0]
            pt_name= "Sou"
            total_cholesterol  = blood_uri.cleaned_data['total_cholesterol']
            triglycerides  = blood_uri.cleaned_data['triglycerides']
            hdl  = blood_uri.cleaned_data['hdl']
            ldl  = blood_uri.cleaned_data['ldl']
            vldl  = blood_uri.cleaned_data['vldl']
            sgot  = blood_uri.cleaned_data['sgot']
            sgpt  = blood_uri.cleaned_data['sgpt']
            blood_urea  = blood_uri.cleaned_data['blood_urea']
            se_creatinin  = blood_uri.cleaned_data['se_creatinin']
            bilirubin_total  = blood_uri.cleaned_data['bilirubin_total']
            bilirubin_dierct  = blood_uri.cleaned_data['bilirubin_dierct']
            alkaline_phosphatase  = blood_uri.cleaned_data['alkaline_phosphatase']

            uric_acid          = blood_uri.cleaned_data['uric_acid']
            fbsl= blood_uri.cleaned_data['fbsl']
            ppbsl= blood_uri.cleaned_data['ppbsl']
            ldl_hdl_ratio= blood_uri.cleaned_data['ldl_hdl_ratio']
            chol_hdl_ratio= blood_uri.cleaned_data['chol_hdl_ratio']
            total_protein= blood_uri.cleaned_data['total_protein']
            albumin= blood_uri.cleaned_data['albumin']
            globumin= blood_uri.cleaned_data['globumin']
            bilirubin_indierct= blood_uri.cleaned_data['bilirubin_indierct']






            if xray_id == 999:
                (blood_obj, created) = models.BloodUrineXRay.objects.update_or_create(
                    
                    
                    patient_name=patient_name.fullname,
                    patient_id_id                = patient_name.id               ,
                    date                        = date                       ,
                    # age                         = age                        ,
                    # gender                      = gender                     ,
                    hb                          = hb                         ,
                    wbc                         = wbc                        ,
                    # diff_wb                     = diff_wb                    ,
                    neutrophils                 = neutrophils                ,
                    lymphocytes                 = lymphocytes                ,
                    eosinophils                 = eosinophils                ,
                    monocytes                   = monocytes                  ,
                    basophil                    = basophil                   ,
                    total_rbc                   = total_rbc                  ,
                    platelet_count              = platelet_count             ,
                    esr                         = esr                        ,
                    rbsl                        = rbsl                       ,
                    blood_group                 = blood_group                ,
                    urine_colour                = urine_colour               ,
                    urine_appearance            = urine_appearance           ,
                    urine_odour                 = urine_odour                ,
                    urine_ph                    = urine_ph                   ,
                    urine_gravity               = urine_gravity              ,
                    urine_deposits              = urine_deposits             ,
                    urine_protein               = urine_protein              ,
                    urine_sugar                 = urine_sugar                ,
                    microscopic_pus_cell        = microscopic_pus_cell       ,
                    microscopic_epithelial_cell = microscopic_epithelial_cell,
                    microscopic_rbc_cells       = microscopic_rbc_cells      ,
                    microscopic_crystals        = microscopic_crystals       ,
                    microscopic_cast            = microscopic_cast           ,
                    microscopic_other_findings  = microscopic_other_findings ,
                    xray_view                   = xray_view                  ,
                    opinion                     = opinion                    ,
                    total_cholesterol  = total_cholesterol,
                    triglycerides  = triglycerides,
                    hdl  = hdl,
                    ldl  = ldl,
                    vldl  = vldl,
                    sgot  = sgot,
                    sgpt  = sgpt,
                    blood_urea  = blood_urea,
                    se_creatinin  = se_creatinin,
                    bilirubin_total  = bilirubin_total,
                    bilirubin_dierct  = bilirubin_dierct,
                    alkaline_phosphatase  = alkaline_phosphatase,
                    uric_acid = uric_acid,
                    fbsl = fbsl,
                    ppbsl = ppbsl,
                    ldl_hdl_ratio = ldl_hdl_ratio,
                    chol_hdl_ratio = chol_hdl_ratio,
                    total_protein = total_protein,
                    albumin = albumin,
                    globumin = globumin,
                    bilirubin_indierct = bilirubin_indierct, 

                    )
            else:
                (blood_obj, created) = models.BloodUrineXRay.objects.update_or_create(
                    id = xray_id, defaults = 
                {
                    
                    'patient_name':patient_name.fullname,
                    'patient_id_id':patient_name.id               ,               
                    'date':date                       ,                       
                    # 'age':age                        ,                        
                    # 'gender':gender                     ,                     
                    'hb':hb                         ,                         
                    'wbc':wbc                        ,                        
                    # 'diff_wb':diff_wb                    ,                    
                    'neutrophils':neutrophils                ,                
                    'lymphocytes':lymphocytes                ,                
                    'eosinophils':eosinophils                ,                
                    'monocytes':monocytes                  ,                  
                    'basophil':basophil                   ,                   
                    'total_rbc':total_rbc                  ,                  
                    'platelet_count':platelet_count             ,             
                    'esr':esr                        ,                        
                    'rbsl':rbsl                       ,                       
                    'blood_group':blood_group                ,                
                    'urine_colour':urine_colour               ,               
                    'urine_appearance':urine_appearance           ,           
                    'urine_odour':urine_odour                ,                
                    'urine_ph':urine_ph                   ,                   
                    'urine_gravity':urine_gravity              ,              
                    'urine_deposits':urine_deposits             ,             
                    'urine_protein':urine_protein              ,              
                    'urine_sugar':urine_sugar                ,                
                    'microscopic_pus_cell':microscopic_pus_cell       ,       
                    'microscopic_epithelial_cell':microscopic_epithelial_cell,
                    'microscopic_rbc_cells':microscopic_rbc_cells      ,      
                    'microscopic_crystals':microscopic_crystals       ,       
                    'microscopic_cast':microscopic_cast           ,           
                    'microscopic_other_findings':microscopic_other_findings , 
                    'xray_view':xray_view                  ,                  
                    'opinion':opinion                    ,                    
                    'total_cholesterol' : total_cholesterol,
                    'triglycerides' : triglycerides,
                    'hdl' : hdl,
                    'ldl' : ldl,
                    'vldl' : vldl,
                    'sgot' : sgot,
                    'sgpt' : sgpt,
                    'blood_urea' : blood_urea,
                    'se_creatinin' : se_creatinin,
                    'bilirubin_total' : bilirubin_total,
                    'bilirubin_dierct' : bilirubin_dierct,
                    'alkaline_phosphatase' : alkaline_phosphatase,
                    'uric_acid': uric_acid,
                    'fbsl': fbsl,
                    'ppbsl': ppbsl,
                    'ldl_hdl_ratio': ldl_hdl_ratio,
                    'chol_hdl_ratio': chol_hdl_ratio,
                    'total_protein': total_protein,
                    'albumin': albumin,
                    'globumin': globumin,
                    'bilirubin_indierct': bilirubin_indierct,


                
                
                 })

            if created:
                messages.success(request, "%s added" % blood_obj.patient_name)
            else:
                messages.success(request, " %s updated" % blood_obj.patient_name)




            return HttpResponseRedirect('/urine_blood/')
        # except Exception:
        #     print("exception")

    def get_initial(self):
        print("inside initial")
        initial = super(UrineBloodView, self).get_initial()
        try:
            if self.kwargs['id']:
                blood_obj = models.BloodUrineXRay.objects.get(id = self.kwargs['id'] )
                initial['xray_id'] = blood_obj.id
                initial['patient_name'] = blood_obj.patient_id_id
                initial['date'] = blood_obj.date
                # initial['age'] = blood_obj.age
                # initial['gender'] = blood_obj.gender
                initial['hb'] = blood_obj.hb
                initial['wbc'] = blood_obj.wbc
                # initial['diff_wb'] = blood_obj.diff_wb
                initial['neutrophils'] = blood_obj.neutrophils
                initial['lymphocytes'] = blood_obj.lymphocytes
                initial['eosinophils'] = blood_obj.eosinophils
                initial['monocytes'] = blood_obj.monocytes
                initial['basophil'] = blood_obj.basophil
                initial['total_rbc'] = blood_obj.total_rbc
                initial['platelet_count'] = blood_obj.platelet_count
                initial['esr'] = blood_obj.esr
                initial['rbsl'] = blood_obj.rbsl
                initial['blood_group'] = blood_obj.blood_group
                initial['urine_colour'] = blood_obj.urine_colour
                initial['urine_appearance'] = blood_obj.urine_appearance
                initial['urine_odour'] = blood_obj.urine_odour
                initial['urine_ph'] = blood_obj.urine_ph
                initial['urine_gravity'] = blood_obj.urine_gravity
                initial['urine_deposits'] = blood_obj.urine_deposits
                initial['urine_protein'] = blood_obj.urine_protein
                initial['urine_sugar'] = blood_obj.urine_sugar
                initial['microscopic_pus_cell'] = blood_obj.microscopic_pus_cell
                initial['microscopic_epithelial_cell'] = blood_obj.microscopic_epithelial_cell
                initial['microscopic_rbc_cells'] = blood_obj.microscopic_rbc_cells
                initial['microscopic_crystals'] = blood_obj.microscopic_crystals
                initial['microscopic_cast'] = blood_obj.microscopic_cast
                initial['microscopic_other_findings'] = blood_obj.microscopic_other_findings
                initial['xray_view'] = blood_obj.xray_view
                initial['opinion'] = blood_obj.opinion
                initial['total_cholesterol'] = blood_obj.total_cholesterol
                initial['triglycerides'] = blood_obj.triglycerides
                initial['hdl'] = blood_obj.hdl
                initial['ldl'] = blood_obj.ldl
                initial['vldl'] = blood_obj.vldl
                initial['sgot'] = blood_obj.sgot
                initial['sgpt'] = blood_obj.sgpt
                initial['blood_urea'] = blood_obj.blood_urea
                initial['se_creatinin'] = blood_obj.se_creatinin
                initial['bilirubin_total'] = blood_obj.bilirubin_total
                initial['bilirubin_dierct'] = blood_obj.bilirubin_dierct
                initial['alkaline_phosphatase'] = blood_obj.alkaline_phosphatase
                initial['uric_acid'] = blood_obj.uric_acid
                initial['fbsl'] = blood_obj.fbsl
                initial['ppbsl'] = blood_obj.ppbsl
                initial['ldl_hdl_ratio'] = blood_obj.ldl_hdl_ratio
                initial['chol_hdl_ratio'] = blood_obj.chol_hdl_ratio
                initial['total_protein'] = blood_obj.total_protein
                initial['albumin'] = blood_obj.albumin
                initial['globumin'] = blood_obj.globumin
                initial['bilirubin_indierct'] = blood_obj.bilirubin_indierct


        except Exception:
            print()
        return initial

    

    def get_context_data(self, **kwargs):
        print("Inside getcontext")
       
        context = super(UrineBloodView, self).get_context_data(**kwargs)
        context['blood_info'] = models.BloodUrineXRay.objects.all()
        print("get context",context)
        return context


class StollView(FormView):
    template_name = 'stool_report.html'
    form_class = StoolReportAddForm


    def post(self, request, *args, **kwargs):
        
        # try:
            c = {}
            c.update(csrf(request))
            stool_form = StoolReportAddForm(request.POST)
            if not stool_form.is_valid():
                variables = {'form': stool_form }
                messages.error(request, 'Invalid data in form')
                return render(request, self.template_name, variables )

            

            stool_id        = stool_form.cleaned_data['stool_id']
            patient_name        = stool_form.cleaned_data['patient_name']
            date        = stool_form.cleaned_data['date']
            # age     = stool_form.cleaned_data['age']
            # gender      = stool_form.cleaned_data['gender']
            colour      = stool_form.cleaned_data['colour']
            consistency     = stool_form.cleaned_data['consistency']
            mucus       = stool_form.cleaned_data['mucus']
            parasites       = stool_form.cleaned_data['parasites']
            frank_blood     = stool_form.cleaned_data['frank_blood']
            occult_blood        = stool_form.cleaned_data['occult_blood']
            # stercobilinogen     = stool_form.cleaned_data['stercobilinogen']
            reaction_pH     = stool_form.cleaned_data['reaction_pH']
            microscope_epithelial_cells     = stool_form.cleaned_data['microscope_epithelial_cells']
            microscope_pus_cells        = stool_form.cleaned_data['microscope_pus_cells']
            microscope_rbs_cells        = stool_form.cleaned_data['microscope_rbs_cells']
            microscope_protozoa     = stool_form.cleaned_data['microscope_protozoa']
            microscope_ova      = stool_form.cleaned_data['microscope_ova']
            microscope_other_findings       = stool_form.cleaned_data['microscope_other_findings']
            widal_salmonella_O      = stool_form.cleaned_data['widal_salmonella_O']
            widal_salmonella_H      = stool_form.cleaned_data['widal_salmonella_H']
            widal_salmonella_AH     = stool_form.cleaned_data['widal_salmonella_AH']
            widal_salmonella_BH     = stool_form.cleaned_data['widal_salmonella_BH']

            hep_A               = stool_form.cleaned_data['hep_A']
            hep_B               = stool_form.cleaned_data['hep_B']
            hep_C               = stool_form.cleaned_data['hep_C']
            vdrl                = stool_form.cleaned_data['vdrl']
            hiv1                = stool_form.cleaned_data['hiv1']
            hiv2                = stool_form.cleaned_data['hiv2']
            sputum                = stool_form.cleaned_data['sputum']
            
            # pt_name = stool_form.cleaned_data['patient_name'][0]
            pt_name = "Sou"
            print(patient_name.id)
                   
            if stool_id == 999:
                (stool_obj, created) = models.StoolReport.objects.update_or_create(
                    
                        patient_name= patient_name.fullname,
                        patient_id_id      = patient_name.id,
                        date      = date,
                        # age      = age,
                        # gender      = gender,
                        colour      = colour,
                        consistency      = consistency,
                        mucus      = mucus,
                        parasites      = parasites,
                        frank_blood      = frank_blood,
                        occult_blood      = occult_blood,
                        # stercobilinogen      = stercobilinogen,
                        reaction_pH      = reaction_pH,
                        microscope_epithelial_cells      = microscope_epithelial_cells,
                        microscope_pus_cells      = microscope_pus_cells,
                        microscope_rbs_cells      = microscope_rbs_cells,
                        microscope_protozoa      = microscope_protozoa,
                        microscope_ova      = microscope_ova,
                        microscope_other_findings      = microscope_other_findings,
                        widal_salmonella_O      = widal_salmonella_O,
                        widal_salmonella_H      = widal_salmonella_H,
                        widal_salmonella_AH      = widal_salmonella_AH,
                        widal_salmonella_BH      = widal_salmonella_BH,
                        hep_A           = hep_A,
                        hep_B           = hep_B,
                        hep_C           = hep_C,
                        vdrl           = vdrl,
                        hiv1           = hiv1,
                        hiv2           = hiv2,
                        sputum           = sputum,
                    
                    

                    )
            else:
                (stool_obj, created) = models.StoolReport.objects.update_or_create(
                    id = stool_id, defaults = 
                {
                    'patient_name':patient_name.fullname,
                    'patient_id_id':patient_name.id,
                    'date':date,
                    # 'age':age,
                    # 'gender':gender,
                    'colour':colour,
                    'consistency':consistency,
                    'mucus':mucus,
                    'parasites':parasites,
                    'frank_blood':frank_blood,
                    'occult_blood':occult_blood,
                    # 'stercobilinogen':stercobilinogen,
                    'reaction_pH':reaction_pH,
                    'microscope_epithelial_cells':microscope_epithelial_cells,
                    'microscope_pus_cells':microscope_pus_cells,
                    'microscope_rbs_cells':microscope_rbs_cells,
                    'microscope_protozoa':microscope_protozoa,
                    'microscope_ova':microscope_ova,
                    'microscope_other_findings':microscope_other_findings,
                    'widal_salmonella_O':widal_salmonella_O,
                    'widal_salmonella_H':widal_salmonella_H,
                    'widal_salmonella_AH':widal_salmonella_AH,
                    'widal_salmonella_BH':widal_salmonella_BH,
                    'hep_A' : hep_A,
                    'hep_B' : hep_B,
                    'hep_C' : hep_C,
                    'vdrl' : vdrl,
                    'hiv1' : hiv1,
                    'hiv2' : hiv2,
                    'sputum' : sputum,
               
                
                
                
                 })

            if created:
                messages.success(request, "%s added" % stool_obj.patient_name)
            else:
                messages.success(request, " %s updated" % stool_obj.patient_name)




            return HttpResponseRedirect('/stool_form/')
        # except Exception:
            # print("exception")

    def get_initial(self):
        print("inside initial")
        initial = super(StollView, self).get_initial()
        try:
            if self.kwargs['id']:
                stool_obj = models.StoolReport.objects.get(id = self.kwargs['id'] )
                initial['stool_id'] = stool_obj.id
                initial['patient_name']=stool_obj.patient_id_id
                initial['date']=stool_obj.date
                # initial['age']=stool_obj.age
                # initial['gender']=stool_obj.gender
                initial['colour']=stool_obj.colour
                initial['consistency']=stool_obj.consistency
                initial['mucus']=stool_obj.mucus
                initial['parasites']=stool_obj.parasites
                initial['frank_blood']=stool_obj.frank_blood
                initial['occult_blood']=stool_obj.occult_blood
                # initial['stercobilinogen']=stool_obj.stercobilinogen
                initial['reaction_pH']=stool_obj.reaction_pH
                initial['microscope_epithelial_cells']=stool_obj.microscope_epithelial_cells
                initial['microscope_pus_cells']=stool_obj.microscope_pus_cells
                initial['microscope_rbs_cells']=stool_obj.microscope_rbs_cells
                initial['microscope_protozoa']=stool_obj.microscope_protozoa
                initial['microscope_ova']=stool_obj.microscope_ova
                initial['microscope_other_findings']=stool_obj.microscope_other_findings
                initial['widal_salmonella_O']=stool_obj.widal_salmonella_O
                initial['widal_salmonella_H']=stool_obj.widal_salmonella_H
                initial['widal_salmonella_AH']=stool_obj.widal_salmonella_AH
                initial['widal_salmonella_BH']=stool_obj.widal_salmonella_BH
                initial['hep_A'] = stool_obj.hep_A
                initial['hep_B'] = stool_obj.hep_B
                initial['hep_C'] = stool_obj.hep_C
                initial['vdrl'] = stool_obj.vdrl
                initial['hiv1'] = stool_obj.hiv1
                initial['hiv2'] = stool_obj.hiv2
                initial['sputum'] = stool_obj.sputum

        except Exception:
            print()
        return initial

    

    def get_context_data(self, **kwargs):
        print("Inside getcontext")
       
        context = super(StollView, self).get_context_data(**kwargs)
        context['stool_info'] = models.StoolReport.objects.all()
        return context




class AudioView(FormView):
    template_name = 'audio_report.html'
    form_class = AudiometryAddForm


    def post(self, request, *args, **kwargs):
        
        # try:
            c = {}
            c.update(csrf(request))
            audio_form = AudiometryAddForm(request.POST)
            if not audio_form.is_valid():
                variables = {'form': audio_form }
                messages.error(request, 'Invalid data in form')
                return render(request, self.template_name, variables )

            

            audio_id        = audio_form.cleaned_data['audio_id']
            patient_name    = audio_form.cleaned_data['patient_name']
            date            = audio_form.cleaned_data['date']
            le_ear_125      = audio_form.cleaned_data['le_ear_125']
            le_ear_250      = audio_form.cleaned_data['le_ear_250']
            le_ear_500      = audio_form.cleaned_data['le_ear_500']
            le_ear_1K       = audio_form.cleaned_data['le_ear_1K']
            le_ear_2K       = audio_form.cleaned_data['le_ear_2K']
            le_ear_4K       = audio_form.cleaned_data['le_ear_4K']
            le_ear_6K       = audio_form.cleaned_data['le_ear_6K']
            le_ear_8K       = audio_form.cleaned_data['le_ear_8K']
            re_ear_125      = audio_form.cleaned_data['re_ear_125']
            re_ear_250      = audio_form.cleaned_data['re_ear_250']
            re_ear_500      = audio_form.cleaned_data['re_ear_500']
            re_ear_1K       = audio_form.cleaned_data['re_ear_1K']
            re_ear_2K       = audio_form.cleaned_data['re_ear_2K']
            re_ear_4K       = audio_form.cleaned_data['re_ear_4K']
            re_ear_6K       = audio_form.cleaned_data['re_ear_6K']
            re_ear_8K       = audio_form.cleaned_data['re_ear_8K']
            bone_le_ear_250 = audio_form.cleaned_data['bone_le_ear_250'] 
            bone_le_ear_500 = audio_form.cleaned_data['bone_le_ear_500']
            bone_le_ear_1K = audio_form.cleaned_data['bone_le_ear_1K']
            bone_le_ear_2K = audio_form.cleaned_data['bone_le_ear_2K']
            bone_le_ear_4K = audio_form.cleaned_data['bone_le_ear_4K']
            bone_re_ear_250 = audio_form.cleaned_data['bone_re_ear_250']
            bone_re_ear_500 = audio_form.cleaned_data['bone_re_ear_500']
            bone_re_ear_1K = audio_form.cleaned_data['bone_re_ear_1K']
            bone_re_ear_2K = audio_form.cleaned_data['bone_re_ear_2K']
            bone_re_ear_4K = audio_form.cleaned_data['bone_re_ear_4K']


            if audio_id == 999:
                (audio_obj, created) = models.Audiometry.objects.update_or_create(
                    
                    patient_name   = patient_name,
                    date   = date,
                    le_ear_125   = le_ear_125,
                    le_ear_250   = le_ear_250,
                    le_ear_500   = le_ear_500,
                    le_ear_1K   = le_ear_1K,
                    le_ear_2K   = le_ear_2K,
                    le_ear_4K   = le_ear_4K,
                    le_ear_6K   = le_ear_6K,
                    le_ear_8K   = le_ear_8K,
                    re_ear_125   = re_ear_125,
                    re_ear_250   = re_ear_250,
                    re_ear_500   = re_ear_500,
                    re_ear_1K   = re_ear_1K,
                    re_ear_2K   = re_ear_2K,
                    re_ear_4K   = re_ear_4K,
                    re_ear_6K   = re_ear_6K,
                    re_ear_8K   = re_ear_8K,
                    bone_le_ear_250 = bone_le_ear_250,
                    bone_le_ear_500 = bone_le_ear_500,
                    bone_le_ear_1K = bone_le_ear_1K,
                    bone_le_ear_2K = bone_le_ear_2K,
                    bone_le_ear_4K = bone_le_ear_4K,
                    bone_re_ear_250 = bone_re_ear_250,
                    bone_re_ear_500 = bone_re_ear_500,
                    bone_re_ear_1K = bone_re_ear_1K,
                    bone_re_ear_2K = bone_re_ear_2K,
                    bone_re_ear_4K = bone_re_ear_4K,
                    
                    
                    )
            else:
                (audio_obj, created) = models.Audiometry.objects.update_or_create(
                    id = audio_id, defaults = 
                {
                    'patient_name'  : patient_name,
                    'date'  : date,
                    'le_ear_125'  : le_ear_125,
                    'le_ear_250'  : le_ear_250,
                    'le_ear_500'  : le_ear_500,
                    'le_ear_1K'  : le_ear_1K,
                    'le_ear_2K'  : le_ear_2K,
                    'le_ear_4K'  : le_ear_4K,
                    'le_ear_6K'  : le_ear_6K,
                    'le_ear_8K'  : le_ear_8K,
                    're_ear_125'  : re_ear_125,
                    're_ear_250'  : re_ear_250,
                    're_ear_500'  : re_ear_500,
                    're_ear_1K'  : re_ear_1K,
                    're_ear_2K'  : re_ear_2K,
                    're_ear_4K'  : re_ear_4K,
                    're_ear_6K'  : re_ear_6K,
                    're_ear_8K'  : re_ear_8K,
                    'bone_le_ear_250':bone_le_ear_250,
                    'bone_le_ear_500':bone_le_ear_500,
                    'bone_le_ear_1K':bone_le_ear_1K,
                    'bone_le_ear_2K':bone_le_ear_2K,
                    'bone_le_ear_4K':bone_le_ear_4K,
                    'bone_re_ear_250':bone_re_ear_250,
                    'bone_re_ear_500':bone_re_ear_500,
                    'bone_re_ear_1K':bone_re_ear_1K,
                    'bone_re_ear_2K':bone_re_ear_2K,
                    'bone_re_ear_4K':bone_re_ear_4K,
            
            
                  })

            if created:
                messages.success(request, "%s added" % audio_obj.patient_name)
            else:
                messages.success(request, " %s updated" % audio_obj.patient_name)




            return HttpResponseRedirect('/audio_form/')
        # except Exception:
            # print("exception")

    def get_initial(self):
        print("inside initial")
        initial = super(AudioView, self).get_initial()
        try:
            if self.kwargs['id']:
                audio_obj = models.Audiometry.objects.get(id = self.kwargs['id'] )
                initial['audio_id'] = audio_obj.id
                initial['patient_name']=audio_obj.patient_name_id
                initial['date']=audio_obj.date          
                initial['le_ear_125'] = audio_obj.le_ear_125
                initial['le_ear_250'] = audio_obj.le_ear_250
                initial['le_ear_500'] = audio_obj.le_ear_500
                initial['le_ear_1K'] = audio_obj.le_ear_1K
                initial['le_ear_2K'] = audio_obj.le_ear_2K
                initial['le_ear_4K'] = audio_obj.le_ear_4K
                initial['le_ear_6K'] = audio_obj.le_ear_6K
                initial['le_ear_8K'] = audio_obj.le_ear_8K
                initial['re_ear_125'] = audio_obj.re_ear_125
                initial['re_ear_250'] = audio_obj.re_ear_250
                initial['re_ear_500'] = audio_obj.re_ear_500
                initial['re_ear_1K'] = audio_obj.re_ear_1K
                initial['re_ear_2K'] = audio_obj.re_ear_2K
                initial['re_ear_4K'] = audio_obj.re_ear_4K
                initial['re_ear_6K'] = audio_obj.re_ear_6K
                initial['re_ear_8K'] = audio_obj.re_ear_8K
                initial['bone_le_ear_250'] = audio_obj.bone_le_ear_250
                initial['bone_le_ear_500'] = audio_obj.bone_le_ear_500
                initial['bone_le_ear_1K'] = audio_obj.bone_le_ear_1K
                initial['bone_le_ear_2K'] = audio_obj.bone_le_ear_2K
                initial['bone_le_ear_4K'] = audio_obj.bone_le_ear_4K
                initial['bone_re_ear_250'] = audio_obj.bone_re_ear_250
                initial['bone_re_ear_500'] = audio_obj.bone_re_ear_500
                initial['bone_re_ear_1K'] = audio_obj.bone_re_ear_1K
                initial['bone_re_ear_2K'] = audio_obj.bone_re_ear_2K
                initial['bone_re_ear_4K'] = audio_obj.bone_re_ear_4K

        except Exception:
            print()
        return initial

    

    def get_context_data(self, **kwargs):
        print("Inside getcontext")
       
        context = super(AudioView, self).get_context_data(**kwargs)
        context['audio_info'] = models.Audiometry.objects.all()
        return context


class ReportView(FormView):
    template_name = 'report.html'
    form_class = ReportsForm


    def post(self, request, *args, **kwargs):
        
        # try:
            c = {}
            c.update(csrf(request))
            report_form = ReportsForm(request.POST)
            # if not report_form.is_valid():
            #     variables = {'form': report_form }
            #     messages.error(request, 'Invalid data in form')
            #     return render(request, self.template_name, variables )
            
            if request.POST['from_date'] and request.POST['to_date']:
                from_date = request.POST['from_date']
                to_date = request.POST['to_date']
            
                
                from_date = datetime.datetime.strptime(from_date,'%m/%d/%Y')
                from_date = datetime.datetime.strptime(str(from_date),'%Y-%m-%d %H:%M:%S')

                to_date = datetime.datetime.strptime(to_date,'%m/%d/%Y')
                to_date = datetime.datetime.strptime(str(to_date),'%Y-%m-%d %H:%M:%S')

                # to_date = datetime.datetime.strptime('%m/%d/%Y',to_date)
                patient_res = models.PatientOverallMedicalDetails.objects.filter(Q(date__gte=from_date) & Q(date__lte=to_date))
                blood_from_to = models.BloodUrineXRay.objects.filter(Q(date__gte=from_date) & Q(date__lte=to_date))
                stool_from_to = models.StoolReport.objects.filter(Q(date__gte=from_date) & Q(date__lte=to_date))
                form7_from_to = models.Form7Details.objects.filter(Q(date__gte=from_date) & Q(date__lte=to_date))
                audio_from_to = models.Audiometry.objects.filter(Q(date__gte=from_date) & Q(date__lte=to_date))

                data={
                    'patient_res':patient_res,
                    'blood_from_to':blood_from_to,
                    'stool_from_to':stool_from_to,
                    'form7_from_to':form7_from_to,
                    'audio_from_to':audio_from_to,
                    'form':ReportsForm()
                }

            if request.POST['company_name']:
                blood_res = []
                stool_res = []
                form7_res = []
                audio_res = []

                company_name = request.POST['company_name']
                patient_res = models.PatientOverallMedicalDetails.objects.filter(organization=company_name)
                for pt in patient_res:
                    print("patient obj",pt)
                    blood_res.append(models.BloodUrineXRay.objects.filter(patient_id=pt))
                    stool_res.append(models.StoolReport.objects.filter(patient_id=pt))
                    form7_res.append(models.Form7Details.objects.filter(patient_id=pt))
                    audio_res.append(models.Audiometry.objects.filter(patient_name_id=pt))

                data={
                    'patient_res':patient_res,
                    'blood_res':blood_res,
                    'stool_res':stool_res,
                    'form7_res':form7_res,
                    'audio_res':audio_res,
                    'form':ReportsForm()
                }
                print("data",blood_res)

                # return render(request,self.template_name,data)

            

            if request.POST['from_date'] and request.POST['to_date'] and request.POST['company_name']: 
                
                blood_res = []
                stool_res = []
                form7_res = []
                audio_res = []
                
                from_date = datetime.datetime.strptime(from_date,'%m/%d/%Y')
                from_date = datetime.datetime.strptime(str(from_date),'%Y-%m-%d %H:%M:%S')

                to_date = datetime.datetime.strptime(to_date,'%m/%d/%Y')
                to_date = datetime.datetime.strptime(str(to_date),'%Y-%m-%d %H:%M:%S')
                patient_res = models.PatientOverallMedicalDetails.objects.filter(Q(date__gte=from_date) & Q(date__lte=to_date) | Q(organization=company_name))
                for pt in patient_res:
                    blood_res.append(models.BloodUrineXRay.objects.filter(Q(date__gte=from_date) & Q(date__lte=to_date) | Q(patient_id=pt)))
                    stool_res.append(models.StoolReport.objects.filter(Q(date__gte=from_date) & Q(date__lte=to_date) | Q(patient_id=pt)))
                    form7_res.append(models.Form7Details.objects.filter(Q(date__gte=from_date) & Q(date__lte=to_date) | Q(patient_id=pt)))
                    audio_res.append(models.Audiometry.objects.filter(Q(date__gte=from_date) & Q(date__lte=to_date) | Q(patient_id=pt)))
                
                
                data={
                    'patient_res':patient_res,
                    'blood_res':blood_res,
                    'stool_res' : stool_res,
                    'form7_res' : form7_res,
                    'audio_res' : audio_res,
                    'form':ReportsForm()
                }
                
            
            

            return render(request,self.template_name,data)
        # except Exception:
            # print("exception")

    def get_context_data(self, **kwargs):
        print("Inside getcontext")
       
        context = super(ReportView, self).get_context_data(**kwargs)
        context['form'] = ReportsForm()
        return context





@login_required
def member_delete(request, user_id):
    member = models.PatientOverallMedicalDetails.objects.get(id=user_id)
    member.delete()
    messages.error(request, "Users  %s deleted" % member)
    return redirect('/memberinfo/')

@login_required
def form7_delete(request, id):
    member = models.Form7Details.objects.get(id=id)
    member.delete()
    messages.error(request, "  %s deleted" % member.patient_name)
    return redirect('/form7/')

@login_required
def urine_blood_delete(request, id):
    member = models.BloodUrineXRay.objects.get(id=id)
    member.delete()
    messages.error(request, "  %s deleted" % member.patient_name)
    return redirect('/urine_blood/')


@login_required
def stool_delete(request, id):
    member = models.StoolReport.objects.get(id=id)
    member.delete()
    messages.error(request, "  %s deleted" % member.patient_name)
    return redirect('/stool_form/')

@login_required
def audio_delete(request, id):
    member = models.Audiometry.objects.get(id=id)
    member.delete()
    messages.error(request, "  %s deleted" % member.patient_name)
    return redirect('/audio_form/')