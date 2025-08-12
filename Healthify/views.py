import json
import socket

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render,redirect,HttpResponse
from.models import *
from datetime import datetime, timedelta, date, time


#common login code

def admin_lgn(request):
    return render(request, 'LOGIN.html')



def admin_add_diet_plan(request):
    return render(request, "ADMIN/Add_diet_plan.html")




def post_diet_plan(request):
    height=request.POST['textfield']
    weight=request.POST['textfield2']
    sugar=request.POST['textfield22']
    cholestrol=request.POST['textfield23']
    pressure=request.POST['textfield24']
    type=request.POST['type']
    age=request.POST['age']
    diet_plan=request.FILES['diet']
    fn = FileSystemStorage()
    fs = fn.save(diet_plan.name, diet_plan)

    db=diet_plan_table()
    db.height=height
    db.weight=weight
    db.sugar=sugar
    db.cholestrol=cholestrol
    db.pressure=pressure
    db.type=type
    db.age=age
    db.diet_plan=fs
    db.save()

    return HttpResponse('''<script>
                  alert("ok "),window.location="/admin_add_diet_plan"</script>''')






def add_diet_chart_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('logout succesfull');window.location="login"</script>''')

    # Name=request.POST['textfield']
    # Date=request.POST['textfield2']
    Diet_charts=request.FILES['fileField3']
    BMI = request.POST['BMI']
    Alcoholabuse = request.POST['Alcoholabuse']
    Allergies = request.POST['Allergies']
    Arthritis = request.POST['Arthritis']
    Asthma = request.POST['Asthma']
    Bloodpressure = request.POST['Bloodpressure']
    Cancer = request.POST['Cancer']
    Cholestrol = request.POST['Cholestrol']
    Depression = request.POST['Depression']
    Diabetes = request.POST['Diabetes']
    Druguse = request.POST['Druguse']
    Gender = request.POST['Gender']
    Headaches = request.POST['Headaches']
    Heartproblem = request.POST['Heartproblem']
    Kidney = request.POST['Kidney']
    Liver = request.POST['Liver']
    Obicity = request.POST['Obicity']
    Pregnancy = request.POST['Pregnancy']
    Smoking = request.POST['Smoking']
    Stroke = request.POST['Stroke']


    yobj=diet_plan_table()
    # yobj.Name=Name
    # yobj.Date=Date

    fn = FileSystemStorage()
    # date = datetime.today()
    fs = fn.save(Diet_charts.name, Diet_charts)

    yobj.Dietplan=fs
    # yobj.Time= datetime.today()
    yobj.BMI=BMI
    yobj.Alcoholabuse=Alcoholabuse
    yobj.Allergies=Allergies
    yobj.Arthritis=Arthritis
    yobj.Asthma=Asthma
    yobj.Bloodpressure=Bloodpressure
    yobj.Cancer=Cancer
    yobj.Cholestrol=Cholestrol
    yobj.Depression=Depression
    yobj.Diabetes=Diabetes
    yobj.Druguse=Druguse
    yobj.Gender=Gender
    yobj.Headaches=Headaches
    yobj.Heartproblem=Heartproblem
    yobj.Kidney=Kidney
    yobj.Liver=Liver
    yobj.Obicity=Obicity
    yobj.Pregnancy=Pregnancy
    yobj.bmi=BMI
    yobj.Smoking=Smoking
    yobj.Stroke=Stroke
    yobj.save()


    return HttpResponse('''<script>alert('diet add');window.location="/admin_add_diet_plan"</script>''')




def login_code(request):
    uname = request.POST['textfield']
    pwd = request.POST['textfield2']
    a = login_table.objects.filter(username=uname, password=pwd)
    if a.exists():
        ob = login_table.objects.get(username=uname,password=pwd)
        if ob.type == "admin":
            ob1=auth.authenticate(username="admin",password="admin")
            if ob1 is not None:
                auth.login(request,ob1)
                request.session['lid'] = ob.id


            return redirect('/admin_hm')
        elif ob.type=='doctor':
            ob1 = auth.authenticate(username="admin", password="admin")
            if ob1 is not None:
                auth.login(request, ob1)
                request.session['lid'] = ob.id
            return redirect('doc_dash')

        elif ob.type == 'hospital':
            ob1 = auth.authenticate(username="admin", password="admin")
            if ob1 is not None:
                auth.login(request, ob1)
                request.session['lid'] = ob.id
            return redirect('hs_dash')
        elif ob.type == 'lab':
            ob1 = auth.authenticate(username="admin", password="admin")
            if ob1 is not None:
                auth.login(request, ob1)
                request.session['lid'] = ob.id
            return redirect('lab_dash')

        else:
            return HttpResponse('''<script>
                  alert("invalid login"),window.location="/"</script>''')


    else:
                                                    return HttpResponse('''<script>
                         alert("invalid login"),window.location="/"</script>''')


# admin  side


def admin_hm(request):
    return render(request, 'ADMIN/adminindex.html')

@login_required(login_url='/')


def admin_view_complaints(request):
    ob = complaint_table.objects.all()
    return render(request, 'ADMIN/ADMIN VIEW COMPLAINTS.html',{"data":ob})

@login_required(login_url='/')


def admin_complaints_reply(request,id):
    com = complaint_table.objects.get(id=id)
    return render(request, 'ADMIN/ADMIN SEND REPLY.html',{'com':com})

@login_required(login_url='/')

def admin_complaints_reply_post(request):
    id = request.POST['id']
    reply = request.POST['textfield']

    com = complaint_table.objects.get(id=id)
    com.reply=reply
    com.save()
    return HttpResponse('''<script>
                            alert("Replied"),window.location="/admin_view_complaints"</script>''')

@login_required(login_url='/')
#admin view hospitals

def admin_verify_hsptl(request):
    ob=hospital_table.objects.filter(LOGIN__type='pending')
    return render(request, 'ADMIN/VERIFY HOSPITAL.html',{"data":ob})


@login_required(login_url='/')
# admin view lab


def admin_verify_lab(request):
    ob=lab_table.objects.filter(LOGIN__type='pending')
    return render(request, 'ADMIN/VERIFY LAB.html',{"data":ob})



@login_required(login_url='/')


#admin accept lab

def admin_accept_lab(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='lab'
    ob.save()
    return HttpResponse('''<script>
            alert("accepted"),window.location="/admin_acpt_lab"</script>''')



@login_required(login_url='/')

#admin reject lab
def admin_reject_lab(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='rejected'
    ob.save()
    return HttpResponse('''<script>
            alert("rejected"),window.location="/admin_acpt_lab"</script>''')


#admin accept hospital\
@login_required(login_url='/')

def admin_accept_hsptl(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='hospital'
    ob.save()
    return HttpResponse('''<script>
            alert("accepted"),window.location="/admin_acpt_hs_doc"</script>''')

@login_required(login_url='/')

#admin reject hospital
def admin_reject_hs(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='rejected'
    ob.save()
    return HttpResponse('''<script>
            alert("rejected"),window.location="/admin_acpt_hs_doc"</script>''')

@login_required(login_url='/')


#admin view accepted hs

def admin_acpt_hs_doc(request):
    ob=hospital_table.objects.filter(LOGIN__type='hospital')
    pd = hospital_table.objects.filter(LOGIN__type='pending')
    return render(request, 'ADMIN/VIEW ACTP HSPTL & DCTR.html',{"data":ob,"requests":pd})


# admin view accepted lab

@login_required(login_url='/')

def admin_acpt_lab(request):
    ob=lab_table.objects.filter(LOGIN__type='lab')
    pd = lab_table.objects.filter(LOGIN__type='pending')
    return render(request, 'ADMIN/VIEW ACCEPT LAB.html',{"data":ob,"request":pd})





# admin search lab
@login_required(login_url='/')

def admin_acpt_lab_search(request):
    n1=request.POST["n1"]
    ob=lab_table.objects.filter(LOGIN__type='lab',name__contains=n1)
    return render(request, 'ADMIN/VIEW ACCEPT LAB.html',{"data":ob})




# admin search hospital

@login_required(login_url='/')

def admin_acpt_hs_doc_search(request):
    n1=request.POST["n1"]
    ob=hospital_table.objects.filter(LOGIN__type='hospital',name__icontains=n1)
    return render(request, 'ADMIN/VIEW ACTP HSPTL & DCTR.html',{"data":ob})

@login_required(login_url='/')

#admin view bookings

def admin_view_bookings(request,hid):
    ob=booking_table.objects.filter(SCHEDULE__DOCTOR__HOSPITAL=hid)
    return render(request, 'ADMIN/VIEW BOOKINGS.html',{"data":ob})

@login_required(login_url='/')

#admin view doctor

def admin_view_dctr(request,id):
    ob=doctor_table.objects.filter(HOSPITAL=id)
    return render(request, 'ADMIN/ADMIN VIEW DR.html',{"data":ob})

@login_required(login_url='/')




#doctor

def doc_dash(request):
    return render(request, 'DOCTOR/doctor_view_data.html')


@login_required(login_url='/')
def doc_view_prf(request):
    ob = doctor_table.objects.get(LOGIN=request.session["lid"])
    return render(request, 'DOCTOR/DOC VIEW PROFILE.html', {"data": ob})


@login_required(login_url='/')
def doc_view_sc(request):
    today = date.today()
    ob = schedule_table.objects.filter(DOCTOR__LOGIN=request.session["lid"], date__gte=today)
    return render(request, 'DOCTOR/DOC VIEW SCHDLE.html', {"d": ob})


@login_required(login_url='/')
def doc_edit_prf(request):
    ob = doctor_table.objects.get(LOGIN=request.session["lid"])
    ob2 = hospital_table.objects.all()
    return render(request, 'DOCTOR/DOC EDIT PROFILE.html', {"i": ob, 'j': ob2})


@login_required(login_url='/')
def doc_editprof(request):
    name = request.POST['textfield']
    email = request.POST['textfield2']
    phone = request.POST['textfield4']
    experience = request.POST['textfield7']

    # login = login_table.objects.get(id=id)

    doctor_profile = doctor_table.objects.get(LOGIN=request.session["lid"])

    if 'image' in request.FILES:
        image = request.FILES['image']
        fs = FileSystemStorage()
        fp = fs.save(image.name, image)
        doctor_profile.image = fp
        doctor_profile.name = name
        doctor_profile.email = email
        doctor_profile.phone = phone
        doctor_profile.experience = experience
        doctor_profile.save()
    else:

        doctor_profile.name = name
        doctor_profile.email = email
        doctor_profile.phone = phone
        doctor_profile.experience = experience
        doctor_profile.save()
    return HttpResponse('''<script>alert('success');window.location='/doc_view_prf'</script>''')


@login_required(login_url='/')
def doc_view_rvw(request):
    obd = doctor_table.objects.get(LOGIN=request.session["lid"])
    ob = review_table.objects.filter(HOSPITAL=obd.HOSPITAL.id)
    return render(request, 'DOCTOR/DOC VIEW REVIEW.html', {"data": ob})


@login_required(login_url='/')
def doc_view_schdl(request):
    return render(request, 'DOCTOR/DOC VIEW SCHDLE.html')


@login_required(login_url='/')
def doc_pres(request, id):
    ob = prescription_table.objects.all()
    return render(request, 'DOCTOR/ADD PRESCRIPTION.html', {"data": ob})


@login_required(login_url='/')
def doc_view_bookings(request, id):
    a = schedule_table.objects.get(id=id)
    print(a.date, 'ygyugyugyugyugyugyu')
    ob = booking_table.objects.filter(SCHEDULE__DOCTOR__LOGIN=request.session["lid"], status="booked")
    past = booking_table.objects.filter(SCHEDULE__DOCTOR__LOGIN=request.session["lid"], status="consulted")
    return render(request, 'DOCTOR/DOC VIEW BOOKINGS.html', {"data": ob, "past_data": past})


@login_required(login_url='/')
def doc_add_prescription(request, id):
    request.session['bid'] = id

    booking = booking_table.objects.get(id=id, SCHEDULE__DOCTOR__LOGIN=request.session['lid'], status="booked")
    user_id = booking.USER_id

    request.session['uid'] = user_id

    bid = booking_table.objects.filter(SCHEDULE__DOCTOR__LOGIN=request.session['lid'], USER_id=user_id,
                                       status="consulted")

    return render(request, 'DOCTOR/ADD PRES.html', {"data": bid})


@login_required(login_url='/')
def doc_view_past_pres(request, id):
    did = prescription_table.objects.filter(BOOKING_id=id)
    return render(request, 'DOCTOR/DOC PREV PRES.html', {"data": did})


@login_required(login_url='/')


#
# def doc_pree(request):
#     # days = request.POST[f'medicine_name_{index}']
#     # morning = request.POST['textfield']
#     # afternoon = request.POST['textfield']
#     # quantity = request.POST['textfield']
#     # night = request.POST['textfield']
#     #
#
#
#
#     pname = request.POST.get(f'medicine_name_{index}')
#     quantity = request.POST.get(f'quantity_{index}')
#     days = request.POST.get(f'days_{index}')
#     morning = request.POST.get(f'morning_{index}')
#     afternoon = request.POST.get(f'afternoon_{index}')
#     night = request.POST.get(f'night_{index}')
#
#     pre=prescription_table()
#     pre.BOOKING=request.session.get('bid')
#     pre.prescription=pname
#     pre.days=days
#     pre.morning=morning
#     pre.afternoon=afternoon
#     pre.quantity=quantity
#     pre.night=night
#     pre.date=datetime.today()
#     pre.save()
#
#
#     rem=reminder_table()
#     rem
#







def doc_add_pre(request):
    if request.method == 'POST':
        booking_id = request.session.get('bid')
        if not booking_id:
            return HttpResponse("Booking ID not found in session.", status=400)

        try:
            booking = booking_table.objects.get(id=booking_id)
        except booking_table.DoesNotExist:
            return HttpResponse("Invalid Booking ID.", status=404)

        index = 0
        while True:
            medicine_key = f'medicine_name_{index}'
            if medicine_key not in request.POST:
                break

            pname = request.POST.get(f'medicine_name_{index}')
            quantity = request.POST.get(f'quantity_{index}')
            days = request.POST.get(f'days_{index}')
            morning = request.POST.get(f'morning_{index}', '').strip()
            afternoon = request.POST.get(f'afternoon_{index}', '').strip()
            night = request.POST.get(f'night_{index}', '').strip()


            def validate_time(time_str, default_time):
                try:
                    return datetime.strptime(time_str, "%H:%M:%S").time() if time_str else default_time
                except ValueError:
                    return default_time


            morning = validate_time(morning, datetime.strptime("08:00:00", "%H:%M:%S").time())
            afternoon = validate_time(afternoon, datetime.strptime("13:00:00", "%H:%M:%S").time())
            night = validate_time(night, datetime.strptime("20:00:00", "%H:%M:%S").time())


            try:
                quantity = int(quantity)
                days = int(days)
            except ValueError:
                return HttpResponse("Invalid quantity or days.", status=400)

            prescription = prescription_table.objects.create(
                BOOKING=booking,
                prescription=pname,
                quantity=quantity,
                days=days,
                morning=morning,
                afternoon=afternoon,
                night=night,
                date=datetime.today()
            )


            reminder_table.objects.create(
                PRESCRIPTION=prescription,
                morning=morning,
                afternoon=afternoon,
                night=night
            )

            index += 1

        booking.status = 'consulted'
        booking.save()

        return HttpResponse('''
            <script>
                alert("Medicines and reminders added successfully.");
                window.location="/doc_view_sc#a";
            </script>
        ''')

    return HttpResponse("Invalid request method.", status=405)


# def doc_add_pre(request):
#     if request.method == 'POST':
#         booking_id = request.session.get('bid')
#         if not booking_id:
#             return HttpResponse("Booking ID not found in session.", status=400)
#
#         try:
#             booking = booking_table.objects.get(id=booking_id)
#         except booking_table.DoesNotExist:
#             return HttpResponse("Invalid Booking ID.", status=404)
#
#         index = 0
#         while True:
#             medicine_key = f'medicine_name_{index}'
#             if medicine_key not in request.POST:
#                 break
#
#             pname = request.POST.get(f'medicine_name_{index}')
#             quantity = request.POST.get(f'quantity_{index}')
#             days = request.POST.get(f'days_{index}')
#             morning = request.POST.get(f'morning_{index}')
#             afternoon = request.POST.get(f'afternoon_{index}')
#             night = request.POST.get(f'night_{index}')
#
#             # Create a new record for each row
#             prescription_table.objects.create(
#                 BOOKING=booking,
#                 prescription=pname,
#                 quantity=int(quantity),
#                 days=int(days),
#                 morning=morning,
#                 afternoon=afternoon,
#                 night=night,
#                 date=datetime.today()
#             )
#             index += 1
#
#         booking.status = 'consulted'
#         booking.save()
#
#
#
#         rm=reminder_table()
#         rm.PRESCRIPTION=
#         rm.morning="8:30"
#         rm.afternoon="8:30"
#         rm.night="8:30"
#
#         return HttpResponse('''
#             <script>
#                 alert(" medicines added ");
#                 window.location="/doc_view_sc#a";
#             </script>
#         ''')
#
#     return HttpResponse("Invalid request method.", status=405)


