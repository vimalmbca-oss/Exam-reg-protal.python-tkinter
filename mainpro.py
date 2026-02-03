import tkinter as t
from tkinter import *
from tkinter import messagebox,ttk
import pymysql as pm
import random
import PIL.Image
from PIL import Image,ImageTk



main=t.Tk()
main.geometry('1366x768')
main.title("EXAM REG")
main.config(background="gray")

container=t.Frame(main,bg='black')
container.place(x=0,y=0,width=1366,height=768)

rg=t.Frame(container,bg="gray")
rd=t.Frame(container,bg="gray")
de=t.Frame(container,bg="gray")
lg=t.Frame(container,bg="GREEN")
dg=t.Frame(container,bg="YELLOW")
vg=t.Frame(container,bg="gray")
vs=t.Frame(container,bg="blue")
vr=t.Frame(container,bg="green")
rr=t.Frame(container,bg="gray")
rt=t.Frame(container,bg="gray")
rs=t.Frame(container,bg="gray")
rv=t.Frame(container,bg="gray")
vt=t.Frame(container,bg="gray")
vh=t.Frame(container,bg="gray")
mv=t.Frame(container,bg="red")

user_data = {}

def register():
    user_data["Name"] = lg_name.get()
    user_data["email"] = lg_email.get()
    user_data["phone"] = lg_phone.get()
    user_data["password"] = lg_pass.get()
    if not all(user_data.values()):
        messagebox.showerror("Error","fill the all feilds")
    else:
        messagebox.showinfo("user ID","User ID Created")
        vg.tkraise()

