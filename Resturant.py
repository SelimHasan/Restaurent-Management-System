from tkinter import *
from tkinter import filedialog, messagebox
import random
import time

root = Tk()
root.geometry('1074x642+270+0')
# root.resizable(0, 0)
root.configure(bg="firebrick4")


def reset():
    text_reciept.delete(1.0, END)
    e_rooti.set(0)
    e_daal.set(0)
    e_vaat.set(0)
    e_beaf.set(0)
    e_chicken.set(0)
    e_vorta.set(0)
    e_fish.set(0)
    e_chaap.set(0)
    e_gril.set(0)

    e_coke.set(0)
    e_sprite.set(0)
    e_tango.set(0)
    e_drinko.set(0)
    e_mojo.set(0)
    e_pepsi.set(0)
    e_dew.set(0)
    e_water.set(0)
    e_lassi.set(0)

    e_oreo.set(0)
    e_apple.set(0)
    e_kitkat.set(0)
    e_vanila.set(0)
    e_banana.set(0)
    e_brownie.set(0)
    e_dragon.set(0)
    e_choco.set(0)
    e_forest.set(0)

    entry_rooti.config(state=DISABLED)
    entry_daal.config(state=DISABLED)
    entry_vaat.config(state=DISABLED)
    entry_beaf.config(state=DISABLED)
    entry_gril.config(state=DISABLED)
    entry_chaap.config(state=DISABLED)
    entry_fish.config(state=DISABLED)
    entry_vorta.config(state=DISABLED)
    entry_chicken.config(state=DISABLED)
    entry_coke.config(state=DISABLED)
    entry_sprite.config(state=DISABLED)
    entry_tango.config(state=DISABLED)
    entry_drinko.config(state=DISABLED)
    entry_daal.config(state=DISABLED)
    entry_mojo.config(state=DISABLED)
    entry_pepsi.config(state=DISABLED)
    entry_dew.config(state=DISABLED)
    entry_water.config(state=DISABLED)
    entry_lassi.config(state=DISABLED)
    entry_oreo.config(state=DISABLED)
    entry_apple.config(state=DISABLED)
    entry_kitkat.config(state=DISABLED)
    entry_vanila.config(state=DISABLED)
    entry_banana.config(state=DISABLED)
    entry_brownie.config(state=DISABLED)
    entry_dragon.config(state=DISABLED)
    entry_choco.config(state=DISABLED)
    entry_forest.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    costoffoodvar.set('')
    costofdrinksvar.set('')
    costofcakesvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')


def send():
    def send_msz():
        messege = textinsend.get(1.0, END)
        number = mobile_entry.get()

    root2 = Toplevel()
    root2.title("Send Bill")
    root2.config(bg="red4")
    root2.geometry("400x570+500+50")

    logoimage = PhotoImage(file="50.png")
    logo_label = Label(root2, image=logoimage, bg='black', width=100, height=65, relief=RIDGE)
    logo_label.pack()
    label2 = Label(root2, text="Mobile Number", font=("arial", 17, "bold", "underline"), bg="red4", foreground="white")
    label2.place(x=117, y=65)
    mobile_entry = Entry(root2, font=("arial", 15, "bold"), bd=5.2, width=30)
    mobile_entry.place(x=31, y=103)
    billlabel = Label(root2, text="Bill Details", font=("arial", 14, "bold", "underline"), bg="red4",
                      foreground="white")
    billlabel.place(x=153, y=148)
    textinsend = Text(root2, bd=2, width=42, height=18)
    textinsend.place(x=31, y=185)
    sendlabel = Button(root2, text="Send", command=send_msz, relief=GROOVE, font=("arial", 15, "bold"), bg="firebrick4",
                       bd=6, width=10,
                       foreground="white")
    sendlabel.place(x=138, y=500)
    textinsend.delete(1.0, END)
    x = random.randint(100, 1000)
    textinsend.insert(END, '\t STS Spicy & Thai Restaurant''\n')
    textinsend.insert(END, '\t\tBogura-5801''\n')

    textinsend.insert(END, '\t<<<<<<<<<<<<<>>>>>>>>>>>>>''\n''\n')
    bill = 'BILL NO:' + str(x)
    date = time.strftime('%d/%m/%Y')
    textinsend.insert(END, 'Reciept Ref: \t\t' + bill + '\t\t' + date + '\n')
    textinsend.insert(END, "******************************************"'\n')
    textinsend.insert(END, 'Items\t\t''Cost of Items(Tk)''\n')
    textinsend.insert(END, "******************************************"'\n')
    if e_rooti.get() != '0':
        textinsend.insert(END, f'rooti\t\t{int(e_rooti.get()) * 10}''\n')
    if e_daal.get() != '0':
        textinsend.insert(END, f'daal\t\t{int(e_daal.get()) * 30}''\n')
    if e_vaat.get() != '0':
        textinsend.insert(END, f'vaat\t\t{int(e_vaat.get()) * 20}''\n')
    if e_beaf.get() != '0':
        textinsend.insert(END, f'beaf\t\t{int(e_beaf.get()) * 10}''\n')
    if e_gril.get() != '0':
        textinsend.insert(END, f'gril\t\t{int(e_gril.get()) * 10}''\n')
    if e_chaap.get() != '0':
        textinsend.insert(END, f'chaap\t\t{int(e_chaap.get()) * 10}''\n')
    if e_fish.get() != '0':
        textinsend.insert(END, f'fish\t\t{int(e_fish.get()) * 10}''\n')
    if e_vorta.get() != '0':
        textinsend.insert(END, f'vorta\t\t{int(e_vorta.get()) * 10}''\n')
    if e_chicken.get() != '0':
        textinsend.insert(END, f'chicken\t\t{int(e_chicken.get()) * 10}''\n')
    if e_coke.get() != '0':
        textinsend.insert(END, f'coke\t\t{int(e_coke.get()) * 10}''\n')
    if e_sprite.get() != '0':
        textinsend.insert(END, f'sprite\t\t{int(e_sprite.get()) * 30}''\n')
    if e_tango.get() != '0':
        textinsend.insert(END, f'tango\t\t{int(e_tango.get()) * 20}''\n')
    if e_drinko.get() != '0':
        textinsend.insert(END, f'drinko\t\t{int(e_drinko.get()) * 10}''\n')
    if e_mojo.get() != '0':
        textinsend.insert(END, f'mojo\t\t{int(e_mojo.get()) * 10}''\n')
    if e_pepsi.get() != '0':
        textinsend.insert(END, f'pepsi\t\t{int(e_pepsi.get()) * 10}''\n')
    if e_dew.get() != '0':
        textinsend.insert(END, f'dew\t\t{int(e_dew.get()) * 10}''\n')
    if e_water.get() != '0':
        textinsend.insert(END, f'water\t\t{int(e_water.get()) * 10}''\n')
    if e_lassi.get() != '0':
        textinsend.insert(END, f'lassi\t\t{int(e_lassi.get()) * 10}''\n')
    if e_oreo.get() != '0':
        textinsend.insert(END, f'oreo\t\t{int(e_oreo.get()) * 10}''\n')
    if e_apple.get() != '0':
        textinsend.insert(END, f'apple\t\t{int(e_apple.get()) * 30}''\n')
    if e_kitkat.get() != '0':
        textinsend.insert(END, f'kitkat\t\t{int(e_kitkat.get()) * 20}''\n')
    if e_vanila.get() != '0':
        textinsend.insert(END, f'vanila\t\t{int(e_vanila.get()) * 10}''\n')
    if e_banana.get() != '0':
        textinsend.insert(END, f'banana\t\t{int(e_banana.get()) * 10}''\n')
    if e_brownie.get() != '0':
        textinsend.insert(END, f'brownie\t\t{int(e_brownie.get()) * 10}''\n')
    if e_dragon.get() != '0':
        textinsend.insert(END, f'dragon\t\t{int(e_dragon.get()) * 10}''\n')
    if e_choco.get() != '0':
        textinsend.insert(END, f'choco\t\t{int(e_choco.get()) * 10}''\n')
    if e_forest.get() != '0':
        textinsend.insert(END, f'forest\t\t{int(e_forest.get()) * 10}''\n')
    textinsend.insert(END, "******************************************"'\n')

    textinsend.insert(END, f'Cost of food:\t\t{priceoffood}Tk''\n')
    textinsend.insert(END, f'Cost of Drinks:\t\t{priceofdrinks}Tk''\n')
    textinsend.insert(END, f'Cost of Cakes:\t\t{priceofcakes}Tk''\n')
    textinsend.insert(END, "******************************************"'\n')
    textinsend.insert(END, f'Sub Total:\t\t{priceoffood + priceofdrinks + priceofcakes}Tk''\n')
    textinsend.insert(END, f'Service Tax:\t\t{50}Tk''\n')
    textinsend.insert(END, f'Total Cost:\t\t{priceoffood + priceofdrinks + priceofcakes + 50}Tk''\n')
    textinsend.insert(END, "******************************************"'\n')

    root2.mainloop()