@login_required(login_url='/')
# def doc_re_pres(request,id):
#     sc = booking_table.objects.get(id=id)
#     sc.status = 'booked'
#     sc.save()
#     return HttpResponse('''<script>alert("data added"),window.location="/doc_view_sc#a"</script>''')
# @login_required(login_url='/')
@login_required(login_url='/')
def doc_ch(request):
    ob = doctor_table.objects.get(LOGIN=request.session["lid"])
    return render(request, 'DOCTOR/DR CHANGE PASSWORD.html', {"data": ob})


@login_required(login_url='/')
def doc_ch_change(request):
    current = request.POST['textfield']
    new = request.POST['textfield2']
    confirm = request.POST['textfield3']
    dchob = login_table.objects.filter(password=current, id=request.session['lid'])
    if dchob.exists():
        if new == confirm:
            dchob1 = login_table.objects.filter(password=current, id=request.session['lid']).update(password=new)
            return HttpResponse('''<script>alert('Password Change');window.location='/'</script>''')
        else:
            return HttpResponse('''<script>alert('Password invalid');window.location='/doc_ch'</script>''')
    else:
        return HttpResponse('''<script>alert('Password invalid');window.location='/doc_ch'</script>''')


@login_required(login_url='/')

#hospital  side


#hospital register

