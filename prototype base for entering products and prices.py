from tkinter import Tk, Label, Entry, Button, Text, OptionMenu, messagebox
import mysql.connector
from tkinter import * 


def unesi_u_bazu():
    naziv = unos_naziva.get()
    sifra = unos_sifre.get()
    cijena = float(unos_cijene.get())

    tabela = var_tabela.get()

    conn = mysql.connector.connect(
        host="localhost",
        user ="root",
        password = "12345678",
        database = "baza1"
    )
    cursor = conn.cursor()

    if tabela == "pproizvodi":
        insert_query = "INSERT INTO pproizvodi (naziv, sifra, cijena) VALUES (%s, %s, %s)"
        
        
    elif tabela == "pproizvodi2":
        insert_query = "INSERT INTO pproizvodi2 (naziv, sifra, cijena) VALUES (%s, %s, %s)"
    else:
            messagebox.showerror("Greška", "Nepoznata tabela!")
            return

    values = (naziv, sifra, cijena)
    cursor.execute(insert_query, values)
    conn.commit()

    messagebox.showinfo("Uspjeh", "Podatak je uspješno unesen!")

        
    unos_naziva.delete(0, 'end')
    unos_sifre.delete(0, 'end')
    unos_cijene.delete(0, 'end')
    

    cursor.close()
    conn.close()

def prikazi_sadrzaj():

    odabrna_tabela = var_tabela.get()
    
    conn = mysql.connector.connect(
        host="localhost",
        user ="root",
        password = "12345678",
        database = "baza1"
    )
    cursor = conn.cursor()

    if odabrna_tabela == "pproizvodi":
        select_query = "SELECT * FROM pproizvodi"
        
        
    elif odabrna_tabela == "pproizvodi2":
        select_query = "SELECT * FROM pproizvodi2"
        
    cursor.execute(select_query)
    rezultati = cursor.fetchall()
        
        
    sadrzaj.delete(1.0, 'end')
    for rezultat in rezultati:
        sadrzaj.insert('end', f"Naziv: {rezultat[0]}, Šifra: {rezultat[1]}, Cijena: {rezultat[2]}\n")


    cursor.close()
    conn.close()

def obrisi_sadrzaj():
    odabrana_tablica = var_tabela.get()
    id = unos_id.get()

    conn = mysql.connector.connect(
        host="localhost",
        user ="root",
        password = "12345678",
        database = "baza1"
    )
    cursor = conn.cursor()

    if odabrana_tablica == "pproizvodi":
        delete_query = "DELETE FROM pproizvodi WHERE sifra = %s"
        cursor.execute(delete_query, (id,))
    elif odabrana_tablica == "pproizvodi2":
        delete_query = "DELETE FROM pproizvodi2 WHERE sifra = %s"
        cursor.execute(delete_query, (id,))

    cursor.execute(delete_query,(id,))

    conn.commit()

    cursor.close()
    conn.close()

    unos_id.delete(0, 'end')
    
def pretrazi_po_sifri():
    odabrana_tablica = var_tabela.get()
    sifra_pretrage = unos_sifre_pretrage.get()

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="baza1"
    )
    cursor = conn.cursor()

    if odabrana_tablica == "pproizvodi":
        select_query = "SELECT * FROM pproizvodi WHERE sifra = %s"
        
        
    elif odabrana_tablica == "pproizvodi2":
        select_query = "SELECT * FROM pproizvodi2 WHERE sifra = %s"
   
    cursor.execute(select_query, (sifra_pretrage,))
    rezultati = cursor.fetchall()

    sadrzaj.delete(1.0, 'end')
    for rezultat in rezultati:
        sadrzaj.insert('end', f"Naziv: {rezultat[0]}, Šifra: {rezultat[1]}, Cijena: {rezultat[2]}\n")

    cursor.close()
    conn.close()

