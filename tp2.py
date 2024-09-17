#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:27:00 2024

@author: antoine.epifanic
"""

#------------------------- Exercice 2 -------------------------------

def mesImpots(revenu):
    créance=0
    if revenu<=10225:
        créance=0
    elif revenu<=26070:
        créance=(revenu-10225)*0.11
    elif revenu<=74545:
        créance=(revenu-26071)*0.3+(26070-10226)
    elif revenu<=160336:
        créance=(revenu-74576)*0.41+(74545-26071)*0.3+(26070-10226)*0.11
    else:
        créance=revenu-160336+(160336-74576)*0.41+(74545-26071)*0.3+(26070-10226)*0.11
    return créance

#Programme principal

RevenuUtilisateur=int(input("Tapez votre revenu net imposable :"))
print(f"Vous allez khalass {mesImpots(RevenuUtilisateur)}€ à l'état")