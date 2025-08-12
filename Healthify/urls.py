from django.urls import path

from Healthify import views

urlpatterns=[


    #admin

    path('admin_hm',views.admin_hm,name='admin_hm'),



    path('admin_add_diet_plan',views.admin_add_diet_plan,name='admin_add_diet_plan'),



    # path('post_diet_plan',views.post_diet_plan,name='post_diet_plan'),


    path('logout',views.logout,name='logout'),


    path('login_code',views.login_code, name='login_code'),


    path('admin_accept_hsptl/<int:id>', views.admin_accept_hsptl, name='admin_accept_hsptl'),

    path('admin_reject_hs/<int:id>',views.admin_reject_hs,name='admin_reject_hs'),
    path('',views.admin_lgn,name='admin_lgn'),
    path('admin_verify_hsptl', views.admin_verify_hsptl, name='admin_verify_hsptl'),
    path('admin_acpt_hs_doc', views.admin_acpt_hs_doc, name='admin_acpt_hs_doc'),
    path('admin_acpt_hs_doc_search', views.admin_acpt_hs_doc_search, name='admin_acpt_hs_doc_search'),
    path('admin_view_bookings/<int:hid>', views.admin_view_bookings, name='admin_view_bookings'),

    path('admin_view_dctr/<int:id>', views.admin_view_dctr, name='admin_view_dctr'),

    path('admin_view_complaints', views.admin_view_complaints, name='admin_view_complaints'),
    path('add_diet_chart_post', views.add_diet_chart_post, name='add_diet_chart_post'),


    path('view_diet_charts', views.view_diet_charts, name='view_diet_charts'),

    path('predict_diet', views.predict_diet, name='predict_diet'),



    path('admin_complaints_reply/<id>', views.admin_complaints_reply, name='admin_complaints_reply'),










    ###################################################doctor##################################################################










    path('doc_dash', views.doc_dash, name='doc_dash'),
    path('doc_view_prf', views.doc_view_prf, name='doc_view_prf'),
    path('doc_edit_prf', views.doc_edit_prf, name='doc_edit_prf'),
    path('doc_editprof', views.doc_editprof, name='doc_editprof'),
    path('doc_view_rvw', views.doc_view_rvw, name='doc_view_rvw'),
    path('doc_view_sc', views.doc_view_sc, name='doc_view_sc'),
    path('doc_view_bookings/<id>', views.doc_view_bookings, name='doc_view_bookings'),
    path('doc_pres', views.doc_pres, name='doc_pres'),
    path('doc_add_prescription/<id>', views.doc_add_prescription, name='doc_add_prescription'),
    path('doc_add_pre', views.doc_add_pre, name='doc_add_pre'),
    # path('doc_re_pres/<id>',views.doc_re_pres,name='doc_re_pres'),
    path('doc_ch', views.doc_ch, name='doc_ch'),
    path('doc_ch_change', views.doc_ch_change, name='doc_ch_change'),

    path('doc_view_past_pres/<id>', views.doc_view_past_pres, name='doc_view_past_pres'),












    #############################hospital      Web###################################################################################################















    path('delete_dr/<int:id>', views.delete_dr, name='delete_dr'),


    path('edit_dr/<int:id>', views.edit_dr, name='edit_dr'),
    path('editdoctor',views.editdoctor,name='editdoctor'),

    path('hs_ch',views.hs_ch,name='hs_ch'),
    path('hs_ch_change',views.hs_ch_change,name='hs_ch_change'),
    path('hs_dash', views.hs_dash, name='hs_dash'),
    path('hs_log', views.hs_log, name='hs_log'),

    path('hs_mng_dr_sc/<id>', views.hs_mng_dr_sc,name='hs_mng_dr_sc'),




    path('hs_add_dr_sc',views.hs_add_dr_sc,name='hs_add_dr_sc'),
    path('hs_add_dr_sc_post',views.hs_add_dr_sc_post,name='hs_add_dr_sc_post'),
    path('hs_mng_dctr',views.hs_mng_dctr,name='hs_mng_dctr'),

    path('hs_reg',views.hs_reg,name='hs_reg'),




    path('hs_reg_post',views.hs_reg_post,name='hs_reg_post'),
    path('hs_viewbk/<id>',views.hs_viewbk,name='hs_viewbk'),
    path('hs_view__bk/<id>',views.hs_view__bk,name='hs_view__bk'),

    path('check_bookings',views.check_bookings,name='check_bookings'),
    path('hs_view_bkng',views.hs_view_bkng,name='hs_view_bkng'),
    path('hs_view_rvw',views.hs_view_rvw,name='hs_view_rvw'),
    path('hs_view_complaint',views.hs_view_complaint,name='hs_view_complaint'),
    path('hs_add_dr',views.hs_add_dr,name='hs_add_dr'),
    path('hs_user_prof/<id>',views.hs_user_prof,name='hs_user_prof'),



    path('hs_add_dr_post',views.hs_add_dr_post,name='hs_add_dr_post'),
    path('and_view_hospital',views.and_view_hospital,name='and_view_hospital'),

    # path('hs_acpt_bk/<int:id>', views.hs_acpt_bk, name='hs_acpt_bk'),




   ############################################################## LAB################################################################





    path('register',views.register,name='register'),
    path('lab_reg_post',views.lab_reg_post,name='lab_reg_post'),

    path('uploadtest/<int:id>',views.uploadtest,name='uploadtest'),


    path('viewuser',views.viewuser,name='viewuser'),
    path('adduser',views.adduser,name='adduser'),
    path('viewprofile',views.viewprofile,name='viewprofile'),
    path('labeditprf',views.labeditprf,name='labeditprf'),
    path('lab_editprof',views.lab_editprof,name='lab_editprof'),
    path('ch_lab_pass',views.ch_lab_pass,name='ch_lab_pass'),
    path('admin_verify_lab',views.admin_verify_lab,name='admin_verify_lab'),
    path('admin_accept_lab/<int:id>',views.admin_accept_lab,name='admin_accept_lab'),
    path('admin_reject_lab/<int:id>',views.admin_reject_lab,name='admin_reject_lab'),
    path('admin_acpt_lab',views.admin_acpt_lab,name='admin_acpt_lab'),
    path('admin_acpt_lab_search',views.admin_acpt_lab_search,name='admin_acpt_lab_search'),
    path('lab_ch_change',views.lab_ch_change,name='lab_ch_change'),


    path('lab_view_user_search',views.lab_view_user_search,name='lab_view_user_search'),
    path('lab_add_user_search',views.lab_add_user_search,name='lab_add_user_search'),
    path('view_user_profile/<id>',views.view_user_profile,name='view_user_profile'),
    path('lad_add_user/<id>',views.lad_add_user,name='lad_add_user'),



    path('result_post',views.result_post,name='result_post'),






    ##############################################user     App################################################################


    path('get-ip/',views.get_ip, name='get_ip'),

    path('logincode',views.logincode),
    path('registrationcode',views.registrationcode,name='registrationcode'),
    path('book_notification',views.book_notification,name='book_notification'),
    path('lab_dash',views.lab_dash,name='lab_dash'),
    path('and_view_profile',views.and_view_profile,name='and_view_profile'),
    path('and_edit_prf',views.and_edit_prf,name='and_edit_prf'),
    path('and_view_hospital',views.and_view_hospital,name='and_view_hospital'),
    path('viewcomplaint',views.viewcomplaint,name='viewcomplaint'),
    path('sendcomplaint',views.sendcomplaint,name='sendcomplaint'),
    path('delcomplaint',views.delcomplaint,name='delcomplaint'),
    path('and_edit_profile_view_details',views.and_edit_profile_view_details,name='and_edit_profile_view_details'),
    path('and_view_doctor',views.and_view_doctor,name='and_view_doctor'),
    path('sendreview',views.sendreview,name='sendreview'),
    path('and_view_sc',views.and_view_sc,name='and_view_sc'),
    path('book',views.book,name='book'),
    path('viewreview',views.viewreview,name='viewreview'),
    path('viewbk',views.viewbk,name='viewbk'),
    path('viewprescription',views.viewprescription,name='viewprescription'),
    path('and_result',views.and_result,name='and_result'),
    path('drawer',views.drawer,name='drawer'),
    path('forgot_password',views.forgot_password,name='forgot_password'),
    path('and_change_password',views.and_change_password,name='and_change_password'),
    path('viewbknotification',views.viewbknotification,name='viewbknotification'),
    path('viewup_coming_appointments',views.viewup_coming_appointments,name='viewup_coming_appointments'),
    path('and_view_all_doctors',views.and_view_all_doctors,name='and_view_all_doctors'),
    path('and_view_departments',views.and_view_departments,name='and_view_departments'),
    path('and_view_dep_doctor',views.and_view_dep_doctor,name='and_view_dep_doctor'),
    path('viewallnotification',views.viewallnotification,name='viewallnotification'),
    path('reminder',views.reminder,name='reminder'),
    path('update_notification_status',views.update_notification_status,name='update_notification_status'),














]