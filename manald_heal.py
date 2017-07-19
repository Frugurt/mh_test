# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 14:45:08 2017

@author: Sergey
"""
import numpy as np


APS = 4.51

electrocute = 2.0
spectral_blade = 1.0
arcane_torrent = 3.0

EC_FPA = np.floor(60 / (APS * electrocute))
SB_FPA = np.floor(60 / (APS * spectral_blade))
SB_1item_FPA = np.floor(60 / (APS * spectral_blade *1.5))
SB_2items_FPA = np.floor(60 / (APS * spectral_blade * 2.25))
AT_FPA = np.floor(60 / (APS * arcane_torrent))

paralysis = {}
paralysis[1] = 0.15
paralysis[2] = 0.07804555427071125
paralysis[3] = 0.05086232538105606
seconds = 10000


def attack_coeff(FPA, speed_coeff):
    chance = paralysis[speed_coeff]
    window_end = 0
    procs = 0
    for t in range(0, seconds * 60, int(FPA)):
        RNG = np.random.rand()
        if RNG <= chance:
            window_end = t + 67
        if t < window_end:
            procs += 1
    return procs
    
def attack_sb(FPA):
    chance = paralysis[1]
    procs = 0
    for t in range(0, seconds * 60, int(FPA)):
        RNG1 = np.random.rand()
        RNG2 = np.random.rand()
        RNG3 = np.random.rand()
        if RNG1 <= chance:
            procs += 1
        if RNG2 <= chance:
            procs += 1
        if RNG3 <= chance:
            procs += 1
    return procs

print("APS: ", APS)

print("spectral blades no items:             {}".format(attack_sb(FPA = SB_FPA)))
print("electrocute:                          {}".format(attack_coeff(FPA = EC_FPA, speed_coeff=electrocute)))
print("arcane torrent (extra bolts ignored): {}".format(attack_coeff(FPA = AT_FPA, speed_coeff=arcane_torrent)))
print("spectral blades 1 item:               {}".format(attack_sb(FPA = SB_1item_FPA)))
print("spectral blades both items:           {}".format(attack_sb(FPA = SB_2items_FPA)))
            