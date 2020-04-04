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

st.title("ITEC-617")
st.title("Digital Transformation Project")
st.header("")
st.header("Welcome Teams and Judges")
#print("Welcome to ITEC-617 Digital Transformation Project Presentations")

@st.cache
def get_teams(fileName = 'ITEC-617 Spring 2020 Names and Teams for DT Project.xlsx'):
    df = pd.read_excel(fileName)
    return df

uploaded_file = st.sidebar.file_uploader("Choose an Excel or CSV file", type=["xlsx", "csv"])
if uploaded_file is not None:
    df = get_teams(uploaded_file)
else:
    df = get_teams()

if uploaded_file is None:
    pass 
else:
    #st.write(df)
    pass

    df = get_teams()
    columnNames = df.columns 
    #print(columnNames)

    #print("Introducing our teams:")
    st.write("Introducing our teams:")
    teamsList = list(set(df['DT TEAM']))
    for aTeam in teamsList:
        #print("...", aTeam)
        st.write("....", aTeam)
    #print()
    st.text("")
    numberOfTeams = len(teamsList)
    
    ## Another way to generate a list of all combinations
    # possiblePermutations = []
    # for aTeamSequence in itertools.permutations(teamsList, 6):
    #     possiblePermutations.append(aTeamSequence)
    # print('Possible sequences:', len(possiblePermutations))

    # print()
    
    #print()
    #print(f"There are {numberOfTeams} teams.")
    st.sidebar.subheader(f"There are {numberOfTeams} teams.")
    #print(f"There are n! {math.factorial(numberOfTeams)} possible combinations.")
    st.sidebar.subheader(f"There are n! {math.factorial(numberOfTeams)} possible combinations.")

    st.text("")

    # some unnecessary for randomness but adds some drama!
    #print("Drum roll please....")
    st.header("Drum roll please....")
    time.sleep(1.5)
    #print("Spin the wheel...")
    st.header("Spin the wheel...")
    time.sleep(2)
    #print()
    #st.text("")
    container = [] # keep track of the various sequences that appeared
    spinLoops = random.randint(100,250)
    for loop, i in enumerate(range(spinLoops)):
        randomSequence = random.sample(teamsList, len(teamsList))
        #print(randomSequence)
        # if loop%15 != 0:
        #     #print(".", end = "")
        # else:
        #     #print()
        #     #time.sleep(1)
        container.append(randomSequence.copy())
    #print(spinLoops, ' spins')
    #print()
    st.balloons()
    # final_count = Counter(map(tuple, container)) # count which sequences appeared the most
    # print("Most common sequences that appeared:")
    # for aSequence in final_count.most_common(5):
    #     print(aSequence)
    # print()

    #print('....the final sequence is:')
    st.sidebar.text("")
    st.sidebar.subheader('....the final sequence is:')
    #print()
    st.sidebar.text("")
    # for n, aTeam in enumerate(randomSequence):
    #     print(n + 1, aTeam)
    #     print("   ", list(df[df['DT TEAM'] == aTeam].sort_values(['NAME'])['NAME']))
    #     print()
    for n, aTeam in enumerate(randomSequence):
        st.sidebar.subheader(str(n + 1) + " " + aTeam)

    st.text("")
        
    # print()
    # print('Let the presentation begin with team:')
    # print()
    # print("...",randomSequence[0])
    # print()
    # print()
    st.text("")
    st.header('Let the presentation begin with:')
    st.text("")
    st.header("..." + randomSequence[0])
    teamMembers = list(df[df['DT TEAM'] == randomSequence[0]].sort_values(['NAME'])['NAME'])
    st.subheader(", ".join(teamMembers))

    #
    #time.sleep(2)
    #print()
    st.text("")
    #print("Introducing our team members...")
    st.text("Team Members List...")
    #print()
    st.text("")
    for n, aTeam in enumerate(teamsList):
        #print(n + 1, aTeam)
        #print("   ", list(df[df['DT TEAM'] == aTeam].sort_values(['NAME'])['NAME']))

        st.text(str(n + 1) + " " + aTeam)
        teamMembers = list(df[df['DT TEAM'] == aTeam].sort_values(['NAME'])['NAME'])
        for aMember in teamMembers:
            st.text("....." + aMember)
        #print()
        st.text("")