def reciept():
    text_reciept.delete(1.0, END)
    x = random.randint(100, 1000)
    text_reciept.insert(END, '\t STS Spicy & Thai Restaurant''\n')
    text_reciept.insert(END, '\t\tBogura-5801''\n')

    text_reciept.insert(END, '\t<<<<<<<<<<<<<<>>>>>>>>>>>>>>>''\n''\n')
    bill = 'BILL NO :' + str(x)
    date = time.strftime('%d/%m/%Y')
    text_reciept.insert(END, 'Reciept Ref: \t\t' + bill + '\t\t' + date + '\n')
    text_reciept.insert(END, "********************************************"'\n')
    text_reciept.insert(END, 'Items\t\t''Cost of Items(Tk)''\n')
    text_reciept.insert(END, "********************************************"'\n')
    if e_rooti.get() != '0':
        text_reciept.insert(END, f'rooti\t\t{int(e_rooti.get()) * 10}''\n')
    if e_daal.get() != '0':
        text_reciept.insert(END, f'daal\t\t{int(e_daal.get()) * 30}''\n')
    if e_vaat.get() != '0':
        text_reciept.insert(END, f'vaat\t\t{int(e_vaat.get()) * 20}''\n')
    if e_beaf.get() != '0':
        text_reciept.insert(END, f'beaf\t\t{int(e_beaf.get()) * 10}''\n')
    if e_gril.get() != '0':
        text_reciept.insert(END, f'gril\t\t{int(e_gril.get()) * 10}''\n')
    if e_chaap.get() != '0':
        text_reciept.insert(END, f'chaap\t\t{int(e_chaap.get()) * 10}''\n')
    if e_fish.get() != '0':
        text_reciept.insert(END, f'fish\t\t{int(e_fish.get()) * 10}''\n')
    if e_vorta.get() != '0':
        text_reciept.insert(END, f'vorta\t\t{int(e_vorta.get()) * 10}''\n')
    if e_chicken.get() != '0':
        text_reciept.insert(END, f'chicken\t\t{int(e_chicken.get()) * 10}''\n')
    if e_coke.get() != '0':
        text_reciept.insert(END, f'coke\t\t{int(e_coke.get()) * 10}''\n')
    if e_sprite.get() != '0':
        text_reciept.insert(END, f'sprite\t\t{int(e_sprite.get()) * 30}''\n')
    if e_tango.get() != '0':
        text_reciept.insert(END, f'tango\t\t{int(e_tango.get()) * 20}''\n')
    if e_drinko.get() != '0':
        text_reciept.insert(END, f'drinko\t\t{int(e_drinko.get()) * 10}''\n')
    if e_mojo.get() != '0':
        text_reciept.insert(END, f'mojo\t\t{int(e_mojo.get()) * 10}''\n')
    if e_pepsi.get() != '0':
        text_reciept.insert(END, f'pepsi\t\t{int(e_pepsi.get()) * 10}''\n')
    if e_dew.get() != '0':
        text_reciept.insert(END, f'dew\t\t{int(e_dew.get()) * 10}''\n')
    if e_water.get() != '0':
        text_reciept.insert(END, f'water\t\t{int(e_water.get()) * 10}''\n')
    if e_lassi.get() != '0':
        text_reciept.insert(END, f'lassi\t\t{int(e_lassi.get()) * 10}''\n')
    if e_oreo.get() != '0':
        text_reciept.insert(END, f'oreo\t\t{int(e_oreo.get()) * 10}''\n')
    if e_apple.get() != '0':
        text_reciept.insert(END, f'apple\t\t{int(e_apple.get()) * 30}''\n')
    if e_kitkat.get() != '0':
        text_reciept.insert(END, f'kitkat\t\t{int(e_kitkat.get()) * 20}''\n')
    if e_vanila.get() != '0':
        text_reciept.insert(END, f'vanila\t\t{int(e_vanila.get()) * 10}''\n')
    if e_banana.get() != '0':
        text_reciept.insert(END, f'banana\t\t{int(e_banana.get()) * 10}''\n')
    if e_brownie.get() != '0':
        text_reciept.insert(END, f'brownie\t\t{int(e_brownie.get()) * 10}''\n')
    if e_dragon.get() != '0':
        text_reciept.insert(END, f'dragon\t\t{int(e_dragon.get()) * 10}''\n')
    if e_choco.get() != '0':
        text_reciept.insert(END, f'choco\t\t{int(e_choco.get()) * 10}''\n')
    if e_forest.get() != '0':
        text_reciept.insert(END, f'forest\t\t{int(e_forest.get()) * 10}''\n')
    text_reciept.insert(END, "********************************************"'\n')

    text_reciept.insert(END, f'Cost of food:\t\t{priceoffood}Tk''\n')
    text_reciept.insert(END, f'Cost of Drinks:\t\t{priceofdrinks}Tk''\n')
    text_reciept.insert(END, f'Cost of Cakes:\t\t{priceofcakes}Tk''\n')
    text_reciept.insert(END, "********************************************"'\n')
    text_reciept.insert(END, f'Sub Total:\t\t{priceoffood + priceofdrinks + priceofcakes}Tk''\n')
    text_reciept.insert(END, f'Service Tax:\t\t{50}Tk''\n')
    text_reciept.insert(END, f'Total Cost:\t\t{priceoffood + priceofdrinks + priceofcakes + 50}Tk''\n')
    text_reciept.insert(END, "********************************************"'\n')


