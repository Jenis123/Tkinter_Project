from django.shortcuts import render, redirect
from django.http import HttpResponse
from projectApp.models import employee ,student, uniq
import re
from django.contrib import messages
from django.contrib.auth import logout
from .forms import UniqForm



def login(request):
    try:
        if request.POST:
            email = request.POST['email']
            password = request.POST['password']
            print("---email ,",email)

            uid = student.objects.filter(email = email)   # ""
            if len(uid) == 0:
                msg= "invalid email or password"
                return render(request,"login.html",{'msg':msg})
            
            elif uid[0].password == password:
                print("sucessfully")
                request.session['email'] = email
                return redirect("disp_index")
            else:
                msg= "invalid email or password"
                return render(request,"login.html",{'msg':msg})
        else:
            return render(request,"login.html")
    # except KeyError as e:
    #     return redirect('login')
    # except IndexError  as e:
    #     msg= "invalid email or password"
    #     return render(request,"login.html",{'msg':msg})
    except Exception as e:
        print(e,"------------------------login")
        return redirect('error')
        
def index(request):
    return render(request,"index.html")

def home(request):
    uid = student.objects.filter(email = request.session['email'])
    if len(uid)!=0:
        h= employee.objects.all()
        return render (request,"dis_index.html",{'uid':uid,'h':h})
    else:
        return render (request,"login.html")

def logout_student(request):
    logout(request)
    return redirect('login')  


def disp_index(request):
    # if request.user.is_authenticated:
    #     return redirect('disp_index')
    
    if request.method=="POST":

        print("post")
        fname = request.POST.get('fname') 
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        address = request.POST.get('address') 
        hobbies = request.POST.get('hobbies') 
        department = request.POST.get('department')
        
        xyz = employee.objects.create(fname=request.POST.get('fname'),
                                lname=request.POST.get('lname'),
                                gender=request.POST.get('gender'),
                                address=request.POST.get('address'),
                                hobbies=", ".join(request.POST.getlist('checks[]')),
                                department=request.POST.get('department'))
    
        h = employee.objects.all()
        # print("-------------",h)
        return render(request,"dis_index.html",{'h':h})

    else:
        print("fetch")
        h = employee.objects.all()
        return render(request,"dis_index.html",{'h':h})


def select_index(request, id):
    empp = employee.objects.get(no=id)
    print(empp.hobbies, type(empp.hobbies))
    a = empp.hobbies.split(",") 
    print(a)
    return render(request, 'edit.html', {'empp': empp,'a':a})

    

def update_index(request, id):
    if request.method == "GET":
        empp = employee.objects.get(no=id)
        return render (request, 'edit.html',{'empp':empp,'a':a})
        
    elif request.method == "POST":
        up_fname = request.POST['fname']
        up_lname = request.POST['lname']
        up_gender = request.POST['gender']
        up_address = request.POST['address']
        a = ",".join(request.POST.getlist('hobbies'))
        up_department = request.POST['department']

        empp = employee.objects.get(no=id)

        empp.fname = up_fname
        empp.lname = up_lname
        empp.gender = up_gender
        empp.address = up_address
        empp.hobbies = a
        empp.department = up_department
        empp.save()
        return redirect('/disp_index/')
    
    return render(request,"dis_index.html")
    
def delete_index(request, id):
    employeee = employee.objects.get(no=id)
    del_emp = employeee.delete()

    return  redirect("/disp_index/",{'del_emp':del_emp})


