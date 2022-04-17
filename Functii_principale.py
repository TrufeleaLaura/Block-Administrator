from Functii_get import *

def apart_chelt_fixdat(lista, sm):
    """
    Functia gaseste apartamentele care au cheltuiala mai mare decat suma data
    input: lista de apartamente,suma data
    output:lista care contine apartamentele care indeplinesc conditia specificata
    """
    li = []
    for ap in lista:
        suma = 0
        lists = apart_sumchelt(ap)  # retine lista cu sumele cheltuite la respectivul apartament
        for i in range(len(lists)):  # se parcurge lista si calculeaza totalul cheltuielilor
            suma = suma + lists[i]
        if suma > sm:
            li.append(nr_apart(ap))
    return li


def total_chelt(lista, tip):
    """
    Functia gaseste toate cheltuielite de un anumit tip
    input:lista de apartamente,tipul cheltuielii
    output: lista care retine cheltuielile de un anumit tip de la fiecare apartament
    """
    li = []
    for ap in lista:
        lists = apart_tipchelt(ap)  # retine lista cu tipurile cheltuielilor de la respectivul apartament
        for i in range(len(lists)):
            if lists[i] == tip:  # daca s-a gasit tipul cheltuielii cerut se va adauga suma corespunzatoare care a fost cheltuita,regasindu-se pe aceleasi pozitii in lista
                aux = apart_sumchelt(ap)  # aux este lista cu suma cheltuielilor de la acel apartament
                li.append(aux[i])
    return li


def sum_chelt(lista, tip):
    """
    Functia calculeaza suma cheltuielilor de un anumit tip
    input:lista de apartamente,tipul cheltuielii
    output: suma cheltuielilor
    """
    suma = 0
    for ap in lista:
        lists = apart_tipchelt(ap)
        for i in range(len(lists)):
            if lists[i] == tip:
                aux = apart_sumchelt(ap)
                suma = suma + aux[i]
    return suma


def validare_tip(data):
    """
    Functia valideaza tipul cheltuielilor (data)"""
    if data == "gaze" or data == "lumina" or data == "canal" or data == "apa" or data == "incalzire":
        return True
    else:
        return False

def validare_apart(data):
    """
    Functia valideaza numarul apartamentului """
    if data>=1 and data<=12:
        return True
    else:
        return False


def elim_chelt(lista, tip):
    """
    Functia elimina cheltuielile de un anumit tip din lista (elimin suma tipului respectiv)
    input: lista apartamente, tipul cheltuielii
    output:lista de dictionare noua conform cerintei
    """
    li=lista
    for ap in li:
        lists = apart_tipchelt(ap)
        for i in range(len(lists)):
            if lists[i] == tip:
                aux = apart_sumchelt(ap)
                apart_sumchelt(ap).remove(aux[i])  # sterg din lista de cheltuieli a apartamentului suma respectivului tip
    return li


def elim_chelt_sum(lista, suma):
    """
    Functia elimina cheltuielile care sunt mai mici decat suma data
    input:lista apartamente, suma
    output:lista de dictionare noua conform cerintei
    """
    li=lista
    for ap in li:
        lists = apart_sumchelt(ap)
        i=0
        while i < len(lists):
            if suma > lists[i]:
                #poz = lists.index(i)
                apart_sumchelt(ap).remove(lists[i])
                continue
            i = i + 1
    return li


def adaugare_tip(li, ap, tip):
    """
    Functia adauga un nou tip la lista actuala de tipuri
    input: lista de apartamente,apartamentul la care se adauga,tipul care se adauga
    output:lista noua de tipuri de cheltuieli ale apartamentului
    """
    lip = []
    lip = apart_tipchelt(li[ap])
    lip.append(tip)
    return lip  # lista noua de tipuri


def adaugare_chelt(li, ap, suma):
    """
     Functia adauga un o noua cheltuiala la lista actuala de cheltuieli
     input: lista de apartamente,apartamentul la care se adauga,suma care se adauga
     output:lista noua de cheltuieli ale apartamentului
     """
    lip = []
    lip = apart_sumchelt(li[ap])
    lip.append(suma)
    return lip  # lista noua de sume


def adaugare(li, ap, tip, suma):
    """
    Functia adauga la apartamentul specificat noile liste de tipuri si cheltuieli
    input:lista de apartamente,apartamentul,tipul cheltuielii,suma
    output: lista de apartamente modificata
    """
    li[ap - 1][1] = adaugare_tip(li, ap - 1, tip)  # i se atribuie cheii tip_chelt noua lista
    li[ap - 1][2] = adaugare_chelt(li, ap - 1, suma)  # i se atribuie cheii  suma  noua lista
    return li


def modificare(li, ap, tip, suma):
    """
    Functia modifica cheltuiala unui tip la apartamentul specificat
    input:lista de apartamente,apartamentul,tipul cheltuielii,suma
    output: suma cea veche si lista modificata
    """
    lip = []
    suma_veche=0
    lip = apart_tipchelt(li[ap - 1])
    for i in range(len(lip)):
        if lip[i] == tip:
            aux = apart_sumchelt(li[ap - 1])
            suma_veche=aux[i]
            aux[i] = suma
    return li,suma_veche

def stergere_chelt(li, ap):
    """
    Funtia sterge toate cheltuielile de la un apartament
    input:lista de apartamente,apartamentul
    output:lista de apartamnete,lista de tipuri care s-a sters si lista de sume
    """
    # adaugare cheie noua li[ap-1]['sum_chelt']=[]
    lista_tipuri=li[ap-1][1]
    lista_sume=li[ap-1][2]
    li[ap - 1][1]=[]
    li[ap-1][2]=[]
    return li,lista_tipuri,lista_sume


