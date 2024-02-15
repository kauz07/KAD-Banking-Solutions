from tkinter import * # imported tkinter module
from tkinter import messagebox # imported tkinter messagebox module
from tkinter import ttk # imported ttk for using combobox
import re

'''   ---------- connecting with mysql.connector -------------  '''

import mysql.connector as ms # imported mysql.connector
connection = ms.connect(host='localhost',user='root',password='1883',database='nb')
mycursor = connection.cursor() # created cursor

'''   -----------------------------x--------------------------  '''

'''   ---------- creating welcome window -------------  '''

welcome_screen = Tk() # created a welcome window
welcome_screen.geometry("1100x700+220+80") # set a geometry for welcome window
welcome_screen.resizable(0,0) # for not resizing the welcome window
welcome_screen.title("  NET BANKING") # setting the title
welcome_screen.iconbitmap(default="directory\\window_icon\\window_icon.ico") # setting icon

'''   -------------------------x----------------------  '''

'''   ------------- importing png images -------------  '''

bank_icon = PhotoImage(file="directory\\png_helper\\bank.png") #bank directory
dollar_icon = PhotoImage(file="directory\\png_helper\\dollar.png") #dollar directory
withdraw_icon = PhotoImage(file="directory\\png_helper\\withdraw.png") #withdraw directory
deposit_icon = PhotoImage(file="directory\\png_helper\\deposit.png") #deposit directory
check_your_balance_icon = PhotoImage(file="directory\\png_helper\\check_your_balance.png") #check_your_balance directory
change_your_pin_icon = PhotoImage(file="directory\\png_helper\\change_your_pin.png") #change_your_pin directory
account_info_icon = PhotoImage(file="directory\\png_helper\\account_info.png") #account_info directory
username_icon = PhotoImage(file="directory\\png_helper\\account_info.png") #username directory
password_icon = PhotoImage(file="directory\\png_helper\\password.png") #password directory
new_icon = PhotoImage(file="directory\\png_helper\\new.png") #new directory
confirm_icon = PhotoImage(file="directory\\png_helper\\confirm.png") #confirm directory

window_bg = PhotoImage(file="directory\\window_bg\\window_bg.png") # window_bg directory

'''   ------------------------x-----------------------  '''

'''   --------------- defining functions --------------  '''

global_username = [" "]
menu_im = [" "," "," "," "," "]
menu_btn = [" "," "," "," "," "]

def fetch_usernames():
        mycursor.execute("select user_name from users;")
        usernames = mycursor.fetchall()
        row = mycursor.rowcount
        us_name = []
        for i in range(row):
                us_name.append(usernames[i][0])
        return us_name

def fetch_password():
        query = "select password from users where user_name = '{}';".format(global_username[0])
        mycursor.execute(query)
        password = mycursor.fetchone()
        password = password[0]
        return password

def fetch_balance():
        query = "select balance from users where user_name = '{}';".format(global_username[0])
        mycursor.execute(query)
        balance = mycursor.fetchone()
        balance = balance[0]
        return balance

def fetch_dob():
        query = "select dob from users where user_name = '{}';".format(global_username[0])
        mycursor.execute(query)
        dob = mycursor.fetchone()
        dob = dob[0]
        return dob

def fetch_gender():
        query = "select gender from users where user_name = '{}';".format(global_username[0])
        mycursor.execute(query)
        gender = mycursor.fetchone()
        gender = gender[0]
        return gender

def save_un_ps_ba_dob_gen(password,dob,gen):
        if (gen==1):
                gender = "MALE"
        else:
                gender = "FEMALE"
        query = "insert into users values('{}','{}',{},'{}','{}');".format(global_username[0],password,0,dob,gender)
        mycursor.execute(query)
        mycursor.execute("commit;")

def update_ps(new_ps):
        un = global_username[0]
        query = "update users set password = '{}' where user_name = '{}';".format(new_ps,un)
        mycursor.execute(query)
        mycursor.execute("commit;")

