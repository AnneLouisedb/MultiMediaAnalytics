# external modules
import streamlit as st
import numpy as np
from jupyterlab_dagitty import DAG
import streamlit.components.v1 as components
import pandas as pd
import altair.vegalite.v4


# import internal modules

st.set_option('deprecation.showPyplotGlobalUse', False)

def main():
    st.write("Fairness in Decision Making")
    m_bias_code = """
    dag {
    A [pos="-2.200,-1.520"]
    B [pos="1.400,-1.460"]
    D [outcome,pos="1.400,1.621"]
    E [exposure,pos="-2.200,1.597"]
    Z [pos="-0.300,-0.082"]
    A -> E
    A -> Z [pos="-0.791,-1.045"]
    B -> D
    B -> Z [pos="0.680,-0.496"]
    E -> D
    }
    """
    dag = DAG(m_bias_code, height=200, mutable=True)
    st.write(dag)
    
  
    # Load in the 2 year COMPAS Recidivism dataset
    df = pd.read_csv("https://raw.githubusercontent.com/propublica/compas-analysis/master/compas-scores-two-years.csv")
    st.write(df)

  

if __name__ == "__main__":
    main()