def total_button():
    global priceoffood, priceofdrinks, priceofcakes, subtotalvar, totalcostvar
    item1 = int(e_rooti.get())
    item2 = int(e_daal.get())
    item3 = int(e_vaat.get())
    item4 = int(e_beaf.get())
    item5 = int(e_gril.get())
    item6 = int(e_chaap.get())
    item7 = int(e_fish.get())
    item8 = int(e_vorta.get())
    item9 = int(e_chicken.get())
    item10 = int(e_coke.get())
    item11 = int(e_sprite.get())
    item12 = int(e_tango.get())
    item13 = int(e_drinko.get())
    item14 = int(e_mojo.get())
    item15 = int(e_pepsi.get())
    item16 = int(e_dew.get())
    item17 = int(e_water.get())
    item18 = int(e_lassi.get())
    item19 = int(e_oreo.get())
    item20 = int(e_apple.get())
    item21 = int(e_kitkat.get())
    item22 = int(e_vanila.get())
    item23 = int(e_banana.get())
    item24 = int(e_brownie.get())
    item25 = int(e_dragon.get())
    item26 = int(e_choco.get())
    item27 = int(e_forest.get())

    priceoffood = (item1 * 10) + (item2 * 30) + (item3 * 20) + (item4 * 10) + (item5 * 10) + (item6 * 10) + (item7 * 10) \
                  + (item8 * 10) + (item9 * 10)
    priceofdrinks = (item10 * 10) + (item11 * 30) + (item12 * 20) + (item13 * 10) + (item14 * 10) + (item15 * 10) \
                    + (item16 * 10) + (item17 * 10) + (item18 * 10)
    priceofcakes = (item19 * 10) + (item20 * 30) + (item21 * 20) + (item22 * 10) + (item23 * 10) + (item24 * 10) \
                   + (item25 * 10) + (item26 * 10) + (item27 * 10)
    costoffoodvar.set(str(priceoffood) + '   Tk.')
    costofdrinksvar.set(str(priceofdrinks) + '   Tk.')
    costofcakesvar.set(str(priceofcakes) + '   Tk.')

    subtotalitem = priceoffood + priceofdrinks + priceofcakes
    subtotalvar.set(str(subtotalitem) + '  Tk.')

    servicetaxvar.set('50 Tk')
    totalfinance = subtotalitem + 50
    totalcostvar.set(str(totalfinance) + 'Tk.')


def save():
    url = filedialog.asksaveasfile(mode='w', defaultextension='txt')

    bill = (text_reciept.get(1.0, END))
    url.write(bill)
    url.close()
    messagebox.showinfo('information', 'Your bill is saved successfully')


def rooti():
    if var1.get() == 1:
        entry_rooti.config(state=NORMAL)
        entry_rooti.delete(0, END)
        entry_rooti.focus()
    else:
        entry_rooti.config(state=DISABLED)
        e_rooti.set(0)


def daal():
    if var2.get() == 1:
        entry_daal.config(state=NORMAL)
        entry_daal.delete(0)
        entry_daal.focus()
    else:
        entry_daal.config(state=DISABLED)
        e_daal.set(0)


def vaat():
    if var3.get() == 1:
        entry_vaat.config(state=NORMAL)
        entry_vaat.delete(0, END)
        entry_vaat.focus()
    else:
        entry_vaat.config(state=DISABLED)
        e_vaat.set(0)


def beaf():
    if var4.get() == 1:
        entry_beaf.config(state=NORMAL)
        entry_beaf.delete(0, END)
        entry_beaf.focus()
    else:
        entry_beaf.config(state=DISABLED)
        e_beaf.set(0)


