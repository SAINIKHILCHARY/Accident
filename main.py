import streamlit as st # type: ignore
import plotly.express as px # type: ignore
import pandas as pd # type: ignore
import functions

#setting application to be displayed in wider layout 
st.set_page_config(layout="wide")
st.markdown("""
<style>
.hed {
    position: relative;
  top:0px
  left: 10px;
  line-height: 70px;
  font-weight: 800;
  background: linear-gradient(90deg, #1600a0, #6c70ce);
  -webkit-background-clip: text;
  display: inline-block;
  width: 973px;
  height: 109px;
  font-size: 40px;
  font-style:Foobar Pro;
}
</style>
""", unsafe_allow_html=True)
#st.markdown() is used for lightweight markup language that allows you to format text
st.markdown('<h4 class="hed">Accident Locations on India Roads</h4>', unsafe_allow_html=True)

#creating dropdown menu in the sidebar to choose an option from the list which selects only one element at a time 
all_states = ['India','Andhra Pradesh', 'Gujarath','Haryana','Madhya Pradesh','Maharastra','Rajasthan','Tamil Nadu','Uttar Pradesh','West Bengal']
functions.sidebar_space(3)         
states = st.sidebar.selectbox("Choose which state you want to see 👇", all_states)

if 'India' in states:
    st.subheader('Accident Locations in India')
    filename = 'indiads'

if 'Andhra Pradesh' in states:
    st.subheader('Accident Locations in Andhra Pradesh')
    filename = 'apdataset'

if 'Gujarath' in states:
    st.subheader('Accident Locations in Gujarath')
    filename = 'gujarathds'

if 'Haryana' in states:
    st.subheader('Accident Locations in Haryana')
    filename = 'hrds'

if 'Maharastra' in states:
    st.subheader('Accident Locations in Maharastra')
    filename = 'mhds'  

if 'Madhya Pradesh' in states:
    st.subheader('Accident Locations in Madhya Pradesh')
    filename = 'mpds'

if 'Rajasthan' in states:
    st.subheader('Accident Locations in Rajasthan')
    filename = 'rajds'

if 'Tamil Nadu' in states:
    st.subheader('Accident Locations in Tamil Nadu')
    filename = 'tnds'

if 'Uttar Pradesh' in states:
    st.subheader('Accident Locations in Uttar Pradesh')
    filename = 'upds'

if 'West Bengal' in states:
    st.subheader('Accident Locations in West Bengal')
    filename = 'wbds'

#Creating dataframe by reading the dataset provided in csv format
#df = pd.read_csv('C:/Users/91934/OneDrive/Desktop/6th/intelunnati_-404_Found--main/Accident/data/{filename}.csv')

file_path = f'C:/Users/91934/OneDrive/Desktop/6th/PROJECT/Accident/data/{filename}.csv' 
df = pd.read_csv(file_path)
#Creating a scatter mapbox plot
fig = px.scatter_mapbox(df,
    lon = df['Longitude'],
    lat = df['Latitude'],
    zoom = 5,
    color = df['Deaths'],
    size = df['Deaths'],
    width = 850,
    height = 700,
    hover_name= df['Address'],
    color_continuous_scale=px.colors.sequential.Aggrnyl
)


fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":50,"l":0,"b":10})
st.plotly_chart(fig) 

class abc:
    n=0
def fun(n):
     if abc.n==0 :
          abc.n=abc.n+1
          st.header('Data visualization of accidents locations in {}'.format(states))

# Function to show section header only once
class DisplayHeader:
    shown = False

def show_header():
    if not DisplayHeader.shown:
        DisplayHeader.shown = True
        st.header(f'Data Visualization of Accident Locations in {all_states}')

# Sidebar: Select Visualization Options
functions.sidebar_space(3)
viz_options = ['Bar Plot', 'Data Frame', 'Meta Data']
selected_viz = st.sidebar.multiselect("Choose visualizations 👇", viz_options)

# Bar Chart
if 'Bar Plot' in selected_viz:
    show_header()
    st.subheader('Bar Plot:')
    st.bar_chart(df, x='Address', y='Deaths', width=700, height=600, use_container_width=True)

# Data Frame
if 'Data Frame' in selected_viz:
    show_header()
    st.subheader('Data Frame:')
    st.dataframe(df)

# Meta Data
if 'Meta Data' in selected_viz:
    show_header()
    st.subheader('Info about Data:')
    c1, c2, c3 = st.columns([1, 2, 1])
    c1.dataframe(functions.df_info(df))