def update_ba(new_ba):
        un = global_username[0]
        query = "update users set balance = {} where user_name = '{}';".format(new_ba,un)
        mycursor.execute(query)
        mycursor.execute("commit;")

def delete_user():
        query = "delete from users where user_name = '{}';".format(global_username[0])
        mycursor.execute(query)
        mycursor.execute("commit;")

def withdraw_window():
        def destroy_all():
                # hiding all the previous widgets 
                window.place_forget() # hiding the main frame
                wd_icon.destroy()
                wd_text.destroy()
                amt_entry.destroy()
                confirm_btn.destroy()
                submit_btn.destroy()
                back_btn.destroy()
        def withdraw_function(event=""):
                cv = confirm_value.get()
                amt = amt_value.get()
                current_balance = fetch_balance()
                if (cv==1) and (amt!=""):
                        amt = int(amt)
                        if (int(current_balance) == 0):
                                messagebox.showinfo("WARNING","YOU HAVE BALANCE OF Rs. 0 , YOU MUST DEPOSIT SOME AMOUNT FIRST")
                                destroy_all()
                        elif (amt>current_balance):
                                amt_entry.delete(0,END)
                                messagebox.showinfo("WARNING","YOU DON'T HAVE THAT MUCH OF BALANCE TO WITHDRAW")
                        else:
                                saving_amt = int(current_balance)-int(amt)
                                update_ba(saving_amt) # update balance of the user
                                amt_entry.delete(0,END)
                                messagebox.showinfo("WITHDRAWAL SUCCESSFUL","YOU HAVE WITHDRAWN Rs. "+str(amt))
                                destroy_all()
                elif (amt==""):
                        messagebox.showinfo("WARNING","PLEASE ENTER THE AMOUNT TO WITHDRAW")
                else :
                        messagebox.showinfo("WARNING","PLEASE CLICK TO CONFIRM FOR CONFIRMATION")
        window = Frame(width=700,height=500,bg="white")
        window.place(x=35,y=130)
        icon = Label(window,bg="white",width=50,height=50,image=withdraw_icon)
        icon.place(x=15,y=10)
        title = Label(window,text=" WITHDRAW CASH ",bg="white",fg="#000066",font="calibri 20")
        title.place(x=250,y=20)
        wd_icon = Label(bg="white",width=50,height=50,image=withdraw_icon)
        wd_icon.place(x=260,y=293)
        wd_text = Label(bg="white",text=" WITHDRAW AMOUNT : ",font="calibri 14",fg="#000066")
        wd_text.place(x=320,y=290)
        amt_value = StringVar()
        amt_entry = Entry(bg="white",fg="#000066",font="calibri",textvariable=amt_value)
        amt_entry.place(x=329,y=320)
        confirm_value = IntVar()
        confirm_btn = Checkbutton(text=" CONFIRM ",font="calibri",variable=confirm_value,bg="white",fg="#000066")
        confirm_btn.place(x=350,y=370)
        submit_btn = Button(command=withdraw_function,text=" PROCEED ",font="calibri",fg="white",bg="#000066",border=0,padx=10,pady=5)
        submit_btn.place(x=350,y=420)

        back_btn = Button(command=destroy_all,text=" BACK ",font="calibri",fg="white",bg="#000066",border=0,padx=10,pady=5)
        back_btn.place(x=360,y=540)

        welcome_screen.bind("<Return>",withdraw_function) # binding enter key to proceed