def stergere_chelt_cons(li, ap1, ap2):
    """
    Functia care sterge toate cheltuielile de la apartamente consecutive
    input:lista de apartamente si cele 2 apartamente
    output:lista cu apartamente si lista cu sumele care s-au sters
    """
    lista_sume=[]
    for i in range(ap1, ap2 + 1):
        lista_sume.append([i,li[i-1][1],li[i-1][2]])
        li[i-1][1]=[]
        li[i-1][2]=[]
    return li,lista_sume


def stergere_chelt_ambele(lista, tip):
    """
    Functia sterge cheltuielile de un anumit tip din lista (sterg suma tipului dar si tipul respectiv)
    input: lista apartamente, tipul cheltuielii
    output:lista de apartamentesi lista de sume
    """
    lista_sume=[]
    for ap in lista:
        lists = apart_tipchelt(ap)
        for i in lists:
            if tip == i:
                poz = lists.index(i)
                aux = apart_sumchelt(ap)
                apart=nr_apart(ap)
                lista_sume.append([apart[0],aux[poz]])
                apart_sumchelt(ap).remove(aux[poz])  # sterg din lista de cheltuieli a apartamentului suma respectivului tip
                apart_tipchelt(ap).remove(lists[poz])  # sterg din lista de tipuri respectivul tip
    return lista,lista_sume
def total_chelt_ap(lista,ap):
    """
    Functia calculeaza suma tuturor cheltuielilor apartamentului dat
    input:lista,apartamentul
    output:totalul de cheltuieli ale apartamentului
    """
    lists=apart_sumchelt(lista[ap-1])
    suma=0
    for i in range(len(lists)):
        suma=suma+lists[i]
    return suma
def apart_descr(lista,tip):
    """
    Functia returneaza lista cu apartamente care au avut acel tip,  in ordine descrescatoare conform sumelor cheltuite de acel tip
    input: lista de apartamente,tipul dat
    output:lista cu apartamentele in ordine descrescatoare dupa sumele cheltuite de acel tip
    """
    list_sume=[] #lista cu sumele cheltuite pe acel tip de la apartamente,care va urma sa fie ordonata
    list_dic={}#dictionar care are ca si cheie suma si ca valoare numarul apartamentului
    list_apart=[]#lista finala de apartamente ordonate descresc dupa sumele cheltuite
    li_apart_fara=[]#lista care va contine apartamentele cu cheltuiala 0 de acel tip
    for ap in lista:
            lists=apart_tipchelt(ap)
            val=False
            for i in lists:
                if i==tip:
                    val=True
                    poz=lists.index(i)
                    aux=apart_sumchelt(ap)
                    list_sume.append(aux[poz])#adaug suma cheltuita la lista
                    list_dic[aux[poz]]=nr_apart(ap)#adaug in dictionar valoarea sumei si apartamentul la care a fost cheltuita
            if val==False:
                 li_apart_fara.append(nr_apart(ap))# se adauga apartamentul in lista cu apartamentele cu cheltuieli 0 de acel tip

    list_sume.sort(reverse=True)#sortez descresc lista cu sumele cheltuite
    for i in list_sume:
            if(i!=0):
                list_apart.append(list_dic[i])# adaug in lista finala numarul apartamnetului corescpunzator sumei cheltuite
                ## astfel fiind in ordine descrescatoare
    list_apart.extend(li_apart_fara) #extind lista apartamentelor ordonate descrescator cu cea a apartamentelor cu cheltuiala 0
    return list_apart

def modif_list_undo(operatie,argumente,list_undo):
    
    """Salveaza in list_undo toate operatiile unui undo si argumentele
"""

    list_undo.append([operatie,argumente])

def reverse_add(li,ap,tip,suma):
    """
    Functia sterge din apartamentul ap suma si tipul cheltuielii
    """
    li[ap-1][1].remove(tip)
    li[ap-1][2].remove(suma)

def undo(li,list_undo):
    if len(list_undo)>0:
        operatie=list_undo.pop()
        if operatie[0]=='m':
            modificare(li,operatie[1][0],operatie[1][1],operatie[1][2])
        elif operatie[0]=='st1':
            for i in range(len(operatie[1][1])):
                adaugare(li,operatie[1][0],operatie[1][1][i],operatie[1][2][i]) #ia fiecare utilitate si o adauga
        elif operatie[0]=='st3':
            for chelt_suma in operatie[1][0]:# parcurg lista cu sumele cheltuite si apartamentele
                adaugare(li,chelt_suma[0],operatie[1][1],chelt_suma[1])#adaug inapoi fiecare pereche
        elif operatie[0]=='st2':
            for apartament in operatie[1]:#parcurg apartamentele cheltuielile sterse
                for i in range(len(apartament[1])):
                    adaugare(li,apartament[0],apartament[1][i],apartament[2][i])
        elif operatie[0]=='ad':
            reverse_add(li,operatie[1][0],operatie[1][1],operatie[1][2])
        return li
    else:
        print("Este lista initiala")

def print_(li):
    for ap in li:
        print(nr_apart(ap)," ",apart_tipchelt(ap)," ",apart_sumchelt(ap))
    """
    class undo1:
    def __init__(self):
        self.list_undo=[]
    def modif(self,lista):
        self.list_undo.append(list(lista.copy()))
    def undo_class(self):
        if len(self.list_undo) > 1:
            self.list_undo.pop()
            return self.list_undo[-1]
        else:
            print("Este lista initiala")
    def print(self):
        for el in self.list_undo:
            print(el)
    """

