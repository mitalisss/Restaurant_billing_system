#restaurant billing system( frontend )

import tkinter  as tk
from tkinter import *
import random

import time
import calendar
import datetime 

import restaurant_bill_backend as q
import mysql.connector

#-----------------------------------------------main window-------------------------------------------------------------------------------------------
root = Tk()
root.geometry("1450x650+0+0")
root.title("THE CENTRAL PERK CAFE")
root.configure(background= 'Cadet Blue')

#------------------------------------------------frames-----------------------------------------------------------------------------------------------

Tops= Frame(root, bg='Cadet Blue', width = 1600,height=70,bd=30, pady =5, relief=SUNKEN)
Tops.pack(side=TOP)

TitFrame = Frame(Tops, width=1700, bd=10, padx=50, pady=20, bg="Powder Blue", relief=RIDGE) 
TitFrame.pack(side=TOP)

# Restaurant name frame
lbltit = Label(TitFrame, font=('Georgia',44,'bold','italic'),text='THE CENTRAL PERK CAFE',bd=13,bg='Cadet Blue',fg='white',justify=CENTER) 
lbltit.grid(row=0, column=0)

f1 = Frame(Tops, height=700, pady=35, bd=6, bg="Cadet Blue", relief=SUNKEN)  
f1.pack(side=LEFT)

# Calculator frame
f2 = Frame(Tops, width=650, height=700, pady=35, bd=6, bg="Cadet Blue", relief=SUNKEN)  
f2.pack(side=RIGHT)

# Button frame
f3 = Frame(root, width=700, height=30, bd=9, bg="Cadet Blue", relief=SUNKEN)  
f3.pack(side=BOTTOM)


#-------------------------------------------------INFO -----------------------------------------------------------------------------------------------

def calc():
    x=random.randint(168,5000)
    randomRef = str(x)
    order_no.set(randomRef)

# dd/mm/YY (date)

    now = datetime.datetime.now()
    d=now.strftime("%Y-%m-%d")
    print ("Current date : ")
    print (now.strftime("%Y-%m-%d "))
    date.set(d)

#time(h,m,s)

    now = datetime.datetime.now()
    t=now.strftime("%H:%M:%S")
    print ("Current time : ")
    print (now.strftime("%H:%M:%S"))
    time.set(t)


    cpc= float(fries.get())
    csp= float(sev_puri.get())
    cpp= float(noodles.get())
    csc= float(Pie.get())
    cdp= float(lasagna.get())
    cos= float(oreo_shake.get())
    cks =float(kitkat_shake.get())
    cb= float(bhel.get())
    cpip= float(pizza_poppers.get())
    catc= float(aloo_tikki.get())
      

    costoffries = cpc*60
    costofsev_puri = csp*45
    costofnoodles = cpp*100
    costofPie = csc*100
    costofkitkat_shake = cks*60
    costoforeo_shake = cos*55
    costofpizza_poppers= cpip*65
    costofbhel = cb*40
    costofaloo_tikki = catc*50
    costoflasagna = cdp*150

    
# cgst=9% , sgst=9%, sevice charge=10% , total gst=18%
     
    costofmeal = ( (costoffries +  costofsev_puri + costofnoodles + costofaloo_tikki + costofpizza_poppers + costoforeo_shake +
                                         costofbhel +  costofPie + costoflasagna  + costofkitkat_shake))
    
    payCGST =((costoffries +  costofsev_puri + costofnoodles + costofaloo_tikki + costofpizza_poppers +
                                    costoforeo_shake+ costofbhel +  costofPie + costoflasagna  + costofkitkat_shake)*0.09  )   
    
    paySGST=( (costoffries +  costofsev_puri + costofnoodles + costofaloo_tikki + costofpizza_poppers +
                      costoforeo_shake + costofbhel +  costofPie + costoflasagna  + costofkitkat_shake)*0.09)
    
    Totalcost=(costoffries +  costofsev_puri+ costofnoodles + costofaloo_tikki + costofpizza_poppers+
                        costoforeo_shake+ costofbhel +  costofPie+ costoflasagna  + costofkitkat_shake)
    
    Ser_Charge=((costoffries +  costofsev_puri + costofnoodles + costofaloo_tikki + costofpizza_poppers +
                 costoforeo_shake + costofbhel +  costofPie + costoflasagna  + costofkitkat_shake)/10)

    
    Service=(Ser_Charge)
    OverAllCost=( payCGST + paySGST + Totalcost + Ser_Charge)
    PaidCGST =( payCGST)
    PaidSGST =( paySGST)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    CGST.set(PaidCGST)
    SGST.set(PaidSGST)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost) 


    