def personal():
    user_data["aadharno"] =vg_adhar.get()
    user_data["yourname"] = vg_names.get()
    user_data["mobilenumber"] = vg_phone.get()
    user_data["address"] = vg_address.get()
    try:
        gender=gendre
        user_data["gender"] = gender
    except:
        messagebox.showerror("error","selectgender")
    user_data["yourage"] = vg_age.get()
    user_data["dateofbirth"] =vg_date.get()
    user_data["fathername"] = vg_father.get()
    user_data["institution"] = comb2.get()
    user_data["higherqualification"] = comb3.get()
    user_data["yearofpassing"] = vs_year.get()
    user_data["nationality"] = comb4.get()
    user_data["mothertongue"] = comb5.get()
    user_data["otherlanguage"] = comb6.get()
    user_data["yourstate"] = comb7.get()
    user_data["yourcity"] = comb8.get()
    if not all(user_data.values()):
        messagebox.showerror("Error", "Fill all fields!")
    else:
        try:
            db = pm.connect(host='localhost',user='root',password='python',db='reg')
            cur = db.cursor()
            query = """INSERT INTO reg1(Name,email,phone,password,aadharno,yourname,mobilenumber,address,gender,yourage,dateofbirth,fathername,institution,higherqualification,
            yearofpassing,nationality,mothertongue,otherlanguage,yourstate,yourcity)VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            values=(user_data["Name"],user_data["email"],user_data["phone"],user_data["password"],user_data["aadharno"],user_data["yourname"],user_data["mobilenumber"],
                    user_data["address"],user_data["gender"],user_data["yourage"],user_data["dateofbirth"],user_data["fathername"],user_data["institution"],user_data["higherqualification"],user_data["yearofpassing"],user_data["nationality"],user_data["mothertongue"],user_data["otherlanguage"],user_data["yourstate"],user_data["yourcity"])
            cur.execute(query, values)
            db.commit()
            db.close()
            messagebox.showinfo("Success", "Registeration Successfully")
            vr.tkraise()


            n = user_data["yourname"]
            m = user_data["mobilenumber"]
            e = user_data["address"]
            g = user_data["gender"]
            # y =
            d = user_data["dateofbirth"]
            f = user_data["fathername"]
            i = user_data["institution"]
            h = user_data["higherqualification"]
            o = user_data["yearofpassing"]
            u = user_data["nationality"]
            w = user_data["mothertongue"]
            s = user_data["yourstate"]
            c = user_data["yourcity"]

            t.Label(rt, text=f"{n}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=140)
            t.Label(rt, text=f"{f}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=170)
            t.Label(rt, text=f"{d}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=200)
            t.Label(rt, text=f"{u}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=230)
            t.Label(rt, text=f"{g}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=260)
            #
            t.Label(rt, text=f"{m}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=360)
            t.Label(rt, text=f"{e}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=390)
            t.Label(rt, text=f"{c}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=420)
            t.Label(rt, text=f"{s}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=450)
            t.Label(rt, text=f"{u}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=480)
            #
            t.Label(rt, text=f"{i}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=570)
            t.Label(rt, text=f"{h}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=600)
            t.Label(rt, text=f"{w}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=630)
            t.Label(rt, text=f"{o}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=660)


        except Exception as e:
            messagebox.showerror("Error", str(e))

def mess():
    messagebox.showinfo("Success","Reapply Successfully")
    vt.tkraise()



def login():
    global  rs_adhar, rs_name, rs_phone, rs_address, rs_gender, rs_age, rs_date, rs_father
    global rv_ins, rv_hier, rv_year, rv_nas, rv_lan, rv_state, rv_city
    email,password=dg_email.get(),dg_pass.get()
    if not all([email,password]):
        messagebox.showerror("Error","fill the all feilds")
    else:
        db = pm.connect(user="root", port=3306, host="localhost", password="python", db="reg")
        cr = db.cursor()
        cr.execute("select * from  reg1 where email=%s and password=%s", (email, password))
        # db.commit()
        # db.close()
        dd=cr.fetchone()
        if dd:
            messagebox.showinfo("login", "login successfully")
            mv.tkraise()
            db.commit()
            db.close()
            a = dd[5]
            n = dd[6]
            m = dd[7]
            e = dd[8]
            g = dd[9]
            y = dd[10]
            d = dd[11]
            f = dd[12]
            i = dd[13]
            h = dd[14]
            o = dd[15]
            u = dd[16]
            w = dd[17]
            l = dd[18]
            s = dd[19]
            c = dd[20]


            rs_adhar = t.Entry(rs, bg="white", foreground="black", width=4, font=("verdana bold", 16))
            rs_adhar.insert(0,a)
            rs_adhar.place(x=470, y=180)
            rs_name = t.Entry(rs, bg="white", foreground="black", font=("verdana bold", 16))
            rs_name.insert(0,n)
            rs_name.place(x=335, y=230)
            rs_phone = t.Entry(rs, bg="white", foreground="black", width=15, font=("verdana bold", 16))
            rs_phone.insert(0,m)
            rs_phone.place(x=335, y=280)
            rs_address = t.Entry(rs, bg="white", foreground="black", width=50, font=("verdana bold", 16))
            rs_address.insert(0,e)
            rs_address.place(x=335, y=330)
            rs_gender = t.Entry(rs, bg="white", foreground="black", width=7,font=("verdana bold", 16))
            rs_gender.insert(0,g)
            rs_gender.place(x=340,y=385)
            rs_age = t.Entry(rs, bg="white", foreground="black", width=3, font=("verdana bold", 16))
            rs_age.insert(0,y)
            rs_age.place(x=335, y=430)
            rs_date = t.Entry(rs, bg="white", foreground="black", width=11, font=("verdana bold", 16))
            rs_date.place(x=335, y=480)
            rs_date.insert(0,d)
            rs_father = t.Entry(rs, bg="white", foreground="black", font=("verdana bold", 16))
            rs_father.insert(0,f)
            rs_father.place(x=335, y=530)
            #
            rv_ins = t.Entry(rv, bg="white",width=35, foreground="black", font=("verdana bold", 16))
            rv_ins.insert(0,i)
            rv_ins.place(x=440, y=180)
            rv_hier = t.Entry(rv, bg="white", width=35, foreground="black", font=("verdana bold", 16))
            rv_hier.insert(0,h)
            rv_hier.place(x=440, y=230)
            rv_year = t.Entry(rv, bg="white", width=5, foreground="black", font=("verdana bold", 16))
            rv_year.insert(0,o)
            rv_year.place(x=440, y=280)
            rv_nas = t.Entry(rv, bg="white", width=35, foreground="black", font=("verdana bold", 16))
            rv_nas.insert(0, u)
            rv_nas.place(x=440, y=330)
            rv_lan = t.Entry(rv, bg="white", width=35, foreground="black", font=("verdana bold", 16))
            rv_lan.insert(0,w)
            rv_lan.place(x=440, y=380)
            rv_eth = t.Entry(rv, bg="white", width=35, foreground="black", font=("verdana bold", 16))
            rv_eth.insert(0,l)
            rv_eth.place(x=440, y=430)
            rv_state = t.Entry(rv, bg="white", width=35, foreground="black", font=("verdana bold", 16))
            rv_state.insert(0,s)
            rv_state.place(x=440, y=480)
            rv_city = t.Entry(rv, bg="white", width=35, foreground="black", font=("verdana bold", 16))
            rv_city.insert(0, c)
            rv_city.place(x=440, y=530)
            #vh
            t.Label(vh, text=f"{n}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=140)
            t.Label(vh, text=f"{f}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=170)
            t.Label(vh, text=f"{d}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=200)
            t.Label(vh, text=f"{u}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=230)
            t.Label(vh, text=f"{g}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=260)
            #
            t.Label(vh, text=f"{m}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=360)
            t.Label(vh, text=f"{e}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=390)
            t.Label(vh, text=f"{c}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=420)
            t.Label(vh, text=f"{s}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=450)
            t.Label(vh, text=f"{u}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=480)
            #
            t.Label(vh, text=f"{i}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=570)
            t.Label(vh, text=f"{h}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=600)
            t.Label(vh, text=f"{w}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=630)
            t.Label(vh, text=f"{o}", bg="white", foreground="#0353a4", font=("georgia bold", 17)).place(x=360, y=660)
            #mv
            t.Label(mv, text=f"{n}", bg="white", foreground="#0353a4", font=("georgia bold", 24)).place(x=225, y=120)

        else:
            messagebox.showerror("error", "invaild data")

#update
def updates():
    try:
        db = pm.connect(host="localhost",user="root",password="python",db="reg")
        cur = db.cursor()
        query = """
            UPDATE reg1 SET 
                yourname=%s,
                mobilenumber=%s,
                address=%s,
                fathername=%s,
                institution=%s,
                higherqualification=%s,
                yearofpassing=%s,
                nationality=%s,
                mothertongue=%s,
                yourstate=%s,
                yourcity=%s
            WHERE email=%s
            """
        values=( rs_name.get(),rs_phone.get(),rs_address.get(),rs_father.get(),rv_ins.get(),rv_hier.get(),rv_year.get(),rv_nas.get(),rv_lan.get(),rv_state.get(),rv_city.get(),dg_email.get())
        cur.execute(query,values)
        db.commit()
        db.close()
        messagebox.showinfo("Success", "Data Updated Successfully")

    except Exception as e:
        messagebox.showerror("Error", str(e))




#otp
def opt():
    email = de_email.get()
    if not all([email]):
        messagebox.showerror("error", "please enter your emial")
    else:
        global a
        otp = ([str(random.randint(0, 9)) for i in range(4)])
        a = ''.join(otp)
        messagebox.showinfo("your OTP",a)

def vef():
    b=de_otp.get()
    email = de_email.get()
    if not all([email]):
        messagebox.showerror("error", "please enter your emial")

    elif b==a:
        messagebox.showinfo("info","your OTP is veified")
        lg.tkraise()

    else:
        messagebox.showerror("info","wrong OTP")

#gender
def selection():
    global gendre
    value=radio.get()
    if value==1:
        gendre="male"
    else:
        gendre="female"

def rem():
    dg_pass.delete(0, t.END)
    dg_email.delete(0,t.END)
    rg.tkraise()

def infrem():
    lg_name.delete(0, t.END)
    lg_phone.delete(0, t.END)
    lg_email.delete(0, t.END)
    lg_pass.delete(0, t.END)
    dg_pass.delete(0, t.END)
    dg_email.delete(0, t.END)
    de_otp.delete(0, t.END)
    de_email.delete(0, t.END)
    vg_adhar.delete(0, t.END)
    vg_names.delete(0, t.END)
    vg_phone.delete(0, t.END)
    vg_address.delete(0, t.END)
    vg_age.delete(0, t.END)
    vg_date.delete(0, t.END)
    vg_father.delete(0, t.END)
    comb2.set("")
    comb3.set("")
    vs_year.delete(0, t.END)
    comb4.set("")
    comb5.set("")
    comb6.set("")
    comb7.set("")
    comb8.set("")
    rg.tkraise()

def otrem():
    de_otp.delete(0, t.END)
    de_email.delete(0, t.END)
    rg.tkraise()

def fulrem():
    lg_name.delete(0, t.END)
    lg_phone.delete(0, t.END)
    lg_email.delete(0, t.END)
    lg_pass.delete(0, t.END)
    de_otp.delete(0, t.END)
    de_email.delete(0, t.END)
    vg_adhar.delete(0, t.END)
    vg_names.delete(0, t.END)
    vg_phone.delete(0, t.END)
    vg_address.delete(0, t.END)
    vg_age.delete(0, t.END)
    vg_date.delete(0, t.END)
    vg_father.delete(0, t.END)
    comb2.set("")
    comb3.set("")
    vs_year.delete(0, t.END)
    comb4.set("")
    comb5.set("")
    comb6.set("")
    comb7.set("")
    comb8.set("")
    dg.tkraise()



for page in [rg,lg,dg,de,rd,vg,vs,vr,rt,rs,rv,vt,vh,mv]:
    page.place(x=0, y=0, width=1366, height=768)

def sp(pg):
    pg.tkraise()



#main page
img=PIL.Image.open(r"C:\Users\Alex\Downloads\conny-schneider-xuTJZ7uD7PI-unsplash.jpg")
img=img.resize((1366,768))
php=PIL.ImageTk.PhotoImage(image=img)
t.Label(rg,image=php).place(x=0, y=0, width=1366, height=768)
canvas=t.Canvas(rg,width=1366,height=768)
canvas.place(x=0, y=0, width=1366, height=768)
canvas.create_image(0,0,image=php,anchor=t.NW)
canvas.create_text(670,120, text="🎓", fill="white", font=("georgia", 100, "bold"))
canvas.create_text(670,300, text="WELCOME ABOARD", fill="white", font=("georgia", 25, "bold"))
canvas.create_text(670,230, text="🎓Live Exams", fill="white", font=("georgia", 20, "bold"))
canvas.create_text(670,350, text="Find Your Dream Life!", fill="white", font=("arial", 18, "bold"))
canvas.create_text(550,500, text="Already Registered?:", fill="white", font=("arial", 18, "bold"))

t.Button(rg,text="Register Now➡",bg="#0353a4",foreground="white",font=("georgia bold",15),command=lambda:sp(rd)).place(x=570,y=400)
t.Button(rg,text="LOGIN HERE",bg="#0353a4",foreground="white",font=("georgia bold",15),height=-3,command=lambda:sp(dg)).place(x=670,y=480)

#registration
canvas=t.Canvas(lg,width=1366,height=768)
canvas.place(x=0, y=0, width=1366, height=768)
canvas.create_image(0,0,image=php,anchor=t.NW)
canvas.create_text(130,20, text="🎓Live Exams", fill="white", font=("georgia", 28, "bold"))
canvas.create_text(670,85, text="💾", fill="white", font=("georgia", 90, "bold"))
canvas.create_text(670,180, text="REGISTERATION", fill="white", font=("georgia", 25, "bold"))
canvas.create_text(500,250, text="🧑User-Name:", fill="white", font=("georgia", 18, "bold"))
lg_name=t.Entry(lg,bg="white",foreground="black",font=("verdana bold",16))
lg_name.place(x=590,y=235)

canvas.create_text(500,300, text="☎User-Phone: ", fill="white", font=("georgia", 18, "bold"))
lg_phone=t.Entry(lg,bg="white",foreground="black",font=("verdana bold",16))
lg_phone.place(x=590,y=285)


canvas.create_text(500,350, text="✉User-Email:", fill="white", font=("georgia", 18, "bold"))
lg_email=t.Entry(lg,bg="white",foreground="black",font=("verdana bold",16))
lg_email.place(x=590,y=335)

canvas.create_text(500,400, text="🔒UserPassword:      ", fill="white", font=("georgia", 18, "bold"))
lg_pass=t.Entry(lg,bg="white",foreground="black",font=("verdana bold",16),show="*")
lg_pass.place(x=590,y=385)

canvas.create_text(550,550, text="Already Registered?:", fill="white", font=("arial", 18, "bold"))
t.Button(lg,text="Register",bg="#0353a4",foreground="white",font=("georgia bold",15),width=15,command=register).place(x=570,y=450)
t.Button(lg,text="GO TO MAIN",bg="#0353a4",foreground="white",font=("georgia bold",15),width=15,command=infrem).place(x=670,y=530)
t.Button(lg,text="LOGIN",bg="#0353a4",foreground="white",font=("georgia bold",15),width=10,command=lambda:sp(dg)).place(x=1200,y=7)


#login
canvas=t.Canvas(dg,width=1366,height=768)
canvas.place(x=0, y=0, width=1366, height=768)
canvas.create_image(0,0,image=php,anchor=t.NW)
canvas.create_text(130,20, text="🎓Live Exams", fill="white", font=("georgia", 28, "bold"))
canvas.create_text(670,250, text="LOGIN", fill="white", font=("georgia", 25, "bold"))
canvas.create_text(670,150, text="👨‍", fill="white", font=("georgia", 100, "bold"))

canvas.create_text(500,300, text="✉User-Email:", fill="white", font=("georgia", 18, "bold"))
dg_email=t.Entry(dg,bg="white",foreground="black",font=("verdana bold",16))
dg_email.place(x=590,y=285)
canvas.create_text(500,350, text="🔒UserPassword:      ", fill="white", font=("georgia", 18, "bold"))
dg_pass=t.Entry(dg,bg="white",foreground="black",font=("verdana bold",16),show="*")
dg_pass.place(x=590,y=335)

canvas.create_text(540,500, text="Wanted To Exite?:", fill="white", font=("georgia", 18, "bold"))
t.Button(dg,text="LOGIN",bg="#0353a4",foreground="white",font=("georgia bold",15),width=15,command=login).place(x=570,y=400)
t.Button(dg,text="CLICK HERE",bg="#0353a4",foreground="white",font=("georgia bold",15),width=10,command=rem).place(x=660,y=480)

#userboard
canvas=t.Canvas(mv,width=1366,height=768)
canvas.place(x=0, y=0, width=1366, height=768)
canvas.create_image(0,0,image=php,anchor=t.NW)
canvas.create_text(130,20, text="🎓Live Exams", fill="white", font=("georgia", 28, "bold"))
img9=PIL.Image.open(r"C:\Users\Alex\Downloads\vima.png")
img9=img9.resize((1200,630))
ph8=PIL.ImageTk.PhotoImage(image=img9)
t.Label(mv,image=ph8).place(x=80,y=70,width=1200,height=630)
t.Label(mv,text="HOME",bg="white",foreground="#343a40",font=("georgia bold",20)).place(x=110,y=70)
# t.Label(mv, text="vimal", bg="white", foreground="black", font=("georgia bold", 24)).place(x=225, y=120)
t.Label(mv, text="Hey", bg="white", foreground="#0353a4", font=("georgia bold", 24)).place(x=150, y=120)
t.Label(mv, text="Welcome aboard on 🎓Live Exam", bg="white", foreground="#0353a4", font=("georgia bold", 20)).place(x=150, y=170)
t.Label(mv,text="------------------------------------------------------------------------------------------------------------------------------------",bg="white",foreground="black",font=("georgia bold",18)).place(x=80,y=200)
paragraph = """-Live Exams is an advanced online examination platform designed to simplify student registration and exam management.
-Our system allows students to securely create accounts, update personal details, and apply for competitive exams with ease.
-We provide a user-friendly interface that ensures smooth navigation and a hassle-free experience.
-The platform maintains data security and accuracy to protect student information at every step.
-Live Exams helps institutions manage applications efficiently and transparently.
-Our mission is to make the examination process simple, reliable, and accessible for everyone.

