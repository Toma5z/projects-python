from tkinter import * 

#-------- Zmienne ----------- 
global OknaMAX, OknaLiczba, okno, Zgoda

OknaMAX = 5                                                             # Maksymalna liczba okien
OknaLiczba = 0                                                          # Liczba otwarych okien
okno = [OknaMAX]                                                        # Tablica zawierająca uchwyty do otwartych okien
Zgoda = False
#-------- Funkcje ------------


def Sprawdz():                                                          # Wyswietla tablice z otwartymi oknami
	global okno
	print('\nTablica okno[] = \n')
	for x in range(len(okno)-1):
		print(str(x+1) + '  ' + str(okno[x+1]))



def ProbaZamknieca(event):
	global Zgoda
	print('\n\nZamknieto okno: '+str(event.widget)) 
	if (Zgoda==False):                                                  # wykonaj jezeli brak zgody na zamkniecie okna   
		print('Brak zgody. Ponowne otwarcie okna!!!')
		k=okno.index(event.widget)                                      # wyszukaj zamkniete okno i podaj jego pozycje w zmiennej k
		print("Znaleziono  " + str(okno[k])+ " w pozycji k = " + str(k))
		okno.remove(okno[k])                                            # usun z tablicy zamkniete okno
		okno.insert(k,Toplevel())                                       # utworz nowe okno z miejsce zamknietego
		print('Przypisano ' + str(okno[k]) + ' pod numerem k = ' + str(k))
		a=30*k + 80                                                     # dodaje przesunięcie okna na podsawie jego numeru porządkowego k                                                       # dodaje przesunięcie okna na podsawie jego numeru porządkowego OknaLiczba
		okno[k].geometry('320x240+'+str(a)+'+'+str(a))
		okno[k].bind('<Destroy>', ProbaZamknieca)                       # dodaje obsługę zdarzenia zamkniecia okna
		
	Zgoda = False
	
	
def Start():                                                            # Funkcja otwiera okna aż do osiągnięcia OknaMAX
	global OknaMax, OknaLiczba, okno	
	if OknaLiczba<OknaMAX:
		OknaLiczba = OknaLiczba + 1
		okno.insert(OknaLiczba,Toplevel())                              # dodaje uchwyt okna do tablicy okno[]
		print("\nStart okno: " + str(OknaLiczba) + "  " + str(okno[OknaLiczba]))
		a=30*OknaLiczba + 80                                            # dodaje przesunięcie okna na podsawie jego numeru porządkowego OknaLiczba
		okno[OknaLiczba].geometry('320x240+'+str(a)+'+'+str(a))
		okno[OknaLiczba].bind('<Destroy>', ProbaZamknieca)
	else:
		print("\nOsiagnieto maksymalna ilosc okien: " + str(OknaMAX))   
	

def Zamknij2():                                                         # Funkcja zamyka pokolei okna aż OknaLiczba = 0
	global OknaLiczba, okno, Zgoda
	Zgoda = True                                                        # Ustawia zgode na zamkniecie okna
	if OknaLiczba>0:
		print("\n\nZamknij: Nr okna: " + str(OknaLiczba))
		okno[OknaLiczba].destroy()
		okno.pop()                                                      # .pop() usuwa ostatni element z tablicy okno[]
		OknaLiczba = OknaLiczba - 1
	else:
		print("\nBrak okien")
		Zgoda = False	



	
#------- Program ------------	
	
okno1 = Tk()                                                            # Tworzymy okno glowne
okno1.geometry('100x100+700+700')

Przycisk1 = Button(okno1, text = 'Dodaj', command = Start)              # Dodaje okno
Przycisk1.pack()
Przycisk2 = Button(okno1, text = 'Zamknij', command = Zamknij2)         # Zamyka ostatnie okno
Przycisk2.pack()
Przycisk3 = Button(okno1, text = 'Sprawdz', command = Sprawdz)          # Wyswietla tablice z otwartymi oknami
Przycisk3.pack()




okno1.mainloop()                                                        # Uruchamiamy petle obslugi zdarzen na oknie glownym
