#!/usr/ bin/env python3

# App for ITEC-617
# Supports the Digital Transformation (DT) Project Presentations phase
# This app reads the student team roster from an Excel file and generates a random sequence for the team presentations to the judges

import pandas as pd 
import os
import random
import streamlit as st
import time
from collections import Counter
import itertools
import math

print("Welcome to ITEC-617 Digital Transformation Project Presentations")

df = pd.read_excel('ITEC-617 Spring 2020 Names and Teams for DT Project.xlsx')
columnNames = df.columns 
#print(columnNames)

print("Introducing our teams:")
teamsList = list(set(df['DT TEAM']))
for aTeam in teamsList:
    print("...", aTeam)
print()
numberOfTeams = len(teamsList)
print(f"There are {numberOfTeams} teams.")
print(f"There are n! {math.factorial(numberOfTeams)} sequence possible combinations.")

## Another way to generate a list of all combinations
# possiblePermutations = []
# for aTeamSequence in itertools.permutations(teamsList, 6):
#     possiblePermutations.append(aTeamSequence)
# print('Possible sequences:', len(possiblePermutations))

# print()
time.sleep(2)
print()
print("Introducing our team members...")
print()
for n, aTeam in enumerate(teamsList):
    print(n + 1, aTeam)
    print("   ", list(df[df['DT TEAM'] == aTeam].sort_values(['NAME'])['NAME']))
    print()

print()

# unnecessary for randomness but adds some drama!
print("Drum roll please....")
time.sleep(0.5)
print("Spin the wheel...")
time.sleep(2)
print()
container = [] # keep track of the various sequences that appeared
spinLoops = random.randint(100,250)
for loop, i in enumerate(range(spinLoops)):
    randomSequence = random.sample(teamsList, len(teamsList))
    #print(randomSequence)
    if loop%15 != 0:
        print(".", end = "")
    else:
        print()
        time.sleep(1)
    container.append(randomSequence.copy())
print(spinLoops, ' spins')
print()

# final_count = Counter(map(tuple, container)) # count which sequences appeared the most
# print("Most common sequences that appeared:")
# for aSequence in final_count.most_common(5):
#     print(aSequence)
# print()

print('....the final sequence is:')
print()
for n, aTeam in enumerate(randomSequence):
    print(n + 1, aTeam)
    print("   ", list(df[df['DT TEAM'] == aTeam].sort_values(['NAME'])['NAME']))
    print()

print()
print('Let the presentation begin with team:')
print()
print("...",randomSequence[0])
print()
print()