def gril():
    if var5.get() == 1:
        entry_gril.config(state=NORMAL)
        entry_gril.delete(0, END)
        entry_gril.focus()
    else:
        entry_gril.config(state=DISABLED)
        e_gril.set(0)


def chaap():
    if var6.get() == 1:
        entry_chaap.config(state=NORMAL)
        entry_chaap.delete(0, END)
        entry_chaap.focus()
    else:
        entry_chaap.config(state=DISABLED)
        e_chaap.set(0)


def fish():
    if var7.get() == 1:
        entry_fish.config(state=NORMAL)
        entry_fish.delete(0, END)
        entry_fish.focus()
    else:
        entry_fish.config(state=DISABLED)
        e_fish.set(0)


def vorta():
    if var8.get() == 1:
        entry_vorta.config(state=NORMAL)
        entry_vorta.delete(0, END)
        entry_vorta.focus()
    else:
        entry_vorta.config(state=DISABLED)
        e_vorta.set(0)


def chicken():
    if var9.get() == 1:
        entry_chicken.config(state=NORMAL)
        entry_chicken.delete(0, END)
        entry_chicken.focus()
    else:
        entry_chicken.config(state=DISABLED)
        e_chicken.set(0)


def coke():
    if var10.get() == 1:
        entry_coke.config(state=NORMAL)
        entry_coke.delete(0, END)
        entry_coke.focus()
    else:
        entry_coke.config(state=DISABLED)
        e_coke.set(0)


def sprite():
    if var11.get() == 1:
        entry_sprite.config(state=NORMAL)
        entry_sprite.delete(0, END)
        entry_sprite.focus()
    else:
        entry_sprite.config(state=DISABLED)
        e_sprite.set(0)


def tango():
    if var12.get() == 1:
        entry_tango.config(state=NORMAL)
        entry_tango.delete(0, END)
        entry_tango.focus()
    else:
        entry_tango.config(state=DISABLED)
        e_tango.set(0)


def drinko():
    if var13.get() == 1:
        entry_drinko.config(state=NORMAL)
        entry_drinko.delete(0, END)
        entry_drinko.focus()
    else:
        entry_drinko.config(state=DISABLED)
        e_drinko.set(0)


def mojo():
    if var14.get() == 1:
        entry_mojo.config(state=NORMAL)
        entry_mojo.delete(0, END)
        entry_mojo.focus()
    else:
        entry_mojo.config(state=DISABLED)
        e_mojo.set(0)


def pepsi():
    if var15.get() == 1:
        entry_pepsi.config(state=NORMAL)
        entry_pepsi.delete(0, END)
        entry_pepsi.focus()
    else:
        entry_pepsi.config(state=DISABLED)
        e_pepsi.set(0)


def dew():
    if var16.get() == 1:
        entry_dew.config(state=NORMAL)
        entry_dew.delete(0, END)
        entry_dew.focus()
    else:
        entry_dew.config(state=DISABLED)
        e_dew.set(0)


def water():
    if var17.get() == 1:
        entry_water.config(state=NORMAL)
        entry_water.delete(0, END)
        entry_water.focus()
    else:
        entry_water.config(state=DISABLED)
        e_water.set(0)


def lassi():
    if var18.get() == 1:
        entry_lassi.config(state=NORMAL)
        entry_lassi.delete(0, END)
        entry_lassi.focus()
    else:
        entry_lassi.config(state=DISABLED)
        e_lassi.set(0)


def oreo():
    if var19.get() == 1:
        entry_oreo.config(state=NORMAL)
        entry_oreo.delete(0, END)
        entry_oreo.focus()
    else:
        entry_oreo.config(state=DISABLED)
        e_oreo.set(0)


def apple():
    if var20.get() == 1:
        entry_apple.config(state=NORMAL)
        entry_apple.delete(0, END)
        entry_apple.focus()
    else:
        entry_apple.config(state=DISABLED)
        e_apple.set(0)


def kitkat():
    if var21.get() == 1:
        entry_kitkat.config(state=NORMAL)
        entry_kitkat.delete(0, END)
        entry_kitkat.focus()
    else:
        entry_kitkat.config(state=DISABLED)
        e_kitkat.set(0)


def vanila():
    if var22.get() == 1:
        entry_vanila.config(state=NORMAL)
        entry_vanila.delete(0, END)
        entry_vanila.focus()
    else:
        entry_vanila.config(state=DISABLED)
        e_vanila.set(0)


def banana():
    if var23.get() == 1:
        entry_banana.config(state=NORMAL)
        entry_banana.delete(0, END)
        entry_banana.focus()
    else:
        entry_banana.config(state=DISABLED)
        e_banana.set(0)


def brownie():
    if var24.get() == 1:
        entry_brownie.config(state=NORMAL)
        entry_brownie.delete(0, END)
        entry_brownie.focus()
    else:
        entry_brownie.config(state=DISABLED)
        e_brownie.set(0)


def dragon():
    if var25.get() == 1:
        entry_dragon.config(state=NORMAL)
        entry_dragon.delete(0, END)
        entry_dragon.focus()
    else:
        entry_dragon.config(state=DISABLED)
        e_dragon.set(0)


def choco():
    if var26.get() == 1:
        entry_choco.config(state=NORMAL)
        entry_choco.delete(0, END)
        entry_choco.focus()
    else:
        entry_choco.config(state=DISABLED)
        e_choco.set(0)


def forest():
    if var27.get() == 1:
        entry_forest.config(state=NORMAL)
        entry_forest.delete(0, END)
        entry_forest.focus()
    else:
        entry_forest.config(state=DISABLED)
        e_forest.set(0)


##############.......Frame

top_frame = Frame(root, bd=5, relief=RIDGE)
top_frame.pack(side=TOP)
menu_frame = Frame(root, bd=8, relief=RIDGE, bg="red4", pady=2)
menu_frame.pack(side=LEFT)

cost_frame = Frame(menu_frame, bd=5, relief=RIDGE, bg="firebrick4", padx=14, pady=17)
cost_frame.pack(side=BOTTOM)