def azuriraj_podatke():
    sifra_azuriranje = unos_sifre_azuriranje.get()
    naziv_azuriranje = unos_naziva_azuriranje.get()
    cijena_azuriranje = float(unos_cijene_azuriranje.get())
    odabrna_tabela = var_tabela.get()

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="baza1"
    )
    cursor = conn.cursor()
    
    if odabrna_tabela == "pproizvodi":
        update_query = "UPDATE pproizvodi SET naziv = %s, cijena = %s WHERE sifra = %s"
    elif odabrna_tabela == "pproizvodi2":
        update_query = "UPDATE pproizvodi2 SET naziv = %s, cijena = %s WHERE sifra = %s"

    
    values = (naziv_azuriranje, cijena_azuriranje, sifra_azuriranje)
    cursor.execute(update_query, values)

    conn.commit()

    cursor.close()
    conn.close()

    unos_sifre_azuriranje.delete(0, 'end')
    unos_naziva_azuriranje.delete(0, 'end')
    unos_cijene_azuriranje.delete(0, 'end')



root = Tk()

label_naziv = Label(root, text="Naziv proizvoda:")
label_naziv.pack()
label_naziv.place(y=0,x=10)
unos_naziva = Entry(root)
unos_naziva.pack()
unos_naziva.place(y=20,x=10)
label_sifra = Label(root, text="Šifra proizvoda:")
label_sifra.pack()
label_sifra.place(y=40,x=10)
unos_sifre = Entry(root)
unos_sifre.pack()
unos_sifre.place(y=60,x=10)

label_cijena = Label(root, text="Cijena proizvoda:")
label_cijena.pack()
label_cijena.place(y=80,x=10)
unos_cijene = Entry(root)
unos_cijene.pack()
unos_cijene.place(y=100,x=10)

tabela_list = ["pproizvodi", "pproizvodi2"]  

var_tabela = StringVar(root)
var_tabela.set(tabela_list[0])  
 
izbornik_tabela = OptionMenu(root, var_tabela, *tabela_list)
izbornik_tabela.pack()
izbornik_tabela.place(y=550, x=10)
dugme_prikazi = Button(root, text="Prikaži sadržaj", command=prikazi_sadrzaj)
dugme_prikazi.pack()
dugme_prikazi.place(y=10,x=250)

dugme_unesi = Button(root, text="Unesi u bazu", command=unesi_u_bazu)
dugme_unesi.pack()
dugme_unesi.place(y=120,x=10)


sadrzaj = Text(root)
sadrzaj.pack()


label_id = Label(root, text="Sifra proizvoda za brisanje:")
label_id.pack()
label_id.place(y=170,x=10)
unos_id = Entry(root)
unos_id.pack()
unos_id.place(y=190,x=10)

dugme_obrisi = Button(root, text="Obriši sadržaj", command=obrisi_sadrzaj)
dugme_obrisi.pack()
dugme_obrisi.place(y=210,x=10)

label_pretraga = Label(root, text="Pretraga po šifri:")
label_pretraga.pack()
label_pretraga.place(y=270,x=10)
unos_sifre_pretrage = Entry(root)
unos_sifre_pretrage.pack()
unos_sifre_pretrage.place(y=290,x=10)
dugme_pretrazi = Button(root, text="Pretraži", command=pretrazi_po_sifri)
dugme_pretrazi.pack()
dugme_pretrazi.place(y=310,x=10)
label_sifra_azuriranje = Label(root, text="Šifra proizvoda za ažuriranje:")
label_sifra_azuriranje.pack()
label_sifra_azuriranje.place(y=340,x=10)
unos_sifre_azuriranje = Entry(root)
unos_sifre_azuriranje.pack()
unos_sifre_azuriranje.place(y=360,x=10)
label_naziv_azuriranje = Label(root, text="Novi naziv proizvoda:")
label_naziv_azuriranje.pack()
label_naziv_azuriranje.place(y=390,x=10)
unos_naziva_azuriranje = Entry(root)
unos_naziva_azuriranje.pack()
unos_naziva_azuriranje.place(y=410,x=10)
label_cijena_azuriranje = Label(root, text="Nova cijena proizvoda:")
label_cijena_azuriranje.pack()
label_cijena_azuriranje.place(y=430,x=10)
unos_cijene_azuriranje = Entry(root)
unos_cijene_azuriranje.pack()
unos_cijene_azuriranje.place(y=450,x=10)

dugme_azuriraj = Button(root, text="Ažuriraj podatke", command=azuriraj_podatke)
dugme_azuriraj.pack()
dugme_azuriraj.place(y=470,x=10)



root.mainloop()


