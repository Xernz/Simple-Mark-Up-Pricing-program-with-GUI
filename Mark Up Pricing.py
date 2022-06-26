#import libraries
from tkinter import *
from tkinter import ttk
import os

#basic window
win = Tk()
frame=Frame(win)
frame.pack
win.resizable(0, 0) # this prevents from resizing the win
win.title("Mark Up Pricing")

#I disabled this part since i didnt put the icon file. you can add other icon by changing the file path.
#win.iconbitmap("X:\Project\Gitas.ico") #iseng

#Background, I disabled this part since i didnt put the image file. you can add other image by changing the file path.
#bg = PhotoImage(file="X:\Project\Gitacut.png")
#label1 = Label(win, image = bg)
#label1.place(x=0,y=0)

#List
namaproduk=[]
bahan = []
ukuran = []
harga = []
qty = []
total = []
per_pcs = []
jual = []
profit = []

#Trick
outputline = 0
locate = str(os.getcwd())#to locate current working directories file

# Fungsi
def b_produk(value):
    try:
        global L_produk
        global L_status
        global L_trouble
        if value=="":
            raise Exception
        elif value==" ":
            raise Exception
        else:
            E1.delete(0,END)
            L_produk = Label(output, text=value)
            L_produk.grid(row=0,column=2)
            E1.config(state= "disabled")
            B1.config(state= "disabled")
            E2.config(state= "normal")
            E3.config(state= "normal")
            E4.config(state= "normal")
            B2.config(state= "normal")
            B3.config(state= "normal")
            L_status.destroy()
            L_status = Label(status, text=">>>Insert nama produk berhasil",pady=2,fg="green")
            L_status.pack()
            L_trouble.destroy()
            L_trouble = Label(troubleshoot, text=" ",pady=2)
            L_trouble.pack()
            namaproduk.append(value)

    except:
        L_status.destroy()
        L_status = Label(status, text=">>>Insert nama produk error",pady=2,fg="red")
        L_status.pack()
        L_trouble.destroy()
        L_trouble = Label(troubleshoot, text="*Jangan kosongkan nama produk",pady=2,fg="red")
        L_trouble.pack()
def b_tambah(value1,value2,value3):
    global L_bahan
    global L_harga
    global L_ukuran
    global L_status
    global L_trouble
    try:
        if value1 == "":
            raise Exception
        elif value1 == " ":
            raise Exception 
        elif value2 == "":
            raise Exception
        elif value2 == " ":
            raise Exception
        elif int(value3) > 0:
            global outputline
            outputline += 1
            bahan.append(value1)
            ukuran.append(value2)
            harga.append(int(value3))
            L_bahan = Label(output,text=value1)
            L_bahan.grid(row=1+outputline,column=0)
            L_ukuran = Label(output,text=value2)
            L_ukuran.grid(row=1+outputline,column=1,columnspan=2)
            L_harga = Label(output,text="Rp. " + value3)
            L_harga.grid(row=1+outputline,column=3)
            E2.delete(0,END)
            E3.delete(0,END)
            E4.delete(0,END)
            L_status.destroy()
            L_status = Label(status, text=">>>Insert cost berhasil",pady=2,fg="green")
            L_status.pack()
            L_trouble.destroy()
            L_trouble = Label(troubleshoot, text=" ",pady=2)
            L_trouble.pack()
        elif value3 != int:
            raise ValueError
        elif value3 <= 0:
            raise ValueError
    except ValueError:
        L_status.destroy()
        L_status = Label(status, text=">>>Insert cost gagal",pady=2,fg="red")
        L_status.pack()
        L_trouble.destroy()
        L_trouble = Label(troubleshoot, text="*Harga haruslah angka interger dan tidak boleh <= 0",pady=2,fg="red")
        L_trouble.pack()
    except:
        L_status.destroy()
        L_status = Label(status, text=">>>Insert cost gagal",pady=2,fg="red")
        L_status.pack()
        L_trouble.destroy()
        L_trouble = Label(troubleshoot, text="*Jangan kosongkan bahan/ukuran/harga",pady=2,fg="red")
        L_trouble.pack()