def hs_reg(request):
    return render(request,'HOSPITAL/HS REG.html')


def hs_reg_post(request):

    hname = request.POST['textfield']
    hemail = request.POST['textfield2']
    hwebsite = request.POST['textfield3']
    hphone = request.POST['textfield5']
    hplace = request.POST['textfield6']
    hpin = request.POST['textfield7']
    hpost = request.POST['textfield8']
    hlatitude = request.POST['textfield9']
    hlongitude = request.POST['textfield10']
    husername = request.POST['textfield11']
    hpassword = request.POST['textfield12']


    if login_table.objects.filter(username=husername).exists():
        return HttpResponse('''<script>alert("UserName already exist"),window.location="/"</script>''')


    else:
        ob=login_table()
        ob.username=husername
        ob.password=hpassword
        ob.type="pending"
        ob.save()



        hob=hospital_table()
        hob.LOGIN=ob
        hob.name=hname
        hob.email=hemail
        hob.website=hwebsite
        hob.contactno=hphone
        hob.place=hplace
        hob.pin=hpin
        hob.post=hpost
        hob.latitude=hlatitude
        hob.longitude=hlongitude
        hob.username=husername
        hob.password=hpassword
        hob.save()

        return HttpResponse('''<script>alert('success');window.location='/'</script>''')



#delete doctor

def delete_dr(request,id):
    ob = login_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>
                alert("deleted"),window.location="/hs_mng_dctr"</script>''')

@login_required(login_url='/')






def edit_dr(request,id):
    request.session['did']=id
    ob = doctor_table.objects.get(id=id)
    return render(request,"HOSPITAL/HS EDIT DOCTOR.html",{"i":ob})

@login_required(login_url='/')





def editdoctor(request):
    try:
        hsdname = request.POST['textfield']
        hsdemail = request.POST['textfield2']
        hsdimg = request.FILES['file1']
        fn=FileSystemStorage()
        fs=fn.save(hsdimg.name,hsdimg)
        hsdphone = request.POST['textfield4']
        hsddept = request.POST['textfield5']
        hsdqualification = request.POST['textfield6']
        hsdexperience = request.POST['textfield7']
        hsdob=doctor_table.objects.get(id=request.session['did'])
        hsdob.name=hsdname
        hsdob.email=hsdemail
        hsdob.image=fs
        hsdob.phone=hsdphone
        hsdob.department=hsddept
        hsdob.qualification=hsdqualification
        hsdob.experience=hsdexperience
        hsdob.save()
        return HttpResponse('''<script>alert('success');window.location='/hs_mng_dctr'</script>''')
    except:
        hsdname = request.POST['textfield']
        hsdemail = request.POST['textfield2']
        hsdphone = request.POST['textfield4']
        hsddept = request.POST['textfield5']
        hsdqualification = request.POST['textfield6']
        hsdexperience = request.POST['textfield7']
        hsdob = doctor_table.objects.get(id=request.session['did'])
        hsdob.name = hsdname
        hsdob.email = hsdemail
        hsdob.phone = hsdphone
        hsdob.department = hsddept
        hsdob.qualification = hsdqualification
        hsdob.experience = hsdexperience
        hsdob.save()
        return HttpResponse('''<script>alert('success');window.location='/hs_mng_dctr'</script>''')

@login_required(login_url='/')









def hs_change_pass(request):
    return render(request, 'HOSPITAL/HS CHANGE PASS.html')

@login_required(login_url='/')
def hs_dash(request):

    return render(request, 'HOSPITAL/hospitalindex.html')

@login_required(login_url='/')

def hs_log(request):
    return render(request, 'HOSPITAL/HS LOGIN.html')

@login_required(login_url='/')


def hs_add_dr_sc(request):
    return render(request,'HOSPITAL/ADD DOC SCHD.html')

# Function to list all dates and days between two dates
def list_dates_between(start_date_str, end_date_str):

    # Define date format
    date_format = "%Y-%m-%d"

    # Convert strings to datetime objects
    start_date = datetime.strptime(start_date_str, date_format)
    end_date = datetime.strptime(end_date_str, date_format)

    # List to hold all dates and their days
    date_list = []

    # Generate all dates between start and end date
    current_date = start_date
    while current_date <= end_date:
        date_list.append((current_date.strftime(date_format), current_date.strftime("%A")))
        current_date += timedelta(days=1)

    return date_list

@login_required(login_url='/')

def hs_add_dr_sc_post(request):

    hsdrscfromdate = request.POST['fd']
    hsdrsctodate = request.POST['td']
    hsdrscfromtime = request.POST['ft']
    hsdrsctotime = request.POST['tt']
    days=request.POST.getlist('day')
    lis=list_dates_between(hsdrscfromdate,hsdrsctodate)

    for i in lis:
        if i[1] in days:
            hsdrscob = schedule_table()
            hsdrscob.date = i[0]
            hsdrscob.fromtime = hsdrscfromtime
            hsdrscob.totime = hsdrsctotime
            hsdrscob.DOCTOR_id=request.session['did']
            hsdrscob.save()
    return HttpResponse('''<script>alert('success');window.location='/hs_mng_dctr'</script>''')

@login_required(login_url='/')


def hs_mng_dr_sc(request,id):
    request.session['did']=id
    ob=schedule_table.objects.filter(DOCTOR__id=id)
    return render(request, 'HOSPITAL/HS MNG DCTR SCHDLE.html',{"sch":ob})

@login_required(login_url='/')




#hospital view bookings and verify

#
def hs_view_bkng(request):
    # hs_v_bk_ob=booking_table.objects.filter(SCHEDULE__DOCTOR__HOSPITAL__LOGIN=request.session["lid"],status="booked")
    hs=doctor_table.objects.filter(HOSPITAL__LOGIN=request.session['lid'])


    # count=booking_table.objects.filter(SCHEDULE__DOCTOR__HOSPITAL__LOGIN=request.session["lid"],status="booked").count()
    return render(request,'HOSPITAL/HS VIEW BOOKING.html',{"data":hs  } )


def hs_viewbk(request,id):
    ob = schedule_table.objects.filter(DOCTOR__HOSPITAL__LOGIN=request.session["lid"], DOCTOR=id)
    return render(request, 'HOSPITAL/HS VIEW BOOKING OF DOC.html',{"data":ob})


def hs_view__bk(request,id):
    ob = booking_table.objects.filter(SCHEDULE__DOCTOR__HOSPITAL__LOGIN=request.session["lid"], status="booked", SCHEDULE_id=id)
    return render(request, 'HOSPITAL/HS VIEW BOOKING SC.html', {"data": ob , "count":ob.count()})


# def hs_view_bkng(request):
#     # Count bookings grouped by SCHEDULE_id
#
#     hs_v_bk_ob = booking_table.objects.filter(
#         SCHEDULE__DOCTOR__HOSPITAL__LOGIN=request.session["lid"],
#         status="booked"
#     ).values(
#         'SCHEDULE_id' ,# Schedule ID
#
#
#     ).annotate(num_bookings=Count('id'))
#     # Count bookings per schedule
#
#     # Fetch related schedule details
#     schedule_details = schedule_table.objects.filter(
#         id__in=[item['SCHEDULE_id'] for item in hs_v_bk_ob]
#     )
#
#     # Create a mapping of schedule_id to schedule data
#     schedule_map = {sch.id: sch for sch in schedule_details}
#
#     # Add schedule data to the booking list
#     for booking in hs_v_bk_ob:
#         schedule_id = booking['SCHEDULE_id']
#         schedule = schedule_map.get(schedule_id)
#         booking['schedule_details'] = schedule
#
#     return render(request, 'HOSPITAL/HS VIEW BOOKING.html', {"data": hs_v_bk_ob})







@login_required(login_url='/')



# def hs_acpt_bk(request,id):
#     ob=booking_table.objects.get(id=id)
#     ob.status='available'
#     ob.save()
#     return HttpResponse('''<script>
#             alert("accepted"),window.location="/hs_view_bkng#a"</script>''')