def deposit_window():
        def destroy_all():
                # hiding all the previous widgets 
                window.place_forget() # hiding the main frame
                dp_icon.destroy()
                dp_text.destroy()
                amt_entry.destroy()
                confirm_btn.destroy()
                submit_btn.destroy()
                back_btn.destroy()
        def deposit_function(event=""):
                cv = confirm_value.get()
                amt = amt_value.get()
                current_balance = fetch_balance()
                if (cv==1) and (amt!=""):
                        saving_amt = int(current_balance)+int(amt)
                        update_ba(saving_amt)
                        amt_entry.delete(0,END)
                        messagebox.showinfo("DEPOSITED SUCCESSFUL","YOU HAVE DEPOSITED Rs. "+str(amt))
                        destroy_all()
                elif (amt==""):
                        messagebox.showinfo("WARNING","PLEASE ENTER THE AMOUNT TO DEPOSIT")
                else :
                        messagebox.showinfo("WARNING","PLEASE CLICK TO CONFIRM FOR CONFIRMATION")
        window = Frame(width=700,height=500,bg="white")
        window.place(x=35,y=130)
        icon = Label(window,bg="white",width=50,height=50,image=deposit_icon)
        icon.place(x=15,y=10)
        title = Label(window,text=" DEPOSIT CASH ",bg="white",fg="#000066",font="calibri 20")
        title.place(x=270,y=20)
        dp_icon = Label(bg="white",width=50,height=50,image=deposit_icon)
        dp_icon.place(x=260,y=293)
        dp_text = Label(bg="white",text=" DEPOSIT AMOUNT : ",font="calibri 14",fg="#000066")
        dp_text.place(x=320,y=290)
        amt_value = StringVar()
        amt_entry = Entry(bg="white",fg="#000066",font="calibri",textvariable=amt_value)
        amt_entry.place(x=329,y=320)
        confirm_value = IntVar()
        confirm_btn = Checkbutton(text=" CONFIRM ",font="calibri",variable=confirm_value,bg="white",fg="#000066")
        confirm_btn.place(x=350,y=370)
        submit_btn = Button(command=deposit_function,text=" PROCEED ",font="calibri",fg="white",bg="#000066",border=0,padx=10,pady=5)
        submit_btn.place(x=350,y=420)

        back_btn = Button(command=destroy_all,text=" BACK ",font="calibri",fg="white",bg="#000066",border=0,padx=10,pady=5)
        back_btn.place(x=360,y=540)

        welcome_screen.bind("<Return>",deposit_function) # binding enter key to proceed

def check_your_balance_window():
        def destroy_all(event=""):
                # destroying previous window
                window.place_forget()
                b_amt.destroy()
                back_btn.destroy()
                #-------x--------
        window = Frame(width=700,height=500,bg="white")
        window.place(x=35,y=130)
        icon = Label(window,bg="white",width=50,height=50,image=check_your_balance_icon)
        icon.place(x=15,y=10)
        title = Label(window,text=" CHECK YOUR BALANCE ",bg="white",fg="#000066",font="calibri 20")
        title.place(x=220,y=20)
        b_amt = Label(text="YOUR CURRENT BALANCE IS Rs. "+str(fetch_balance()),font="calibri 20",fg="#000066",bg="white")
        b_amt.place(x=200,y=350)

        back_btn = Button(command=destroy_all,text=" BACK ",font="calibri",fg="white",bg="#000066",border=0,padx=10,pady=5)
        back_btn.place(x=360,y=420)

        welcome_screen.bind("<BackSpace>",destroy_all) # binding backspace key to destroy_all

