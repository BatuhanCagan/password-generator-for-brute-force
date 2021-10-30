import itertools
from itertools import product, repeat

def h():
     while 1:
          c = input("Programın hangi aşamasındasınız?\n(1), (2) ya da çıkmak için (3)\n")
          if c == '1':
               x = input("Lütfen kelimeleri boşluk kullanmadan giriniz:")
               f = open("şifreler.txt", "x")
               w = open("şifreler.txt", "w")
               q = "12345"
               combs = [''.join(comb) for comb in product(x, repeat=len(q))] #repeat=len(x)
               combs
               for sayı in combs:
                    print(sayı)
                    w.write(sayı)
                    w.write("\n")
          if c == '2':
               x = input("Lütfen rakamları boşluk kullanmadan giriniz:")
               f = open("şifreler2.txt", "x")
               w = open("şifreler2.txt", "w")
               def foo(l):
                    yield from itertools.product(*([l] * 4))
               for sayı in foo(x):
                    print(''.join(sayı))
                    w.write(''.join(sayı))
                    w.write("\n")
          
          if c == '3':
               exit()

h()