@login_required(login_url='/')

def hs_view_rvw(request):
    ob=review_table.objects.filter(HOSPITAL__LOGIN=request.session["lid"])
    return render(request,'HOSPITAL/HS VIEW REVIEW.html',{"data":ob})

@login_required(login_url='/')

def hs_view_complaint(request):
    ob=complaint_table.objects.all()
    return render(request, 'HOSPITAL/HS VIEW COMPLAINTS.html',{"data":ob})

@login_required(login_url='/')

def hs_ch(request):
    return render(request, 'HOSPITAL/HS CHANGE PASSWORD.html')

@login_required(login_url='/')

def hs_ch_change(request):
    current = request.POST['textfield']
    new = request.POST['textfield2']
    confirm = request.POST['textfield3']
    chob = login_table.objects.filter(password=current,id=request.session['lid'])
    if chob.exists():
        if new == confirm:
            chob1 = login_table.objects.filter(password=current, id=request.session['lid']).update(password=new)
            return HttpResponse('''<script>alert('Password Change');window.location='/'</script>''')
        else:
            return HttpResponse('''<script>alert('Password invalid');window.location='/hs_ch'</script>''')
    else:
        return HttpResponse('''<script>alert('Password invalid');window.location='/hs_ch'</script>''')

@login_required(login_url='/')



def hs_add_dr(request):
    return render(request, 'HOSPITAL/HS ADD DOCTOR.html')

@login_required(login_url='/')


def hs_user_prof(request,id):
    a=booking_table.objects.filter(id=id)
    return render(request, 'HOSPITAL/USER PROFILE.html',{'data':a})

@login_required(login_url='/')




#hospital view manage doctors
def hs_mng_dctr(request):
    hsdob=doctor_table.objects.filter(HOSPITAL__LOGIN=request.session["lid"])
    return render(request, 'HOSPITAL/HS MNG DCTR.html',{"data":hsdob})

@login_required(login_url='/')



@login_required(login_url='/')


def hs_add_dr_post(request):
    hsdname = request.POST['textfield']
    hsdemail = request.POST['textfield2']
    hsdimg = request.FILES['file1']
    fn=FileSystemStorage()
    fs=fn.save(hsdimg.name,hsdimg)
    hsdphone = request.POST['textfield4']
    hsddept = request.POST['textfield5']
    hsdqualification = request.POST['textfield6']
    hsdexperience = request.POST['textfield7']
    hsdusername = request.POST['textfield8']
    hsdpassword = request.POST['textfield9']

    if login_table.objects.filter(username=hsdusername).exists():
        return HttpResponse('''<script>alert("Doctor already exist"),window.location="/hs_add_dr"</script>''')
    else:
        hsob = login_table()
        hsob.username = hsdusername
        hsob.password = hsdpassword
        hsob.type = 'doctor'
        hsob.save()

        hsdob = doctor_table()
        hsdob.LOGIN = hsob
        hsdob.HOSPITAL = hospital_table.objects.get(LOGIN__id=request.session["lid"])

        hsdob.name = hsdname
        hsdob.email = hsdemail
        hsdob.image = fs
        hsdob.phone = hsdphone
        hsdob.department = hsddept
        hsdob.qualification = hsdqualification
        hsdob.experience = hsdexperience
        hsdob.username = hsdusername
        hsdob.password = hsdpassword
        hsdob.save()

        return HttpResponse('''<script>alert('success');window.location='/hs_mng_dctr'</script>''')

@login_required(login_url='/')

def logout(request):
    auth.logout(request)
    return render(request,"Login.html")

@login_required(login_url='/')

def ch_doc(request):
    return render(request,'HOSPITAL/CK_DOC_AV.html')





#----------------------------------------LAB-----------------------------------------------------



def register(request):
    return render(request,'LAB/REGISTER.html')


def lab_dash(request):
    return render(request,'LAB/labindex.html')



def lab_reg_post(request):

    hname = request.POST['textfield']
    hemail = request.POST['textfield2']
    hwebsite = request.POST['textfield3']
    hphone = request.POST['textfield5']
    hplace = request.POST['textfield6']
    hpin = request.POST['textfield7']
    hpost = request.POST['textfield8']
    hlatitude = request.POST['textfield9']
    hlongitude = request.POST['textfield10']
    husername = request.POST['textfield11']
    hpassword = request.POST['textfield12']


    if login_table.objects.filter(username=husername).exists():
        return HttpResponse('''<script>alert("UserName already exist"),window.location="/"</script>''')


    else:
        ob=login_table()
        ob.username=husername
        ob.password=hpassword
        ob.type="pending"
        ob.save()



        hob=lab_table()
        hob.LOGIN=ob
        hob.name=hname
        hob.email=hemail
        hob.website=hwebsite
        hob.contactno=hphone
        hob.place=hplace
        hob.pin=hpin
        hob.post=hpost
        hob.latitude=hlatitude
        hob.longitude=hlongitude
        hob.username=husername
        hob.password=hpassword
        hob.save()

        return HttpResponse('''<script>alert('success');window.location='/'</script>''')








def uploadtest(request,id):
    request.session['uid']=id
    ob=user_table.objects.get(id=id)
    return render(request,'LAB/UPLOAD TEST.html',{"data":ob})


def result_post(request):
    ts=request.POST['test']
    rs=request.FILES['file']
    fn=FileSystemStorage()
    fs=fn.save(rs.name,rs)



    ob1=test_table()
    ob1.USER=user_table.objects.get(id=request.session['uid'])
    ob1.LAB=lab_table.objects.get(LOGIN_id=request.session['lid'])



    ob1.test_name=ts
    ob1.result=fs
    ob1.date=datetime.today()
    ob1.save()

    return HttpResponse('''<script>alert('uploaded');window.location='/viewuser'</script>''')





def viewuser(request):
    ob=user_table.objects.filter(LOGIN__type="user",lab="lab")
    return render(request,'LAB/VIEW USER.html',{"data":ob})



def adduser(request):
    return render(request,'LAB/ADD USER.html')

def ch_lab_pass(request):
    return render(request,'LAB/CHANGE PASSWORD.html')


def editprf(request):
    return render(request,'LAB/LAB EDIT PROFILE.html')


def viewprofile(request):
    ob=lab_table.objects.get(LOGIN=request.session["lid"])
    return render(request,'LAB/VIEW PROF.html',{"data":ob})



def labeditprf(request):
    ob = lab_table.objects.get(LOGIN=request.session["lid"])

    return render(request,'LAB/LAB EDIT PROFILE.html',{"i":ob})



def lab_editprof(request):
    name = request.POST['textfield']
    email = request.POST['textfield2']
    contactno = request.POST['textfield4']
    website = request.POST['textfield7']
    place = request.POST['textfield8']
    pin = request.POST['textfield9']
    post = request.POST['textfield10']
    latitude = request.POST['textfield11']
    longitude = request.POST['textfield12']


    lab_profile = lab_table.objects.get(LOGIN=request.session["lid"])


    lab_profile.name = name
    lab_profile.email = email
    lab_profile.contactno = contactno
    lab_profile.website = website
    lab_profile.place = place
    lab_profile.pin = pin
    lab_profile.post = post
    lab_profile.latitude = latitude
    lab_profile.longitude = longitude
    lab_profile.save()

    return HttpResponse('''<script>alert('success');window.location='/viewprofile#go'</script>''')

