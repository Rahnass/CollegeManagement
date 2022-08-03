import os
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib import messages
from CollegeApp.models import UserMember , course ,student
from django.contrib.auth import authenticate, login as dj_login
from django.db import connection


# Create your views here.
# -----------homepage----------
def index(request):
    return render(request,'index.html')

#---------------signup page-------------

def signup(request):
    courses=course.objects.all()
    context={'courses':courses}
    return render(request,'user/signup.html',context)

#------------login page---------------
def login(request):
    return render(request,'login.html')

#------------add course------
@login_required(login_url='index')
def course1(request):
    return render(request,'admin/course.html')   

#-------------add student page---------
@login_required(login_url='index')
def student1(request):
    courses=course.objects.all()
    context={'courses':courses}
    return render(request,'admin/student.html',context)     

#----------admin home page---------
def admin_home(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'admin/admin_homepage.html')          

#----------user home page---------
def user_home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'user/user_homepage.html')       


def profile(request):
    user = UserMember.objects.filter(user=request.user)
    context = {'user':user}
    return render(request,'user/profile.html',context)

def edit_page(request):
    umember = UserMember.objects.get(user=request.user) 
    context = {'umember':umember}
    return render(request,'user/edit_profile.html',context)  

def add_course(request):
    if request.method=='POST':
        cname=request.POST['coursename']
        cfee=request.POST['coursefee']      
        crs=course()
        crs.course_name=cname 
        crs.course_fee=cfee
        crs.save() 
        messages.info(request, 'Course added Successfully')
        return redirect('course1')

#--------------add student ---------------

def add_student(request):
    if request.method=='POST':
        sname=request.POST['stdname']
        saddress=request.POST['stdaddress']
        sage=request.POST['stdage']
        sdate=request.POST['joindate']
        ssel=request.POST['sel']
        course1=course.objects.get(id=ssel)
        std=student(student_name=sname,
                       student_address=saddress,
                       student_age=sage,
                       joining_date=sdate,
                       course=course1)
        std.save()
        messages.info(request, 'Student added Successfully')
        return redirect('student1')     


def edit_profile(request):
    if request.method == 'POST':
        umember = UserMember.objects.get(user=request.user)
        umember.user.first_name = request.POST.get('fname')
        umember.user.last_name = request.POST.get('lname')
        umember.user_address = request.POST.get('address')
        umember.user_gender = request.POST.get('gender')
        umember.user_contact = request.POST.get('contact')
        umember.user.email = request.POST.get('mail')
      
        #umember.user_image = request.FILES.get('pic')
        if request.FILES.get('pic') is not None:
            if not umember.user_image == "images/dp.png":
                os.remove(umember.user_image.path)
                umember.user_image = request.FILES['pic']
            else:
                umember.user_image = request.FILES['pic']
        else:
            os.remove(umember.user_image.path)
            umember.user_image = "images/dp.png"

        umember.user.save()
        umember.save()
        return redirect('profile')
   

def third(request):
    return render(request,'third.html')

def show_details(request):
    cursor=connection.cursor()
    cursor.execute("Select CollegeApp_course.id,CollegeApp_student.student_name,CollegeApp_student.student_address,CollegeApp_student.student_age,CollegeApp_student.joining_date,CollegeApp_course.course_name,CollegeApp_course.course_fee from CollegeApp_student join CollegeApp_course on CollegeApp_student.course_id=CollegeApp_course.id")
    results=cursor.fetchall()
    return render(request,'admin/show_student.html',{'stdcrs':results})  

def show_teachers(request):
    UserMembers = UserMember.objects.all()
    return render(request,'admin/show_teachers.html',{'UserMembers':UserMembers})      

# --------------teacher signup-----------

def user_create(request):
    if request.method=='POST':
        first_name=request.POST.get('fname')
        last_name=request.POST.get('lname')
        t_address=request.POST.get('address')
        t_gender=request.POST.get('gender')
        t_contact=request.POST.get('contact')
        #t_image=request.FILES.get('pic')
        t_cou=request.POST.get('sel')
        course1=course.objects.get(id=t_cou)
        username=request.POST.get('username')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        email=request.POST.get('mail')
        if request.FILES.get('pic') is not None:
            t_image = request.FILES['pic']
        else:
            t_image = "images/dp.png"    

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This username already exists!!!!!!')
               
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This email already exists!!!!!!')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email
                    )
                user.save()
                U=User.objects.get(id=user.id)
                member=UserMember(user_address=t_address,user_gender=t_gender,user_contact=t_contact,user_image=t_image,user_course=course1,user=U)
                member.save()
                
                
        else:
            messages.info(request, 'Password doesnt match!!!!!!!') 
            return redirect('signup')   
        return redirect('login')
    else:
        return render(request,'signup.html')   


def user_login(request):
    if request.method=='POST':
            username=request.POST['uname']
            password=request.POST['passw']
            user = authenticate(username=username,password=password)
            request.session["uid"]=user.id
            if user is not None:
               if user.is_staff:
                  dj_login(request, user)
                  messages.info(request,f'Welcome {username}')
                  return redirect('admin_home')
               else:
                  dj_login(request,user)
                  auth.login(request,user)
                  messages.info(request,f'Welcome {username}')
                  return redirect('user_home')
            else:
               messages.info(request,'Invalid Username or password.Try again!')
               return redirect('user_login')     
    else:
        return render(request,'login.html')                    


@login_required(login_url='index')
def user_logout(request):
    auth.logout(request)
    return redirect('index')    