def change_your_pin_window():
        def destroy_all():
                # destroying all previous widgets
                window.place_forget()
                newps_icon.destroy()
                newps_text.destroy()
                newps_entry.destroy()
                cps_icon.destroy()
                cps_text.destroy()
                cps_entry.destroy()
                confirm_btn.destroy()
                submit_btn.destroy()
                back_btn.destroy()
                # ------x------
        def proceed(event=""):
                new_ps = newps_value.get()
                c_ps = cps_value.get()
                c_value = confirm_value.get()
                if (new_ps=="" or c_ps==""):
                        messagebox.showinfo("WARNING","PLEASE FILL NEW PASSWORD OR CONFIRM PASSWORD")
                elif (c_value==0):
                        messagebox.showinfo("WARNING","PLEASE CHECK THE CONFIRM BOX")
                elif (new_ps!=c_ps):
                        newps_entry.delete(0,END)
                        cps_entry.delete(0,END)
                        messagebox.showinfo("WARNING","YOUR NEW PASSWORD AND CONFIRM PASSWORD DOES NOT MATCH")
                elif (len(new_ps) <= 4):
                        newps_entry.delete(0,END)
                        cps_entry.delete(0,END)
                        messagebox.showinfo("WARNING","YOUR NEW PASSWORD IS TOO SHORT")
                else:
                        update_ps(new_ps)
                        newps_entry.delete(0,END)
                        cps_entry.delete(0,END)
                        messagebox.showinfo("SUCCESSFULY PROCEEDED","YOUR PASSWORD IS CHANGED SUCCESSFULY")
                        destroy_all()
        window = Frame(width=700,height=500,bg="white")
        window.place(x=35,y=130)
        icon = Label(window,bg="white",width=50,height=50,image=change_your_pin_icon)
        icon.place(x=15,y=10)
        title = Label(window,text=" CHANGE YOUR PIN ",bg="white",fg="#000066",font="calibri 20")
        title.place(x=250,y=20)
        newps_icon = Label(bg="white",width=50,height=50,image=new_icon)
        newps_icon.place(x=260,y=274)
        newps_text = Label(bg="white",text=" NEW PASSWORD : ",font="calibri 14",fg="#000066")
        newps_text.place(x=320,y=270)
        newps_value = StringVar()
        newps_entry = Entry(bg="white",fg="#000066",font="calibri",textvariable=newps_value,show="X")
        newps_entry.place(x=329,y=300)
        cps_icon = Label(bg="white",width=50,height=50,image=confirm_icon)
        cps_icon.place(x=260,y=364)
        cps_text = Label(bg="white",text="CONFIRM PASSWORD :",font="calibri 14",fg="#000066")
        cps_text.place(x=320,y=360)
        cps_value = StringVar()
        cps_entry = Entry(bg="white",fg="#000066",font="calibri",textvariable=cps_value,show="X")
        cps_entry.place(x=329,y=390)
        confirm_value = IntVar()
        confirm_btn = Checkbutton(text=" CONFIRM ",font="calibri",variable=confirm_value,bg="white",fg="#000066")
        confirm_btn.place(x=350,y=430)
        submit_btn = Button(command=proceed,text=" PROCEED ",font="calibri",fg="white",bg="#000066",border=0,padx=10,pady=5)
        submit_btn.place(x=350,y=470)

        back_btn = Button(command=destroy_all,text=" BACK ",font="calibri",fg="white",bg="#000066",border=0,padx=10,pady=5)
        back_btn.place(x=360,y=540)

        welcome_screen.bind("<Return>",proceed) # binding enter key to proceed

