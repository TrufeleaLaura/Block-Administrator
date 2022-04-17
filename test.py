def generare_bloc():
    return [{'Apartament': 1, 'tip_chelt': ['gaze', 'apa'], 'suma': [170, 280]},
            {'Apartament': 2, 'tip_chelt': ['apa', 'lumina', 'gaze'], 'suma': [300, 240, 560]},
            {'Apartament': 3, 'tip_chelt': ['canal', 'incalzire'], 'suma': [100, 420]},
            {'Apartament': 4, 'tip_chelt': ['lumina', 'apa', 'gaze', 'canal'], 'suma': [200, 300, 420, 180]},
            ]


def nr_apart(apart):
    """
    Functia returneaza numarul apartamentului
    """
    return apart['Apartament']


def apart_tipchelt(apart):
    """
    Functia returneaza lista cu tipurile cheltuielilor de la acel apartament
    """
    return apart['tip_chelt']


def apart_sumchelt(apart):
    """
    Functia returneaza lista cu sumele cheltuite de la acel apartament
    """
    return apart['suma']




def validare_tip(data):
        """
        Functia valideaza tipul cheltuielilor (data)"""
        if data == "gaze" or data == "lumina" or data == "canal" or data == "apa" or data == "incalzire":
                return True
        else:
                return False


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
            ok=0
            for i in lists:
                if i==tip:
                    ok=1
                    poz=lists.index(i)
                    aux=apart_sumchelt(ap)
                    list_sume.append(aux[poz])#adaug suma cheltuita la lista
                    list_dic[aux[poz]]=nr_apart(ap)#adaug in dictionar valoarea sumei si apartamentul la care a fost cheltuita
            if ok==0:
                 li_apart_fara.append(nr_apart(ap))# se adauga apartamentul in lista cu apartamentele cu cheltuieli 0 de acel tip

    list_sume.sort(reverse=True)#sortez descresc lista cu sumele cheltuite
    for i in list_sume:
            if(i!=0):
                list_apart.append(list_dic[i])# adaug in lista finala numarul apartamnetului corescpunzator sumei cheltuite
                ## astfel fiind in ordine descrescatoare
    list_apart.extend(li_apart_fara) #extind lista apartamentelor ordonate descrescator cu cea a apartamentelor cu cheltuiala 0
    return list_apart



def crt_undo_list(crt_undo,lst):
    """
    Face o copie la o lista de dictionare
    :param lst: lista care se copiaza
    :type lst: list (of dicts)
    :return: copie a listei date
    :rtype: list (of dicts)
    """
    cpy = []
    for el in lst:
        crt_elem_dict = {}
        for key, value in el.items():
            crt_elem_dict[key] = value
        cpy.append(crt_elem_dict)

    return cpy
def undo_op(crt_undo):
    crt_undo.pop(-1)
    return crt_undo

def undo_ui(crt_undo):
    try:
        if crt_undo==[]:
            print("Nu se mai pot face operatii de undo")
            print()
            return []
        else:
            undo_op(crt_undo)
            if crt_undo==[]:
                print("Lista este goala")
                print()
                return []
            else return crt_undo[-1]
    except ValueError:
        print("iesoire")




# PARTEA DE INTERFATA CU UTILIZATORUL

def meniu():
        print("1.1 Se adauga cheltuiala pentru un apartament.")
        print("1.2 Se modifica cheltuiala pentru un apartament .")
        print("2.1.Sterge toata cheltuiala pentru un apartament .")
        print("2.2 Sterge cheltuiala de la apartamente consecutive.")
        print("2.3 Sterge toata cheltuiala de la un anumit tip de la toate apartamentele .")
        print("5.2 Elimina toate cheltuielile mai mici decat o suma data .")
        print("iesire.Iesire din aplicatie.")

def stergere_chelt_ambele(lista, tip):
    """
    Functia sterge cheltuielile de un anumit tip din lista (sterg suma tipului dar si tipul respectiv)
    input: lista apartamente, tipul cheltuielii
    output:lista de dictionare noua conform cerintei
    """
    for ap in lista:
        lists = apart_tipchelt(ap)
        for i in lists:
            if tip == i:
                poz = lists.index(i)
                aux = apart_sumchelt(ap)
                apart_sumchelt(ap).remove(aux[poz])  # sterg din lista de cheltuieli a apartamentului suma respectivului tip
                apart_tipchelt(ap).remove(lists[poz])  # sterg din lista de tipuri respectivul tip
    return lista
def stergere_chelt_cons(li, ap1, ap2):
    """
    Functia care sterge toate cheltuielile de la apartamente consecutive
    input:lista de apartamente si cele 2 apartamente
    output:lista cu apartamente
    """
    for i in range(ap1, ap2 + 1):
        li[i - 1]['suma'].clear()
    return li

def afis_stergere_chelt_ambele(li):
    """
    Functia afiseaza lista de apartamente din care s-a sters de la toate atat tipul dat, cat si suma tipului
    """
    try:
        tip_chel = input("Introduceti tipul cheltuielii: ")
        if validare_tip(tip_chel) == False:
            print("data invalida")
            return
        print('S-a efectuat stergerea cheltuialelilor apartamentelor de acel tip : ',
              stergere_chelt_ambele(li, tip_chel))
    except ValueError:
        print("data invalida")

def afis_stergere_chelt_cons(li):
    """
    Functia afiseaza lista modificata, din care s au sters cheltuielile de la apartamentele date,dar si de la cele care se afla intre ele
    """
    try:
        ap1 = int(input("Introduceti numarul apartamentului 1: "))
        ap2 = int(input("Introduceti numarul apartamentului 2: "))
        if ap1 < ap2:
            print('S-a efectuat stergerea cheltuielilor de la apartamentele consecutive ',
                  stergere_chelt_cons(li, ap1, ap2))
        else:
            print('S-a efectuat stergerea cheltuielilor de la apartamentele consecutive ',
                  stergere_chelt_cons(li, ap2, ap1))
    except ValueError:
        print('data invalida')


def run():
    def run():
        list_bloc = generare_bloc()
        crt_undo=[]
        parcurs = False
        while not parcurs:
            meniu()
            cmd = input("Introduceti numarul cerintei: ")
            if cmd == '1.1':
                afis_stergere_chelt_cons(list_bloc)
                crt_undo_list(crt_undo,list_bloc)
            elif cmd=='1.2':
                afis_stergere_chelt_ambele(list_bloc)
                crt_undo_list(crt_undo,list_bloc)
            elif cmd=='1.3':
                undo_ui(crt_undo)

run()



