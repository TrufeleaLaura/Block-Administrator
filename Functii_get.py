def generare_bloc():
    return [[[ 1],  ['gaze', 'apa'],  [170, 280]],
            [[2],  ['apa', 'lumina', 'gaze'], [300, 240, 560]],
            [[3],  ['canal', 'incalzire'], [100, 420]],
            [[4],  ['lumina', 'apa', 'gaze', 'canal'],  [200, 300, 420, 180]],
            [[5],  ['gaze', 'apa'],  [300, 270]],
            [[6], ['lumina', 'canal'], [200, 90]],
            [[7],  ['incalzire', 'lumina'],  [530, 380]],
            [[8],  ['lumina', 'apa', 'gaze'],  [250, 130, 800]],
            [ [9],  ['gaze'], [410]],
            [ [10],  ['apa', 'canal'],  [330, 220]],
            [[11],  ['incalzire', 'lumina'],  [525, 600]],
            [[12],  ['canal', 'apa'],  [320, 440]]]


def nr_apart(apart):
    """
    Functia returneaza numarul apartamentului
    """
    return apart[0]


def apart_tipchelt(apart):
    """
    Functia returneaza lista cu tipurile cheltuielilor de la acel apartament
    """
    return apart[1]


def apart_sumchelt(apart):
    """
    Functia returneaza lista cu sumele cheltuite de la acel apartament
    """
    return apart[2]