def account_info_window():
        def destroy_all():
                # destroying all the previous window
                window.place_forget()
                confirm_btn.destroy()
                delete_btn.destroy()
                back_btn.destroy()
                menu_im[0].destroy()
                menu_im[1].destroy()
                menu_im[2].destroy()
                menu_im[3].destroy()
                menu_im[4].destroy()
                menu_btn[0].destroy()
                menu_btn[1].destroy()
                menu_btn[2].destroy()
                menu_btn[3].destroy()
                menu_btn[4].destroy()
                creating_verifying_form()
                #-------x-------
        def back(event=""):
                # destroying all the previous window
                window.place_forget()
                confirm_btn.destroy()
                delete_btn.destroy()
                back_btn.destroy()
                #-------x-------
        def delete_my_acc(event=""):
                c_v = confirm_value.get()
                if (c_v==1):
                        delete_user()
                        messagebox.showinfo("SUCCESSFUL","YOUR ACCOUNT IS DELETED")
                        destroy_all()
                else :
                        messagebox.showinfo("WARNING","PLEASE CHECK CONFIRM BUTTON")
        window = Frame(width=700,height=500,bg="white")
        window.place(x=35,y=130)
        icon = Label(window,bg="white",width=50,height=50,image=account_info_icon)
        icon.place(x=15,y=10)
        title = Label(window,text=" ACCOUNT INFO ",bg="white",fg="#000066",font="calibri 20")
        title.place(x=270,y=20)
        acc_name = Label(window,text=" ACCOUNT NAME :  "+global_username[0].upper(),bg="white",fg="#000066",font="calibri 20")
        acc_name.place(x=100,y=130)
        dob_name = Label(window,text=" DATE OF BIRTH :  "+fetch_dob(),bg="white",fg="#000066",font="calibri 20")
        dob_name.place(x=100,y=190)
        gen_name = Label(window,text=" GENDER :  "+fetch_gender(),bg="white",fg="#000066",font="calibri 20")
        gen_name.place(x=100,y=250)
        confirm_value = IntVar()
        confirm_btn = Checkbutton(text=" CONFIRM ",font="calibri",variable=confirm_value,bg="white",fg="#000066")
        confirm_btn.place(x=350,y=430)
        delete_btn = Button(command=delete_my_acc,text=" DELETE MY ACCOUNT ",font="calibri",fg="white",bg="#000066",border=0,padx=10,pady=5)
        delete_btn.place(x=305,y=480)
        back_btn = Button(command=back,text=" BACK ",font="calibri",fg="white",bg="#000066",border=0,padx=10,pady=5)
        back_btn.place(x=360,y=540)

        welcome_screen.bind("<Return>",delete_my_acc) # binding enter key to proceed
        welcome_screen.bind("<BackSpace>",back) # binding backspace key to back

def menu_screen():
        #  creating withdraw button with an icon beside of it
        withdraw_image = Label(bg="white",width=50,height=50,image=withdraw_icon)
        withdraw_image.place(x=770,y=188)
        menu_im[0] = withdraw_image
        withdraw_btn = Button(command=withdraw_window,text=" WITHDRAW CASH ",font="calibri 12",bg="white",fg="#000066",padx=60,pady=10)
        withdraw_btn.place(x=830,y=190)
        menu_btn[0] = withdraw_btn
        #  creating deposit button with an icon beside of it
        deposit_image = Label(bg="white",width=50,height=50,image=deposit_icon)
        deposit_image.place(x=770,y=268)
        menu_im[1] = deposit_image
        deposit_btn = Button(command=deposit_window,text=" DEPOSIT CASH ",font="calibri 12",bg="white",fg="#000066",padx=71,pady=10)
        deposit_btn.place(x=830,y=270)
        menu_btn[1] = deposit_btn
        #  creating check_your_balance button with an icon beside of it
        check_your_balance_image = Label(bg="white",width=50,height=50,image=check_your_balance_icon)
        check_your_balance_image.place(x=770,y=348)
        menu_im[2] = check_your_balance_image
        check_your_balance_btn = Button(command=check_your_balance_window,text=" CHECK YOUR BALANCE ",font="calibri 12",bg="white",fg="#000066",padx=43,pady=10)
        check_your_balance_btn.place(x=830,y=350)
        menu_btn[2] = check_your_balance_btn
        #  creating change_your_pin button with an icon beside of it
        change_your_pin_image = Label(bg="white",width=50,height=50,image=change_your_pin_icon)
        change_your_pin_image.place(x=770,y=428)
        menu_im[3] = change_your_pin_image
        change_your_pin_btn = Button(command=change_your_pin_window,text=" CHANGE YOUR PIN ",font="calibri 12",bg="white",fg="#000066",padx=56,pady=10)
        change_your_pin_btn.place(x=830,y=430)
        menu_btn[3] = change_your_pin_btn
        #  creating account_info button with an icon beside of it
        account_info_image = Label(bg="white",width=50,height=50,image=account_info_icon)
        account_info_image.place(x=770,y=508)
        menu_im[4] = account_info_image
        account_info_btn = Button(command=account_info_window,text=" ACCOUNT INFO ",font="calibri 12",bg="white",fg="#000066",padx=67,pady=10)
        account_info_btn.place(x=830,y=510)
        menu_btn[4] = account_info_btn

