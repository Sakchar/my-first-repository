"""
Name: C. Sakiman

Date: 11/17/2023

Porgram description: Optimalisatie van een Wiskundige Functie
"""

def deeltje_trajectorie(t, zwaartekracht, beginsnelheid):
    positie = -0.5 * zwaartekracht * t**2 + beginsnelheid * t
    return positie

