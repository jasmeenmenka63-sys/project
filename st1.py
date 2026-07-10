
import streamlit as st
import plotly.express as px
import pandas as pd

import seaborn as sns
from streamlit_option_menu import option_menu
st.set_page_config(page_title="Indian Schools performance analysis ",page_icon="📱",layout="wide")

df1=pd.read_csv("dropout ratio.csv")
df2=pd.read_csv("gross enrollment.csv")
df3=pd.read_csv("infrastructure.csv")
with st.sidebar:
    menu=option_menu("📚 Indian schools performance analysis",["🏠 Overview","📊 Dataset summary","📚Data visualization","🔬 Key Insights"],menu_icon="cast",default_index=0)
    st.sidebar.subheader("🎛 Filters")

st.write(menu) 
if menu=="🏠 Overview":
    # project name
    st.title("Indian Schools performance analysis ")
    st.markdown(" An Interactive Dashboard for Analyzing Dropout Rates, Gross Enrollment Ratio,and School Infrastructure Across India")
    
    col1,col2,col3,col4=st.columns(4)
    col1.metric("States and UT Covered",36)
    col2.metric("Years Covered","2012-2016")
    col3.metric("Datasets",3)
    col4.metric("Education levels ",4)
    
    #about the project
    
    st.subheader("📖 About the Project")
    st.write("""This dashboard provides an interactive analysis of Indian school education using three datasets:\n
    • 📉 Dropout Rate\n
    • 📚 Gross Enrollment Ratio\n
    • 🏫 School Infrastructure\n
    Users can explore trends across states, years,and education levels through interactive visualizations.""")
   
    col1, col2, col3 = st.columns(3)
    with col1:
        st.success(""" 
    ### 📉 Dropout Analysis
    ✔ Primary
                   
    ✔ Upper Primary
                   
    ✔ Secondary 
                   
    ✔ Higher Secondary
    """)
    with col2:
        st.success("""
    ### 📚 Gross Enrollment

    ✔ Enrollment Trends

    ✔ Gender Comparison

    ✔ State-wise Analysis

    ✔ Year-wise Analysis
    """)
    with col3:
        st.success("""
    ### 🏫 Infrastructure

    ✔ Electricity

    ✔ Drinking Water

    ✔ Computer Facilities

    ✔ Toilets for Girls and Boys
    """)
    st.subheader("⭐ Key Features")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        -  Interactive Dashboard
        -  State-wise Analysis
        -  Year-wise Analysis
        -  Dynamic Charts
        """)

    with col2:
        st.markdown("""
        -  Plotly Visualizations
        -  Data Cleaning
        -  Insights
        -  Export Results
        """)
    st.subheader("🔄 Project Workflow")
    col1,col2,col3,col4,col5=st.columns(5)

    col1.info("📂 Raw Data")
    col2.info("🧹 Data Cleaning")
    col3.info("📊 Analysis")
    col4.info("📈 Visualization")
    col5.info("💡 Insights")
        
elif menu=="📊 Dataset summary":

    
    select=st.selectbox("select dataset",["📉 Dropout Rate Analysis","📚 Gross Enrollment Rate Analysis","🏢Infrastructure Analysis"])
    if select=="📉 Dropout Rate Analysis":
        col1,col2,col3,col4,col5=st.columns(5)
        col1.metric("Rows",len(df1))
        col2.metric("Columns",df1.shape[1])
        completeness = (1 - df1.isnull().sum().sum() / df1.size) * 100
        col3.metric("Data Completeness",completeness)
        col4.metric("Education levels ",4)
        col5.metric("Years covered",len(df1["year"].unique()))
        st.subheader("Dataset")
        st.write(df1)
        st.subheader("Statistical summary")
        st.write(df1.describe())

        st.title("Column-wise Analysis")
        column = st.selectbox("Select a Column", df1.columns)
        st.write("**Data Type:**", df1[column].dtype)
        st.write("**Missing Values:**", df1[column].isnull().sum())
        st.write("**Unique Values:**", df1[column].nunique())
        st.write("**Sample Values:**")
       # x = st.number_input("Enter number of rows", min_value=10, max_value=len(df1))
        st.write(df1[column].head(5))

    elif select=="📚 Gross Enrollment Rate Analysis":
        col1,col2,col3,col4,col5=st.columns(5)
        col1.metric("Rows",len(df2))
        col2.metric("Columns",df2.shape[1])
        completeness = (1 - df2.isnull().sum().sum() / df2.size) * 100
        col3.metric("Data Completeness",completeness)
        col4.metric("Education levels ",4)
        col5.metric("Years covered",len(df2["Year"].unique()))
        st.subheader("Dataset")
        st.write(df2)
        st.subheader("Statistical summary")
        st.write(df2.describe())

        st.title("Column-wise Analysis")
        column = st.selectbox("Select a Column", df2.columns)
        st.write("**Data Type:**", df2[column].dtype)
        st.write("**Missing Values:**", df2[column].isnull().sum())
        st.write("**Unique Values:**", df2[column].nunique())
        st.write("**Sample Values:**")
#x = st.number_input("Enter number of rows", min_value=10, max_value=len(df2))
        st.write(df2[column].head(5))

    elif select=="🏢Infrastructure Analysis":
        col1,col2,col3,col4,col5=st.columns(5)
        col1.metric("Rows",len(df3))
        col2.metric("Columns",df3.shape[1])
        completeness = (1 - df3.isnull().sum().sum() / df3.size) * 100
        col3.metric("Data Completeness",completeness)
        col4.metric("Education levels ",4)
        col5.metric("Years covered",len(df3["year"].unique()))
        st.subheader("Dataset")
        st.write(df3)
        st.subheader("Statistical summary")
        st.write(df3.describe())    

        st.title("Column-wise Analysis")
        column = st.selectbox("Select a Column", df3.columns)
        st.write("**Data Type:**", df3[column].dtype)
        st.write("**Missing Values:**", df3[column].isnull().sum())
        st.write("**Unique Values:**", df3[column].nunique())
        st.write("**Sample Values:**")
        #x = st.number_input("Enter number of rows", min_value=10, max_value=len(df3))
        st.write(df3[column].head(5))

       



elif menu=="📚Data visualization":
    select=st.selectbox(" select Dataset",["📉 Dropout Rate Analysis","📚 Gross Enrollment Rate Analysis","🏢Infrastructure Analysis"])
    if select=="📉 Dropout Rate Analysis":
            
            #no of rows select for dropout
            s=st.selectbox("select education level",["Primary_Total", "Upper Primary_Total",  "Secondary _Total", "HrSecondary_Total"])
            rows=st.slider("select number of rows ",min_value=10,max_value=len(df1),value=10)
            fig=px.bar(df1.head(rows),x="year",y=s,color="State_UT",title=f"Dropout rate analysis for {s} across state and UT")
            st.plotly_chart(fig)

            #top dropout states
            year = st.selectbox("Select Year", sorted(df1["year"].unique()))
            column = st.selectbox(
                "Select Dropout Column",
                ["Primary_Total", "Upper_Primary_Total", "Secondary_Total", "HrSecondary_Total"]
                )
            top= st.slider("Top States", 5,20)
            filtered = df1[df1["year"] == year].sort_values(column, ascending=False).head(top)
            fig = px.bar(filtered,x=column,y="State_UT",text=column,title=f"Top {top} States with Highest Dropout")
            st.plotly_chart(fig,use_container_width=True) 

            c1,c2=st.columns(2)
            with c1:

                #pie between girls and boys
                boys = (df1["Primary_Boys"].mean() +df1["Upper Primary_Boys"].mean() +df1["Secondary _Boys"].mean() +df1["HrSecondary_Boys"].mean())
                girls = (df1["Primary_Girls"].mean() +df1["Upper Primary_Girls"].mean() +df1["Secondary _Girls"].mean() +df1["HrSecondary_Girls"].mean() )
                pie_df1 = pd.DataFrame({"Category": ["Boys", "Girls"],"Dropout": [boys, girls]})
                fig = px.pie(pie_df1,names="Category",values="Dropout",title="Overall Average Dropout: Boys vs Girls",hole=0.4)
                st.plotly_chart(fig,use_container_width=True)
            with c2:

                #bar for educational level
                level_df = pd.DataFrame({ "Education Level": ["Primary","Upper Primary","Secondary","Higher Secondary"],"Average Dropout Rate": [ df1["Primary_Total"].mean(),df1["Upper Primary_Total"].mean(),df1["Secondary _Total"].mean(),df1["HrSecondary_Total"].mean()]})

                fig = px.bar(level_df,x="Education Level",y="Average Dropout Rate",color="Education Level",title="Average Dropout Rate Across Education Levels")
                st.plotly_chart(fig, use_container_width=True)

           
 
            filtered = df1[df1["year"] == year]
            box_df = df1.melt(value_vars=["Primary_Total","Upper Primary_Total","Secondary _Total","HrSecondary_Total"],var_name="Education Level",value_name="Dropout Rate")
            fig = px.box(box_df,x="Education Level",y="Dropout Rate",color="Education Level", points="outliers", title="Dropout Rate Distribution Across Education Levels")
            st.plotly_chart(fig, use_container_width=True)


    elif select=="📚 Gross Enrollment Rate Analysis":
        level = st.selectbox("Select Education Level",["Primary_Total","Upper Primary_Total","Secondary _Total","HrSecondary_Total"])
        trend = df1.groupby("year")[level].mean().reset_index()
        fig = px.line(trend,x="year",y=level,markers=True,title=f"{level.replace('_',' ')} Gross Enrollment Rate Trend")
        fig.update_layout(xaxis_title="Year",yaxis_title="Gross Enrollment Rate",hovermode="x unified" )
        st.plotly_chart(fig, use_container_width=True)  

        level1 = st.selectbox("Select Education Level",["Primary", "Upper Primary", "Secondary", "Higher Secondary"],key="level1")
        boys = {"Primary": "Primary_Boys","Upper Primary": "Upper_Primary_Boys","Secondary": "Secondary_Boys","Higher Secondary": "Higher_Secondary_Boys"}
        girls = {"Primary": "Primary_Girls","Upper Primary": "Upper_Primary_Girls","Secondary": "Secondary_Girls","Higher Secondary": "Higher_Secondary_Girls"}
        fig = px.scatter(df2,x=boys[level1],y=girls[level1],color="State_UT",hover_name="State_UT",title=f"{level1} Boys vs Girls Gross Enrollment Rate")
        fig.update_layout( xaxis_title="Boys GER",yaxis_title="Girls GER")
        st.plotly_chart(fig, use_container_width=True) 

        values = [df2["Primary_Total"].mean(),df2["Upper_Primary_Total"].mean(),df2["Secondary_Total"].mean(),df2["Higher_Secondary_Total"].mean()]
        labels = ["Primary","Upper Primary","Secondary","Higher Secondary"]
        fig = px.pie( names=labels,values=values,hole=0.4,title="Average Gross Enrollment Rate by Education Level")
        st.plotly_chart(fig, use_container_width=True)

        level_avg = df2.groupby("Year")[["Primary_Total", "Upper_Primary_Total","Secondary_Total", "Higher_Secondary_Total"]].mean().reset_index()
        level_avg = level_avg.melt(id_vars="Year",var_name="Education Level",value_name="GER")
        fig = px.bar(level_avg,x="Year",y="GER",color="Education Level",barmode="group",title="Average Gross Enrollment Rate by Education Level Over Years")
        st.plotly_chart(fig, use_container_width=True)





    elif select=="🏢Infrastructure Analysis":
        t1,t2,t3=st.tabs(["overview","Dataset","Analysis"])
        with t1:
            st.title("overview")
        
        with t2:
            st.write(df3)

        with t3:
            st.title("tab 3")  
   

elif menu=="🔬 Key Insights":
    st.title("key insights")
elif menu=="📌 Conclusion":
    st.title("conclusion")
          

    
    


  