def create_new_account_screen():
        def back():
                # destroying all the previous window
                window.place_forget() # hiding the main frame
                un_icon.destroy()
                un_text.destroy()
                un_entry.destroy()
                ps_icon.destroy()
                ps_text.destroy()
                ps_entry.destroy()
                cps_icon.destroy()
                cps_text.destroy()
                cps_entry.destroy()
                dob_label.destroy()
                year_box.destroy()
                month_box.destroy()
                date_box.destroy()
                gender_label.destroy()
                male.destroy()
                female.destroy()
                submit_btn.destroy()
                back_btn.destroy()
                #-------x-------
                creating_verifying_form()
        def proceed_to_menu_screen():
                # hiding all the previous widgets 
                window.place_forget() # hiding the main frame
                un_icon.destroy()
                un_text.destroy()
                un_entry.destroy()
                ps_icon.destroy()
                ps_text.destroy()
                ps_entry.destroy()
                cps_icon.destroy()
                cps_text.destroy()
                cps_entry.destroy()
                dob_label.destroy()
                year_box.destroy()
                month_box.destroy()
                date_box.destroy()
                gender_label.destroy()
                male.destroy()
                female.destroy()
                submit_btn.destroy()
                back_btn.destroy()
                #-------x-------
                menu_screen()
        def create_account(event=""):
                un = un_value.get()
                ps = ps_value.get()
                cps = cps_value.get()
                year = year_box.get()
                month = month_box.get()
                date = date_box.get()
                dob = date + " " + month + " " + "," + " " + year
                gen = gender.get()
                usernames = fetch_usernames()
                regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
                if (un=="") :
                        messagebox.showinfo("WARNING","PLEASE TYPE YOUR USERNAME")
                elif (len(un) <= 5) or (len(un) >= 25):
                        un_entry.delete(0,END)
                        messagebox.showinfo("WARNING","PLEASE TYPE GENUINE USERNAME")
                elif (ps=="") :
                        messagebox.showinfo("WARNING","PLEASE TYPE YOUR PASSWORD")
                elif (cps=="") :
                        messagebox.showinfo("WARNING","PLEASE TYPE YOUR CONFIRM PASSWORD")
                elif (un in usernames) :
                        un_entry.delete(0,END)
                        messagebox.showinfo("WARNING","THIS USERNAME ALREADY EXISTS")
                elif (ps != cps) :
                        ps_entry.delete(0,END)
                        cps_entry.delete(0,END)
                        messagebox.showinfo("WARNING","YOUR PASSWORD AND CONFIRM PASSWORD DOES NOT MATCH")
                elif (len(ps) <= 8):
                        ps_entry.delete(0,END)
                        cps_entry.delete(0,END)
                        messagebox.showinfo("WARNING","YOUR PASSWORD SHOULD CONTAIN ATLEAST 8 CHARACTERS")
                elif ps.islower():
                        ps_entry.delete(0,END)
                        cps_entry.delete(0,END)
                        messagebox.showinfo("WARNING","YOUR PASSWORD SHOULD CONTAIN A UPPERCASE LETTER")
                elif ps.isupper():
                        ps_entry.delete(0,END)
                        cps_entry.delete(0,END)
                        messagebox.showinfo("WARNING","YOUR PASSWORD SHOULD CONTAIN A LOWERCASE LETTER")
                elif(regex.search(ps) == None):
                        ps_entry.delete(0,END)
                        cps_entry.delete(0,END)
                        messagebox.showinfo("WARNING","YOUR PASSWORD SHOULD CONTAIN A SPECIAL CHARACTER")
                elif (dob == "1 JANUARY , 2019"):
                        messagebox.showinfo("WARNING","PLEASE MENTION YOUR DATE OF BIRTH")
                elif (gen!=1) and (gen!=0):
                        messagebox.showinfo("WARNING","PLEASE DETERMINE YOUR GENDER")
                else :
                        global_username[0] = un
                        save_un_ps_ba_dob_gen(ps,dob,gen)
                        messagebox.showinfo("SUCCESSFUL","YOU HAVE SUCCESSFULY CREATED A NEW ACCOUNT : YOUR USERNAME IS-> "+un)
                        proceed_to_menu_screen()
        window = Frame(width=700,height=500,bg="white")
        window.place(x=210,y=130)
        icon = Label(window,bg="white",width=50,height=50,image=account_info_icon)
        icon.place(x=15,y=10)
        title = Label(window,text=" CREATING NEW ACCOUNT ",bg="white",fg="#000066",font="calibri 20")
        title.place(x=200,y=20)
        un_icon = Label(bg="white",width=50,height=50,image=username_icon)
        un_icon.place(x=430,y=244)
        un_text = Label(bg="white",text=" USERNAME : ",font="calibri 14",fg="#000066")
        un_text.place(x=490,y=240)
        un_value = StringVar()
        un_entry = Entry(bg="white",fg="#000066",font="calibri",textvariable=un_value)
        un_entry.place(x=499,y=270)
        ps_icon = Label(bg="white",width=50,height=50,image=password_icon)
        ps_icon.place(x=430,y=324)
        ps_text = Label(bg="white",text=" PASSWORD : ",font="calibri 14",fg="#000066")
        ps_text.place(x=490,y=320)
        ps_value = StringVar()
        ps_entry = Entry(bg="white",fg="#000066",font="calibri",textvariable=ps_value,show="X")
        ps_entry.place(x=499,y=350)
        cps_icon = Label(bg="white",width=50,height=50,image=confirm_icon)
        cps_icon.place(x=430,y=404)
        cps_text = Label(bg="white",text="CONFIRM PASSWORD :",font="calibri 14",fg="#000066")
        cps_text.place(x=490,y=400)
        cps_value = StringVar()
        cps_entry = Entry(bg="white",fg="#000066",font="calibri",textvariable=cps_value,show="X")
        cps_entry.place(x=499,y=430)

        dob_label = Label(window,text="D.O.B :",bg="white",fg="#000066")
        dob_label.place(x=70,y=370)
        year_box = ttk.Combobox(window,width=5)
        year_box["values"] = (2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000,1999,1998,1997,1996,1995,1994,1993,1992,1991,1990,1989,1988,1987,1986,1985,1984,1983,1982,1981,1980)
        year_box.current(0)
        year_box.place(x=130,y=370)
        month_box = ttk.Combobox(window,width=10)
        month_box["values"] = ("JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER")
        month_box.current(0)
        month_box.place(x=200,y=370)
        date_box = ttk.Combobox(window,width=10)
        date_box["values"] = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
        date_box.current(0)
        date_box.place(x=300,y=370)

        gender_label = Label(window,text="GENDER :",bg="white",fg="#000066")
        gender_label.place(x=400,y=370)
        gender = IntVar()
        gender.set(2)
        male = Radiobutton(window,text="MALE",value=1,variable=gender,bg="white")
        female = Radiobutton(window,text="FEMALE",value=0,variable=gender,bg="white")
        male.place(x=480,y=370)
        female.place(x=560,y=370)
        
        submit_btn = Button(command=create_account,text=" PROCEED ",font="calibri",fg="white",bg="#000066",border=0,padx=10,pady=5)
        submit_btn.place(x=580,y=550)

        back_btn = Button(command=back,text=" BACK ",font="calibri",fg="white",bg="#000066",border=0,padx=10,pady=5)
        back_btn.place(x=450,y=550)

        welcome_screen.bind("<Return>",create_account) # binding enter key to proceed