def b_selesai():
    E2.delete(0,END)
    E3.delete(0,END)
    E4.delete(0,END)
    E2.config(state= "disabled")
    E3.config(state= "disabled")
    E4.config(state= "disabled")
    B2.config(state= "disabled")
    B3.config(state= "disabled")
    B4.config(state= "normal")
    E5.config(state= "normal")
def b_qty(value):
    global qty
    global L_status
    global L_trouble
    try:
        if 0< int(value)<=100:
            E5.delete(0,END)
            B4.config(state= "disabled")
            E5.config(state= "disabled")
            L_qty = Label(output,text="_____________________________\n\nProduk yang dihasilkan : "+value)
            L_qty.grid(row=2+outputline,column=0)
            L_status.destroy()
            L_status = Label(status, text=">>>Insert Qty berhasil",pady=2,fg="green")
            L_status.pack()
            L_trouble.destroy()
            L_trouble = Label(troubleshoot, text=" ",pady=2)
            L_trouble.pack()
            qty.append(int(value))
            B5.config(state= "normal")
            B6.config(state= "normal")
        else:
            raise Exception
    except:
        L_status.destroy()
        L_status = Label(status, text=">>>Insert Qty gagal",pady=2,fg="red")
        L_status.pack()
        L_trouble.destroy()
        L_trouble = Label(troubleshoot, text="*Qty haruslah angka interger\n*Qty tidak boleh <= 0 dan >100",pady=2,fg="red")
        L_trouble.pack()
def pricing():
    global L_status
    totall = sum(harga)
    per_pcss = totall/qty[0]
    profitt = 50/100*per_pcss
    juals = per_pcss + profitt
    total.append(totall)
    perpcs = int(per_pcss)
    profits = int(profitt)
    jualss=int(juals)
    per_pcs.append(perpcs)
    profit.append(profits)
    jual.append(jualss)
    B5.config(state= "disabled")
    L_status.destroy()
    L_status = Label(status, text=">>>Proses Mark Up berhasil",pady=2,fg="green")
    L_status.pack()
    L_total = Label(output,text="_____________________________\n\nTotal Cost : Rp. "+str(totall))
    L_total.grid(row=2+outputline,column=3)
    L_pcs = Label(output,text=f"Cost per pcs : Rp. {per_pcs[0]}",pady=5)
    L_pcs.grid(row=3+outputline,column=0)
    L_profit = Label(output,text=f"Profit 50% : Rp. {profit[0]}")
    L_profit.grid(row=4+outputline,column=0)
    L_jual = Label(output,text=f"Harga jual : Rp. {jual[0]}")
    L_jual.grid(row=5+outputline,column=0)
def save():
    global L_status
    global L_trouble
    namafile = f"Mark up harga {namaproduk[0]}.txt"
    file = open(f"{locate}\{namafile}", "w")
    file.write(f"Produk : {namaproduk[0]}\n_____________\ncost :\n")
    for i in range(len(bahan)):
        file.write(f"{i+1}. {bahan[i]} {ukuran[i]} : Rp. {harga[i]}\n")
    file.write(f"\n_____________\nJumlah produk yang dibuat(qty) = {qty[0]} porsi/pcs")
    file.write(f"\n_____________\nTotal Cost = Rp. {total[0]}\nModal = Rp. {per_pcs[0]}/pcs\nHarga Jual = Rp. {jual[0]}/pcs\nProfit/laba per pcs = Rp. {profit[0]}")
    file.close()
    L_status.destroy()
    L_status = Label(status, text=f">>>file saved in {locate}\{namafile}",pady=2, padx=5,fg="green")
    L_status.pack()
    L_trouble.destroy()
    L_trouble = Label(troubleshoot, text=" ",pady=2)
    L_trouble.pack()
    B6.config(state= "disabled")

#Frame
frame1 = LabelFrame(win, text="Product",pady=5,padx=20,bd=5)
frame1.grid(row=1, column=0,columnspan=2,pady=10)
frame2 = LabelFrame(win, text="Cost",pady=5,padx=10,bd=5)
frame2.grid(row=1,rowspan=2, column=2,columnspan=3,padx=20,pady=10)
frame3 = LabelFrame(win, text="Hasil",pady=5,padx=10,bd=5)
frame3.grid(row=2, column=0,columnspan=2,padx=10,pady=10)
status = LabelFrame(win,text="Status log",bd=3)
status.grid(row=3,column=0,padx=10,pady=20)
troubleshoot = LabelFrame(win,text="Troubleshoot",bd=3)
troubleshoot.grid(row=3,column=1,padx=5,pady=20)
output = LabelFrame(win, text="Output",pady=5,padx=10,bd=5)
output.grid(row=3,column=2,columnspan=3,padx=5,pady=10)

