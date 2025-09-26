import streamlit as st
import seaborn as sns
import plotly.express as px
st.title("Welcome To Dashboard")


st.title("Explore the Insight of Titanic" )
df=sns.load_dataset("titanic")
#st.dataframe(df)




#gender filter

gender=st.sidebar.multiselect("Gender",options=df['sex'].unique(),
                        
                               default=df['sex'].unique() 
                               )                                    # unique gives 2 options ie male and female else a list will appear)

#class filter
class_filter=st.sidebar.multiselect("Class",options=df['class'].unique(),
                              
                               default=df['class'].unique() )

#age filter
min_age,max_age=st.sidebar.slider("Age",
                             min_value=int(df['age'].min()),
                             max_value=int(df['age'].max()),
                             value=(int(df['age'].min()),int(df['age'].max())))

filtered_df=df[
             (df['sex'].isin(gender)) &
             (df['class'].isin(class_filter)) &
             (df['age']>=min_age) &
             (df['age']<=max_age)
             ]

st.dataframe(filtered_df)


#total survived by class

fig=px.bar(filtered_df,x='class',y='survived',
           title="Total survived By Class",
           labels={'class':"Class",'survived':'Total Survived'},
           color='survived',template="plotly_dark")
st.plotly_chart(fig)


                             

#Age Distribution
fig=px.histogram(filtered_df,x='age',
                 title='Age Distribution',
                 labels={'age':'Age'},
                 color_discrete_sequence=['#F39C12'],
                 template='plotly_dark'
                 )

st.plotly_chart(fig)

#Ppie chart for class distribution


fig=px.pie(filtered_df,names='class',
           title='Class Distribution',
           color_discrete_sequence=px.colors.sequential.RdBu,
           template='plotly_dark'
           )

st.plotly_chart(fig)





st.title("Explore the insights of penguins")
dd=sns.load_dataset("penguins")
st.dataframe(dd)


#chart based on body mass

fig=px.bar(dd, x='island',y='body_mass_g',
           title='Body mass on the Island',
           labels={'island':'Island', 'body_mass_g':'Body Mass'},
          template='plotly_dark'
           )

st.plotly_chart(fig)

#histograph based on gender and body mass g

fig=px.histogram(dd,x='body_mass_g',y='sex',
                 title='Gender Division Based on Island',
                 labels={'body_mass_g':'Island','sex':'Gender'},
                 template='plotly_dark')

st.plotly_chart(fig)



fig=px.pie(dd,names='bill_length_mm',
           title='Pie Chart Displaying Bill Length',
           color_discrete_sequence=px.colors.sequential.RdBu,
           template='plotly_dark')


#slidebar

min_mass, max_mass = st.sidebar.slider(
    'Body Mass',
    min_value=float(dd['body_mass_g'].min()),
    max_value=float(dd['body_mass_g'].max()),
    value=(float(dd['body_mass_g'].min()), float(dd['body_mass_g'].max()))
)

