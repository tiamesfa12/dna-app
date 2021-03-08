import streamlit as st 
import pandas as pd 
import altair as alt 
from PIL import Image 

image = Image.open('dna-logo.jpg')

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app will be counting the nucleotide composition of query DNA!





***
""")
# input the textbox
#st.sidebar.header('Enter DNA Sequence')
st.header('Enter DNA Count')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] # skips the sequence name (first line)
sequence = ''.join(sequence) # concatenates the string

st.write("""
***
""")

st.header('INPUT (DNA Query)')
sequence

# DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count')

# 1. Print dictionary
st.subheader('1. Print Dictionary')
def DNA_nucleotide_count(seq):
	d = dict([
				('A', seq.count('A')),
				('T', seq.count('T')),
				('G', seq.count('G')),
				('C', seq.count('C'))
				])
	return d 

X = DNA_nucleotide_count(sequence)

#X_label = list(X)
#X_values = list(X.values())

X 


# 2. Print text
st.subheader('2. Print Text')
st.write("There are " + str(X['A']) + " adenine (A)")
st.write("There are " + str(X['T']) + " thymine (T)")
st.write("There are " + str(X['C']) + " guanine (G)")
st.write("There are " + str(X['T']) + " cytosine(C)")

# Display Dataframe
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

# Display Bar Chart Using Altair
st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
	x='nucleotide',
	y='count'
)

p = p.properties(
	width=alt.Step(80) # controls the width of the bar
)
st.write(p)





