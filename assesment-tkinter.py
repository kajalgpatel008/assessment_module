from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

def create_conn():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="billing_system"
        )

def insert_data():
     if ( e_bathsoap.get()=="" or 
          e_facecream.get()=="" or
          e_facewash.get()==""or
          e_hairspray.get()==""or
          e_bodylotion.get()=="" or
          e_rice.get()==""or
          e_foodoil.get()=="" or
          e_daal.get()==""or
          e_wheat.get()==""or
          e_sugar.get()==""or
          e_maza.get()==""or
          e_coke.get()==""or
          e_frooti.get()==""or
          e_nimkos.get()==""or
          e_biscuits.get()==""or
          e_totalcosmetic.get()==""or
          e_totalgrocery.get()==""or
          e_totalothers.get()==""or
          e_taxcosmetic.get()==""or
          e_taxgrocery.get()==""or
          e_taxothers.get()=="" ):
       msg.showinfo("Insert Status","All Fields Are Mandatory")
     else: 
        conn=create_conn()
        cursor=conn.cursor()  
        query="insert into bills(bath_soap,face_cream,face_wash,hair_spray,body_lotion,rice,food_oil,daal,wheat,sugar,maza,coke,frooti,nimkos,biscuits,total_cosmetic,total_grocery,total_others,tax_cosmetic,tax_grocery,tax_others) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        args=( e_bathsoap.get(),e_facecream.get(),e_facewash.get(),e_hairspray.get(), e_bodylotion.get(),e_rice.get(),
            e_foodoil.get(),e_daal.get(),e_wheat.get(),e_sugar.get(),e_maza.get(),e_coke.get(), e_frooti.get(),
            e_nimkos.get(),e_biscuits.get(), e_totalcosmetic.get(),e_totalgrocery.get(),e_totalothers.get(),e_taxcosmetic.get(),
             e_taxgrocery.get(),e_taxothers.get())
        cursor.execute(query,args)
        conn.commit()
        e_bathsoap.delete(0,'end')
        e_facecream.delete(0,'end')
        e_facewash.delete(0,'end')
        e_hairspray.delete(0,'end')
        e_bodylotion.delete(0,'end')
        e_rice.delete(0,'end')
        e_foodoil.delete(0,'end')
        e_daal.delete(0,'end')
        e_wheat.delete(0,'end')
        e_sugar.delete(0,'end')
        e_maza.delete(0,'end')
        e_coke.delete(0,'end')
        e_frooti.delete(0,'end')
        e_nimkos.delete(0,'end')
        e_biscuits.delete(0,'end')
        e_totalcosmetic.delete(0,'end')
        e_totalgrocery.delete(0,'end')
        e_totalothers.delete(0,'end')
        e_taxcosmetic.delete(0,'end')
        e_taxgrocery.delete(0,'end')
        e_taxothers.delete(0,'end')
        msg.showinfo("Insert Status","Data Inserted Successfully")
        conn.close()        
def search_data():
        e_bathsoap.delete(0,'end')
        e_facecream.delete(0,'end')
        e_facewash.delete(0,'end')
        e_hairspray.delete(0,'end')
        e_bodylotion.delete(0,'end')
        e_rice.delete(0,'end')
        e_foodoil.delete(0,'end')
        e_daal.delete(0,'end')
        e_wheat.delete(0,'end')
        e_sugar.delete(0,'end')
        e_maza.delete(0,'end')
        e_coke.delete(0,'end')
        e_frooti.delete(0,'end')
        e_nimkos.delete(0,'end')
        e_biscuits.delete(0,'end')
        e_totalcosmetic.delete(0,'end')
        e_totalgrocery.delete(0,'end')
        e_totalothers.delete(0,'end')
        e_taxcosmetic.delete(0,'end')
        e_taxgrocery.delete(0,'end')
        e_taxothers.delete(0,'end')
        if e_bill_no.get()=="":   
            msg.showinfo("Search Status","Bill No Is Mandatory")
        else:
           conn=create_conn()
           cursor=conn.cursor()
           query="select * from bills where bill_no=%s "
           args=(e_bill_no.get(),)
           cursor.execute(query,args)
           row=cursor.fetchall()
           if row:
                e_bathsoap.insert(0,row[0][1])
                e_facecream.insert(0,row[0][2])
                e_facewash.insert(0,row[0][3])
                e_hairspray.insert(0,row[0][4])
                e_bodylotion.insert(0,row[0][5])
                e_rice.insert(0,row[0][6])
                e_foodoil.insert(0,row[0][7])
                e_daal.insert(0,row[0][8])
                e_wheat.insert(0,row[0][9])
                e_sugar.insert(0,row[0][10])
                e_maza.insert(0,row[0][11])
                e_coke.insert(0,row[0][12])
                e_frooti.insert(0,row[0][13])
                e_nimkos.insert(0,row[0][14])
                e_biscuits.insert(0,row[0][15])
                e_totalcosmetic.insert(0,row[0][16])
                e_totalgrocery.insert(0,row[0][17])
                e_totalothers.insert(0,row[0][18])
                e_taxcosmetic.insert(0,row[0][19])
                e_taxgrocery.insert(0,row[0][20])
                e_taxothers.insert(0,row[0][21])
                    
           else: 
              msg.showinfo("Search Status","Bill No Not Found")
           conn.close()  

