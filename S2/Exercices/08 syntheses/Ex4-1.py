listes = [[], [1], ['spam', 100], ['spam', 100, 'bacon'],
          [1, 2, 3, 100], [1, 2, 100, 4, 5],
          ['si', 'pair', 'alors', 'dernier'],
          ['retourne', 'le', 'milieu', 'si', 'impair']]
listes_2 = ['', 'a', 'ab', 'abc', 'abcd', 'abcde']
var = ''


def laccess(liste):
    if not liste:
        return
    if len(liste) % 2 == 0:
        return liste[-1]
    else:
        return liste[len(liste)//2]


def test(laliste):
    for liste in laliste:
        longueur = 50 - len(str(liste))
        print(f"laccess({liste}) {var:<{longueur}} donne : {laccess(liste)}")


test(listes)
test(listes_2)
