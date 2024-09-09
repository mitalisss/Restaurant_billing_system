#restaurant billing system backend

import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",password="mitali@2003", database="pythonpro")

if db.is_connected():
    print("connected")
else:
    print("dis")
    
def cafebillData():
    cur=db.cursor()                                   
    qry="create table if not exists foodbill(date date, time time ,order_no int, name char(30) , oreo_shake int, kitkat_shake int, sev_puri int, noodles int,\
            lasagna int, aloo_tikki int, fries int, Pie int, pizza_poppers int, bhel int,\
             cost float, Service_Charge float, CGST float, SGST float, Subtotal float, Total float)"
    cur.execute(qry)
    db.commit()
      

def addbillRec(date , time  ,order_no, name , oreo_shake , kitkat_shake , sev_puri , noodles , lasagna , aloo_tikki ,\
              fries , Pie , pizza_poppers , bhel ,\
              cost , Service_Charge , CGST , SGST , Subtotal , Total ):
    
    print("connected to add bill")
    
    cur=db.cursor()
    st="INSERT INTO foodbill VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)"
    val = (date , time  ,order_no , name , oreo_shake , kitkat_shake , sev_puri , noodles ,lasagna , aloo_tikki , fries , \
                 Pie ,pizza_poppers , bhel ,cost , Service_Charge , CGST , SGST , Subtotal , Total)
    
    cur.execute(st, val)
    db.commit()
    db.close()

cafebillData()