def update_data():
       if ( e_bill_no.get()=="" or 
            e_bathsoap.get()=="" or 
            e_facecream.get()=="" or
            e_facewash.get()==""or
            e_hairspray.get()==""or
            e_bodylotion.get()=="" or
            e_rice.get()==""or
            e_foodoil.get()=="" or
            e_daal.get()==""or
            e_wheat.get()==""or
            e_sugar.get()==""or
            e_maza.get()==""or
            e_coke.get()==""or
            e_frooti.get()==""or
            e_nimkos.get()==""or
            e_biscuits.get()==""or
            e_totalcosmetic.get()==""or
            e_totalgrocery.get()==""or
            e_totalothers.get()==""or
            e_taxcosmetic.get()==""or
            e_taxgrocery.get()==""or
            e_taxothers.get()=="" ):
         msg.showinfo("Update Status","All Fields Are Mandatory")
       else:
          conn=create_conn()
          cursor=conn.cursor()
          query="update bills set bath_soap=%s,face_cream=%s,face_wash=%s,hair_spray=%s body_lotion=%s rice=%s food_oil=%s daal=%s wheat=%s sugar=%s maza=%s coke=%s frooti=%s nimkos=%s biscuits=%s total_cosmetic=%s total_grocery=%s total_others=%s tax_cosmetic=%s tax_grocery=%s tax_others=%s where bill_no =%s"
          args=( e_bill_no.get(),e_bathsoap.get(),e_facecream.get(),e_facewash.get(),e_hairspray.get(), e_bodylotion.get(),e_rice.get(),
            e_foodoil.get(),e_daal.get(),e_wheat.get(),e_sugar.get(),e_maza.get(),e_coke.get(), e_frooti.get(),
            e_nimkos.get(),e_biscuits.get(), e_totalcosmetic.get(),e_totalgrocery.get(),e_totalothers.get(),e_taxcosmetic.get(),
             e_taxgrocery.get(),e_taxothers.get())
          cursor.execute(query, args)
          conn.commit()
          e_bathsoap.delete(0,'end')
          e_facecream.delete(0,'end')
          e_facewash.delete(0,'end')
          e_hairspray.delete(0,'end')
          e_bodylotion.delete(0,'end')
          e_rice.delete(0,'end')
          e_foodoil.delete(0,'end')
          e_daal.delete(0,'end')
          e_wheat.delete(0,'end')
          e_sugar.delete(0,'end')
          e_maza.delete(0,'end')
          e_coke.delete(0,'end')
          e_frooti.delete(0,'end')
          e_nimkos.delete(0,'end')
          e_biscuits.delete(0,'end')
          e_totalcosmetic.delete(0,'end')
          e_totalgrocery.delete(0,'end')
          e_totalothers.delete(0,'end')
          e_taxcosmetic.delete(0,'end')
          e_taxgrocery.delete(0,'end')
          e_taxothers.delete(0,'end')
          msg.showinfo("Update Status","Data Updated Successfully")
               
    
def delete_data():
     if e_bill_no.get()=="": 
            msg.showinfo("Delete Status","Bill No Is Mandatory")
     else:
         conn=create_conn()
         cursor=conn.cursor()
         query="delete from bills where bill_no=%s "
         args=(e_bill_no.get(),)
         cursor.execute(query,args)
         conn.commit()
         e_bathsoap.delete(0,'end')
         e_facecream.delete(0,'end')
         e_facewash.delete(0,'end')
         e_hairspray.delete(0,'end')
         e_bodylotion.delete(0,'end')
         e_rice.delete(0,'end')
         e_foodoil.delete(0,'end')
         e_daal.delete(0,'end')
         e_wheat.delete(0,'end')
         e_sugar.delete(0,'end')
         e_maza.delete(0,'end')
         e_coke.delete(0,'end')
         e_frooti.delete(0,'end')
         e_nimkos.delete(0,'end')
         e_biscuits.delete(0,'end')
         e_totalcosmetic.delete(0,'end')
         e_totalgrocery.delete(0,'end')
         e_totalothers.delete(0,'end')
         e_taxcosmetic.delete(0,'end')
         e_taxgrocery.delete(0,'end')
         e_taxothers.delete(0,'end')
         msg.showinfo("Delete Status","Data Deleted Successfully")
        
    
root=Tk()
root.title("Billing Software")
root.geometry("920x800")

root.resizable(width=False,height=False)


c_details=LabelFrame(root,text="Customer Details",font=("times new roman",15,"bold"))
c_details.place(x=40,y=10,width=850,height=100)

c_name=Label(root,text="Customer Name")
c_name.place(x=50,y=50)

c_name=Entry(root)
c_name.place(x=150,y=50)

phone_no=Label(root,text="Phone No")
phone_no.place(x=350,y=50)

phone_no=Entry(root)
phone_no.place(x=450,y=50)