@login_required(login_url='/')


def lab_ch_change(request):
    current = request.POST['textfield']
    new = request.POST['textfield2']
    confirm = request.POST['textfield3']
    lchob = login_table.objects.filter(password=current,id=request.session['lid'])
    if lchob.exists():
        if new == confirm:
            lchob1 = login_table.objects.filter(password=current, id=request.session['lid']).update(password=new)
            return HttpResponse('''<script>alert('Password Changed');window.location='/'</script>''')
        else:
            return HttpResponse('''<script>alert('Password invalid');window.location='/ch_lab_pass'</script>''')
    else:
        return HttpResponse('''<script>alert('Password invalid');window.location='/ch_lab_pass'</script>''')

@login_required(login_url='/')


def lab_add_user_search(request):
    n1=request.POST["n1"]
    ob=user_table.objects.filter(LOGIN__type='user',lab='none',LOGIN__username=n1)
    return render(request, 'LAB/ADD USER.html',{"data":ob})




def lab_view_user_search(request):


    n1 = request.POST["n1"]
    ob=user_table.objects.filter(LOGIN__type='user',lab='lab',LOGIN__username=n1)

    return render(request, 'LAB/VIEW USER.html',{"data":ob})





def view_user_profile(request,id):
    request.session['uid']=id
    ob=user_table.objects.filter(id=id)
    return render(request,'LAB/VIEW USER PROFILE.html',{"data":ob})



def lad_add_user(request,id):
    ob=user_table.objects.get(id=id)
    ob.lab='lab'
    ob.save()
    return HttpResponse('''<script>
            alert("added"),window.location="/viewuser#go"</script>''')












#------------------------------------------------------------USER-------------------------------------------------------------------------------

import socket
from django.http import JsonResponse

def get_ip(request):
    try:
        # Create a UDP socket to get the actual IP address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Connect to Google's DNS
        ip_address = s.getsockname()[0]  # Get the IP address
        s.close()

        return JsonResponse({'ip': ip_address}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

#
#

#
# import socket
#
#
# def get_ip(request):
#     try:
#         # Fetch the local IP address dynamically
#         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         s.connect(("8.8.8.8", 80))
#         ip_address = s.getsockname()[0]
#         s.close()
#         print("hello")
#
#         return JsonResponse({'ip': ip_address}, status=200)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)




















def logincode(request):
    print(request.POST)
    un = request.POST['username']
    pwd = request.POST['password']
    print(un, pwd)
    try:
        ob = login_table.objects.get(username=un, password=pwd)

        if ob is None:
            data = {"task": "invalid"}
        else:
            print("user logined successfully")

            data = {"task": "valid", "lid": ob.id,"type":ob.type}


        return JsonResponse(data)
    except:
        data = {"task": "invalid"}
        r = json.dumps(data)
        print(r)
        return JsonResponse(r)

def registrationcode(request):
        try:
            print(request.POST, "uuuki")
            name = request.POST['name']
            dob = request.POST['dob']
            pin = request.POST['pin']
            place = request.POST['place']
            post = request.POST['post']
            email = request.POST['email']
            phone = request.POST['phone']
            username = request.POST['username']
            password = request.POST['password']
            img = request.FILES['image']
            fs=FileSystemStorage()
            fn=fs.save(img.name,img)
            lob1 = login_table()
            lob1.username = username
            lob1.password = password
            lob1.type = 'user'
            lob1.save()

            lab=lab_table()


            lob = user_table()
            lob.name = name
            lob.dob = dob
            lob.post = post
            lob.pin = pin
            lob.place = place
            lob.phone = phone
            lob.email = email
            lob.image = fn
            lob.LOGIN = lob1
            lob.save()
            print("uuuuuuuuu", lob)
            return JsonResponse({'task': 'valid'})
        # except:
        #     return JsonResponse({"task": "invalid"})
        except Exception as e:
            print("----"+str(e))
            return JsonResponse({"task": "invalid"})

#
def and_view_profile(request):
    lid=request.POST['lid']
    user=user_table.objects.get(LOGIN_id=lid)
    return JsonResponse({'status':'ok',
                         'id':user.id,
                         'name':user.name,
                         'email':user.email,
                         'place':user.place,
                         'dob':str(user.dob),
                         'phone':str(user.phone),
                         'pin':str(user.pin),
                         'post':user.post,
                         'image':request.build_absolute_uri(user.image.url),



                         })

def and_edit_profile_view_details(request):
    lid=request.POST['lid']
    user=user_table.objects.get(LOGIN_id=lid)
    return JsonResponse({'status':'ok',
                         'id':user.id,
                         'name':user.name,
                         'email':user.email,
                         'place':user.place,
                         'dob':str(user.dob),
                         'phone':str(user.phone),
                         'pin':str(user.pin),
                         'post':user.post,
                         'image':request.build_absolute_uri(user.image.url),



                         })


def and_edit_prf(request):
    try:
        id = request.POST['lid']
        user = user_table.objects.get(LOGIN=id)
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.place = request.POST['place']
        user.dob = request.POST['dob']
        user.phone = request.POST['phone']
        user.pin = request.POST['pin']
        user.post = request.POST['post']
        if 'image' in request.FILES:
            image = request.FILES['image']
            fs = FileSystemStorage()
            fp = fs.save(image.name, image)
            user.image = fp

            # Save the user record
        user.save()
        return JsonResponse({'status': 'ok'})
    except user_table.DoesNotExist:
        id = request.POST['lid']
        user = user_table.objects.get(LOGIN=id)
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.place = request.POST['place']
        user.dob = request.POST['dob']
        user.phone = request.POST['phone']
        user.pin = request.POST['pin']
        user.post = request.POST['post']
        user.save()
        return JsonResponse({'status': 'ok'})






def and_view_hospital(request):

    try:
        ob = hospital_table.objects.all()
        if not ob.exists():
            return JsonResponse({"status": "no_data", "data": []})

        mdata = []
        for i in ob:
            data = {
                'id': i.id,
                'name': i.name,
                'email': i.email,
                'website': i.website,
                'contactno': i.contactno,
                'place': i.place,
                'pin': i.pin,
                'post': i.post,
                'latitude': i.latitude,
                'longitude': i.longitude,
            }
            mdata.append(data)

        print("Final Response Data:", mdata)
        return JsonResponse({"status": "ok", "data": mdata})
    except Exception as e:
        print(f"Error in and_view_hospital: {str(e)}")
        return JsonResponse({"status": "error", "message": str(e)})




# def and_view_hospital(request):
#     user=hospital_table.objects.all()
#     return JsonResponse({'status':'ok',
#                          'id':user.id,
#                          'name':user.name,
#                          'email':user.email,
#                          'place':user.place,
#                          'dob':user.dob,
#                          'phone':user.phone,
#                          'pin':user.pin,
#                          'post':user.post,
#
#
#
#                          })

# def and_view_profile(request):
#     print(request.POST,'kkkkk')
#     if request.method == 'POST':
#         lid = request.POST.get('lid')
#         try:
#             us = user_table.objects.get(id=lid)
#             return JsonResponse({
#                 'status': 'ok',
#                 'id':us.id,
#                 'name': str(us.name),
#                 'place': str(us.place),
#                 'email': str(us.email),
#                 'phone': str(us.phone),
#                 'pin': str(us.pin),
#                 'post': str(us.post),
#                 'dob': str(us.dob),
#             })
#         except user_table.DoesNotExist:
#             return JsonResponse({'status': 'error', 'message': 'Doctor not found'})
#         except Exception as e:
#             return JsonResponse({'status': 'error', 'message': str(e)})
#     else:
#             return JsonResponse({'status': 'error', 'message': 'Invalid request method'})



# def and_view_profile(request):
#     lid = request.POST['lid']
#     ob=user_table.objects.filter(LOGIN__id=lid)
#     mdata = []
#     for us in ob:
#         data={'id':us.id,
#                 'name': us.name,
#                 'place': us.place,
#                 'email': us.email,
#                 'phone': us.phone,
#                 'pin': us.pin,
#                 'post': us.post,
#                 'dob': us.dob,}
#         mdata.append(data)
#         print(mdata)
#     return JsonResponse({"status":"ok","data":mdata})




# def sendfeedback(request):
#     comp = request.POST['feedback']
#     lid = request.POST['lid']
#     lob = review_table()
#     lob.USER = user_table.objects.get(LOGIN__id=lid)
#     lob.feedback = comp
#     lob.date = datetime.today()
#     lob.save()
#     return JsonResponse({'task': 'ok'})


def sendcomplaint(request):
    comp = request.POST['complaint']
    lid = request.POST['lid']
    lob = complaint_table()
    lob.USER = user_table.objects.get(LOGIN__id=lid)
    lob.complaint = comp
    lob.reply='pending'
    lob.date = datetime.today()
    lob.save()
    return JsonResponse({'status': 'ok'})

def viewcomplaint(request):
    lid = request.POST['lid']
    ob=complaint_table.objects.filter(USER__LOGIN_id=lid)
    print(ob,"HHHHHHHHHHHHHHH")
    mdata=[]
    for i in ob:
        data={'complaint':i.complaint,'uname':i.USER.name,'date':i.date,'cid':str(i.id),'reply':i.reply}
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})



