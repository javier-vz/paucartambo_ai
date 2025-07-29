# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 19:59:09 2024

@author: u_humanidades
"""

import chatbees as cb
import streamlit as st

# Create an API key on UI after signup/signin.
# Configure cb to use the newly minted API key.
cb.init(api_key="MDMtMDAwMDAwMDAtMDAwMDAxLWU4NjQwNTQyLWI1MWEtN2M5MC0yMTJhLTU2YjJiODE1MWI0NA==", account_id="Q76KV9K9")

# Create a new collection
Q = cb.Collection(name="paucartambo")
 
st.write("""
         **Prototipo de sistema RAG**. 
""")

query_str = st.text_input("Pregunta algo sobre xxx. En lo posible, te sugerimos formular preguntas específicas.",
                          value="¿qué sabes sobre Qoyllorit'i?")

answer = dict(Q.ask(query_str))

st.write("""
         **respuesta :)**
""")
st.write(answer['answer'])

st.write("""
         **referencias**
""")
st.write(answer['refs'])