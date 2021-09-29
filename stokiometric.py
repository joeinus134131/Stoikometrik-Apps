#program buatan untuk menghitung rasio bahan bakar
#GUI Hitung Rasio Bahan Bakar PLTU
#IDNMakerspace Algorithm Factory

import math
import tkinter as tk
from tkinter import StringVar
import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageTk, Image

#kandungan kimia
#Co2
#So2
#O2
#N2

#Parameter

#carbon, hidrogen, sulfur, oxygen, nitrogen, ash, TM
rho = 1.2 #density 1.2 kg/m3
m = 500 #massa udara yang dibutuhkan perjam
aktualair = 11.25

#Gui Setting
gui = tk.Tk()
gui.title("Stokiometrik Apps Calculator PLTU TARAHAN")
gui.geometry("650x600")
gui.iconbitmap('E:\\PROJECT-KODINGAN\\1. PYTHON\\3. 2021 PENGUJIAN MODULE\\logo_itera_oke_bvD_icon.ico')

#Gambar
image=Image.open("E:\\PROJECT-KODINGAN\\1. PYTHON\\3. 2021 PENGUJIAN MODULE\\Logo_PLN.png")
image.thumbnail((100,300),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
label_image=tk.Label(image=photo)
label_image.place(x=400, y=50)

#gambar=Image.open("E:\\PROJECT-KODINGAN\\1. PYTHON\\3. 2021 PENGUJIAN MODULE\\logo itera oke.png")
#gambar.thumbnail((100,200),Image.ANTIALIAS)
#foto=ImageTk.PhotoImage(gambar)
#label_imager=tk.Label(gambar=foto)
#label_imager.place(x=750, y=50)

#Manual Input
#aktual = input("Masukan nilai aktual : ")
#stokiometri = input("Masukan  data Stokiometrik : ")

aktualdata = float()
stokiometridata = float()

#Gui Input massa unsur
labelapp = tk.Label(gui, font="arial 20 bold", text="ITERA x PLTU UPK TARAHAN")
labelapp.pack()

labelkarbon = tk.Label(gui, font = "arial 12 bold", text = "Carbon: ")
labelkarbon.place(x=10, y=50)
karboninput = tk.Entry()
karboninput.place(x=200, y=50)

labelhidrogen = tk.Label(gui, font = "arial 12 bold", text = "Hydrogen : ")
labelhidrogen.place(x=10, y=80)
hidrogeninput = tk.Entry()
hidrogeninput.place(x=200, y=80)

labelsulfur = tk.Label(gui, font = "arial 12 bold", text = "Sulfur : ")
labelsulfur.place(x=10, y=110)
sulfurinput = tk.Entry()
sulfurinput.place(x=200, y=110)

labeloksigen = tk.Label(gui, font = "arial 12 bold", text = "Oxygen : ")
labeloksigen.place(x=10, y=140)
oksigeninput = tk.Entry()
oksigeninput.place(x=200, y=140)

labelnitrogen = tk.Label(gui, font = "arial 12 bold", text = "Nitrogen : ")
labelnitrogen.place(x=10, y=170)
nitrogeninput = tk.Entry()
nitrogeninput.place(x=200, y=170)

labelash = tk.Label(gui, font = "arial 12 bold", text = "Ash : ")
labelash.place(x=10, y=200)
ashinput = tk.Entry()
ashinput.place(x=200, y=200)

labeltm = tk.Label(gui, font = "arial 12 bold", text = "TM: ")
labeltm.place(x=10, y=230)
tminput = tk.Entry()
tminput.place(x=200, y=230)

labeltcf = tk.Label(gui, font = "arial 12 bold", text = "TCF : ")
labeltcf.place(x=10, y=260)
tcfinput = tk.Entry()
tcfinput.place(x=200, y=260)

labellhv = tk.Label(gui, font = "arial 12 bold", text = "LHV : ")
labellhv.place(x=10, y=290)
lhvinput = tk.Entry()
lhvinput.place(x=200, y=290)

labelhhv = tk.Label(gui, font = "arial 12 bold", text = "HHV : ")
labelhhv.place(x=10, y=320)
hhvinput = tk.Entry()
hhvinput.place(x=200, y=320)

labelo2 = tk.Label(gui, font = "arial 12 bold", text = "%O2 : ")
labelo2.place(x=10, y=350)
o2input = tk.Entry()
o2input.place(x=200, y=350)

#fungsi hitung stokometri
def hitung_stokiometrik():
    #pengurangan = (float(aktualinput.get())-float(stokiometriinput.get()))

    #z = float(pengurangan)
    #persentase = float(z/float(stokiometriinput.get()))*100

     #O2 yang diminta
    c = float(karboninput.get())*(32/12)
    h = float(hidrogeninput.get())*(16/2)
    s = float(sulfurinput.get())*(32/32)
    o = -1*(float(oksigeninput.get()))

    tcf = float(tcfinput.get())*(1000/3600)
    hhv = float(hhvinput.get())*4.1868

    #o2 yg giminta total
    o2total = c+h+s+o

    n2 = o2total*(76.7/23.3)

    stoichair = o2total+n2
    #produk

    #heat input
    heatinput = tcf*hhv

    stoichairflow = stoichair*tcf

    #exccessair
    excessair = (float(o2input.get())/(21-float(o2input.get())))*100

    #excessairflow
    excessairflow = (excessair*stoichairflow)/100

    #total air flow
    totalairflow = stoichairflow + excessairflow

    #primaryairflow
    primaryairflow = 1.8*tcf

    #secondaryairflow
    secondaryairflow = stoichairflow-primaryairflow

    #subtotalsaflow
    subtotalsaairflow = secondaryairflow + excessairflow

    textArea = tk.Text(gui,height=10,width=50)
    textArea.place(x=200, y=420)
    jawabano2total = " O2 : {o2} ,".format(o2=o2total)
    jawabann2 = " N2 : {n2plus} ,".format(n2plus=n2)
    jawabanstoichair = " Stoich Air : {stoich} ,".format(stoich=stoichair)
    jawabanheatinput = " Heat input : {heatin} Watt, ".format(heatin=heatinput)
    jawabansaf = " Stoich Air Flow : {saf} tph,".format(saf=stoichairflow)
    jawabanea = " Excess Air : {ea} %,".format(ea=excessair)
    jawabaneaf = " Excess Air Flow : {eaf} tph,".format(eaf=excessairflow)
    jawabanpaf = " Primary Air Flow : {paf} tph,".format(paf=primaryairflow)
    jawabansndaf = " Secondary Air Flow : {sndaf} tph,".format(sndaf=secondaryairflow)
    jawabanstaf = " subTotal Air Flow : {staf} tph,".format(staf=subtotalsaairflow)

    textArea.insert(tk.END, jawabano2total)
    textArea.insert(tk.END, jawabann2)
    textArea.insert(tk.END, jawabanstoichair)
    textArea.insert(tk.END, jawabanheatinput)
    textArea.insert(tk.END, jawabansaf)
    textArea.insert(tk.END, jawabanea)
    textArea.insert(tk.END, jawabaneaf)
    textArea.insert(tk.END, jawabanpaf)
    textArea.insert(tk.END, jawabansndaf)
    textArea.insert(tk.END, jawabanstaf)

    print("hasil total", o2total)
    #print("nilai z = ", z)
    #print("Hasil Persentase : ", persentase)


#def printdata():
    #print("data aktual : ", float(aktualinput.get()))
    #print("data stokiometri : ", float(stokiometriinput.get()))


def flowrate_fungsi():
    flowrate = aktualair*(m/(rho*3600))  #satuan m3/s

    print(flowrate)

def tampilgrafik():
    series = np.array(4, 3)
    x = np.array(5, 10, 1)
    plt.plot(series, x)
    plt.show()

def thermal_efisiensi():
    inlet = input("Masukan inlet Steam : ")
    outlet = input("Masukan outlet Steam : ")
    efisiensi = (outlet/inlet)*100
    print(efisiensi)

#fungsi reset data
def reset():
    karboninput.delete(0)
    hidrogeninput.delete(0)
    sulfurinput.delete(0)
    oksigeninput.delete(0)
    ashinput.delete(0)
    tminput.delete(0)
    tcfinput.delete(0)
    lhvinput.delete(0)
    hhvinput.delete(0)
    o2input.delete(0)

#tombol hitung
tombolhitung = tk.Button(gui, font="arial 13 bold", text = "Hitung", command = hitung_stokiometrik)
tombolhitung.place(x=200, y=380)

tombolreset = tk.Button(gui, font="arial 13 bold", text = "Reset", command = reset)
tombolreset.place(x=300, y=380)

#tombolhitungfr = tk.Button(gui, font="arial 13 bold", text = "Hitung Flow Rate", command = flowrate_fungsi)
#tombolhitungfr.place(x=220, y=350)

tampilkangrafik = tk.Button(gui, font="arial 13 bold", text = "Grafik", command = tampilgrafik)
tampilkangrafik.place(x=400, y=380)

#Hasil
labelhasil=tk.Label(gui, font="arial 12 bold", text="Hasil :")
labelhasil.place(x=10, y=420)

gui.mainloop()