def creating_verifying_form():
        def proceed_to_menu_screen():
                # hiding all the previous widgets 
                window.place_forget() # hiding the main frame
                un_icon.destroy()
                un_text.destroy()
                un_entry.destroy()
                ps_icon.destroy()
                ps_text.destroy()
                ps_entry.destroy()
                submit_btn1.destroy()
                submit_btn2.destroy()
                #-------x-------
                menu_screen()
        def proceed_to_create_new_account_screen():
                # hiding all the previous widgets 
                window.place_forget() # hiding the main frame
                un_icon.destroy()
                un_text.destroy()
                un_entry.destroy()
                ps_icon.destroy()
                ps_text.destroy()
                ps_entry.destroy()
                submit_btn1.destroy()
                submit_btn2.destroy()
                #-------x-------
                create_new_account_screen()
        def verify_un_and_ps(event=""):
                username = un_value.get()
                password = ps_value.get()
                registered_usernames = fetch_usernames()
                if (username in registered_usernames):
                        global_username[0] = username # inserted username in global_username
                        registered_password = fetch_password()
                        if (registered_password==password):
                                proceed_to_menu_screen()
                        elif (password==""):
                                messagebox.showinfo(" WARNING "," PLEASE ENTER YOUR PASSWORD ")
                        else:
                                ps_entry.delete(0,END)
                                messagebox.showinfo(" WARNING "," YOUR PASSWORD IS WRONG ")
                else :
                        un_entry.delete(0,END)
                        ps_entry.delete(0,END)
                        messagebox.showinfo(" WARNING ", " PLEASE ENTER YOUR USERNAME AND PASSWORD CORRECTLY ")
        # verifying form
        window = Frame(width=700,height=500,bg="white")
        window.place(x=210,y=130)
        icon1 = Label(window,bg="white",width=50,height=50,image=account_info_icon)
        icon1.place(x=15,y=10)
        icon2 = Label(window,bg="white",width=50,height=50,image=account_info_icon)
        icon2.place(x=630,y=10)
        title = Label(window,text=" VERIFY YOUR ACCOUNT ",bg="white",fg="#000066",font="calibri 20")
        title.place(x=215,y=20)
        
        un_icon = Label(bg="white",width=50,height=50,image=username_icon)
        un_icon.place(x=430,y=274)
        un_text = Label(bg="white",text=" USERNAME : ",font="calibri 14",fg="#000066")
        un_text.place(x=490,y=270)
        un_value = StringVar()
        un_entry = Entry(bg="white",fg="#000066",font="calibri",textvariable=un_value)
        un_entry.place(x=499,y=300)
        ps_icon = Label(bg="white",width=50,height=50,image=password_icon)
        ps_icon.place(x=430,y=374)
        ps_text = Label(bg="white",text=" PASSWORD : ",font="calibri 14",fg="#000066")
        ps_text.place(x=490,y=370)
        ps_value = StringVar()
        ps_entry = Entry(bg="white",fg="#000066",font="calibri",textvariable=ps_value,show="X")
        ps_entry.place(x=499,y=400)
        submit_btn1 = Button(command=verify_un_and_ps,text=" PROCEED ",font="calibri",fg="white",bg="#000066",border=0,padx=10,pady=5)
        submit_btn1.place(x=520,y=470)
        submit_btn2 = Button(command=proceed_to_create_new_account_screen,text=" CREATE A NEW ACCOUNT ",font="calibri",fg="white",bg="#000066",border=0,padx=10,pady=5)
        submit_btn2.place(x=465,y=530)

        welcome_screen.bind("<Return>",verify_un_and_ps) # binding enter key to proceed

'''   ------------------------x-----------------------  '''

# ----------------------- main code start here -----------------------

'''   ------------ creating image background ----------   '''

bg_image = Label(image = window_bg).pack() # setting image as a background

'''   -------------------------x-----------------------   '''


header = Label(text = "KAD NETBANKING",font = "calibri 20",bg="#fff",fg="#000066",width=80,pady=15) #creating header 
header.place(x=0,y=0) #header placing at top

icon1 = Label(image = bank_icon,bg="#fff",height=50,width=50) #icon1 showing
icon1.place(x=350,y=6)                                            #icon1 placing
icon2 = Label(image = bank_icon,bg="#fff",height=50,width=50) #icon2 showing
icon2.place(x=720,y=6)                                            #icon2 placing

creating_verifying_form()


welcome_screen.mainloop() # stoping welcome window to close
