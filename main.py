from Functii_principale import *
from Functii_get import *
from Functii_principale import *
from Functii_afisare import *

def meniu():
    print("1.1 Se adauga cheltuiala pentru un apartament.")
    print("1.2 Se modifica cheltuiala pentru un apartament .")
    print("'stergere'(2.1).Sterge toata cheltuiala pentru un -apartament- .")
    print("2.2 Sterge cheltuiala de la apartamente consecutive.")
    print("2.3 Sterge toata cheltuiala de la un anumit tip de la toate apartamentele .")
    print("'tipariresuma'(3.1) Se tiparesc toate apartamentele care au cheltuieli mai mari decât o -sumă data-.")
    print("'tipariretip'(3.2) Se tiparesc toate cheltuielile de un anumit -tip- de la toate apartamentele.")
    print("4.1 Se tipareste suma totală pentru un tip de cheltuială.")
    print("4.2 Se tiparesc toate apartamentele sortate descrescator dupa un tip de cheltuiala")
    print("'tiparireapart'(4.3)Se tipareste totalul de cheltuieli pentru un -apartament- dat.")
    print("5.1 Se elimină toate cheltuielile de un anumit tip")
    print("5.2 Elimina toate cheltuielile mai mici decat o suma data .")
    print("6.Reface ultima operatie(undo)")
    print("iesire.Iesire din aplicatie.")

def run():
    list_undo=[]
    list_bloc = generare_bloc()
    parcurs = False
    while not parcurs:
        meniu()
        cmds= input("Introduceti numarul cerintelor si argumentele necesare: ").split(';')
        for cmd in cmds:
            arg_details=cmd.split(' ')
            if len(arg_details)==1:
                if arg_details[0]=="tipariresuma" or arg_details[0]=='tiparireapart' or arg_details[0]=='tipariretip' or arg_details[0]=='stergere':
                    print("argumente invalide")
                    continue
            cmd=arg_details[0]
            if cmd == 'tipariresuma':
                try:
                    arg=int(arg_details[1])
                    afis_apart_chelt_fixdat(list_bloc,arg)
                except ValueError:
                    print("argumente invalide")
            elif cmd == 'tiparireapart':
                try:
                    arg = int(arg_details[1])
                    if validare_apart(arg) == True:
                        afis_total_chelt_ap(list_bloc,arg)
                except ValueError:
                    print("argumente invalide")
            elif cmd == 'tipariretip':
                try:
                    arg=arg_details[1]
                    if validare_tip(arg)==True:
                        afis_total_chelt(list_bloc,arg)
                    else:
                        print("argument invalid")
                except ValueError:
                    print("argumente invalide")
            elif cmd=='stergere':
                try:
                    arg = int(arg_details[1])
                    if validare_apart(arg)==True:
                        afis_stergere_chelt(list_bloc,list_undo,arg)
                    else:
                        print("argument invalid")
                except ValueError:
                    print("argumente invalide")
            elif cmd == '4.1':
                afis_sum_chelt(list_bloc)
            elif cmd == '5.1':
                afis_elim_chelt(list_bloc)
            elif cmd=='5.2':
                afis_elim_chelt_sum(list_bloc)
            elif cmd=='1.1':
                afis_adaugare(list_bloc,list_undo)
            elif cmd=='1.2':
                afis_modificare(list_bloc,list_undo)
            elif cmd=='2.2':
                afis_stergere_chelt_cons(list_bloc,list_undo)
            elif cmd=='2.3':
                afis_stergere_chelt_ambele(list_bloc,list_undo)
            elif cmd=='4.2':
                afis_apart_descr(list_bloc)
            elif cmd=='6':
                if len(list_undo)>0:
                    list_bloc=undo(list_bloc,list_undo)
                    print_(list_bloc)
                else:
                        print("Este versiunea initiala a listei de apartamente")
            elif cmd == 'iesire':
                parcurs = True
            else:
                print("comanda invalida")


run()


# TESTE
def test_apart_chelt_fixdat():
    test_list = generare_bloc()

    mai_mare_decat_1000 = apart_chelt_fixdat(test_list, 1000)
    assert (mai_mare_decat_1000 == [[2], [4], [8], [11]])

    mai_mare_decat_500 = apart_chelt_fixdat(test_list, 500)
    assert (mai_mare_decat_500 == [[2], [3], [4], [5], [7], [8], [10], [11], [12]])

    mai_mare_decat_800 = apart_chelt_fixdat(test_list, 800)
    assert (mai_mare_decat_800 == [[2],[ 4], [7], [8], [11]])


