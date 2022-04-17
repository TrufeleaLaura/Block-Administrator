from Functii_get import *
from Functii_principale import *

def afis_apart_chelt_fixdat(li,sum):
    """
    Functia afiseaza apartamentele care au cheltuiala mai mare decat suma data
    """
    try:
        lista_apart = apart_chelt_fixdat(li, sum)
        print('Apartamentele cu o cheltuiala mai mare decat suma data sunt: ', lista_apart)
    except ValueError:
        print("date invalide")


def afis_total_chelt(li,tip):
    """
    Functia afiseaza cheltuielile de un anumit tip de la toate apartamentele
    """
    try:
        if (validare_tip(tip) == False):
            print("data invalida")
            return
        list_chelt = total_chelt(li, tip)
        print("Cheltuielile de acest tip de la toate apartamentele sunt: ", list_chelt)
    except ValueError:
        print("data invalida")


def afis_sum_chelt(li):
    """
    Functia afiseaza suma cheltuielilor a tipului dat
    """
    try:
        tip = str(input("Tipul cheltuielii este: "))
        if (validare_tip(tip) == False):
            print("data invalida")
            return
        cheltuiala = sum_chelt(li, tip)
        print("Suma cheltuielilor de acest tip este: ", cheltuiala)
    except ValueError:
        print("data invalida")


def afis_elim_chelt(li):
    """
    Functia afiseaza lista de dictionare cu anumitul tip specificat de cheltuieli eliminat"""
    try:
        tip = str(input("Tipul cheltuielii este: "))
        if (validare_tip(tip) == False):
            print("data invalida")
            return
        list_afis = elim_chelt(li, tip)
        #modif_list_undo(list_afis,list_undo)
        #list_undo.modif(list_afis)
        print_(list_afis)
    except ValueError:
        print("data invalida")


def afis_elim_chelt_sum(li):
    """
    Functia afiseaza lista de dictionare fara sumele de cheltuieli mai mici decat suma data"""
    try:
        suma = int(input("Suma este: "))
        list_afis = elim_chelt_sum(li, suma)
        #modif_list_undo(list_afis, list_undo)
        #list_undo.modif(list_afis)
        print("S-a efectuata eliminarea cheltuielilor mai micic decat aceasta suma. ")
        print_(list_afis)
    except ValueError:
        print("data invalida")


def afis_adaugare(li,list_undo):
    """
    Functia afiseaza lista de apartamente modificata ,din care s-au sters sumele cheltuielilor
    """
    try:
        ap = int(input("Introduceti numarul apartamentului: "))
        if validare_apart(ap) == False:
            print("data invalida")
            return
        tip_chel = input("Introduceti tipul cheltuielii: ")
        if validare_tip(tip_chel) == False:
            print("data invalida")
            return
        suma = int(input("Introduceti suma cheltuita: "))
        modif_list_undo('ad',[ap,tip_chel,suma],list_undo)
        li = adaugare(li, ap, tip_chel, suma)
        print_(li)
    except ValueError:
        print("data invalida")


def afis_modificare(li,list_undo):
    """
    Functia afiseaza lista de apartamente modificata, adica s-a modificat suma tipului specificat cu suma data

    """
    try:
        ap = int(input("Introduceti numarul apartamentului: "))
        if validare_apart(ap) == False:
            print("data invalida")
            return
        tip_chel = input("Introduceti tipul cheltuielii: ")
        if validare_tip(tip_chel) == False:
            print("data invalida")
            return
        suma = int(input("Introduceti suma cheltuita: "))
        li,suma_veche = modificare(li, ap, tip_chel, suma)
        modif_list_undo('m',[ap,tip_chel,suma_veche],list_undo)
        print('S-a efectuat modificarea cheltuialelii apartamentului : ')
        print_(li)
    except ValueError:
        print("data invalida")


def afis_stergere_chelt(li,list_undo,ap):
    """
    Functia afiseaza lista de apartamente care a suferit modificari,s-a sters cheltuiala de la apartamentul dat
    """
    try:
        li,lista_sume,lista_tipuri=stergere_chelt(li,ap)
        modif_list_undo('st1',[ap,lista_sume,lista_tipuri],list_undo)
        print('S-a efectuat stergerea sumei totale cheltuite ')
        print_(li)
    except ValueError:
        print('data invalida')


def afis_stergere_chelt_cons(li,list_undo):
    """
    Functia afiseaza lista modificata, din care s au sters cheltuielile de la apartamentele date,dar si de la cele care se afla intre ele
    """
    try:
        ap1 = int(input("Introduceti numarul apartamentului 1: "))
        ap2 = int(input("Introduceti numarul apartamentului 2: "))
        if validare_apart(ap1) == False or validare_apart(ap2) == False :
            print("data invalida")
            return
        if (ap1 >ap2):
            ap1, ap2 = ap2, ap1
        print('S-a efectuat stergerea cheltuielilor de la apartamentele consecutive ')
        li,lista_sume=stergere_chelt_cons(li, ap1, ap2)
        modif_list_undo('st2',lista_sume, list_undo)
        print_(li)
    except ValueError:
        print('data invalida')


def afis_stergere_chelt_ambele(li,list_undo):
    """
    Functia afiseaza lista de apartamente din care s-a sters de la toate atat tipul dat, cat si suma tipului de la toate apartamentele
    """
    try:
        tip_chel = input("Introduceti tipul cheltuielii: ")
        if validare_tip(tip_chel) == False:
            print("data invalida")
            return
        li,lista_sume=stergere_chelt_ambele(li, tip_chel)
        modif_list_undo('st3',[lista_sume,tip_chel], list_undo)
        print('S-a efectuat stergerea cheltuialelilor apartamentelor de acel tip : ')
        print_(li)
    except ValueError:
        print("data invalida")

def afis_total_chelt_ap(li,ap):
    """
    Functia afiseaza totalul cheltuielilor pentru aparatmentul dat
    """
    try:
        chelt=total_chelt_ap(li, ap)
        print("Totalul cheltuielilor pentru acest apartament este: ", chelt)
    except ValueError:
        print("data invalida")

def afis_apart_descr(li):
    """
    Functia afiseaza toate apartamentele ordonate descrescator dupa tipul de cheltuiala specificat
    """
    try:
        tip_chel=tip_chel = input("Introduceti tipul cheltuielii: ")
        if validare_tip(tip_chel) == False:
            print("data invalida")
            return
        print("Lista cu apartamentele in ordine descrescatoare in functie de cheltuiala este: ",apart_descr(li,tip_chel))
    except ValueError:
        print("data invalida")

