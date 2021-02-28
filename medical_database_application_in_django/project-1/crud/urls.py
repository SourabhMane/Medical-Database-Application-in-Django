from . import views
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.AddGeneralDetailsView.as_view(), name='index'),
    url(r'^pdf/$', views.GenerateMedicalPdf.as_view(), name='pdf'),
    url(r'^pdf/(?P<patient_id>[0-9]{1,10})/$', views.GenerateMedicalPdf.as_view(), name='pdf'),
    url(r'^pdf/blood/(?P<blood_id>[0-9]{1,10})/$', views.GenerateBloodPdf.as_view(), name='pdf_blood'),
    url(r'^pdf/form7/(?P<form7_id>[0-9]{1,10})/$', views.GenerateForm7Pdf.as_view(), name='pdf_form7'),
    url(r'^pdf/stool/(?P<stool_id>[0-9]{1,10})/$', views.GenerateStoolPdf.as_view(), name='pdf_stool'),

    url(r'^graph/(?P<id>[0-9]{1,10})/$', views.GenerateGraph.as_view(), name='graph'),


    url(r'^django_admin/', admin.site.urls),

    url(r'^memberinfo/$', views.AddGeneralDetailsView.as_view(), name='member_list'),
    url(r'^memberinfo/(?P<user_id>[0-9]{1,10})/$', views.AddGeneralDetailsView.as_view(), name='member_list'),
    url(r'^memberinfo/(?P<user_id>[0-9]{1,10})/delete/$', views.member_delete, name='delete_member'),
    
    url(r'^form7/$', views.Form7View.as_view(), name='form7_list'),
    url(r'^form7/(?P<id>[0-9]{1,10})/$', views.Form7View.as_view(), name='form7_list'),
    url(r'^form7/(?P<id>[0-9]{1,10})/delete/$', views.form7_delete, name='form7_delete'),
    
    url(r'^urine_blood/$', views.UrineBloodView.as_view(), name='urine_blood_list'),
    url(r'^urine_blood/(?P<id>[0-9]{1,10})/$', views.UrineBloodView.as_view(), name='urine_blood_list'),
    url(r'^urine_blood/(?P<id>[0-9]{1,10})/delete/$', views.urine_blood_delete, name='urine_blood_delete'),
    
    url(r'^stool_form/$', views.StollView.as_view(), name='stool_form_list'),
    url(r'^stool_form/(?P<id>[0-9]{1,10})/$', views.StollView.as_view(), name='stool_form_list'),
    url(r'^stool_form/(?P<id>[0-9]{1,10})/delete/$', views.stool_delete, name='stool_delete'),
   
    url(r'^audio_form/$', views.AudioView.as_view(), name='audio_form_list'),
    url(r'^audio_form/(?P<id>[0-9]{1,10})/$', views.AudioView.as_view(), name='audio_form_list'),
    url(r'^audio_form/(?P<id>[0-9]{1,10})/delete/$', views.audio_delete, name='audio_delete'),

    url(r'^reports/$', views.ReportView.as_view(), name='report'),

    # url(r'^fileupload$', views.fileupload, name='fileupload'),
    # # url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    # url(r'^ajax/$', views.ajax, name='ajax'),
    # url(r'^ajax/ajax$', views.ajax, name='ajaxpost'),
    # url(r'^ajax/delete$', views.ajax_delete, name='ajax_delete'),
    # url(r'^ajax/getajax$', views.getajax, name='getajax'),
    # url(r'^register/$', views.register,name='register'),
    # url(r'^register/success/$',views.register_success,name='register_success'),
    # url(r'^users/$',views.users,name='users'),
    # url(r'^users/delete/(?P<id>\d+)$', views.user_delete, name='user_delete'),
    # url(r'^upload/csv/$', views.upload_csv, name='upload_csv'),
    # url(r'^change_password$', views.changePassword, name='changePassword'),
    #url(r'^file/delete$', views.changePassword, name='changePassword'),
    #url(r'^file/delete/(?P<id>\d+)$', views.deleteFiles, name='deleteFiles'),
]