def test_total_chelt():
    test_list = generare_bloc()

    cheltuieli_gaze = total_chelt(test_list, "gaze")
    assert (cheltuieli_gaze == [170, 560, 420, 300, 800, 410])

    cheltuieli_lumina = total_chelt(test_list, "lumina")
    assert (cheltuieli_lumina == [240, 200, 200, 380, 250, 600])

    cheltuieli_apa = total_chelt(test_list, "apa")
    assert (cheltuieli_apa == [280, 300, 300, 270, 130, 330, 440])


def test_sum_chelt():
    test_list = generare_bloc()

    suma_chelt_lumina = sum_chelt(test_list, "lumina")
    assert (suma_chelt_lumina == 1870)

    suma_chelt_apa = sum_chelt(test_list, "apa")
    assert (suma_chelt_apa == 2050)

    suma_chelt_canal = sum_chelt(test_list, "canal")
    assert (suma_chelt_canal == 910)


def test_validare():
    assert (validare_tip("gaze") == True)
    assert (validare_tip("job") == False)
    assert (validare_tip("lumina") == True)

def test_apart():
    lista=generare_bloc()
    assert (nr_apart(lista[0])==[1])
    assert(nr_apart(lista[6])==[7])
def test_aptip():
    lista = generare_bloc()
    assert(apart_tipchelt(lista[1])==['apa','lumina','gaze'])
    assert(apart_tipchelt(lista[2])==['canal','incalzire'])
def test_chelt():
    lista = generare_bloc()
    assert(apart_sumchelt(lista[4])==[300,270])
    assert(apart_sumchelt(lista[11])==[320,440])

def test_elim_chelt():
    lista=[[[1], ['gaze','apa'],  [170,280]],
        [[2], ['apa','lumina','gaze'], [300,240,560]]]
    lista_modif=[[[1], ['gaze','apa'],  [280]],
                 [[2], ['apa','lumina','gaze'], [300,240]]]
    list=elim_chelt(lista,'gaze')
    assert list[1]==lista_modif[1]

def test_elim_chelt_suma():
    lista=[[[1], ['gaze','apa'],  [170,280]],
        [[2], ['apa','lumina','gaze'], [300,240,560]]]
    lista_modif=[[[1], ['gaze','apa'],  [280]],
                 [[2], ['apa','lumina','gaze'], [300]]]
    list=elim_chelt(lista,250)
    assert list==lista_modif

def test_adaugare_tip():
    lista = [[[1], ['gaze','apa'],  [170,280]],
        [[2], ['apa','lumina','gaze'], [300,240,560]]]
    li=adaugare_tip(lista,0,'canal')
    assert li==['gaze','apa','canal']
def test_adaugare_chelt():
    lista = [[[1], ['gaze','apa'],  [170,280]],
        [[2], ['apa','lumina','gaze'], [300,240,560]]]
    li = adaugare_chelt(lista,0, 300)
    assert li == [170,280,300]
def test_adaugare():
    lista = [[[1], ['gaze','apa'],  [170,280]],
        [[2], ['apa','lumina','gaze'], [300,240,560]]]
    li = adaugare(lista,1, 'canal',250)
    assert li == [[[1], ['gaze','apa','canal'],  [170,280,250]],
        [[2], ['apa','lumina','gaze'], [300,240,560]]]
def test_modificare():
    lista = [[[1], ['gaze','apa'],  [170,280]],
        [[2], ['apa','lumina','gaze'], [300,240,560]]]
    li,suma = modificare(lista, 1, 'apa', 500)
    assert li,suma ==([[[1],['gaze', 'apa'],[170, 500]],
               [[2],['apa', 'lumina', 'gaze'], [300, 240, 560]]],280)

def test_stergere_chelt():
    lista = [[[1], ['gaze','apa'],  [170,280]],
        [[2], ['apa','lumina','gaze'], [300,240,560]]]
    li,lista_tip,lista_Sume = stergere_chelt(lista, 1)
    assert (li,lista_tip,lista_Sume)==([[[1], [], []],
        [[2], ['apa','lumina','gaze'], [300,240,560]]],['gaze','apa'],[170,280])
def test_stergere_chelt_cons():
    lista = [[[1], ['gaze','apa'],  [170,280]],
        [[2], ['apa','lumina','gaze'], [300,240,560]]]
    li ,lista_Sume= stergere_chelt_cons(lista,1,2)
    assert (li,lista_Sume)==([[[1], [],  []],
        [[2], [], []]],[[1,['gaze','apa'], [170,280]],[2, ['apa','lumina','gaze'], [300,240,560]]])