#
#
# def viewfeedback(request):
#     ob=complaint_table.objects.all()
#     print(ob,"HHHHHHHHHHHHHHH")
#     mdata=[]
#     for i in ob:
#         data={'feedback':i.complaint,'uname':i.USER.name,'date':str(i.date),'id':i.id}
#         mdata.append(data)
#         print(mdata)
#     return JsonResponse({"status":"ok","data":mdata})


def delcomplaint(request):
    cid = request.POST['cid']
    comp=complaint_table.objects.get(id=cid)
    comp.delete()
    return JsonResponse({"status": "ok"})


def and_view_doctor(request):

    hid=request.POST['hid']
    ob=doctor_table.objects.filter(HOSPITAL_id=hid)
    print(ob,"HHHHHHHHHHHHHHH")
    mdata=[]
    for i in ob:
        data={
              'id': i.id,
              'name':i.name,
              'email':i.email,
              'department':i.department,
              'qualification':i.qualification,
              'phone':i.phone,
              'experience':i.experience,
              'image': request.build_absolute_uri(i.image.url),


              }
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})


def and_view_dep_doctor(request):
    dep=request.POST['department']
    ob=doctor_table.objects.filter(department=dep)
    print(ob,"HHHHHHHHHHHHHHH")
    mdata=[]
    for i in ob:
        data={
              'id': i.id,
              'name':i.name,
              'email':i.email,
              'department':i.department,
              'qualification':i.qualification,
              'phone':i.phone,
              'experience':i.experience,
              'image': request.build_absolute_uri(i.image.url),


              }
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})


def and_view_all_doctors(request):
    ob=doctor_table.objects.all()
    print(ob,"HHHHHHHHHHHHHHH")
    mdata=[]
    for i in ob:
        data={
              'id': i.id,
              'name':i.name,
              'email':i.email,
              'department':i.department,
              'qualification':i.qualification,
              'hospital':i.HOSPITAL.name,
              'experience':i.experience,
              'image': request.build_absolute_uri(i.image.url),


              }
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})



def and_view_departments(request):
    ob=doctor_table.objects.all()
    print(ob,"HHHHHHHHHHHHHHH")
    mdata=[]
    for i in ob:
        data={
              'id': i.id,
              'department':i.department,



              }
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})





def sendreview(request):
    rev = request.POST['review']
    rating = request.POST['rating']
    lid = request.POST['lid']
    hid = request.POST['hid']
    lob = review_table()
    lob.HOSPITAL = hospital_table.objects.get(id=hid)
    lob.USER = user_table.objects.get(LOGIN__id=lid)
    lob.review = rev
    lob.rating= rating
    lob.date = datetime.today()
    lob.save()
    return JsonResponse({'status': 'ok'})


def viewreview(request):
    lid = request.POST['lid']
    ob=review_table.objects.filter(USER__LOGIN_id=lid)
    print(ob,"HHHHHHHHHHHHHHH")
    mdata=[]
    for i in ob:
        data={'review':i.review,'uname':i.USER.name,'date':i.date,'cid':str(i.id),'rating':i.rating}
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})



#
def and_view_sc(request):
    lid=request.POST['lid']
    did = request.POST['did']
    user=user_table.objects.get(LOGIN_id=lid)
    ob = schedule_table.objects.filter(DOCTOR_id=did, date__gte=datetime.today())

    total_count = 1

    print(ob, "HHHHHHHHHHHHHHH")
    mdata = []

    for i in ob:
        count1 = booking_table.objects.filter(SCHEDULE_id=i, status="booked").count()
        book = booking_table.objects.filter(SCHEDULE_id=i, USER_id=user).exists()

        print(book)

        if book:
            avail = "Booking Successful"


        elif count1>=total_count:
            avail = "booking full"


        else:
            avail= "available"


        data  = {
            'id': i.id,
            'date': i.date.strftime('%Y-%m-%d'),
            'fromtime': i.fromtime.strftime('%H:%M'),
            'status':avail,
            'totime': i.totime.strftime('%H:%M'),
        }
        mdata.append(data)
    print(mdata)
    return JsonResponse({"status": "ok", "data": mdata})






def book(request):
    lid=request.POST['lid']
    sid=request.POST['sid']
    user=user_table.objects.get(LOGIN_id=lid)
    print(user,"hello")

    schedule = schedule_table.objects.get(id=sid)
    existing_booking = booking_table.objects.filter(SCHEDULE_id=schedule,USER_id=user).exists()

    if existing_booking:
        return JsonResponse({"status": "error", "message": "You have already booked this schedule"}, status=400)

    count1 = booking_table.objects.filter(SCHEDULE_id=sid, status="booked").count()
    total_count = 1
    avail = count1 >= total_count

    if avail :
        return JsonResponse({"status": "error", "message": "booking full"}, status=410)



    else:
        bk = booking_table()
        bk.status = 'booked'
        bk.date = datetime.now().date()
        bk.SCHEDULE = schedule_table.objects.get(id=sid)
        print(bk, 'hello')
        bk.USER = user_table.objects.get(LOGIN_id=lid)
        bk.save()
        return JsonResponse({"status": "ok", "message": "You have already booked this schedule"}, status=200)




def viewbk(request):
    lid = request.POST['lid']
    bookings = booking_table.objects.filter(USER__LOGIN_id=lid)
    mdata = []

    for booking in bookings:
        data = {
            'id': booking.id,
            'hsname': booking.SCHEDULE.DOCTOR.HOSPITAL.name,
            'dname': booking.SCHEDULE.DOCTOR.name,
            'date': booking.SCHEDULE.date.strftime('%Y-%m-%d'),
            'totime': booking.SCHEDULE.totime.strftime('%H:%M'),
            'fromtime': booking.SCHEDULE.fromtime.strftime('%H:%M'),
            'status': booking.status,
            'department': booking.SCHEDULE.DOCTOR.department,
        }
        mdata.append(data)

    return JsonResponse({"status": "ok", "data": mdata})





def viewup_coming_appointments(request):
    lid = request.POST['lid']
    bookings = booking_table.objects.filter(USER__LOGIN_id=lid,status="booked")
    mdata = []

    for booking in bookings:
        data = {
            'id': booking.id,
            'hsname': booking.SCHEDULE.DOCTOR.HOSPITAL.name,
            'dname': booking.SCHEDULE.DOCTOR.name,
            'date': booking.SCHEDULE.date.strftime('%Y-%m-%d'),
            'totime': booking.SCHEDULE.totime.strftime('%H:%M'),
            'fromtime': booking.SCHEDULE.fromtime.strftime('%H:%M'),
            'status': booking.status,
            'department': booking.SCHEDULE.DOCTOR.department,
        }
        mdata.append(data)

    return JsonResponse({"status": "ok", "data": mdata})


def viewprescription(request):
    try:
        bid = request.POST['bid']
        pr = prescription_table.objects.filter(BOOKING_id=bid)
        mdata = []

        for i in pr:
            data = {
                "id": i.id,
                "date": i.date,
                "prescription": i.prescription,
                "quantity": i.quantity,
                "days": i.days,
                "morning": i.morning,
                "afternoon": i.afternoon,
                "night": i.night,
                "date": i.date
            }
            mdata.append(data)
        return JsonResponse({"status": "ok", "data": mdata})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)



def and_result(request):
    lid = request.POST['lid']
    bk = test_table.objects.filter(USER__LOGIN_id=lid,)
    mdata = []

    for i in bk:
        data = {
            'id': i.id,
            'testname': i.test_name,
            'date': i.date,
            'result': request.build_absolute_uri(i.result.url),
            'lab': i.LAB.name,



        }
        mdata.append(data)

    return JsonResponse({"status": "ok", "data": mdata})


