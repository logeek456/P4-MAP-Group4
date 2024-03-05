from tkinter import *
APL = Tk()
APL.geometry('1000x1000')

APL.title('Fenêtre test') #nom de ma fenêtre test
T1 = Label(APL, text='Bonjour le groupe 4', bg = 'red', fg='white', font=('tajawal', 17, 'bold')).pack(fill=X) #texte de mon label
T2 = Label(APL, text='Veuillez entrer votre nom',font=('tajawal', 17))#texte de mon label
T2.pack() 
T2.place(x=375, y=100)
E1 = Entry(APL, justify= 'center', bg = 'powder blue') # Pour écrire 
E1.pack()  #pour afficher
E1.place(x=420, y=150) #pour afficher

T3 = Label(APL, text='Veuillez entrer votre prénom',font=('tajawal', 17))#texte de mon label
T3.pack() 
T3.place(x=375, y=250) 

E2 = Entry(APL, justify= 'center')#pour écrire aussi 
E2.pack #pour afficher aussi
E2.place(x=420, y=300) #encore

#Bouton enter  
Bt1 = Button(APL, text='Ca clique à balle', width= 25, bg = 'cyan') #pour le bouton
Bt1.pack() #pour afficher
Bt1.place(x=400, y=400) #encore

APL.mainloop()