#-----------------------------------------------------------------------------------------------------------------------------------------------------    
#------------------------------------defining---------------------------------------------------------------------------------------------------------

    
name = StringVar()
order_no = StringVar()
fries = StringVar()
sev_puri = StringVar()
noodles= StringVar()
aloo_tikki = StringVar()
kitkat_shake = StringVar()
Pie= StringVar()
pizza_poppers= StringVar()
lasagna= StringVar()
bhel = StringVar()
oreo_shake = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
SGST = StringVar()
cost = StringVar()
CGST = StringVar()
time=StringVar()
date=StringVar()

#-----------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------frame 1----------------------------------------------------------------------------------------------------
#date, time
#orderno,name
# Labels and Entries for Frame 1
lbldate = Label(f1, font=('cambria', 17, 'bold'), text="DATE", fg="black", bd=10, anchor='w', bg="Cadet blue")
lbldate.grid(row=0, column=0)
txtdate = Entry(f1, font=('ariel', 16, 'bold'), textvariable=date, bd=6, insertwidth=6, bg="white", justify='right')
txtdate.grid(row=0, column=1)

lbltime = Label(f1, font=('cambria', 17, 'bold'), text="TIME", fg="black", bd=10, anchor='w', bg="Cadet blue")
lbltime.grid(row=0, column=2)
txttime = Entry(f1, font=('ariel', 16, 'bold'), textvariable=time, bd=6, insertwidth=6, bg="white", justify='right')
txttime.grid(row=0, column=3)

lblreference = Label(f1, font=('cambria', 17, 'bold'), text="ORDER NO", fg="black", bd=15, anchor='w', bg="Cadet blue")
lblreference.grid(row=1, column=0)
txtreference = Entry(f1, font=('ariel', 16, 'bold'), textvariable=order_no, bd=6, insertwidth=6, bg="white", justify='right')
txtreference.grid(row=1, column=1)

lblname = Label(f1, font=('cambria', 17, 'bold'), text="NAME", fg="black", bd=15, anchor='w', bg="Cadet blue")
lblname.grid(row=1, column=2)
txtname = Entry(f1, font=('ariel', 16, 'bold'), textvariable=name, bd=6, insertwidth=6, bg="white", justify='right')
txtname.grid(row=1, column=3)

lblitmes = Label(f1, font=('Rockwell', 16, 'bold'), text="FOOD ITEMS..", fg="black", bd=8, anchor='w', bg="Cadet blue")
lblitmes.grid(row=2, column=0)
#------------------------------------------------------col 0&1----------------------------------------------------------------------------------------


# Food items in Frame 1
lblkitkat_shake = Label(f1, font=('aria', 16, 'bold'), text="Kitkat Shake", fg="black", bd=12, anchor='w', bg="Cadet blue")
lblkitkat_shake.grid(row=3, column=0)
txtkitkat_shake = Entry(f1, font=('ariel', 16, 'bold'), textvariable=kitkat_shake, bd=6, insertwidth=4, bg="white", justify='right')
txtkitkat_shake.grid(row=3, column=1)

lbloreo_shake = Label(f1, font=('aria', 16, 'bold'), text="Oreo Shake", fg="black", bd=12, anchor='w', bg="Cadet blue")
lbloreo_shake.grid(row=4, column=0)
txtoreo_shake = Entry(f1, font=('ariel', 16, 'bold'), textvariable=oreo_shake, bd=6, insertwidth=4, bg="white", justify='right')
txtoreo_shake.grid(row=4, column=1)

lblsev_puri = Label(f1, font=('aria', 16, 'bold'), text="Sev Puri", fg="black", bd=12, anchor='w', bg="Cadet blue")
lblsev_puri.grid(row=5, column=0)
txtsev_puri = Entry(f1, font=('ariel', 16, 'bold'), textvariable=sev_puri, bd=6, insertwidth=4, bg="white", justify='right')
txtsev_puri.grid(row=5, column=1)