#label
L1 = Label(win, text = "Program Mark Up Pricing by Muhammad Daffa Aushaf")
L2 = Label(frame1, text = "Nama Produk : ")
L3 = Label(frame2, text = "*Sertakan Kg/L/Pcs ",fg="gray")
L4 = Label(frame2, text = "Bahan : ")
L5 = Label(frame2, text = "Ukuran(Kg/L/Pcs) : ")
L6 = Label(frame2, text = "Harga : ")
L7 = Label(frame2, text = "*Tekan tombol selesai jika semua bahan yang dibutuhkan sudah ditambahkan",fg="gray")
L8 = Label(frame3, text = "Quantity : ")
L9 = Label(frame3, text = "*Jumlah produk yang dapat dihasilkan dari bahan tersebut",fg="gray")
Lproduk = Label(output,text="Produk: ")
Lbahan = Label(output,text="Bahan: ")
Lukuran = Label(output,text="Ukuran: ")
Lharga = Label(output,text="Harga: ")
L_status = Label(status, text="=Program Started=")
L_trouble = Label(troubleshoot, text="=Solusi masalah akan ditampilkan disini=")

#Label Position
L1.grid(row=0, column=0,columnspan=5,pady = 10)
L2.grid(row = 0, column = 0)
L3.grid(row = 1, column = 2,columnspan=2)
L4.grid(row = 0, column = 0)
L5.grid(row = 1, column = 0)
L6.grid(row = 2, column = 0)
L7.grid(row = 4,column=0,columnspan=4,pady = 5)
L8.grid(row = 0,column=0)
L9.grid(row = 1,column=0, columnspan = 2,pady = 5)
Lproduk.grid(row=0,column=1,pady=10)
Lbahan.grid(row=1,column=0,padx=48,pady=3)
Lukuran.grid(row=1,column=1,columnspan=2,padx=47,pady=3)
Lharga.grid(row=1,column=3,padx=47,pady=3)
L_status.pack()
L_trouble.pack()

#Entry
E1 = Entry(frame1, width=30, borderwidth=2)
E1.grid(row = 0, column = 1,padx=10,pady = 5)
E2 = Entry(frame2, width=30, borderwidth=2)
E2.grid(row = 0, column = 1,pady = 5)
E3 = Entry(frame2, width=30, borderwidth=2)
E3.grid(row = 1, column = 1,pady = 5)
E4 = Entry(frame2, width=30, borderwidth=2)
E4.grid(row = 2, column = 1,pady = 5)
E5 = Entry(frame3, width=30, borderwidth=2)
E5.grid(row=0,column=1,pady = 5)

#Button
B1 = Button(frame1,text = "Enter",command=lambda:b_produk(E1.get()))
B1.grid(row=0, column=2)
B2 = Button(frame2,text = "Tambahkan",command=lambda:b_tambah(E2.get(),E3.get(),E4.get()))
B2.grid(row=3, column=2)
B3 = Button(frame2,text = "Selesai",command=lambda:b_selesai())
B3.grid(row=3, column=3)
B4 = Button(frame3,text = "Enter",command=lambda:b_qty(E5.get()))
B4.grid(row=0, column=2)
B5 = Button(win,text = "Mark Up",padx=20,command=lambda:pricing())
B5.grid(row=4,column=2)
B6 = ttk.Button(win, text = 'Save', command = lambda : save())
B6.grid(row=4,column=4,pady=5)

#disable
E2.config(state= "disabled")
E3.config(state= "disabled")
E4.config(state= "disabled")
E5.config(state= "disabled")
B2.config(state= "disabled")
B3.config(state= "disabled")
B4.config(state= "disabled")
B5.config(state= "disabled")
B6.config(state= "disabled")

win.mainloop()