def test_stergere_chelt_ambele():
    lista = [{'Apartament': 1, 'tip_chelt': [ 'gaze','apa'], 'suma': [170, 280]},
             {'Apartament': 2, 'tip_chelt': ['apa', 'lumina', 'gaze'], 'suma': [300, 240, 560]}]
    li,lista_sume=stergere_chelt_ambele(lista,'gaze')
    assert (li,lista_sume)==([[[1],  ['apa'], [280]],
                [[2],  ['apa', 'lumina'],  [300,240]]],[[1,170],[2,560]])
def test_apart_descr():
    lista=[[[1],  ['gaze', 'apa'],  [170, 280]],
            [[ 2],  ['apa', 'lumina', 'gaze'],  [300, 240, 560]],
            [[ 3],  ['canal', 'incalzire'], [100, 420]],
            [[ 4],  ['lumina', 'apa', 'gaze', 'canal'],  [200, 300, 420, 180]]]
    li=apart_descr(lista,'gaze')
    assert li==[[2],[4],[1],[3]]
def test_total_chelt_ap():
    lista = [[[1],  ['gaze', 'apa'],  [170, 280]],
            [[ 2],  ['apa', 'lumina', 'gaze'],  [300, 240, 560]],
            [[ 3],  ['canal', 'incalzire'], [100, 420]],
            [[ 4],  ['lumina', 'apa', 'gaze', 'canal'],  [200, 300, 420, 180]]]
    suma=total_chelt_ap(lista,1)
    assert suma==450

def test_undo():
    li=[[[ 1],  ['gaze', 'apa'],  [170, 280]],
            [[2],  ['apa', 'lumina', 'gaze'], [300, 240, 560]],
            [[3],  ['canal', 'incalzire'], [100, 420]],
            [[4],  ['lumina', 'apa', 'gaze', 'canal'],  [200, 300, 420, 180]],
            [[5],  ['gaze', 'apa'],  [300, 270]]]
    list_undo=[]
    li, suma_veche = modificare(li, 1, 'apa', 500)
    modif_list_undo('m', [1, 'apa', suma_veche], list_undo)
    modif_list_undo('ad', [3,'apa',500], list_undo)
    li = adaugare(li, 3,'apa', 500)
    li==undo(li,list_undo)
    assert li==[[[ 1],  ['gaze', 'apa'],  [170, 500]],
            [[2],  ['apa', 'lumina', 'gaze'], [300, 240, 560]],
            [[3],  ['canal', 'incalzire'], [100, 420]],
            [[4],  ['lumina', 'apa', 'gaze', 'canal'],  [200, 300, 420, 180]],
            [[5],  ['gaze', 'apa'],  [300, 270]]]
def test_undo1():
    li=[[[8],  ['lumina', 'apa', 'gaze'],  [250, 130, 800]],
            [ [9],  ['gaze'], [410]],
            [ [10],  ['apa', 'canal'],  [330, 220]],
            [[11],  ['incalzire', 'lumina'],  [525, 600]],
            [[12],  ['canal', 'apa'],  [320, 440]]]
    list_undo=[]
    li, lista_sume, lista_tipuri = stergere_chelt(li, 8)
    modif_list_undo('st1', [8, lista_sume, lista_tipuri], list_undo)
    li, lista_sum = stergere_chelt_cons(li, 10, 12)
    modif_list_undo('st2', lista_sum, list_undo)
    assert li==[[[8],  [],  []],
            [ [9],  ['gaze'], [410]],
            [ [10],  ['apa', 'canal'],  [330, 220]],
            [[11],  ['incalzire', 'lumina'],  [525, 600]],
            [[12],  ['canal', 'apa'],  [320, 440]]]
def test_validareapart():
    assert validare_apart(15)==False
    assert validare_apart(8)==True
    assert validare_apart(10)==True

def test_reverseadd():
    li = [[[8], ['lumina', 'apa', 'gaze'], [250, 130, 800]],
          [[9], ['gaze'], [410]],
          [[10], ['apa', 'canal'], [330, 220]],
          [[11], ['incalzire', 'lumina'], [525, 600]],
          [[12], ['canal', 'apa'], [320, 440]]]
    reverse_add(li,8,'gaze',800)
    assert li==[[[8],  ['lumina', 'apa'],  [250, 130]],
            [ [9],  ['gaze'], [410]],
            [ [10],  ['apa', 'canal'],  [330, 220]],
            [[11],  ['incalzire', 'lumina'],  [525, 600]],
            [[12],  ['canal', 'apa'],  [320, 440]]]



test_apart_chelt_fixdat()
test_total_chelt()
test_sum_chelt()
test_validare()
test_validareapart()
test_apart()
test_aptip()
test_chelt()
test_elim_chelt()
test_adaugare_chelt()
test_adaugare_tip()
test_adaugare()
test_modificare()
test_stergere_chelt()
test_stergere_chelt_cons()
test_apart_descr()
test_total_chelt_ap()
test_undo()
test_undo()