lblnoodles = Label(f1, font=('aria', 16, 'bold'), text="Veg Noodles", fg="black", bd=12, anchor='w', bg="Cadet blue")
lblnoodles.grid(row=6, column=0)
txtnoodles = Entry(f1, font=('ariel', 16, 'bold'), textvariable=noodles, bd=6, insertwidth=4, bg="white", justify='right')
txtnoodles.grid(row=6, column=1)

lbllasagna = Label(f1, font=('aria', 16, 'bold'), text="Lasagna", fg="black", bd=12, anchor='w', bg="Cadet blue")
lbllasagna.grid(row=7, column=0)
txtlasagna = Entry(f1, font=('ariel', 16, 'bold'), textvariable=lasagna, bd=6, insertwidth=4, bg="white", justify='right')
txtlasagna.grid(row=7, column=1)

#---------------------------------------------------col 2&3-------------------------------------------------------------------------------------------

lblaloo_tikki = Label(f1, font=('aria', 16, 'bold'), text="Aloo Tikki", fg="black", bd=12, anchor='w', bg="Cadet blue")
lblaloo_tikki.grid(row=3, column=2)
txtaloo_tikki = Entry(f1, font=('ariel', 16, 'bold'), textvariable=aloo_tikki, bd=6, insertwidth=4, bg="white", justify='right')
txtaloo_tikki.grid(row=3, column=3)

lblfries = Label(f1, font=('aria', 16, 'bold'), text="Peri Peri fries", fg="black", bd=12, anchor='w', bg="Cadet blue")
lblfries.grid(row=4, column=2)
txtfries = Entry(f1, font=('ariel', 16, 'bold'), textvariable=fries, bd=6, insertwidth=4, bg="white", justify='right')
txtfries.grid(row=4, column=3)

lblPie = Label(f1, font=('aria', 16, 'bold'), text="Veg Pie", fg="black", bd=12, anchor='w', bg="Cadet blue")
lblPie.grid(row=5, column=2)
txtPie = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Pie, bd=6, insertwidth=4, bg="white", justify='right')
txtPie.grid(row=5, column=3)

lblpizza_poppers = Label(f1, font=('aria', 16, 'bold'), text="Pizza Poppers", fg="black", bd=12, anchor='w', bg="Cadet blue")
lblpizza_poppers.grid(row=6, column=2)
txtpizza_poppers = Entry(f1, font=('ariel', 16, 'bold'), textvariable=pizza_poppers, bd=6, insertwidth=4, bg="white", justify='right')
txtpizza_poppers.grid(row=6, column=3)

lblbhel = Label(f1, font=('aria', 16, 'bold'), text="Sweet Spicy Bhel", fg="black", bd=12, anchor='w', bg="Cadet blue")
lblbhel.grid(row=7, column=2)
txtbhel = Entry(f1, font=('ariel', 16, 'bold'), textvariable=bhel, bd=6, insertwidth=4, bg="white", justify='right')
txtbhel.grid(row=7, column=3)


#------------------------------------------calculation(frame 2)-------------------------------------------------------

lblcost = Label(f2, font=('cambria', 19, 'bold'), text="COST", fg="black", bd=18, anchor='w', bg="Cadet blue")
lblcost.grid(row=0, column=0)
txtcost = Entry(f2, font=('ariel', 14, 'bold'), textvariable=cost, bd=7, insertwidth=6, bg="white", justify='right')
txtcost.grid(row=0, column=1)

lblService_Charge = Label(f2, font=('cambria', 19, 'bold'), text="SERVICE CHARGE", fg="black", bd=18, anchor='w', bg="Cadet blue")
lblService_Charge.grid(row=1, column=0)
txtService_Charge = Entry(f2, font=('ariel', 14, 'bold'), textvariable=Service_Charge, bd=7, insertwidth=6, bg="white", justify='right')
txtService_Charge.grid(row=1, column=1)

lblCGST = Label(f2, font=('cambria', 19, 'bold'), text="CGST", fg="black", bd=18, anchor='w', bg="Cadet blue")
lblCGST.grid(row=2, column=0)
txtCGST = Entry(f2, font=('ariel', 14, 'bold'), textvariable=CGST, bd=7, insertwidth=6, bg="white", justify='right')
txtCGST.grid(row=2, column=1)

lblSGST = Label(f2, font=('cambria', 19, 'bold'), text="SGST", fg="black", bd=18, anchor='w', bg="Cadet blue")
lblSGST.grid(row=3, column=0)
txtSGST = Entry(f2, font=('ariel', 14, 'bold'), textvariable=SGST, bd=7, insertwidth=6, bg="white", justify='right')
txtSGST.grid(row=3, column=1)

