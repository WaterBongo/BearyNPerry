import streamlit as st
import webbrowser,random,string

st.markdown("# Whos Avaliable? ❄️")
st.sidebar.markdown("# Finder ❄️")
st.sidebar.image("./assets/logo.png", width=250)
#create a table in streamlit
#create a table with 10 random names for the keys
#create a np table with 10 random names
#convert the np table to a pandas dataframe
import streamlit as st
import pandas as pd
import numpy as np

st.sidebar.markdown("# Finder ❄️")
st.sidebar.image("./assets/logo.png", width=250)

# Define names for keys
names = np.random.choice(['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Felix', 'Gina', 'Hank', 'Ivy', 'Jack'], size=10)

# Create a np table with 10 random names
keys = np.random.choice(names, size=10)

def tiny_url():
  re = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
  return f"tinyurl.com/{re}"

# Define values for the available/not available column
available = np.random.choice(["✅", "❌"], size=10)
oppsite_avaliable = []
for val in available:
  if val == "✅":
    #generate a fake tinyurl link

    oppsite_avaliable.append(tiny_url())
  else:
    oppsite_avaliable.append(":(")
    
print(available)
#if ❌, then create another variable with

# Convert the np table to a pandas dataframe
df = pd.DataFrame({'Tutors': keys, 'Available': available,"Link":oppsite_avaliable})

# Display the dataframe as a 
st.table(df)