food_frame = LabelFrame(menu_frame, text="Foods", font=("arial", 17, "bold"), pady=4.5, bd=5, foreground="green",
                        relief=RIDGE, )
food_frame.pack(side=LEFT)

Drinks_frame = LabelFrame(menu_frame, text="Drinks", font=("arial", 17, "bold"), pady=4.5, foreground="green", bd=5,
                          relief=RIDGE)
Drinks_frame.pack(side=LEFT)

Cakes_frame = LabelFrame(menu_frame, text="Cakes", font=("arial", 17, "bold"), pady=4.5, foreground="green", bd=5,
                         relief=RIDGE)
Cakes_frame.pack(side=LEFT)

right_frame = Frame(root, bd=8, relief=RIDGE, bg="red4", pady=4)
right_frame.pack(side=RIGHT)

calc_frame = Frame(right_frame, bd=1, relief=RIDGE, pady=15, padx=7, bg="red4")
calc_frame.pack()

reciept_frame = Frame(right_frame, bd=1, relief=RIDGE, pady=3, bg="firebrick4", width=20)
reciept_frame.pack()

Button_frame = Frame(right_frame, bd=4.5, relief=RIDGE, pady=2.5, padx=6, bg="red4")
Button_frame.pack()

##############..........Foods

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

e_rooti = StringVar()
e_daal = StringVar()
e_vaat = StringVar()
e_beaf = StringVar()
e_gril = StringVar()
e_fish = StringVar()
e_vorta = StringVar()
e_chaap = StringVar()
e_chicken = StringVar()

e_coke = StringVar()
e_sprite = StringVar()
e_tango = StringVar()
e_drinko = StringVar()
e_mojo = StringVar()
e_pepsi = StringVar()
e_dew = StringVar()
e_water = StringVar()
e_lassi = StringVar()

e_oreo = StringVar()
e_apple = StringVar()
e_kitkat = StringVar()
e_vanila = StringVar()
e_banana = StringVar()
e_brownie = StringVar()
e_dragon = StringVar()
e_choco = StringVar()
e_forest = StringVar()

costoffoodvar = StringVar()
costofdrinksvar = StringVar()
costofcakesvar = StringVar()
subtotalvar = StringVar()
servicetaxvar = StringVar()
totalcostvar = StringVar()

##########Entry set()

e_rooti.set(0)
e_daal.set(0)
e_vaat.set(0)
e_beaf.set(0)
e_chicken.set(0)
e_vorta.set(0)
e_fish.set(0)
e_chaap.set(0)
e_gril.set(0)

e_coke.set(0)
e_sprite.set(0)
e_tango.set(0)
e_drinko.set(0)
e_mojo.set(0)
e_pepsi.set(0)
e_dew.set(0)
e_water.set(0)
e_lassi.set(0)

e_oreo.set(0)
e_apple.set(0)
e_kitkat.set(0)
e_vanila.set(0)
e_banana.set(0)
e_brownie.set(0)
e_dragon.set(0)
e_choco.set(0)
e_forest.set(0)

rooti = Checkbutton(food_frame, text="Rooti", font=("arial", 15, "bold"), onvalue=1, offvalue=0, command=rooti,
                    variable=var1)
rooti.grid(row=0, column=0, sticky=W)

Daal = Checkbutton(food_frame, text="Daal", command=daal, font=("arial", 15, "bold"), onvalue=1, offvalue=0,
                   variable=var2)
Daal.grid(row=1, column=0, sticky=W)

Vaat = Checkbutton(food_frame, text="Vaat", command=vaat, font=("arial", 15, "bold"), onvalue=1, offvalue=0,
                   variable=var3)
Vaat.grid(row=2, column=0, sticky=W)

Beaf = Checkbutton(food_frame, text="Beaf", command=beaf, font=("arial", 15, "bold"), onvalue=1, offvalue=0,
                   variable=var4)
Beaf.grid(row=3, column=0, sticky=W)

Griil = Checkbutton(food_frame, text="Griil", command=gril, font=("arial", 15, "bold"), onvalue=1, offvalue=0,
                    variable=var5)
Griil.grid(row=4, column=0, sticky=W)

Chaap = Checkbutton(food_frame, text="Chaap", command=chaap, font=("arial", 15, "bold"), onvalue=1, offvalue=0,
                    variable=var6)
Chaap.grid(row=5, column=0, sticky=W)

Fish = Checkbutton(food_frame, text="Fish Rui", command=fish, font=("arial", 15, "bold"), onvalue=1, offvalue=0,
                   variable=var7)
Fish.grid(row=6, column=0, sticky=W)

Vorta = Checkbutton(food_frame, text="S.Vorta", command=vorta, font=("arial", 15, "bold"), onvalue=1, offvalue=0,
                    variable=var8)
Vorta.grid(row=7, column=0, sticky=W)

Chicken = Checkbutton(food_frame, text="Chicken", command=chicken, font=("arial", 15, "bold"), onvalue=1, offvalue=0,
                      variable=var9)
Chicken.grid(row=8, column=0, sticky=W)

########Entry_for_Rooti

entry_rooti = Entry(food_frame, bd=7, relief=RIDGE, textvariable=e_rooti, width=6, state=DISABLED,
                    font=("arial", 13, "bold"))
entry_rooti.grid(row=0, column=1)

entry_daal = Entry(food_frame, bd=7, relief=RIDGE, textvariable=e_daal, state=DISABLED, width=6,
                   font=("arial", 13, "bold"))
entry_daal.grid(row=1, column=1)

entry_vaat = Entry(food_frame, bd=7, relief=RIDGE, textvariable=e_vaat, state=DISABLED, width=6,
                   font=("arial", 13, "bold"))
entry_vaat.grid(row=2, column=1)

entry_beaf = Entry(food_frame, bd=7, relief=RIDGE, textvariable=e_beaf, state=DISABLED, width=6,
                   font=("arial", 13, "bold"))
entry_beaf.grid(row=3, column=1)
entry_gril = Entry(food_frame, bd=7, relief=RIDGE, textvariable=e_gril, width=6, state=DISABLED,
                   font=("arial", 13, "bold"))
