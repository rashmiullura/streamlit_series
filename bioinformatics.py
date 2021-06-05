#Import the libraries

from typing import Sequence
from altair.vegalite.v4.api import sequence
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

#graph -> altair library

#Page Title

image = Image.open('logo.jpeg')
st.image(image, use_column_width=True)

st.write(
    """
    # DNA Nucleotide Count Web App
    This app counts the neucleotide composition of query DNA!

    ***
    """
)
#*** -> horizontal line
#Input textbox

st.header('Enter DNA Sequence') #sidebar header

sequence_input ="DNA QUERY 1\nGGAAATTTCCCAAAGGGTTTCCCGATCGATCGTATCTTAGC"

#to get paragraph as input
sequence = st.text_area("Sequence Input", sequence_input, height=150)
sequence = sequence.splitlines() #generally to create an obejct with different elements just like \n
sequence = sequence[1:] #to skip the sequence name
# sequence -> sequence name -dna query 1\n acgacg..... \n accgg
sequence = ''.join(sequence) #concatenates list to string

#print the input dna sequence
st.header('INPUT (DNA QUERY)')
sequence
#print DNA neucleotide count
st.header('OUTPUT(DNA Neucleotide Count)')

#print dictionary
st.subheader('1. Print Dictionary')

def DNA_nucleotide_count(sequence):
    d = dict(
        [
            ('A', sequence.count('A')),
            ('T', sequence.count('T')),
            ('G', sequence.count('G')),
            ('C',sequence.count('C'))
        ]
    )
    return d;

x = DNA_nucleotide_count(sequence)

x_label = list(x)
x_values=list(x.values())

x

st.subheader('2. Print text')
st.write('There are '+str(x['A'])+'adenine (A)')
st.write('There are '+str(x['T'])+'thymine (T)')
st.write('There are '+str(x['G'])+'guanine (G)')
st.write('There are '+str(x['C'])+'cystocine (C)')

#display dataframe
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(x, orient='index')
df = df.rename({0:'count'},axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index':'nucleotide'})
st.write(df)

#display barchart using altair
st.subheader('4. Disply Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)

p = p.properties(
    width=alt.Step(80) #controls the width of the bar
)

st.write(p)