lblSubtotal = Label(f2, font=('cambria', 19, 'bold'), text="SUBTOTAL", fg="black", bd=18, anchor='w', bg="Cadet blue")
lblSubtotal.grid(row=4, column=0)
txtSubtotal = Entry(f2, font=('ariel', 14, 'bold'), textvariable=Subtotal, bd=7, insertwidth=6, bg="white", justify='right')
txtSubtotal.grid(row=4, column=1)

lblTotal = Label(f2, font=('cambria', 19, 'bold'), text="TOTAL", fg="black", bd=18, anchor='w', bg="Cadet blue")
lblTotal.grid(row=5, column=0)
txtTotal = Entry(f2, font=('ariel', 14, 'bold'), textvariable=Total, bd=7, insertwidth=6, bg="white", justify='right')
txtTotal.grid(row=5, column=1)


#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------button cammands---------------------------------------------------------------------------------------------

#closing window    
def qexit():
    root.destroy()

#clearing contents
def reset():
    order_no.set("")
    lasagna.set("")
    sev_puri.set("")
    noodles.set("")
    aloo_tikki.set("")
    kitkat_shake.set("")
    Pie.set("")
    pizza_poppers.set("")
    bhel.set("")
    fries.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    oreo_shake.set("")
    CGST.set("")
    SGST.set("")
    cost.set("")
    name.set("")   
    date.set("")
    time.set("")