entry_gril.grid(row=4, column=1)

entry_chaap = Entry(food_frame, bd=7, relief=RIDGE, textvariable=e_chaap, width=6, state=DISABLED,
                    font=("arial", 13, "bold"))
entry_chaap.grid(row=5, column=1)

entry_fish = Entry(food_frame, bd=7, relief=RIDGE, textvariable=e_fish, width=6, state=DISABLED,
                   font=("arial", 13, "bold"))
entry_fish.grid(row=6, column=1)
entry_vorta = Entry(food_frame, bd=7, relief=RIDGE, textvariable=e_vorta, state=DISABLED, width=6,
                    font=("arial", 13, "bold"))
entry_vorta.grid(row=7, column=1)

entry_chicken = Entry(food_frame, bd=7, relief=RIDGE, textvariable=e_chicken, state=DISABLED, width=6,
                      font=("arial", 13, "bold"))
entry_chicken.grid(row=8, column=1)

############ Drinks

coke = Checkbutton(Drinks_frame, text="Coke", command=coke, font=("arial", 15, "bold"), onvalue=1, offvalue=0,
                   variable=var10)
coke.grid(row=0, column=1, sticky=W)

sprite = Checkbutton(Drinks_frame, text="Sprite", command=sprite, font=("arial", 15, "bold"), onvalue=1, offvalue=0,
                     variable=var11)
sprite.grid(row=1, column=1, sticky=W)

tango = Checkbutton(Drinks_frame, text="Tango", command=tango, font=("arial", 15, "bold"), onvalue=1, offvalue=0,
                    variable=var12)
tango.grid(row=2, column=1, sticky=W)

drinko = Checkbutton(Drinks_frame, text="Drinko", command=drinko, font=("arial", 15, "bold"), onvalue=1, offvalue=0,
                     variable=var13)
drinko.grid(row=3, column=1, sticky=W)

mojo = Checkbutton(Drinks_frame, text="Mojo", command=mojo, font=("arial", 15, "bold"), onvalue=1, offvalue=0,
                   variable=var14)
mojo.grid(row=4, column=1, sticky=W)

pepsi = Checkbutton(Drinks_frame, text="Pepsi", command=pepsi, font=("arial", 15, "bold"), onvalue=1, offvalue=0,
                    variable=var15)
pepsi.grid(row=5, column=1, sticky=W)

dew = Checkbutton(Drinks_frame, text="M.Dew ", command=dew, font=("arial", 15, "bold"), onvalue=1, offvalue=0,
                  variable=var16)
dew.grid(row=6, column=1, sticky=W)

water = Checkbutton(Drinks_frame, text="Water 1L", command=water, font=("arial", 15, "bold"), onvalue=1, offvalue=0,
                    variable=var17)
water.grid(row=7, column=1, sticky=W)

lassi = Checkbutton(Drinks_frame, text="Lassi 1L", command=lassi, font=("arial", 15, "bold"), onvalue=1, offvalue=0,
                    variable=var18)
lassi.grid(row=8, column=1, sticky=W)

######### Entry for Drinks

entry_coke = Entry(Drinks_frame, bd=7, relief=RIDGE, textvariable=e_coke, width=6, state=DISABLED,
                   font=("arial", 13, "bold"))
entry_coke.grid(row=0, column=2)
entry_sprite = Entry(Drinks_frame, bd=7, relief=RIDGE, textvariable=e_sprite, width=6, state=DISABLED,
                     font=("arial", 13, "bold"))
entry_sprite.grid(row=1, column=2)
entry_tango = Entry(Drinks_frame, bd=7, relief=RIDGE, textvariable=e_tango, width=6, state=DISABLED,
                    font=("arial", 13, "bold"))
entry_tango.grid(row=2, column=2)
entry_drinko = Entry(Drinks_frame, bd=7, relief=RIDGE, textvariable=e_drinko, width=6, state=DISABLED,
                     font=("arial", 13, "bold"))
entry_drinko.grid(row=3, column=2)
entry_mojo = Entry(Drinks_frame, bd=7, relief=RIDGE, textvariable=e_mojo, width=6, state=DISABLED,
                   font=("arial", 13, "bold"))
entry_mojo.grid(row=4, column=2)
entry_pepsi = Entry(Drinks_frame, bd=7, relief=RIDGE, textvariable=e_pepsi, width=6, state=DISABLED,
                    font=("arial", 13, "bold"))
entry_pepsi.grid(row=5, column=2)
entry_dew = Entry(Drinks_frame, bd=7, relief=RIDGE, textvariable=e_dew, width=6, state=DISABLED,
                  font=("arial", 13, "bold"))
entry_dew.grid(row=6, column=2)
entry_water = Entry(Drinks_frame, bd=7, relief=RIDGE, textvariable=e_water, width=6, state=DISABLED,
                    font=("arial", 13, "bold"))
entry_water.grid(row=7, column=2)
entry_lassi = Entry(Drinks_frame, bd=7, relief=RIDGE, textvariable=e_lassi, width=6, state=DISABLED,
                    font=("arial", 13, "bold"))
entry_lassi.grid(row=8, column=2)

###########Cakes

Oreo = Checkbutton(Cakes_frame, text="Oreo", command=oreo, font=("arial", 15, "bold"), onvalue=1, offvalue=0,
                   variable=var19)
Oreo.grid(row=0, column=0, sticky=W)
Apple = Checkbutton(Cakes_frame, text="Apple", command=apple, font=("arial", 15, "bold"), onvalue=1, offvalue=0,
                    variable=var20)
Apple.grid(row=1, column=0, sticky=W)
Kitkat = Checkbutton(Cakes_frame, text="Kitkat", command=kitkat, font=("arial", 15, "bold"), onvalue=1, offvalue=0,
                     variable=var21)
Kitkat.grid(row=2, column=0, sticky=W)
Vanila = Checkbutton(Cakes_frame, text="Vanila", command=vanila, font=("arial", 15, "bold"), onvalue=1, offvalue=0,
                     variable=var22)