def drawer(request):
    lid=request.POST['lid']
    user=user_table.objects.get(LOGIN_id=lid)
    return JsonResponse({'status':'ok',
                         'id':user.id,
                         'name':user.name,
                         'email':user.email,
                         'place':user.place,
                         'dob':str(user.dob),
                         'phone':str(user.phone),
                         'pin':str(user.pin),
                         'post':user.post,
                         'image':request.build_absolute_uri(user.image.url),



                         })


def forgot_password(request):
    print(request.POST)
    try:
        username = request.POST['username']
        s = login_table.objects.get(username=username)

        # If user is not found or doesn't exist, return an invalid response
        if s is None:
            return JsonResponse({"status": "Invalid username"})
        else:
            # Fetch the Organization associated with the Login object
            try:
                organization = user_table.objects.get(LOGIN=s)
                email_address = organization.email  # Assuming email is in Organization model
            except user_table.DoesNotExist:
                return JsonResponse({"status": "Email not available in Organization"})

            if not email_address:
                return JsonResponse({"status": "Email not available"})

            # Create the email content
            subject = 'Healthify'
            message = f"This is from Healthify, and your password is :  {s.password}"
            from_email = 'deepakvk6334@gmail.com'

            try:
                # Send the email with the password to the user's email address
                send_mail(subject, message, from_email, [email_address])
                return JsonResponse({"status": "ok"})
            except Exception as e:
                print(f"Error sending email: {str(e)}")
                return JsonResponse({"status": "Email sending failed"})
    except Exception as e:
        print(f"Error: {str(e)}")
        return JsonResponse({"status": "Error occurred"})







def book_notification(request):
    lid=request.POST['lid']
    lastid=request.POST["lastid"]

    pt = booking_table.objects.filter(USER__LOGIN_id=lid,date__exact=datetime.today(),id__gt=lastid)
    print(pt,"notification")


    if len(pt)>0:
        return JsonResponse({"status": "true","lastid":pt[0].id})
    else:
        return JsonResponse({"status": "true"})




def and_change_password(request):
    lid=request.POST['lid']
    current = request.POST['current']
    new = request.POST['new']
    lchob = login_table.objects.filter(password=current, id=lid)
    if lchob.exists():
        login_table.objects.filter(password=current, id=lid).update(password=new)
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'message': 'error'})


#
#
#
# from sklearn.neighbors import KNeighborsClassifier
#
#
# def recoment_code(diet_type,height,weight,sugar,cholestrol,pressure,age):
#     ob=diet_plan_table.objects.filter(type=diet_type)
#
#     dataset=[]
#     output=[]
#     for i in ob:
#         r=[i.height,i.weight,i.sugar,i.cholestrol,i.pressure,i.age]
#         dataset.append(r)
#         output.append(i.diet_plan.url)
#     output1=[]
#     for i in range(0,len(output)):
#         output1.append(i)
#     knn = KNeighborsClassifier(n_neighbors=1)
#     knn.fit(dataset, output1)
#     rr=[height,weight,sugar,cholestrol,pressure,age]
#     res=knn.predict([rr])[0]
#     return  output[res]



from django.http import JsonResponse
from django.utils.timezone import now


def check_bookings(request):
    today = now().date()
    user_id = request.POST("lid")

    #
    upcoming_bookings = booking_table.objects.filter(date=today,USER__LOGIN__id=user_id)

    return JsonResponse({"reminders": list(upcoming_bookings)})


def updatelocation(request):
    print(request.POST)
    lid=request.POST['lid']
    ob=booking_table.objects.filter(USER__LOGIN__id=lid)
    lids=[]
    for i in ob:
        lids.append(i.id)
    ob1=booking_table.objects.exclude(id__in=lids)
    # return JsonResponse({"task": "True"})    if len(ob1)==0:
        # return JsonResponse({"task":"True"})        return JsonResponse({"task":"False"})

    for i in ob1:
        obb=booking_table()
        obb.CAMERA=i
        obb.User=user_table.objects.get(LOGIN__id=lid)
        obb.save()
    return JsonResponse({"task": "True"})



def user_view_notification(request):
    lid=request.POST['lid']
    date=datetime.now().today().date()
    a=booking_table.objects.get(USER__LOGIN_id=lid,date=date)
    return JsonResponse({"status": "ok",'id':a.id,'SCHEDULE':a.SCHEDULE.fromtime})








#####################################################AI##################################################################








import json
import numpy as np

def cosine_similarity(list1, list2):
    # Convert lists to numpy arrays
    vector1 = np.array(list1)
    vector2 = np.array(list2)

    # Calculate the dot product
    dot_product = np.dot(vector1, vector2)

    # Calculate the magnitudes of the vectors
    magnitude1 = np.linalg.norm(vector1)
    magnitude2 = np.linalg.norm(vector2)

    # Calculate cosine similarity
    similarity = dot_product / (magnitude1 * magnitude2)

    return similarity