l_bill_no=Label(root,text="Bill No.")
l_bill_no.place(x=650,y=50)

e_bill_no=Entry(root)
e_bill_no.place(x=750,y=50)

cosmetics_frame=LabelFrame(root,text="Cosmetics",font=("times new roman",15,"bold"))
cosmetics_frame.place(x=40,y=130,width=250,height=300)

l_bathsoap=Label(root,text="Bath Soap")
l_bathsoap.place(x=50,y=170)

l_facecream=Label(root,text="Face Cream")
l_facecream.place(x=50,y=220)

l_facewash=Label(root,text="Face Wash")
l_facewash.place(x=50,y=270)

l_hairspray=Label(root,text="Hair Spray")
l_hairspray.place(x=50,y=320)

l_bodylotion=Label(root,text="Body Lotion")
l_bodylotion.place(x=50,y=370)

e_bathsoap=Entry(root)
e_bathsoap.place(x=150,y=170)

e_facecream=Entry(root)
e_facecream.place(x=150,y=220)

e_facewash=Entry(root)
e_facewash.place(x=150,y=270)

e_hairspray=Entry(root)
e_hairspray.place(x=150,y=320)

e_bodylotion=Entry(root)
e_bodylotion.place(x=150,y=370)

grocery_frame=LabelFrame(root,text="Grocery",font=("times new roman",15,"bold"))
grocery_frame.place(x=340,y=130,width=250,height=300)

l_rice=Label(root,text="Rice")
l_rice.place(x=350,y=170)

l_foodoil=Label(root,text="Food Oil")
l_foodoil.place(x=350,y=220)

l_daal=Label(root,text="Daal")
l_daal.place(x=350,y=270)

l_wheat=Label(root,text="Wheat")
l_wheat.place(x=350,y=320)

l_sugar=Label(root,text="Sugar")
l_sugar.place(x=350,y=370)

e_rice=Entry(root)
e_rice.place(x=450,y=170)

e_foodoil=Entry(root)
e_foodoil.place(x=450,y=220)

e_daal=Entry(root)
e_daal.place(x=450,y=270)

e_wheat=Entry(root)
e_wheat.place(x=450,y=320)

e_sugar=Entry(root)
e_sugar.place(x=450,y=370)


others_frame=LabelFrame(root,text="Others",font=("times new roman",15,"bold"))
others_frame.place(x=640,y=130,width=250,height=300)

l_maza=Label(root,text="Maza")
l_maza.place(x=650,y=170)

l_coke=Label(root,text="Coke")
l_coke.place(x=650,y=220)

l_frooti=Label(root,text="Frooti")
l_frooti.place(x=650,y=270)

l_nimkos=Label(root,text="Nimkos")
l_nimkos.place(x=650,y=320)

l_biscuits=Label(root,text="Biscuits")
l_biscuits.place(x=650,y=370)

e_maza=Entry(root)
e_maza.place(x=750,y=170)

e_coke=Entry(root)
e_coke.place(x=750,y=220)

e_frooti=Entry(root)
e_frooti.place(x=750,y=270)

e_nimkos=Entry(root)
e_nimkos.place(x=750,y=320)

e_biscuits=Entry(root)
e_biscuits.place(x=750,y=370)

billmenu_frame=LabelFrame(root,text="Bill Menu",font=("times new roman",15,"bold"))
billmenu_frame.place(x=40,y=460,width=550,height=200)

l_totalcosmetic=Label(root,text="Total Cosmetic")
l_totalcosmetic.place(x=50,y=500)

l_totalgrocery=Label(root,text="Total Grocery")
l_totalgrocery.place(x=50,y=550)

l_totalothers=Label(root,text="Total Others")
l_totalothers.place(x=50,y=600)

l_taxcosmetic=Label(root,text="Cosmetics Tax")
l_taxcosmetic.place(x=350,y=500)

l_taxgrocery=Label(root,text="Grocery Tax")
l_taxgrocery.place(x=350,y=550)

l_taxothers=Label(root,text="Others Tax")
l_taxothers.place(x=350,y=600)

e_totalcosmetic=Entry(root)
e_totalcosmetic.place(x=150,y=500)

e_totalgrocery=Entry(root)
e_totalgrocery.place(x=150,y=550)

e_totalothers=Entry(root)
e_totalothers.place(x=150,y=600)

e_taxcosmetic=Entry(root)
e_taxcosmetic.place(x=450,y=500)

e_taxgrocery=Entry(root)
e_taxgrocery.place(x=450,y=550)

e_taxothers=Entry(root)
e_taxothers.place(x=450,y=600)


insert=Button(root,text="INSERT",bg="black",fg="white",font=("forte",12),command=insert_data)
insert.place(x=445,y=700)

search=Button(root,text="SEARCH",bg="black",fg="white",font=("forte",12),command=search_data)
search.place(x=535,y=700)

update=Button(root,text="UPDATE",bg="black",fg="white",font=("forte",12),command=update_data)
update.place(x=630,y=700)

delete=Button(root,text="DELETE",bg="black",fg="white",font=("forte",12),command=delete_data)
delete.place(x=725,y=700)


root.mainloop()