Vanila.grid(row=3, column=0, sticky=W)
Banana = Checkbutton(Cakes_frame, text="Banana", command=banana, font=("arial", 15, "bold"), onvalue=1, offvalue=0,
                     variable=var23)
Banana.grid(row=4, column=0, sticky=W)
Brownie = Checkbutton(Cakes_frame, text="Brownie", command=brownie, font=("arial", 15, "bold"), onvalue=1, offvalue=0,
                      variable=var24)
Brownie.grid(row=5, column=0, sticky=W)
Dragon = Checkbutton(Cakes_frame, text="Dragon", command=dragon, font=("arial", 15, "bold"), onvalue=1, offvalue=0,
                     variable=var25)
Dragon.grid(row=6, column=0, sticky=W)
Choco = Checkbutton(Cakes_frame, text="Choco", command=choco, font=("arial", 15, "bold"), onvalue=1, offvalue=0,
                    variable=var26)
Choco.grid(row=7, column=0, sticky=W)
forest = Checkbutton(Cakes_frame, text="Forest", command=forest, font=("arial", 15, "bold"), onvalue=1, offvalue=0,
                     variable=var27)
forest.grid(row=8, column=0, sticky=W)

############Entry  For Cakes

entry_oreo = Entry(Cakes_frame, bd=7, relief=RIDGE, textvariable=e_oreo, width=6, state=DISABLED,
                   font=("arial", 13, "bold"))
entry_oreo.grid(row=0, column=2)
entry_apple = Entry(Cakes_frame, bd=7, relief=RIDGE, textvariable=e_apple, width=6, state=DISABLED,
                    font=("arial", 13, "bold"))
entry_apple.grid(row=1, column=2)
entry_kitkat = Entry(Cakes_frame, bd=7, relief=RIDGE, textvariable=e_kitkat, width=6, state=DISABLED,
                     font=("arial", 13, "bold"))
entry_kitkat.grid(row=2, column=2)
entry_vanila = Entry(Cakes_frame, bd=7, relief=RIDGE, textvariable=e_vanila, width=6, state=DISABLED,
                     font=("arial", 13, "bold"))
entry_vanila.grid(row=3, column=2)
entry_banana = Entry(Cakes_frame, bd=7, relief=RIDGE, textvariable=e_banana, width=6, state=DISABLED,
                     font=("arial", 13, "bold"))
entry_banana.grid(row=4, column=2)
entry_brownie = Entry(Cakes_frame, bd=7, relief=RIDGE, textvariable=e_brownie, width=6, state=DISABLED,
                      font=("arial", 13, "bold"))
entry_brownie.grid(row=5, column=2)
entry_dragon = Entry(Cakes_frame, bd=7, relief=RIDGE, textvariable=e_dragon, width=6, state=DISABLED,
                     font=("arial", 13, "bold"))
entry_dragon.grid(row=6, column=2)
entry_choco = Entry(Cakes_frame, bd=7, relief=RIDGE, textvariable=e_choco, width=6, state=DISABLED,
                    font=("arial", 13, "bold"))
entry_choco.grid(row=7, column=2)
entry_forest = Entry(Cakes_frame, bd=7, relief=RIDGE, textvariable=e_forest, width=6, state=DISABLED,
                     font=("arial", 13, "bold"))
entry_forest.grid(row=8, column=2)

#############Cost of foods

foodCost = Label(cost_frame, text="Cost of Foods", bg="firebrick4", fg="white", font=("arial", 12, "bold"))
foodCost.grid(row=0, column=0)
foodCost_entry = Entry(cost_frame, font=("arial", 12, "bold"), bd=4, width=12, state='readonly',
                       textvariable=costoffoodvar)
foodCost_entry.grid(row=0, column=1)

drinksCost = Label(cost_frame, text="Cost of Drinks", bg="firebrick4", fg="white", font=("arial", 12, "bold"))
drinksCost.grid(row=1, column=0)
drinksCost_entry = Entry(cost_frame, font=("arial", 12, "bold"), bd=4, width=12, state='readonly',
                         textvariable=costofdrinksvar)
drinksCost_entry.grid(row=1, column=1)

cakesCost = Label(cost_frame, text="Cost of Cakes", bg="firebrick4", fg="white", font=("arial", 12, "bold"))
cakesCost.grid(row=2, column=0)
cakesCost_entry = Entry(cost_frame, font=("arial", 12, "bold"), bd=4, width=12, state='readonly',
                        textvariable=costofcakesvar)
cakesCost_entry.grid(row=2, column=1)

sub_total = Label(cost_frame, text="Sub Total", bg="firebrick4", fg="white", font=("arial", 12, "bold"), pady=6)
sub_total.grid(row=0, column=2)
sub_total_entry = Entry(cost_frame, font=("arial", 12, "bold"), bd=4, width=12, state='readonly',
                        textvariable=subtotalvar)
sub_total_entry.grid(row=0, column=3, padx=43)

service_tax = Label(cost_frame, text=" Service Tax", bg="firebrick4", fg="white", font=("arial", 12, "bold"), pady=6)
service_tax.grid(row=1, column=2)
service_tax_entry = Entry(cost_frame, font=("arial", 12, "bold"), bd=4, width=12, state='readonly',
                          textvariable=servicetaxvar)
service_tax_entry.grid(row=1, column=3, padx=43)

total_cost = Label(cost_frame, text="Total Cost", bg="firebrick4", fg="white", font=("arial", 12, "bold"), pady=6)
total_cost.grid(row=2, column=2)
total_cost_entry = Entry(cost_frame, font=("arial", 12, "bold"), bd=4, width=12, state='readonly',
                         textvariable=totalcostvar)
total_cost_entry.grid(row=2, column=3, padx=43)

##########Right_frame
###########Button

button_total = Button(Button_frame, text="Total", command=total_button, font=("arial", 12, "bold"), bg="red4", bd=3,
                      foreground="white")
button_total.grid(row=0, column=0, padx=2)

