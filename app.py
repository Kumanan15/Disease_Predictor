import streamlit as st
from main import show_predict_page
from explore import graphs,visual2
from doc_page import doc


col1,col2 = st.sidebar.columns([4,3])
col1.image("/Users/kumanan/OneDrive/Desktop/ml/doc 2.jpeg",width=120)
col2.write("")
col2.write("")
col2.write("")
col2.write("""# I Doctor""")
st.sidebar.write("")
st.sidebar.write("")

choice = st.sidebar.selectbox("Menu",['Diagnose','Explore','Brief'])

if choice == 'Diagnose':
    show_predict_page()
elif choice == 'Explore':
    graphs()
else:
    doc()
