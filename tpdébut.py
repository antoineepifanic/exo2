# -*- coding: utf-8 -*-
def TestBissextile(N): #Teste si ma fonction est bissextile
    if N%4==0 and N%1==0:
        return True
    elif N%400==0:
        return True
    else:
        return False
   
    
L31=["Janvier", "Mars", "Mai", "Juillet", "Août", "Octobre", "Décembre"]
L30=["Avril", "Juin", "Septembre", "Novembre"]

def NmbJoursMois(M, L): #M est une chaîne de caractères, L année entière  
    if M in L31:
        J=31
    elif M in L30:
        J=30
    elif TestBissextile(L):
        J=29
    else:
        J=28
    return(J)
        

MOIS=["Janvier", "Mars", "Mai", "Juillet", "Août", "Octobre", "Décembre", "Février", "Avril", "Juin", "Septembre", "Novembre"]

def VérifDate(A, B, C): # A : jour, B : mois, C: année
    if A>31:
        return False
    elif B not in MOIS:
        return False
    if A>NmbJoursMois(B, C):
        return False
    else:
        return True

#--------------------Programme Principal ----------------------

JourUtilisateur = int(input("Tapez le jour : "))
MoisUtilisateur = input("Tapez le mois (en lettres) : ")
AnnéeUtilisateur = input("Tapez l'année : ")
if VérifDate(JourUtilisateur, MoisUtilisateur, AnnéeUtilisateur):
    print(f"Le {JourUtilisateur} {MoisUtilisateur} {AnnéeUtilisateur} est une date valide ")
else:
    print(f"Réflechis un peu...Tu penses vraiment que : {JourUtilisateur} {MoisUtilisateur} {AnnéeUtilisateur} est une date valide ?")