button_reciept = Button(Button_frame, text="Reciept", font=("arial", 12, "bold"), command=reciept, bg="red4", bd=3,
                        foreground="white")
button_reciept.grid(row=0, column=1, padx=2)

button_save = Button(Button_frame, text="Save", command=save, font=("arial", 12, "bold"), bg="red4", bd=3,
                     foreground="white")
button_save.grid(row=0, column=2, padx=2)

button_send = Button(Button_frame, text="Send", font=("arial", 12, "bold"), command=send, bg="red4", bd=3,
                     foreground="white")
button_send.grid(row=0, column=3, padx=2)

button_reset = Button(Button_frame, text="Reset", font=("arial", 12, "bold"), command=reset, bg="red4", bd=3,
                      foreground="white")
button_reset.grid(row=0, column=4, padx=2)

button_print = Button(Button_frame, text="Print", font=("arial", 12, "bold"), bg="red4", bd=3, foreground="white")
button_print.grid(row=0, column=5, padx=2)

button_quit = Button(Button_frame, text="Quit", font=("arial", 12, "bold"), bg="red4", bd=3, foreground="white")
button_quit.grid(row=0, column=6, padx=2)

###########Text area in reciept frame

text_reciept = Text(reciept_frame, font=("courier new", 12), pady=7, bd=4, width=44, height=12.4)
text_reciept.grid(row=0, column=0)

###########Calculator_frame

operator = ''


def button_click(numbers):
    global operator
    operator = operator + numbers
    calculatorarea.delete(0, END)
    calculatorarea.insert(END, operator)


def clear():
    global operator
    operator = ''
    calculatorarea.delete(0, END)


def answer():
    global operator
    result = str(eval(operator))
    calculatorarea.delete(0, END)
    calculatorarea.insert(0, result)
    operator = ''


calculatorarea = Entry(calc_frame, font=("arial", 15, "bold"), width=39, bd=4)
calculatorarea.grid(row=0, column=0, columnspan=28)

button7 = Button(calc_frame, text="7", font=("arial", 12, "bold"), bg="red4", foreground="yellow", bd=4, width=9
                 , command=lambda: button_click('7'))
button7.grid(row=1, column=0)

button8 = Button(calc_frame, text="8", font=("arial", 12, "bold"), bg="red4", foreground="yellow", bd=4, width=9,
                 command=lambda: button_click('8'))
button8.grid(row=1, column=1)

button9 = Button(calc_frame, text="9", font=("arial", 12, "bold"), bg="red4", foreground="yellow", bd=4, width=9,
                 command=lambda: button_click('9'))
button9.grid(row=1, column=2)

button_addition = Button(calc_frame, text="+", font=("arial", 12, "bold"), bg="red4", foreground="yellow", bd=4,
                         command=lambda: button_click('+'), width=9)
button_addition.grid(row=1, column=3)

button4 = Button(calc_frame, text="4", font=("arial", 12, "bold"), bg="red4", foreground="yellow", bd=4, width=9,
                 command=lambda: button_click('4'))
button4.grid(row=2, column=0)

button5 = Button(calc_frame, text="5", font=("arial", 12, "bold"), bg="red4", foreground="yellow", bd=4, width=9,
                 command=lambda: button_click('5'))
button5.grid(row=2, column=1)

button6 = Button(calc_frame, text="6", font=("arial", 12, "bold"), bg="red4", foreground="yellow", bd=4, width=9,
                 command=lambda: button_click('6'))
button6.grid(row=2, column=2)

buttonminus = Button(calc_frame, text="-", font=("arial", 12, "bold"), bg="red4", foreground="yellow", bd=4, width=9,
                     command=lambda: button_click('-'))
buttonminus.grid(row=2, column=3)

button1 = Button(calc_frame, text="1", font=("arial", 12, "bold"), bg="red4", foreground="yellow", bd=4, width=9,
                 command=lambda: button_click('1'))
button1.grid(row=3, column=0)

button2 = Button(calc_frame, text="2", font=("arial", 12, "bold"), bg="red4", foreground="yellow", bd=4, width=9,
                 command=lambda: button_click('2'))
button2.grid(row=3, column=1)

button3 = Button(calc_frame, text="3", font=("arial", 12, "bold"), bg="red4", foreground="yellow", bd=4, width=9,
                 command=lambda: button_click('3'))
button3.grid(row=3, column=2)

buttonmulti = Button(calc_frame, text="*", font=("arial", 12, "bold"), bg="red4", foreground="yellow", bd=4, width=9,
                     command=lambda: button_click('*'))
buttonmulti.grid(row=3, column=3)

buttonans = Button(calc_frame, text="Ans", font=("arial", 12, "bold"), bg="red4", foreground="yellow", bd=4, width=9,
                   command=answer)
buttonans.grid(row=4, column=0)

buttonclear = Button(calc_frame, text="Clear", font=("arial", 12, "bold"), bg="red4", foreground="yellow", bd=4,
                     width=9, command=clear)
buttonclear.grid(row=4, column=1)

button0 = Button(calc_frame, text="0", font=("arial", 12, "bold"), bg="red4", foreground="yellow", bd=4, width=9,
                 command=lambda: button_click('0'))
button0.grid(row=4, column=2)

buttondiv = Button(calc_frame, text="/", font=("arial", 12, "bold"), bg="red4", foreground="yellow", bd=4, width=9,
                   command=lambda: button_click('/'))
buttondiv.grid(row=4, column=3)

##############.......Label

head_label = Label(top_frame, text="STS Spicy & Thai Restaurant", bd=8, bg="#5c0600", foreground="yellow",
                   font=("vernada", 25, "bold"), width=52, height=1)
head_label.grid(row=0, column=0)

head2_label = Label(top_frame, text="Shajahanpur,Bogura-5801", bd=4, bg="#5c0600", foreground="white",
                    font=("arial", 10), width=131)
head2_label.grid(row=1, column=0)

credit_label = Label(text='All Rights are reserved by SELIM HASAN-2022', font=("arial", 6), bg='firebrick4',
                     foreground='white')
credit_label.place(x=5, y=624)
root.mainloop()