#menu
def menu():
    roo = Tk()
    roo.geometry("400x350+0+0")
    roo.title("MENU")
    lblinfo = Label(roo, font=('cambria', 15, 'bold','italic'), text="ITEM", fg="black", bd=5, anchor=W)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('cambria', 15, 'bold','italic'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=5)

    lblinfo = Label(roo, font=('aria', 15, 'bold','italic'), text="SEV PURI", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold','italic'), text="45", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=5)

    lblinfo = Label(roo, font=('aria', 15, 'bold','italic'), text="VEG NOODLES", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold','italic'), text="100", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=5)

    lblinfo = Label(roo, font=('aria', 15, 'bold','italic'), text=" LASAGNA", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold','italic'), text="150", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=5)

    lblinfo = Label(roo, font=('aria', 15, 'bold','italic'), text="FRIES ", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold','italic'), text="60", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=5)

    lblinfo = Label(roo, font=('aria', 15, 'bold','italic'), text="ALOO TIKKI", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold','italic'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=5)

    lblinfo = Label(roo, font=('aria', 15, 'bold','italic'), text="SWEET SPICY BHEL", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold','italic'), text="40", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=5)

    lblinfo = Label(roo, font=('aria', 15, 'bold','italic'), text="OREO SHAKE", fg="steel blue", anchor=W)
    lblinfo.grid(row=7, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold','italic'), text="55", fg="steel blue", anchor=W)
    lblinfo.grid(row=7, column=5)

    lblinfo = Label(roo, font=('aria', 15, 'bold','italic'), text="KITKAT SHAKE", fg="steel blue", anchor=W)
    lblinfo.grid(row=8, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold','italic'), text="60", fg="steel blue", anchor=W)
    lblinfo.grid(row=8, column=5)

    lblinfo = Label(roo, font=('aria', 15, 'bold','italic'), text="PIZZA POPPERS", fg="steel blue", anchor=W)
    lblinfo.grid(row=9, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold','italic'), text="65", fg="steel blue", anchor=W)
    lblinfo.grid(row=9, column=5)

    lblinfo = Label(roo, font=('aria', 15, 'bold','italic'), text="VEG PIE", fg="steel blue", anchor=W)
    lblinfo.grid(row=10, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold','italic'), text="100", fg="steel blue", anchor=W)
    lblinfo.grid(row=10, column=5)


    roo.mainloop()

#---------------------------buttons-------------------------------------------------------------------------------------------------------------------

btnTotal = Button(f3, padx=11, pady=8, bd=7, fg="black", font=('ariel', 16, 'bold'), width=9, text="TOTAL", bg="Cadet blue", command=calc)
btnTotal.grid(row=1, column=0)

btnreset = Button(f3, padx=11, pady=8, bd=7, fg="black", font=('ariel', 16, 'bold'), width=9, text="RESET", bg="Cadet blue", command=reset)
btnreset.grid(row=1, column=6)

btnexit = Button(f3, padx=11, pady=8, bd=7, fg="black", font=('ariel', 16, 'bold'), width=9, text="EXIT", bg="Cadet blue", command=qexit)
btnexit.grid(row=1, column=7)

btnprice = Button(f3, padx=11, pady=8, bd=7, fg="black", font=('ariel', 16, 'bold'), width=9, text="MENU", bg="Cadet blue", command=menu)
btnprice.grid(row=1, column=1)


#-----------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------data related button commands---------------------------------------------------------------------------------

#saving bill      
def addbill():

    cg=round(float(CGST.get()))
    c=round(float(cost.get()))
    s_c=round(float(Service_Charge.get()))
    sg=round(float (SGST.get()))
    st=round(float(Subtotal.get()))
    t=round(float( Total.get()))

    if(len(order_no.get())!=0):
      q.addbillRec( date.get(), time.get() ,order_no.get(), name.get() , oreo_shake.get() , kitkat_shake.get() , sev_puri.get() , noodles.get() ,lasagna.get() ,\
                                   aloo_tikki.get() , fries.get() , Pie.get() ,pizza_poppers.get() , bhel.get() ,\
                                   c , s_c , cg , sg , st ,t )
      print("BILL SAVED IN SQL")

    
    # saving bill in txt fill 
    def bill():
        file=open("Receipt.txt", "a")
        file.write("\n DATE: ")
        file.write("   ")
        file.write(date.get())
        
        file.write("   ")
        file.write(" TIME: ")
        file.write("   ")
        file.write(time.get())
        
        file.write("   ")
        file.write("  NAME: ")
        file.write("   ")
        file.write(name.get())
        
        file.write("   ")
        file.write("  ORDER NO: ")
        file.write("   ")
        file.write(order_no.get())
        
        file.write("   ")
        file.write(" cost of meal: ")
        file.write("   ")
        file.write(cost.get())
        
        file.write("   ")
        file.write(" service charge: ")
        file.write("   ")
        file.write(Service_Charge.get())
        
        file.write("   ")
        file.write(" GST: ")
        file.write("   ")
        file.write(CGST.get())
        file.write(" , ")
        file.write(SGST.get())
        
        file.write("   ")
        file.write(" TOTAL AMOUNT: ")
        file.write("   ")
        file.write(Total.get())
        
        file.close()

        print("BILL SAVED TO TXT FILE")
    
    bill()
            
       
### viewing all bills             
def viewdata():
    roo = Tk()
    roo.geometry("400x350+0+0")
    roo.title("All Bill Record")

    #date,time,name,or.no
    
    lblinfo = Label(roo, font=('aria', 9, 'bold'), text="DATE", fg="black",anchor=W)
    lblinfo.grid(row=0, column=0)
    
    lblinfo = Label(roo, font=('aria', 9, 'bold'), text="TIME", fg="black", anchor=W)
    lblinfo.grid(row=0, column=1)

    lblinfo = Label(roo, font=('aria', 9, 'bold'), text="ORDER NO", fg="black",anchor=W)
    lblinfo.grid(row=0, column=2)
    
    lblinfo = Label(roo, font=('aria', 9, 'bold'), text="NAME", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    
    #items
    
    lblinfo = Label(roo, font=('aria', 9,'bold'), text="OREO \n SHAKE", fg="black")
    lblinfo.grid(row=0, column=4)
    
    lblinfo = Label(roo, font=('aria', 9, 'bold'), text="KITKAT \n SHAKE", fg="black")
    lblinfo.grid(row=0, column=5)
    
    lblinfo = Label(roo, font=('aria', 9, 'bold'), text="SEV PURI", fg="black")
    lblinfo.grid(row=0, column=6)
    
    lblinfo = Label(roo, font=('aria', 9, 'bold'), text="VEG NOODLES", fg="black")
    lblinfo.grid(row=0, column=7)

    lblinfo = Label(roo, font=('aria', 9, 'bold'), text="LASAGNA", fg="black")
    lblinfo.grid(row=0, column=8)

    lblinfo = Label(roo, font=('aria', 8, 'bold'), text="ALOO TIKKI ", fg="black")
    lblinfo.grid(row=0, column=9)
    
    lblinfo = Label(roo, font=('aria', 9, 'bold'), text="FRIES ", fg="black")
    lblinfo.grid(row=0, column=10)
    
    lblinfo = Label(roo, font=('aria', 9, 'bold'), text="VEG PIE", fg="black")
    lblinfo.grid(row=0, column=11)

    lblinfo = Label(roo, font=('aria', 9, 'bold'), text="PIZZA \n POPPERS", fg="black")
    lblinfo.grid(row=0, column=12)
    
    lblinfo = Label(roo, font=('aria', 9, 'bold'), text="SW & SP \n BHEL" , fg="black")
    lblinfo.grid(row=0, column=13)
    
    lblinfo = Label(roo, font=('aria', 9, 'bold'), text="COST", fg="black")
    lblinfo.grid(row=0, column=14)

    lblinfo = Label(roo, font=('aria', 9, 'bold'), text="SERVICE \n CHARGE", fg="black")
    lblinfo.grid(row=0, column=15)

    lblinfo = Label(roo, font=('aria',9, 'bold'), text=" CGST ", fg="black")
    lblinfo.grid(row=0, column=16)
    
    lblinfo = Label(roo, font=('aria', 9, 'bold'), text=" SGST ", fg="black")
    lblinfo.grid(row=0, column=17)
    
    lblinfo = Label(roo, font=('aria', 9, 'bold'), text="SUBTOTAL", fg="black")
    lblinfo.grid(row=0, column=18)

    lblinfo = Label(roo, font=('aria', 9, 'bold'), text=" TOTAL ", fg="black")
    lblinfo.grid(row=0, column=19)
    
    
    
    my_connect = mysql.connector.connect(
      host="localhost",user="root",password="mitali@2003", database="pythonpro"
    )
    my_conn = my_connect.cursor()
    my_conn.execute("SELECT * FROM foodbill")
    m_r = my_conn.fetchall()
    i=0 
    for i in range(len(m_r)): 
        for j in range(len(m_r[0])):
            e = Entry(roo, width=10, fg='blue') 
            e.grid(row=i+1, column=j) 
            e.insert(END, m_r[i][j])
        i=i+1
        
    print("viewing all Records")
    roo.mainloop()

    
   
# show current single bill 
def current_bill():
    ro = Tk()
    ro.geometry("450x580+0+0")
    ro.title("current bill")


    billframe = Frame(ro,bd=10,bg="white",relief=RIDGE)
    billframe.place(width=450,height=580)
    
    title=Label(billframe,bd=1,fg="dark blue",font=('Georgia' ,16,'bold','italic'),width=10, text="WELCOME TO \n THE CENTRAL PERK CAFE \n***********************************************",bg="white",relief=RIDGE).pack(fill=X)
   
    txtarea=Text(billframe,bd=1)
    txtarea.pack(fill=BOTH,expand=1)

    #date,time,name,orderno
    datelabel = Label(txtarea,bg="white", text=date.get()).grid(row=1, column=1)
    datelabel1 = Label(txtarea,bg="white",font=('Rockwell' ,12,'bold'), text="DATE").grid(row=1, column=0)

    timelabel = Label(txtarea,bg="white", text=time.get()).grid(row=1, column=4)
    timelabel = Label(txtarea,bg="white",font=('Rockwell' ,12,'bold'),  text="TIME").grid(row=1, column=3)
    
    order_nolabel = Label(txtarea,bg="white", text=order_no.get()).grid(row=4, column=1)
    order_nolabel = Label(txtarea,bg="white",font=('Rockwell' ,12,'bold'),  text="ORDER NO").grid(row=4, column=0)
    
    namelabel = Label(txtarea,bg="white", text=name.get()).grid(row=4, column=4)
    namelabel = Label(txtarea,bg="white", font=('Rockwell' ,12,'bold'), text="NAME").grid(row=4, column=3)

    namelabel = Label(txtarea,bg="white", text="").grid(row=5, column=1)

    # items, qty, price (col name)
    itemslabel = Label(txtarea,bg="white",font=('Arial Black' ,10,'bold'), text="ITEMS").grid(row=6, column=0)

    qtylabel = Label(txtarea,bg="white", font=('Arial Black' ,10,'bold'),text="QTY").grid(row=6, column=2)

    pricelabel = Label(txtarea,bg="white",font=('Arial Black' ,10,'bold'), text="PRICE").grid(row=6, column=4)

    #defining  
    os=float(float(oreo_shake.get())*55)
    ks=float(float(kitkat_shake.get())* 60)
    sp=float(float(sev_puri.get())*45)
    n=float(float(noodles.get())*100)
    l=float(float(lasagna.get())*150)
    atc=float(float(aloo_tikki.get())*50)
    f=float(float(fries.get())*60)
    p=float(float(Pie.get())*100)
    pip=float(float(pizza_poppers.get())*65)
    b=float(float(bhel.get())*40)

    cg=round(float(CGST.get()))
    c=round(float(cost.get()))
    s_c=round(float(Service_Charge.get()))
    sg=round(float (SGST.get()))
    st=round(float(Subtotal.get()))
    t=round(float( Total.get()))


    # itmes,qty,price
    o_slabel = Label(txtarea,bg="white",font=('Arial' ,9,'bold'), text="1)  oreo shake").grid(row=7, column=0)
    o_slabel = Label(txtarea,bg="white", text=oreo_shake.get()).grid(row=7, column=2)
    o_slabel = Label(txtarea,bg="white", text=os).grid(row=7, column=4)
    
    k_slabel = Label(txtarea,bg="white",font=('Arial' ,9,'bold'), text="2)  kitkat shake").grid(row=8, column=0)
    k_slabel = Label(txtarea,bg="white", text=kitkat_shake.get()).grid(row=8, column=2)
    k_slabel = Label(txtarea,bg="white", text=ks).grid(row=8, column=4)
    
    s_plabel = Label(txtarea,bg="white",font=('Arial' ,9,'bold'), text="3)   sev puri    ").grid(row=9, column=0)
    s_plabel = Label(txtarea,bg="white", text=sev_puri.get()).grid(row=9, column=2)
    s_plabel = Label(txtarea,bg="white", text=sp).grid(row=9, column=4)

    p_plabel = Label(txtarea,bg="white",font=('Arial' ,9,'bold'), text="4)  veg noodles  ").grid(row=10, column=0)
    p_plabel = Label(txtarea,bg="white", text=noodles.get()).grid(row=10, column=2)
    p_plabel = Label(txtarea,bg="white", text=n).grid(row=10, column=4)
      
    d_plabel = Label(txtarea,bg="white",font=('Arial' ,9,'bold'), text="5)  lasagna    ").grid(row=11, column=0)
    d_plabel = Label(txtarea,bg="white", text=lasagna.get()).grid(row=11, column=2)
    d_plabel = Label(txtarea,bg="white", text=l).grid(row=11, column=4)

    a_t_clabel = Label(txtarea,bg="white", font=('Arial' ,9,'bold'),text="6)  aloo tikki ").grid(row=12, column=0)
    a_t_clabel = Label(txtarea,bg="white", text=aloo_tikki.get()).grid(row=12, column=2)
    a_t_clabel = Label(txtarea,bg="white", text=atc).grid(row=12, column=4)

    s_clabel = Label(txtarea,bg="white", font=('Arial' ,9,'bold'),text="7)   veg pie").grid(row=13, column=0)
    s_clabel = Label(txtarea,bg="white", text=Pie.get()).grid(row=13, column=2)
    s_clabel = Label(txtarea,bg="white", text=p).grid(row=13, column=4)

    pi_plabel = Label(txtarea,bg="white",font=('Arial' ,9,'bold'), text="8)  pizza poppers").grid(row=14, column=0)
    pi_plabel = Label(txtarea,bg="white", text=pizza_poppers.get()).grid(row=14, column=2)
    pi_plabel = Label(txtarea,bg="white", text=pip).grid(row=14, column=4)

    bhellabel = Label(txtarea,bg="white",font=('Arial' ,9,'bold'), text="9)  sw & sp  bhel ").grid(row=15, column=0)
    bhellabel = Label(txtarea,bg="white", text=bhel.get()).grid(row=15, column=2)
    bhellabel = Label(txtarea,bg="white", text=b).grid(row=15, column=4)

    p_clabel = Label(txtarea,bg="white",font=('Arial' ,9,'bold'), text="10) peri peri fries ").grid(row=16, column=0)
    p_clabel = Label(txtarea,bg="white", text=fries.get()).grid(row=16, column=2)
    p_clabel = Label(txtarea,bg="white", text=f).grid(row=16, column=4)

    linelabel = Label(txtarea,bg="white", font=('bold'), text="----------------------").grid(row=17, column=0)
    linelabel = Label(txtarea,bg="white", font=('bold'), text="---------").grid(row=17, column=1)
    linelabel = Label(txtarea,bg="white", font=('bold'), text="---------").grid(row=17, column=2)
    linelabel = Label(txtarea,bg="white", font=('bold'), text="---------").grid(row=17, column=3)
    linelabel = Label(txtarea,bg="white", font=('bold'),  text="---------").grid(row=17, column=4)
    linelabel = Label(txtarea,bg="white", font=('bold'), text="---------").grid(row=17, column=5)


    # cost, total,gst    
    clabel = Label(txtarea,bg="white", font=('Arial' ,10,'bold'),text="COST").grid(row=20, column=0)
    clabel = Label(txtarea,bg="white", text=c).grid(row=20, column=4)

    clabel = Label(txtarea,bg="white",font=('Arial' ,10,'bold'), text="SERVICE CHARGE").grid(row=21, column=0)
    clabel = Label(txtarea,bg="white", text= s_c).grid(row=21, column=4)

    sgstlabel = Label(txtarea,bg="white", font=('Arial' ,10,'bold'),text="SGST ").grid(row=22, column=0)
    sgstlabel = Label(txtarea,bg="white", text=sg).grid(row=22, column=4)
     
    cgstlabel = Label(txtarea,bg="white",font=('Arial' ,10,'bold'), text="CGST").grid(row=23, column=0)
    csgtlabel = Label(txtarea,bg="white", text=cg).grid(row=23, column=4)

    stlabel = Label(txtarea,bg="white", font=('Arial' ,10,'bold'),text="SUBTOTAL").grid(row=24, column=0)
    stlabel = Label(txtarea,bg="white", text= st).grid(row=24, column=4)
    
    tlabel = Label(txtarea,bg="white",font=('Arial' ,10,'bold'), text="TOTAL").grid(row=25, column=0)
    tlabel = Label(txtarea,bg="white", text=t).grid(row=25, column=4)


    print("viewed current bill")



def delete():
    ro1= Tk()
    ro1.geometry("300x300+0+0")
    ro1.title("delete bill")
    orderno=StringVar()
    
    Label(ro1,text="").pack()
    Label(ro1,text="").pack()
    Label(ro1, font=( 'cambria' ,14, 'bold','italic'),text="enter order no of bill to be deleted",fg="red",anchor='w').pack()
    Label(ro1,text="").pack()
    Label(ro1,text="").pack()
    Label(ro1,text="").pack()
    Label(ro1, font=( 'cambria' ,15, 'bold','italic'),text="order no",fg="dark blue",anchor='w').pack()
    Label(ro1,text="").pack()
    orderno = Entry(ro1, textvariable=orderno)
    orderno.pack()

    def deleterec():
        o_no=orderno.get()
        my_connect = mysql.connector.connect(
          host="localhost",user="root",password="tiger", database="test")
        my_conn = my_connect.cursor()
        delete="DELETE FROM foodbill WHERE order_no=%s"%(o_no)
        my_conn.execute(delete)
        my_connect.commit()
        print("bill delete")
        
        
    Label(ro1,text="").pack()
    
    Button(ro1,text="DELETE", height="2", width="30", bg="yellow", command=deleterec).pack()

    ro1.mainloop()

#------------------------------------data related buttons---------------------------------------------------------------------------------------------

btnaddbillRec=Button(f3,padx=11,pady=8, bd=7 ,fg="black",font=('ariel' ,16,'bold'),width=9, text="SAVE BILL", bg="Cadet blue",command=addbill)
btnaddbillRec.grid(row=1, column=2)
# save bill

btnviewRec=Button(f3,padx=11,pady=8, bd=7 ,fg="black",font=('ariel' ,16,'bold'),width=9, text="ALL BILLS", bg="Cadet blue",command=viewdata)
btnviewRec.grid(row=1, column=4)
#view all bills

btnviewbill=Button(f3,padx=11,pady=8, bd=7 ,fg="black",font=('ariel' ,16,'bold'),width=9, text="VIEW BILL", bg="Cadet blue",command=current_bill)
btnviewbill.grid(row=1, column=3)
# view current bill

btnviewbill=Button(f3,padx=11,pady=8, bd=7 ,fg="black",font=('ariel' ,16,'bold'),width=9, text="DELETE BILL", bg="Cadet blue",command=delete)
btnviewbill.grid(row=1, column=5)
# delete bill 

#-----------------------------------------------------------------------------------------------------------------------------------------------------

#closing main window

root.mainloop()