-So,go ahead Explore opportunities.Experience Certainty
"""
t.Label(mv, text=paragraph, bg="white", foreground="#343a40", font=("georgia bold", 14),wraplength=950,justify="left").place(x=150, y=240)
t.Label(mv,text="------------------------------------------------------------------------------------------------------------------------------------",bg="white",foreground="black",font=("georgia bold",18)).place(x=80,y=540)
t.Button(mv,text="EDIT-MYDATA",bg="#70e000",foreground="white",font=("georgia bold",15),width=15,command=lambda:sp(rs)).place(x=460,y=600)
t.Button(mv,text="VIEW-FORM",bg="#70e000",foreground="white",font=("georgia bold",15),width=15,command=lambda:sp(vh) ).place(x=690,y=600)
t.Button(mv,text="EXIT",bg="#0353a4",foreground="white",font=("georgia bold",15),width=10,command=lambda:sp(rg)).place(x=1200,y=7)





#rd
canvas=t.Canvas(rd,width=1366,height=768)
canvas.place(x=0, y=0, width=1366, height=768)
canvas.create_image(0,0,image=php,anchor=t.NW)
canvas.create_text(130,20, text="🎓Live Exams", fill="white", font=("georgia", 28, "bold"))
canvas.create_text(670,250, text="SELECT CATRGORY", fill="white", font=("georgia", 20, "bold"))
canvas.create_text(670,150, text="💻", fill="white", font=("georgia", 100, "bold"))
t.Button(rd,text="IT",bg="#0353a4",foreground="white",font=("georgia bold",15),width=15,command=lambda:sp(de)).place(x=400,y=300)
t.Button(rd,text="BPS",bg="#0353a4",foreground="white",font=("georgia bold",15),width=15,command=lambda:sp(de)).place(x=670,y=300)
canvas.create_text(550,550, text="Go To Main:", fill="white", font=("georgia", 20, "bold"))
t.Button(rd,text="CLICK HERE",bg="#0353a4",foreground="white",font=("georgia bold",15),width=10,command=lambda:sp(rg)).place(x=640,y=530)
img1=PIL.Image.open(r"C:\Users\Alex\Downloads\download (22).jpg")
img1=img1.resize((250,150))
ph=PIL.ImageTk.PhotoImage(image=img1)
t.Label(rd,image=ph).place(x=380,y=360,width=250,height=150)
t.Button(rd,text="LOGIN",bg="#0353a4",foreground="white",font=("georgia bold",15),width=10,command=lambda:sp(dg)).place(x=1200,y=7)

img2=PIL.Image.open(r"C:\Users\Alex\Downloads\download (23).jpg")
img2=img2.resize((250,150))
ph1=PIL.ImageTk.PhotoImage(image=img2)
t.Label(rd,image=ph1).place(x=660,y=360,width=250,height=150)

#de
canvas=t.Canvas(de,width=1366,height=768)
canvas.place(x=0, y=0, width=1366, height=768)
canvas.create_image(0,0,image=php,anchor=t.NW)
canvas.create_text(130,20, text="🎓Live Exams", fill="white", font=("georgia", 28, "bold"))
canvas.create_text(670,220, text="Email - Verification", fill="white", font=("georgia", 25, "bold"))
canvas.create_text(670,150, text="✉", fill="white", font=("georgia", 100, "bold"))

canvas.create_text(500,280, text="✉User-Email:", fill="white", font=("georgia", 18, "bold"))
de_email=t.Entry(de,bg="white",foreground="black",font=("verdana bold",16))
de_email.place(x=590,y=265)
t.Button(de,text="Get OTP",bg="#0353a4",foreground="white",font=("georgia bold",15),width=15,command=opt).place(x=570,y=320)

canvas.create_text(515,405, text="Enter-OTP:", fill="white", font=("georgia", 18, "bold"))
de_otp=t.Entry(de,bg="white",foreground="black",font=("verdana bold",16))
de_otp.place(x=590,y=390)
t.Button(de,text="Procceed",bg="#0353a4",foreground="white",font=("georgia bold",15),width=15,command=vef).place(x=570,y=445)

canvas.create_text(550,570, text="Go To Main:", fill="white", font=("georgia", 20, "bold"))
t.Button(de,text="CLICK HERE",bg="#0353a4",foreground="white",font=("georgia bold",15),width=10,command=otrem).place(x=640,y=550)
t.Button(de,text="LOGIN",bg="#0353a4",foreground="white",font=("georgia bold",15),width=10,command=lambda:sp(dg)).place(x=1200,y=7)
#vg
canvas=t.Canvas(vg,width=1366,height=768)
canvas.place(x=0, y=0, width=1366, height=768)
canvas.create_image(0,0,image=php,anchor=t.NW)
canvas.create_text(130,20, text="🎓Live Exams", fill="white", font=("georgia", 28, "bold"))
img3=PIL.Image.open(r"C:\Users\Alex\Downloads\vima.png")
img3=img3.resize((1200,620))
ph2=PIL.ImageTk.PhotoImage(image=img3)


t.Label(vg,image=ph2).place(x=80,y=70,width=1200,height=620)

t.Label(vg,text="👨‍Personal-Details",bg="white",foreground="black",font=("georgia bold",20)).place(x=560,y=100)
t.Label(vg,text="Aadhar no:xxxx-xxxx-",bg="white",foreground="black",font=("verdana bold",16)).place(x=200,y=180)
vg_adhar=t.Entry(vg,bg="white",foreground="black",width=4,font=("verdana bold",16))
vg_adhar.place(x=470,y=180)

t.Label(vg,text="YourName:",bg="white",foreground="black",font=("verdana bold",16)).place(x=200,y=230)
vg_names=t.Entry(vg,bg="white",foreground="black",font=("verdana bold",16))
vg_names.place(x=335,y=230)

t.Label(vg,text="Mobile-no :",bg="white",foreground="black",font=("verdana bold",16)).place(x=200,y=280)
vg_phone=t.Entry(vg,bg="white",foreground="black",width=15,font=("verdana bold",16))
comb1=ttk.Combobox(vg,values=['+91','+1','+82','+44','+33'],font="arial 15",width=4,state="r").place(x=335,y=280)
vg_phone.place(x=400,y=280)

t.Label(vg,text="  Address  :",bg="white",foreground="black",font=("verdana bold",16)).place(x=200,y=330)
vg_address=t.Entry(vg,bg="white",foreground="black",width=50,font=("verdana bold",16))
vg_address.place(x=335,y=330)

radio=IntVar()

t.Label(vg,text=" Gender    :",bg="white",foreground="black",font=("verdana bold",16)).place(x=200,y=380)
r1=ttk.Radiobutton(vg,text="MALE",variable=radio,value=1,command=selection)
r1.place(x=340,y=385)
r2=ttk.Radiobutton(vg,text="FEMALE",variable=radio,value=2,command=selection)
r2.place(x=420,y=385)

t.Label(vg,text="YourAge:",bg="white",foreground="black",font=("verdana bold",16)).place(x=220,y=430)
vg_age=t.Entry(vg,bg="white",foreground="black",width=3,font=("verdana bold",16))
vg_age.place(x=335,y=430)

t.Label(vg,text="DateOfBirth:",bg="white",foreground="black",font=("verdana bold",16)).place(x=180,y=480)
vg_date=t.Entry(vg,bg="white",foreground="black",width=11,font=("verdana bold",16))
vg_date.place(x=335,y=480)
vg_date.insert(0,"dd/mm/yyyy")
# vg_date = Calendar(vg,selectmode="day",year=2000,month=1,day=1,date_pattern="dd/mm/yyyy")
# vg_date.place(x=335,y=480)

t.Label(vg,text=" FatherName:",bg="white",foreground="black",font=("verdana bold",16)).place(x=170,y=530)
vg_father=t.Entry(vg,bg="white",foreground="black",font=("verdana bold",16))
vg_father.place(x=335,y=530)


t.Button(vg,text="NEXT➡",bg="#70e000",foreground="white",font=("georgia bold",15),width=15,command=lambda:sp(vs)).place(x=570,y=600)
t.Button(vg,text="LOGIN",bg="#0353a4",foreground="white",font=("georgia bold",15),width=10,command=fulrem).place(x=1200,y=7)

#vs
canvas=t.Canvas(vs,width=1366,height=768)
canvas.place(x=0, y=0, width=1366, height=768)
canvas.create_image(0,0,image=php,anchor=t.NW)
canvas.create_text(130,20, text="🎓Live Exams", fill="white", font=("georgia", 28, "bold"))
img4=PIL.Image.open(r"C:\Users\Alex\Downloads\vima.png")
img4=img4.resize((1200,620))
ph3=PIL.ImageTk.PhotoImage(image=img4)
t.Label(vs,image=ph3).place(x=80,y=70,width=1200,height=620)



t.Label(vs,text="📖Other-Details",bg="white",foreground="black",font=("georgia bold",20)).place(x=560,y=100)
t.Label(vs,text="Institution:",bg="white",foreground="black",font=("verdana bold",16)).place(x=200,y=180)
comb2=ttk.Combobox(vs,values=['Loyola College, Chennai','Mahandra Arts And Scinece college,Salem','PSG College of Arts and Science, Coimbatore','Government Arts College, Coimbatore','Indian Institute of Technology Madras (IIT Madras), Chennai'],font="arial 15",width=40,state="r")
comb2.place(x=440,y=180)

t.Label(vs,text="HigherQualification:",bg="white",foreground="black",font=("verdana bold",16)).place(x=200,y=230)
comb3=ttk.Combobox(vs,values=['Bachelor of Computer Applications','Bachelor of Fine Arts ','M.Sc. in Physics','M.Sc. in Mathematics','M.Sc. in Computer Science','Master of Commerce (M.Com.)','M.Sc. in Data Science'],font="arial 15",width=40,state="r")
comb3.place(x=440,y=230)

t.Label(vs,text="YearOfPassing:",bg="white",foreground="black",font=("verdana bold",16)).place(x=200,y=280)
vs_year=t.Entry(vs,bg="white",foreground="black",font=("arial bold",16))
vs_year.place(x=440,y=280)



t.Label(vs,text="Nationality:",bg="white",foreground="black",font=("verdana bold",16)).place(x=200,y=330)
comb4=ttk.Combobox(vs,values=['India','United States','United Kingdom','Canada','Australia','France','Italy'],font="arial 15",state="r")
comb4.place(x=440,y=330)


t.Label(vs,text="MotherTongue:",bg="white",foreground="black",font=("verdana bold",16)).place(x=200,y=380)
comb5=ttk.Combobox(vs,values=['Tamil','English','Hindi','Malayalam','Kannada','Telugu','Sanskrit','Marathi'],font="arial 15",state="r")
comb5.place(x=440,y=380)


t.Label(vs,text="OtherLanguage:",bg="white",foreground="black",font=("verdana bold",16)).place(x=200,y=430)
comb6=ttk.Combobox(vs,values=['Tamil','English','Hindi','Malayalam','Kannada','Telugu','Sanskrit','Marathi'],font="arial 15",state="r")
comb6.place(x=440,y=430)


t.Label(vs,text="YourState:",bg="white",foreground="black",font=("verdana bold",16)).place(x=200,y=480)
comb7=ttk.Combobox(vs,values=['Andhra Pradesh','Tamil Nadu ','Punjab','Telangana','Karnataka','Kerala','Maharashtra'],font="arial 15",state="r")
comb7.place(x=440,y=480)

t.Label(vs,text="YourCity:",bg="white",foreground="black",font=("verdana bold",16)).place(x=200,y=530)
comb8=ttk.Combobox(vs,values=['Mumbai','Delhi','Chennai','Bengaluru','Salem','Coimbatore','Trichy','Tirunelveli','Hyderabad'],font="arial 15",state="r")
comb8.place(x=440,y=530)


t.Button(vs,text="⬅GOBACK",bg="#70e000",foreground="white",font=("georgia bold",15),width=15,command=lambda:sp(vg)).place(x=350,y=600)
t.Button(vs,text="Submite➡",bg="#70e000",foreground="white",font=("georgia bold",15),width=15,command=personal).place(x=590,y=600)
t.Button(vs,text="LOGIN",bg="#0353a4",foreground="white",font=("georgia bold",15),width=10,command=fulrem).place(x=1200,y=7)

#vr
canvas=t.Canvas(vr,width=1366,height=768)
canvas.place(x=0, y=0, width=1366, height=768)
canvas.create_image(0,0,image=php,anchor=t.NW)
canvas.create_text(670,120, text="🎓", fill="white", font=("georgia", 100, "bold"))
canvas.create_text(670,300, text="WELCOME ABOARD", fill="white", font=("georgia", 25, "bold"))
canvas.create_text(670,230, text="🎓Live Exams", fill="white", font=("georgia", 20, "bold"))
canvas.create_text(670,350, text="Your Registration Is Completed", fill="white", font=("arial", 18, "bold"))
canvas.create_text(670,400, text="Be Prepare For Your Examination", fill="white", font=("arial", 18, "bold"))
canvas.create_text(670,450, text="Good Luck", fill="white", font=("arial", 18, "bold"))
canvas.create_text(670,500, text="Your Exam Form Is Submitted", fill="white", font=("arial", 18, "bold"))
t.Button(vr,text="View Your Form ",bg="#0353a4",foreground="white",font=("georgia bold",15),command=lambda:sp(rt)).place(x=590,y=550)


t.Button(vr,text="EXIT",bg="#0353a4",foreground="white",font=("georgia bold",15),width=10,command=infrem).place(x=1200,y=7)

#rt
canvas=t.Canvas(rt,width=1366,height=768)
canvas.place(x=0, y=0, width=1366, height=768)
canvas.create_image(0,0,image=php,anchor=t.NW)
canvas.create_text(130,20, text="🎓Live Exams", fill="white", font=("georgia", 28, "bold"))
img5=PIL.Image.open(r"C:\Users\Alex\Downloads\vima.png")
img5=img5.resize((1200,630))
ph4=PIL.ImageTk.PhotoImage(image=img5)
t.Label(rt,image=ph4).place(x=80,y=70,width=1200,height=630)
t.Label(rt,text="🎓Live Exams Registration Form",bg="white",foreground="black",font=("georgia bold",20)).place(x=460,y=70)
t.Label(rt,text="👨‍Personal-Details:",bg="white",foreground="black",font=("georgia bold",18)).place(x=80,y=100)
t.Label(rt,text="StudentName:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=140)
t.Label(rt,text="FatherName:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=170)
t.Label(rt,text="DateOfBirth:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=200)
t.Label(rt,text="Nationality:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=230)
t.Label(rt,text="Gender:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=260)
t.Label(rt,text="------------------------------------------------------------------------------------------------------------------------------------",bg="white",foreground="black",font=("georgia bold",18)).place(x=80,y=290)
t.Label(rt,text="📄Contacts",bg="white",foreground="black",font=("georgia bold",18)).place(x=80,y=320)
t.Label(rt,text="PhoneNo:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=360)
t.Label(rt,text="Address:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=390)
t.Label(rt,text="City:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=420)
t.Label(rt,text="State:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=450)
t.Label(rt,text="country:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=480)
t.Label(rt,text="------------------------------------------------------------------------------------------------------------------------------------",bg="white",foreground="black",font=("georgia bold",18)).place(x=80,y=510)
t.Label(rt,text="📖Education-Details",bg="white",foreground="black",font=("georgia bold",18)).place(x=80,y=540)
t.Label(rt,text="Institution:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=570)
t.Label(rt,text="HigherQualification:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=600)
t.Label(rt,text="MotherTongue:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=630)
t.Label(rt,text="YearOfPassing:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=660)

t.Button(rt,text="EXIT",bg="#0353a4",foreground="white",font=("georgia bold",15),width=10,command=lambda:sp(rg)).place(x=1200,y=7)


#rs
canvas=t.Canvas(rs,width=1366,height=768)
canvas.place(x=0, y=0, width=1366, height=768)
canvas.create_image(0,0,image=php,anchor=t.NW)
canvas.create_text(130,20, text="🎓Live Exams", fill="white", font=("georgia", 28, "bold"))
img6=PIL.Image.open(r"C:\Users\Alex\Downloads\vima.png")
img6=img6.resize((1200,620))
ph5=PIL.ImageTk.PhotoImage(image=img6)
t.Label(rs,image=ph5).place(x=80,y=70,width=1200,height=620)
t.Label(rs,text="👨‍Personal-Details",bg="white",foreground="black",font=("georgia bold",20)).place(x=560,y=100)
t.Label(rs,text="Aadhar no:xxxx-xxxx-",bg="white",foreground="black",font=("verdana bold",16)).place(x=200,y=180)
t.Label(rs,text="YourName:",bg="white",foreground="black",font=("verdana bold",16)).place(x=200,y=230)
t.Label(rs,text="Mobile-no :",bg="white",foreground="black",font=("verdana bold",16)).place(x=200,y=280)
t.Label(rs,text="  Address  :",bg="white",foreground="black",font=("verdana bold",16)).place(x=200,y=330)
t.Label(rs,text=" Gender    :",bg="white",foreground="black",font=("verdana bold",16)).place(x=200,y=380)
t.Label(rs,text="YourAge:",bg="white",foreground="black",font=("verdana bold",16)).place(x=220,y=430)
t.Label(rs,text="DateOfBirth:",bg="white",foreground="black",font=("verdana bold",16)).place(x=180,y=480)
t.Label(rs,text=" FatherName:",bg="white",foreground="black",font=("verdana bold",16)).place(x=170,y=530)

t.Button(rs,text="NEXT➡",bg="#70e000",foreground="white",font=("georgia bold",15),width=15,command=lambda:sp(rv)).place(x=570,y=600)
t.Button(rs,text="HOME",bg="#0353a4",foreground="white",font=("georgia bold",15),width=10,command=lambda:sp(mv)).place(x=1200,y=7)

#rv
canvas=t.Canvas(rv,width=1366,height=768)
canvas.place(x=0, y=0, width=1366, height=768)
canvas.create_image(0,0,image=php,anchor=t.NW)
canvas.create_text(130,20, text="🎓Live Exams", fill="white", font=("georgia", 28, "bold"))
img7=PIL.Image.open(r"C:\Users\Alex\Downloads\vima.png")
img7=img7.resize((1200,620))
ph6=PIL.ImageTk.PhotoImage(image=img7)
t.Label(rv,image=ph6).place(x=80,y=70,width=1200,height=620)
t.Label(rv,text="📖Other-Details",bg="white",foreground="black",font=("georgia bold",20)).place(x=560,y=100)
t.Label(rv,text="Institution:",bg="white",foreground="black",font=("verdana bold",16)).place(x=200,y=180)
t.Label(rv,text="HigherQualification:",bg="white",foreground="black",font=("verdana bold",16)).place(x=200,y=230)
t.Label(rv,text="YearOfPassing:",bg="white",foreground="black",font=("verdana bold",16)).place(x=200,y=280)
t.Label(rv,text="Nationality:",bg="white",foreground="black",font=("verdana bold",16)).place(x=200,y=330)
t.Label(rv,text="MotherTongue:",bg="white",foreground="black",font=("verdana bold",16)).place(x=200,y=380)
t.Label(rv,text="OtherLanguage:",bg="white",foreground="black",font=("verdana bold",16)).place(x=200,y=430)
t.Label(rv,text="YourState:",bg="white",foreground="black",font=("verdana bold",16)).place(x=200,y=480)
t.Label(rv,text="YourCity:",bg="white",foreground="black",font=("verdana bold",16)).place(x=200,y=530)

t.Button(rv,text="⬅GOBACK",bg="#70e000",foreground="white",font=("georgia bold",15),width=15,command=lambda:sp(rs)).place(x=350,y=600)
t.Button(rv,text="UPDATE&SUBMIT➡",bg="#70e000",foreground="white",font=("georgia bold",15),width=15,command=updates).place(x=590,y=600)
t.Button(rv,text="HOME",bg="#0353a4",foreground="white",font=("georgia bold",15),width=10,command=lambda:sp(mv)).place(x=1200,y=7)

#vt
canvas=t.Canvas(vt,width=1366,height=768)
canvas.place(x=0, y=0, width=1366, height=768)
canvas.create_image(0,0,image=php,anchor=t.NW)
canvas.create_text(670,120, text="🎓", fill="white", font=("georgia", 100, "bold"))
canvas.create_text(670,300, text="WELCOME ABOARD", fill="white", font=("georgia", 25, "bold"))
canvas.create_text(670,230, text="🎓Live Exams", fill="white", font=("georgia", 20, "bold"))
canvas.create_text(670,350, text="Your Registration Is Completed", fill="white", font=("arial", 18, "bold"))
canvas.create_text(670,400, text="Be Prepare For Your Examination", fill="white", font=("arial", 18, "bold"))
canvas.create_text(670,450, text="Good Luck", fill="white", font=("arial", 18, "bold"))
canvas.create_text(670,500, text="Your Exam Form Is Submitted", fill="white", font=("arial", 18, "bold"))
t.Button(vt,text="View Your Form ",bg="#0353a4",foreground="white",font=("georgia bold",15),command=lambda:sp(vh)).place(x=590,y=550)


t.Button(vt,text="EXIT",bg="#0353a4",foreground="white",font=("georgia bold",15),width=10,command=infrem).place(x=1200,y=7)

#vh
canvas=t.Canvas(vh,width=1366,height=768)
canvas.place(x=0, y=0, width=1366, height=768)
canvas.create_image(0,0,image=php,anchor=t.NW)
canvas.create_text(130,20, text="🎓Live Exams", fill="white", font=("georgia", 28, "bold"))
img8=PIL.Image.open(r"C:\Users\Alex\Downloads\vima.png")
img8=img8.resize((1200,630))
ph7=PIL.ImageTk.PhotoImage(image=img8)
t.Label(vh,image=ph7).place(x=80,y=70,width=1200,height=630)
t.Label(vh,text="🎓Live Exams Registration Form",bg="white",foreground="black",font=("georgia bold",20)).place(x=460,y=70)
t.Label(vh,text="👨‍Personal-Details",bg="white",foreground="black",font=("georgia bold",18)).place(x=80,y=100)
t.Label(vh,text="StudentName:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=140)
t.Label(vh,text="FatherName:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=170)
t.Label(vh,text="DateOfBirth:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=200)
t.Label(vh,text="Nationality:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=230)
t.Label(vh,text="Gender:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=260)
t.Label(vh,text="------------------------------------------------------------------------------------------------------------------------------------",bg="white",foreground="black",font=("georgia bold",18)).place(x=80,y=290)
t.Label(vh,text="📄Contacts",bg="white",foreground="black",font=("georgia bold",18)).place(x=80,y=320)
t.Label(vh,text="PhoneNo:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=360)
t.Label(vh,text="Address:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=390)
t.Label(vh,text="City:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=420)
t.Label(vh,text="State:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=450)
t.Label(vh,text="country:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=480)
t.Label(vh,text="------------------------------------------------------------------------------------------------------------------------------------",bg="white",foreground="black",font=("georgia bold",18)).place(x=80,y=510)
t.Label(vh,text="📖Education-Details",bg="white",foreground="black",font=("georgia bold",18)).place(x=80,y=540)
t.Label(vh,text="Institution:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=570)
t.Label(vh,text="HigherQualification:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=600)
t.Label(vh,text="MotherTongue:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=630)
t.Label(vh,text="YearOfPassing:",bg="white",foreground="black",font=("georgia bold",17)).place(x=110,y=660)

t.Button(vh,text="HOME",bg="#0353a4",foreground="white",font=("georgia bold",15),width=10,command=lambda:sp(mv)).place(x=1200,y=7)
t.Button(vh,text="REAPPLY",bg="#0353a4",foreground="white",font=("georgia bold",15),width=10,command=mess).place(x=1040,y=7)





rg.tkraise()
main.mainloop()