def register(request):
    try:
        if request.method=="POST":
            user_name=request.POST['username']
            email=request.POST['email']
            mobileno=request.POST['phoneno']
            password=request.POST['password']
            repeat_password=request.POST['confirm_password']
            print("username : ",user_name)

            # email
            regex = r'\b[A-Za-z0-9._%+-]+@gmail.com\b'

            if(re.fullmatch(regex, email)):
                pass   
            else:
                print("invalid email")
                e_msg = "invalid email"
                return render(request,"registration.html",{'e_msg':e_msg})


            #  mobile no:
            
            if mobileno.isdigit():
                if len(mobileno)== 10:
                    print("valid")
                else:
                    print("invalid")
                    m_msg = "invalid phone number"
                    return render(request,"registration.html",{'m_msg':m_msg}) 
            else:
                print("invalid data")
                m_msg = "invalid phone number"
                return render(request,"registration.html",{'m_msg':m_msg})

        
            # password 

            reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

            if len(password)>=8 :
                if(re.fullmatch(reg, password)):
                    pass   
                else:
                    print("invalid email")
                    p_msg = "invalid password"
                    return render(request,"registration.html",{'p_msg':p_msg}) 
            else:
                print("password too short")
                p_msg = "invalid password"
                return render(request,"registration.html",{'p_msg':p_msg}) 


            if password == repeat_password :
                pass
            else:
                p_msg = "invalid password"
                print("password does not match",{'p_msg':p_msg})

            uid= student.objects.create(
                                        username=user_name,
                                        email=email,
                                        phone_no=mobileno,
                                        password=password
                                    )

            context={
                'uid':uid
            }
            print("sucessfully registerd ")
        
            return render(request,"login.html",{'uid':uid})
        else:
            return render(request,"registration.html")
    except:
         print("Something else went wrong")         
            
            
  
def error(request):
    return render(request,"error.html")


# def emp_insert(request):
#     # form = UniqForm()
#     if request.method == 'POST':
#         form = UniqForm(request.POST)
#         if  form.is_valid():
#             x = form.cleaned_data['hobbies']
#             print(x)
#             hobbies = ",".join(x)
#             # hobbies.save()
#             # form.set('hobbies', 'hobbies');
#             form['hobbies'] = hobbies 
#             print("************************valid",hobbies)
#             form.save()
#             print("-------------form")
#             return redirect('emp_disp')
            
#                 # print("=================================")
#                 # return render(request, 'emp_insert.html',{'form':form})
#         else:
#             print("////////////////////////")
#             return render(request, 'emp_insert.html',{'form':form})
#     else:
#         form = UniqForm()
#         return render(request, 'emp_insert.html',{'form':form})
            
            
def emp_insert(request):
    # form = UniqForm()
    if request.method == 'POST':
        form = UniqForm(request.POST)
        if  form.is_valid():
            # emp_form = form.save(commit = False)
            # x = form.cleaned_data['hobbies']
            # hobby = ",".join(x)
            # print(hobby)
            
            # emp_form.hobbies = hobby
            
            form.save()
            return redirect('emp_disp')

        else:
            print("////////////////////////")
            return render(request, 'emp_insert.html',{'form':form})
    else:
        form = UniqForm()
        return render(request, 'emp_insert.html',{'form':form})
    

def emp_disp(request):
    emp_all = uniq.objects.all()
    
    for x in emp_all:
        
        print("===========",x.hobbies)
        h = x.hobbies
       
        if h[0] =="[" and h[-1] =="]":
            print("#########################",type(h))
        # d = ",".join(h)
            x.hobbies = h[1:-1]
    
    return render(request, 'emp_disp.html',{'emp_all':emp_all})

def emp_select(request,id):
    uniqq = uniq.objects.get(uniq_id=id)
    form = UniqForm(instance=uniqq)
    return render(request, 'emp_update.html', {'uniqq': form})

def emp_update(request,id):
    if request.method == "GET":
        uniqq = uniq.objects.get(uniq_id=id)
        form = UniqForm(instance=uniqq)
        return render(request, 'emp_update.html', {'uniqq': form})
    elif request.method=="POST":
        print("=============", uniqq)
        form = UniqForm(request.POST, instance=uniqq)
        print("++++++++++++++", form.errors)
        if form.is_valid():
            print("===========================================")
            form.save()
            return redirect("/emp_disp/")
        # return render(request, 'emp_update.html', {'uniqq': form})


#  if request.method == "GET":
#         empp = employee.objects.get(no=id)
#         return render (request, 'edit.html',{'empp':empp,'a':a})
        
#     elif request.method == "POST":
#         up_fname = request.POST['fname']
#         up_lname = request.POST['lname']
#         up_gender = request.POST['gender']
#         up_address = request.POST['address']
#         a = ",".join(request.POST.getlist('hobbies'))
#         up_department = request.POST['department']

#         empp = employee.objects.get(no=id)

#         empp.fname = up_fname
#         empp.lname = up_lname
#         empp.gender = up_gender
#         empp.address = up_address
#         empp.hobbies = a
#         empp.department = up_department
#         empp.save()
#         return redirect('/disp_index/')
    
#     return render(request,"dis_index.html")
    