def predict_diet(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Extract input data
        gender = data.get('Gender')
        print(gender,"hello")
        obesity = data.get('Obicity')
        alcohol_abuse = data.get('Alcoholabuse')
        drug_use = data.get('Druguse')
        smoking = data.get('Smoking')
        headaches = data.get('Headaches')
        asthma = data.get('Asthma')
        cancer = data.get('Cancer')
        stroke = data.get('Stroke')
        kidney = data.get('Kidney')
        liver = data.get('Liver')
        depression = data.get('Depression')
        allergies = data.get('Allergies')
        arthritis = data.get('Arthritis')
        pregnancy = data.get('Pregnancy')
        bmi = data.get('BMI')
        blood_pressure = data.get('BloodPressure')

        l_gender =[]
        l_obesity = []
        l_alcohol_abuse = []
        l_drug_use = []
        l_smoking = []
        l_headaches = []
        l_asthma = []
        l_cancer = []
        l_stroke = []
        l_kidney = []
        l_liver = []
        l_depression = []
        l_allergies = []
        l_arthritis = []
        l_pregnancy = []

        l_blood_pressure = []











        ob=diet_plan_table.objects.all()
        res=[]
        dataset=[]
        for i in ob:
            r=[]
            if i.Gender not in l_gender:
                l_gender.append(i.Gender)



            if i.Obicity not in l_obesity:
                l_obesity.append(i.Obicity)

            if i.Bloodpressure not in l_blood_pressure:
                l_blood_pressure.append(i.Bloodpressure)

            if i.Alcoholabuse not in l_alcohol_abuse:
                l_alcohol_abuse.append(i.Alcoholabuse)

            if i.Druguse not in l_drug_use:
                l_drug_use.append(i.Druguse)


            if i.Asthma not in l_asthma:
                l_asthma.append(i.Asthma)

            if i.Headaches not in l_headaches:
                l_headaches.append(i.Headaches)


            if i.Liver not in l_liver:
                l_liver.append(i.Liver)

            if i.Stroke not in l_stroke:
                l_stroke.append(i.Stroke)

            if i.Kidney not in l_kidney:
                l_kidney.append(i.Kidney)
            if i.Depression not in l_depression:
                l_depression.append(i.Depression)

            if i.Allergies not in l_allergies:
                l_allergies.append(i.Allergies)


            if i.Pregnancy not in l_pregnancy:
                l_pregnancy.append(i.Pregnancy)


            if i.Arthritis not in l_arthritis:
                l_arthritis.append(i.Arthritis)

            if i.Smoking not in l_smoking:
                l_smoking.append(i.Smoking)

            if i.Cancer not in l_cancer:
                l_cancer.append(i.Cancer)


            r.append(l_gender.index(i.Gender))
            r.append(l_obesity.index(i.Obicity))
            r.append(l_blood_pressure.index(i.Bloodpressure))
            r.append(l_alcohol_abuse.index(i.Alcoholabuse))
            r.append(l_drug_use.index(i.Druguse))
            r.append(l_asthma.index(i.Asthma))
            r.append(l_headaches.index(i.Headaches))
            r.append(l_liver.index(i.Liver))
            r.append(l_stroke.index(i.Stroke))
            r.append(l_kidney.index(i.Kidney))
            r.append(l_depression.index(i.Depression))
            r.append(l_allergies.index(i.Allergies))
            r.append(l_pregnancy.index(i.Pregnancy))
            r.append(l_arthritis.index(i.Pregnancy))
            r.append(l_smoking.index(i.Smoking))
            r.append(l_cancer.index(i.Cancer))
            r.append(float(i.bmi))

            dataset.append(r)
            res.append(i.id)
        feat=[]
        print(l_gender)
        try:
            feat.append(l_gender.index(gender))
        except:
            feat.append(-1)
        try:
            feat.append(l_obesity.index(obesity))
        except:
            feat.append(-1)
        try:
            feat.append(l_blood_pressure.index(blood_pressure))
        except:
            feat.append(-1)
        try:
            feat.append(l_alcohol_abuse.index(alcohol_abuse))
        except:
            feat.append(-1)
        try:
            feat.append(l_drug_use.index(drug_use))
        except:
            feat.append(-1)
        try:
            feat.append(l_asthma.index(asthma))
        except:
            feat.append(-1)
        try:
            feat.append(l_headaches.index(headaches))
        except:
            feat.append(-1)
        try:
            feat.append(l_liver.index(liver))
        except:
            feat.append(-1)
        try:
            feat.append(l_stroke.index(stroke))
        except:
            feat.append(-1)
        try:
            feat.append(l_kidney.index(kidney))
        except:
            feat.append(-1)
        try:
            feat.append(l_depression.index(depression))
        except:
            feat.append(-1)
        try:
            feat.append(l_allergies.index(allergies))
        except:
            feat.append(-1)
        try:
            feat.append(l_pregnancy.index(pregnancy))
        except:
            feat.append(-1)

        try:
            feat.append(l_allergies.index(allergies))
        except:
            feat.append(-1)
        try:
            feat.append(l_smoking.index(smoking))
        except:
            feat.append(-1)
        try:
            feat.append(l_cancer.index(cancer))
        except:
            feat.append(-1)
        try:
            feat.append(float(bmi))
        except:
            feat.append(-1)
        reslist=[]
        print(feat,"feat")
        for i in range(0,len(dataset)):
            print(dataset[i])
            dis=cosine_similarity(feat,dataset[i])
            reslist.append({"id":res[i],"dis":dis})
        print(reslist)

        # Example logic to generate diet plan (use your algorithm or model here)
        diet_plan = "This is a predicted diet plan based on your input conditions."
        sorted_data = sorted(reslist, key=lambda x: x['dis'], reverse=True)
        ids=[]
        print(sorted_data)
        for i in sorted_data:
            ids.append(i['id'])
            if len(ids)>3:
                break
        mdata = []

        diet_charts = diet_plan_table.objects.filter(id__in=ids)


        for i in diet_charts:
            data = {

                'dietplan': request.build_absolute_uri(i.Dietplan.url),
                # request.build_absolute_uri(i.result.url)
                # 'dietplan': i.Dietplan,
                'gender': i.Gender,
                'obicity': i.Obicity,
                'bloodpressure': i.Bloodpressure,
                'diabetes': i.Diabetes,
                'cholestrol': i.Cholestrol,
                'alcoholabuse': i.Alcoholabuse,
                'druguse': i.Druguse,
                'smoking': i.Smoking,
                'headaches': i.Headaches,
                'asthma': i.Asthma,
                'heartproblem': i.Heartproblem,
                'cancer': i.Cancer,
                'stroke': i.Stroke,
                'kidney': i.Kidney,
                'liver': i.Liver,
                'depression': i.Depression,
                'allergies': i.Allergies,
                'arthritis': i.Arthritis,
                'pregnancy': i.Pregnancy,
                'bmi': i.bmi
            }
            mdata.append(data)
        print(mdata)

        return JsonResponse({'dietPlans': mdata})


def view_diet_charts(request):
    mdata = []
    diet_charts = diet_plan_table.objects.all()
    for i in diet_charts:
        data = {

            'dietplan': i.Dietplan,
            'gender': i.Gender,
            'obicity': i.Obicity,
            'bloodpressure': i.Bloodpressure,
            'diabetes': i.Diabetes,
            'cholestrol': i.Cholestrol,
            'alcoholabuse': i.Alcoholabuse,
            'druguse': i.Druguse,
            'smoking': i.Smoking,
            'headaches': i.Headaches,
            'asthma': i.Asthma,
            'heartproblem': i.Heartproblem,
            'cancer': i.Cancer,
            'stroke': i.Stroke,
            'kidney': i.Kidney,
            'liver': i.Liver,
            'depression': i.Depression,
            'allergies': i.Allergies,
            'arthritis': i.Arthritis,
            'pregnancy': i.Pregnancy,
            'bmi': i.bmi
        }
        mdata.append(data)
    print(mdata)
    return JsonResponse({"status": "ok", "data": mdata})






def viewallnotification(request):
    lid=request.POST['lid']
    noti = booking_table.objects.all()
    # noti = booking_table.objects.filter(USER__LOGIN_id=lid)

    mdata = []

    for i in noti:
        data = {
            "id": i.id,
            "date": i.date,
            "notification": i.status,


        }
        mdata.append(data)


    return JsonResponse({'status':'ok', "data": mdata})




def viewallnotification(request):
    lid=request.POST['lid']
    noti = booking_table.objects.filter(USER__LOGIN_id=lid,notificationstatus="notopened")

    mdata = []

    for i in noti:
        data = {
            "id": i.id,
            "date": i.date,
            "notification": i.status,
            "doctorname": i.SCHEDULE.DOCTOR.name,
            "hospitalname": i.SCHEDULE.DOCTOR.HOSPITAL.name,
            "notistatus": i.notificationstatus,

        }
        mdata.append(data)


    return JsonResponse({'status':'ok', "data": mdata})


def viewbknotification(request):
    lid=request.POST['lid']
    noti = booking_table.objects.filter(USER__LOGIN_id=lid)

    mdata = []

    for i in noti:
        data = {
            "id": i.id,
            "date": i.date,
            "notification": i.status,
            "doctorname": i.SCHEDULE.DOCTOR.name,
            "hospitalname": i.SCHEDULE.DOCTOR.HOSPITAL.name,
            "notistatus": i.notificationstatus,

        }
        mdata.append(data)


    return JsonResponse({'status':'ok', "data": mdata})




def update_notification_status(request):
    nid=request.POST["notification_id"]
    ob=booking_table.objects.get(id=nid)
    ob.notificationstatus="opened"
    ob.save()
    return JsonResponse({'status': 'ok'})



# def user_view_notification(request):
#     lid = request.POST['lid']
#
#
#     noti = prescription_table.objects.get(BOOKING__USER__LOGIN_id=lid)
#
#
#
#     date=datetime.now().today().date()
#
#     noti = prescription_table.objects.get(BOOKING__USER__LOGIN_id=lid)
#
#     a=booking_table.objects.get(USER__LOGIN_id=lid,date=date)
#     return JsonResponse({"status": "ok",'id':a.id,'SCHEDULE':a.SCHEDULE.fromtime})



# def reminder(request):
#     lid=request.POST['lid']
#     noti = prescription_table.objects.filter(BOOKING__USER__LOGIN_id=lid)
#
#     mdata = []
#
#     for i in noti:
#         data = {
#             "id": i.id,
#
#
#
#         }
#         mdata.append(data)
#
#
#     return JsonResponse({'status':'ok', "data": mdata})


from django.http import JsonResponse
from datetime import datetime
from .models import reminder_table

def reminder(request):
    lid = request.POST.get('lid')
    if not lid:
        return JsonResponse({'status': 'error', 'message': 'User ID is required'}, status=400)

    now = datetime.now().strftime("%H:%M")  # Get current time in HH:MM format
    print(f"Current time: {now}, Received lid: {lid}")  # Debugging print

    # Fetch reminders for the given user
    reminders = reminder_table.objects.filter(PRESCRIPTION__BOOKING__USER__LOGIN_id=lid)
    print(f"Reminders found: {reminders.count()}")  # Debugging print

    mdata = []
    for i in reminders:
        # Extract times and convert them to HH:MM format
        times = [i.morning, i.afternoon, i.night]
        formatted_times = []
        for t in times:
            if t:  # Ensure it's not None
                formatted_times.append(t.strftime("%H:%M"))

        print(f"Checking reminder: {i.PRESCRIPTION.prescription}, Times: {formatted_times}")  # Debugging print

        # Check if the current time matches any reminder time
        if now in formatted_times:
            data = {
                "id": i.id,
                "prescription": i.PRESCRIPTION.prescription,
                "reminder_time": now,
                "notification": f"Time to take your medicine: {i.PRESCRIPTION.prescription}"
            }
            mdata.append(data)

    if not mdata:
        return JsonResponse({'status': 'no_reminders', 'message': 'No reminders for this time'}, status=200)

    return JsonResponse({'status': 'ok', 'data': mdata})

