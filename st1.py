import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd


st.markdown("""
<style>
h1,h2,h3{
    color:#2563EB !important;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""<style>.stApp{background-color:#F8FAFC;}div[data-testid="stMetric"]{background:white;padding:20px;border-radius:15px;border-left:6px solid #2563EB;box-shadow:0px 4px 12px rgba(0,0,0,0.15);text-align:center;}div[data-testid="stMetricLabel"]{font-size:18px;font-weight:bold;color:#1F2937;}div[data-testid="stMetricValue"]{font-size:32px;font-weight:bold;color:#2563EB;}.stPlotlyChart{background:white;padding:15px;border-radius:15px;box-shadow:0px 4px 12px rgba(0,0,0,0.12);}.stAlert{border-radius:15px;}h1,h2,h3{color:#0F172A;font-weight:bold;}</style>""",unsafe_allow_html=True)
st.markdown("""<style>.box{background:#EAF4FF;border-left:6px solid #2563EB;padding:12px 15px;border-radius:10px;margin-bottom:8px;font-size:16px;font-weight:500;color:#1F2937;}</style>""",unsafe_allow_html=True)
st.set_page_config(page_title="Indian Schools performance analysis ",page_icon="📱",layout="wide")

df1=pd.read_csv("dropout ratio.csv")
df2=pd.read_csv("gross enrollment.csv")
df3=pd.read_csv("infrastructure.csv")
f1=pd.read_csv("dropout-ratio-2012-2015.csv")
f2=pd.read_csv("gross-enrollment-ratio-2013-2016.csv")
f3=pd.read_csv("infrastructure_merged_uncleaned.csv")
df=pd.read_csv("comparison_ready.csv")
st.markdown("""
        <style>
        .section-header{background:#001f54;color:white;padding:14px;border-radius:10px;font-size:28px;font-weight:bold;text-align:center;margin-bottom:20px;}
        .graph-box{background:white;padding:20px;border-radius:12px;box-shadow:0 4px 10px rgba(0,0,0,0.15);margin-bottom:20px;}
        .insight-box{background:#EEF4FF;border-left:6px solid #001f54;padding:15px;border-radius:10px;font-size:16px;color:#222;margin-top:15px;}
        </style>
        """,unsafe_allow_html=True)


# st.markdown("""<style>section[data-testid="stSidebar"]{background-color:#0F172A !important;}section[data-testid="stSidebar"] *{color:white !important;}</style>""",unsafe_allow_html=True)
st.markdown("""<style>section[data-testid="stSidebar"]{background:#0F172A!important;}section[data-testid="stSidebar"] h1,section[data-testid="stSidebar"] h2,section[data-testid="stSidebar"] h3,section[data-testid="stSidebar"] label,section[data-testid="stSidebar"] p{color:white!important;}section[data-testid="stSidebar"] div[data-baseweb="select"] *{color:black!important;}</style>""",unsafe_allow_html=True)
with st.sidebar:
    st.markdown("<h1 style='text-align:center;font-size:34px;font-weight:bold;color:white;'>📚 Indian Schools Performance Analysis</h1>",unsafe_allow_html=True)
    st.markdown("---")
    menu=option_menu(menu_title="Main menu",options=["🏠 Overview","📊 Dataset Summary","🧹 Data Cleaning","📈 Data Visualization","⚖️ Camparative analysis","🔬 Key Insights"],menu_icon="list",default_index=0,styles={"container":{"padding":"0!important","background-color":"#0F172A"},"menu-title":{"color":"white","font-size":"22px","font-weight":"bold"},"icon":{"color":"white","font-size":"18px"},"nav-link":{"font-size":"17px","text-align":"left","margin":"5px","padding":"12px","border-radius":"8px","color":"white","--hover-color":"#1E3A8A"},"nav-link-selected":{"background-color":"#2563EB","color":"white","font-weight":"bold"}})

# st.markdown(f"<h1 style='font-size:36px;color:#2563EB;'>{menu}</h1>", unsafe_allow_html=True)
if menu=="🏠 Overview":
    # project name
    st.markdown("""<style>.stApp{background-color:#F8FAFC;}div[data-testid="stMetric"]{background:#FFFFFF;border-radius:15px;padding:18px;border-left:6px solid #2563EB;box-shadow:0px 4px 12px rgba(0,0,0,0.12);}div[data-testid="stMetric"] label{font-size:18px !important;font-weight:bold !important;color:#1F2937 !important;}div[data-testid="stMetricValue"]{font-size:34px !important;font-weight:bold !important;color:#2563EB !important;}div[data-testid="stVerticalBlock"]{border-radius:12px;}h1{color:#0F172A;font-size:42px !important;font-weight:700 !important;}h2,h3{color:#0F172A;font-weight:600 !important;}div.stAlert{border-radius:15px;}hr{border:1px solid #CBD5E1;}</style>""",unsafe_allow_html=True)
    st.markdown("<div style='background:#0F172A;border:3px solid #2563EB;padding:28px;border-radius:18px;text-align:center;box-shadow:0 8px 18px rgba(0,0,0,0.25);margin-bottom:25px;'><h1 style='color:white;margin:0;font-size:40px;font-weight:bold;'>📚 Indian Schools Performance Analysis</h1><p style='color:#E2E8F0;font-size:19px;margin-top:12px;'>An Interactive Dashboard for Analyzing Dropout Rates, Gross Enrollment Ratio and School Infrastructure Across India</p></div>",unsafe_allow_html=True)
    # st.markdown("<div style='background:#0F172A;border:3px solid #FBBF24;padding:28px;border-radius:18px;text-align:center;box-shadow:0 8px 18px rgba(0,0,0,0.25);margin-bottom:25px;'><h1 style='color:#FBBF24;margin:0;font-size:40px;font-weight:bold;'>📚 Indian Schools Performance Analysis</h1><p style='color:white;font-size:19px;margin-top:12px;'>An Interactive Dashboard for Analyzing Dropout Rates, Gross Enrollment Ratio and School Infrastructure Across India</p></div>",unsafe_allow_html=True)
    # st.title("Indian Schools performance analysis ")
    # st.markdown("<h1 style='text-align:center;'>📚 Indian Schools Performance Analysis</h1>",unsafe_allow_html=True)
    # st.markdown(" An Interactive Dashboard for Analyzing Dropout Rates, Gross Enrollment Ratio,and School Infrastructure Across India")
    # st.markdown("<p style='text-align:center;font-size:20px;color:#475569;'>An Interactive Dashboard for Analyzing Dropout Rates, Gross Enrollment Ratio and School Infrastructure Across India</p>",unsafe_allow_html=True)
    
    col1,col2,col3,col4=st.columns(4)
    col1.metric("States and UT Covered",36)
    col2.metric("Datasets",3)
    col3.metric("Education levels ",4)
    col4.metric("Years Covered","4")
    c1,c2=st.columns(2)
    with c1:
        st.subheader("Graph b/w boys'toilet and state_UT")    
        graph=px.bar(df3.head(20),x="State_UT",y="Boys_toilet_All Schools") 
        graph.update_layout(paper_bgcolor="white",plot_bgcolor="white",margin=dict(l=20,r=20,t=60,b=20),shapes=[dict(type="rect",xref="paper",yref="paper",x0=0,y0=0,x1=1,y1=1,line=dict(color="#2563EB",width=2),fillcolor="rgba(0,0,0,0)")]) 
        st.plotly_chart(graph) 
    with c2:
        st.subheader("Graph b/w computers and state_UT")    
        graph=px.bar(df3.head(20),x="State_UT",y="Computers_All Schools")  
        graph.update_layout(paper_bgcolor="white",plot_bgcolor="white",margin=dict(l=20,r=20,t=60,b=20),shapes=[dict(type="rect",xref="paper",yref="paper",x0=0,y0=0,x1=1,y1=1,line=dict(color="#2563EB",width=2),fillcolor="rgba(0,0,0,0)")])
        st.plotly_chart(graph)
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
    col1,col2=st.columns(2)
    col1.markdown("<div style='background:#E3F2FD;padding:18px;border-radius:12px;text-align:center;font-weight:bold;color:#0D47A1;'>📊<br>Interactive Dashboard</div>",unsafe_allow_html=True)
    col2.markdown("<div style='background:#E8F5E9;padding:18px;border-radius:12px;text-align:center;font-weight:bold;color:#1B5E20;'>🗺️<br>State-wise Analysis</div>",unsafe_allow_html=True)

    col3,col4=st.columns(2)
    col3.markdown("<div style='background:#FFF3E0;padding:18px;border-radius:12px;text-align:center;font-weight:bold;color:#E65100;'>📅<br>Year-wise Analysis</div>",unsafe_allow_html=True)
    col4.markdown("<div style='background:#F3E5F5;padding:18px;border-radius:12px;text-align:center;font-weight:bold;color:#6A1B9A;'>📈<br>Dynamic Charts</div>",unsafe_allow_html=True)

    col5,col6=st.columns(2)
    col5.markdown("<div style='background:#E1F5FE;padding:18px;border-radius:12px;text-align:center;font-weight:bold;color:#01579B;'>📉<br>Plotly Visualizations</div>",unsafe_allow_html=True)
    col6.markdown("<div style='background:#FCE4EC;padding:18px;border-radius:12px;text-align:center;font-weight:bold;color:#AD1457;'>🧹<br>Data Cleaning</div>",unsafe_allow_html=True)

    col7,col8=st.columns(2)
    col7.markdown("<div style='background:#F1F8E9;padding:18px;border-radius:12px;text-align:center;font-weight:bold;color:#33691E;'>💡<br>Insights</div>",unsafe_allow_html=True)
    col8.markdown("<div style='background:#FFF8E1;padding:18px;border-radius:12px;text-align:center;font-weight:bold;color:#F57F17;'>📥<br>Export Results</div>",unsafe_allow_html=True)
    col1, col2 = st.columns(2)


     
    st.subheader("🔄 Project Workflow")
    col1,col2,col3,col4,col5=st.columns(5)

    col1.info("📂 Raw Data")
    col2.info("🧹 Data Cleaning")
    col3.info("📊 Analysis")
    col4.info("📈 Visualization")
    col5.info("💡 Insights")
        
elif menu=="📊 Dataset Summary":
   
    t1,t2,t3=st.tabs(["📉 Dropout rates","📚 Gross enrollment","🏢 Infrastructure"])
    
    # select=st.selectbox("select dataset",["Dropout Rate Analysis"," Gross Enrollment Rate Analysis","Infrastructure Analysis"])
    with t1:
        
        # uploaded_file = st.file_uploader("Upload Dataset",type=["csv"],key="dataset1")
        # if uploaded_file is not None:

            df1= pd.read_csv("dropout ratio.csv")
            # st.success("Dataset Uploaded Successfully!")
            st.title("Dataset Summary")
            # total_rows = df1.shape[0]
            # total_columns = df1.shape[1]
            duplicate=f1.duplicated().sum()
            total_states = df1["State_UT"].nunique() if "State_UT" in df1.columns else "Not Available"
            total_years = df1["year"].nunique() if "year" in df1.columns else "Not Available"
            missing_value=df1.isnull().sum().sum()
            # size = round(uploaded_file.size / (1024 * 1024), 2)
            col1, col2, col3, col4 = st.columns(4)

            # col1.metric("Rows", total_rows)
            # col1.metric("Columns", total_columns)
            col1.metric("States/UTs", total_states)
            col2.metric("Years", total_years)
            col3.metric("Duplicate values",duplicate)
            col4.metric("Missing value",missing_value)
            st.divider()
            
            st.subheader("Dataset Preview")
            rows = st.slider("Rows to Preview",min_value=5,max_value=min(50, len(df1)),value=10,key="data1")
            st.dataframe(df1.head(rows), use_container_width=True)
            st.divider()
            # ---------------- Column Names ---------------- #

            st.subheader("Column Names")
            st.write(list(df1.columns))
            st.divider()
            # ---------------- Data Types ---------------- #
            st.subheader("Data Types")
            st.dataframe(pd.DataFrame(df1.dtypes, columns=["Data Type"]),use_container_width=True)
            st.divider()

            # ---------------- Statistical Summary ---------------- #
            st.subheader("Statistical Summary")
            st.dataframe(df1.describe(), use_container_width=True)
            st.divider()

            st.title("Column-wise Analysis")
            column = st.selectbox("Select a Column", df1.columns)
            st.write("**Data Type:**", df1[column].dtype)
            st.write("**Missing Values:**", df1[column].isnull().sum())
            st.write("**Unique Values:**", df1[column].nunique())
           
          
        # else:
        #     st.info("Please upload a CSV dataset.")

    with t2:
        # uploaded_file = st.file_uploader("upload file",type=["csv"],key="dataset2")
        # if uploaded_file is not None:
            df3= pd.read_csv("gross enrollment.csv")
            # st.success("Dataset Uploaded Successfully!")
            st.title("Dataset Summary")
            # total_rows = df2.shape[0]
            # total_columns = df2.shape[1]
            total_states = df2["State_UT"].nunique() if "State_UT" in df2.columns else "Not Available"
            total_years = df2["Year"].nunique() if "Year" in df2.columns else "Not Available"
            missing_value=df2.isnull().sum().sum()
            duplicate=f2.duplicated().sum()
            # size = round(uploaded_file.size / (1024 * 1024), 2)
            col1, col2, col3, col4 = st.columns(4)
            # col1.metric("Rows", total_rows)
            # col2.metric("Columns", total_columns)
            col1.metric("States/UTs", total_states)
            col2.metric("Years", total_years)
            col3.metric("Duplicate values",duplicate)
            # col5.metric("Size (MB)", size)
            col4.metric("Missing values",missing_value)
            st.divider()
            st.subheader("Dataset Preview")
            rows = st.slider("Rows to Preview",min_value=5,max_value=min(50, len(df3)),value=10,key="data2")
            st.dataframe(df2.head(rows), use_container_width=True)
            st.divider()
            st.subheader("Column Names")
            st.write(list(df2.columns))
            st.divider()
            st.subheader("Data Types")
            st.dataframe(pd.DataFrame(df2.dtypes, columns=["Data Type"]),use_container_width=True)
            st.divider()
            st.subheader("Statistical Summary")
            st.dataframe(df2.describe(), use_container_width=True)
            st.divider()
            st.title("Column-wise Analysis")
            column = st.selectbox("Select a Column", df2.columns)
            st.write("**Data Type:**", df2[column].dtype)
            st.write("**Missing Values:**", df2[column].isnull().sum())
            st.write("**Unique Values:**", df2[column].nunique())
        # else:
        #     st.info("Please upload a CSV dataset.")

    with t3:
        # uploaded_file = st.file_uploader("Upload Dataset",type=["csv"],key="dataset3")
        # if uploaded_file is not None:
            df3= pd.read_csv("infrastructure.csv")
            # st.success("Dataset Uploaded Successfully!")
            st.title("Dataset Summary")
            # total_rows = df3.shape[0]
            # total_columns = df3.shape[1]
            total_states = df3["State_UT"].nunique() if "State_UT" in df3.columns else "Not Available"
            total_years = df3["year"].nunique() if "year" in df3.columns else "Not Available"
            missing_value=df3.isnull().sum().sum()
            duplicate=f1.duplicated().sum()
            # size = round(uploaded_file.size / (1024 * 1024), 2)
            col1, col2, col3, col4 = st.columns(4)
            # col1.metric("Rows", total_rows)
            # col2.metric("Columns", total_columns)
            col1.metric("States/UTs", total_states)
            col2.metric("Years", total_years)
            col3.metric("Duplicate values",duplicate)
            col4.metric("Missing values",missing_value)
            
            # col5.metric("Size (MB)", size)
            st.divider()
            st.subheader("Dataset Preview")
            rows = st.slider("Rows to Preview",min_value=5,max_value=min(50, len(df3)),value=10,key="data3")
            st.dataframe(df3.head(rows), use_container_width=True)
            st.divider()
            st.subheader("Column Names")
            st.write(list(df3.columns))
            st.divider()
            st.subheader("Data Types")
            st.dataframe(pd.DataFrame(df3.dtypes, columns=["Data Type"]),use_container_width=True)
            st.divider()
            st.subheader("Statistical Summary")
            st.dataframe(df3.describe(), use_container_width=True)
            st.divider()
            st.title("Column-wise Analysis")
            column = st.selectbox("Select a Column", df3.columns)
            st.write("**Data Type:**", df3[column].dtype)
            st.write("**Missing Values:**", df3[column].isnull().sum())
            st.write("**Unique Values:**", df3[column].nunique())
            
        # else:
        #     st.info("Please upload a CSV dataset.")
       

elif menu=="🧹 Data Cleaning":
  
    t1,t2,t3=st.tabs(["Dropout rates","Gross enrollment","Infrastructure"])
    with t1:
        
        st.write("""This page shows the preprocessing steps performed on the original dataset before it was used for analysis and visualization.""")
        c1,c2,c3,c4=st.columns(4)
        total_missing=f1.isnull().sum().sum()
        duplicate=f1.duplicated().sum()
        c1.metric("Original columns",f1.shape[1])
        c2.metric("Rows",f1.shape[0])
        c3.metric("Missing values", total_missing)
        c4.metric("Duplicate",duplicate)
        st.subheader("Original Dataset")
        show=st.slider("Rows",min_value=5,max_value=len(f1),key="row1")
        st.dataframe(f1.head(show))
        st.markdown("<div style='background-color:#E3F2FD;padding:15px;border-radius:10px;border-left:6px solid #1976D2;color:#0D47A1;'><b>Cleaning Steps</b><br><br>✔ Loaded the original dataset.<br>✔ Checked missing values.<br>✔ Filled missing values using the median.<br>✔ Corrected data types.<br>✔ Saved the cleaned dataset.</div>", unsafe_allow_html=True)
        
        st.divider()
        st.title("After Cleaning")
        c1,c2,c3,c4=st.columns(4)
        total_missing=df1.isnull().sum().sum()
        duplicate=df1.duplicated().sum()
        c1.metric("Original columns",df1.shape[1])
        c2.metric("Rows",df1.shape[0])
        c3.metric("Missing values", total_missing)
        c4.metric("Duplicate",duplicate)
        st.slider("Rows",min_value=5,max_value=len(df1),key="row_df1")
        st.dataframe(df1.head())
    with t2:
        
        st.write("""This page shows the preprocessing steps performed on the original dataset before it was used for analysis and visualization.""")
        c1,c2,c3,c4=st.columns(4)
        total_missing=f2.isnull().sum().sum()
        duplicate=f2.duplicated().sum()
        c1.metric("Original columns",f2.shape[1])
        c2.metric("Rows",f2.shape[0])
        c3.metric("Missing values", total_missing)
        c4.metric("Duplicate",duplicate)
        st.subheader("Original Dataset")
        st.slider("Rows",min_value=5,max_value=len(f2),key="row2")
        st.dataframe(f2.head())
        st.markdown("<div style='background-color:#E3F2FD;padding:15px;border-radius:10px;border-left:6px solid #1976D2;color:#0D47A1;'><b>Cleaning Steps</b><br><br>✔ Loaded the original dataset.<br>✔ Checked missing values.<br>✔ Corrected data types.<br>✔ Removed the unnecessary columns.<br>✔ Saved the cleaned dataset.</div>", unsafe_allow_html=True)
       
        st.divider()
        st.title("After Cleaning")
        c1,c2,c3,c4=st.columns(4)
        total_missing=df2.isnull().sum().sum()
        duplicate=df2.duplicated().sum()
        c1.metric("Original columns",df2.shape[1])
        c2.metric("Rows",df2.shape[0])
        c3.metric("Missing values", total_missing)
        c4.metric("Duplicate",duplicate)
        st.slider("Rows",min_value=5,max_value=len(df2),key="row_df2")
        st.dataframe(df2.head())

    with t3:
        
        st.write("""This page shows the preprocessing steps performed on the original dataset before it was used for analysis and visualization.""")
        c1,c2,c3,c4=st.columns(4)
        total_missing=f3.isnull().sum().sum()
        duplicate=f3.duplicated().sum()
        c1.metric("Original columns",f3.shape[1])
        c2.metric("Rows",f3.shape[0])
        c3.metric("Missing values", total_missing)
        c4.metric("Duplicate",duplicate)
        st.subheader("Original Dataset")
        show=st.slider("Rows",min_value=5,max_value=len(f2),key="row3")
        st.dataframe(f3.head(show))
        st.markdown("<div style='background-color:#E3F2FD;padding:15px;border-radius:10px;border-left:6px solid #1976D2;color:#0D47A1;'><b>Cleaning Steps</b><br><br>✔ Loaded the original dataset.<br>✔ Checked missing values.<br>✔ Corrected data types.<br>✔ Removed the unnecessary columns.<br>✔ Saved the cleaned dataset.</div>", unsafe_allow_html=True)
        
        st.divider()

        st.title("After Cleaning")
        c1,c2,c3,c4=st.columns(4)
        total_missing=df3.isnull().sum().sum()
        duplicate=df3.duplicated().sum()
        c1.metric("Original columns",df3.shape[1])
        c2.metric("Rows",df3.shape[0])
        c3.metric("Missing values", total_missing)
        c4.metric("Duplicate",duplicate)
        st.slider("Rows",min_value=5,max_value=len(df3),key="row_df3")
        st.dataframe(df3.head())
   

elif menu=="📈 Data Visualization":
    st.title("📈 Data Visualization")
    select=st.selectbox("Select Dataset",["📉 Dropout Rate Analysis","📚 Gross Enrollment Rate Analysis","🏢Infrastructure Analysis"])
    st.sidebar.subheader("🎛 Filters")
    top_n = st.sidebar.slider("Select Top N States", 5, 20, 10)
    if select=="📉 Dropout Rate Analysis":
            states = st.sidebar.multiselect("Select State(s)",df1["State_UT"].unique(),default=df1["State_UT"].unique()[:3] )  # Shows first 3 states by default)
            filtered_df = df1[df1["State_UT"].isin(states)]
           
            s=st.sidebar.selectbox("select education level",["Primary_Total", "Upper Primary_Total",  "Secondary _Total", "HrSecondary_Total"])
            fig = px.bar(filtered_df,x="year",y=s,color="State_UT",title=f"Dropout Rate Analysis for {s} Across Selected States")
            fig.update_layout(paper_bgcolor="white",plot_bgcolor="white",margin=dict(l=20,r=20,t=60,b=20),shapes=[dict(type="rect",xref="paper",yref="paper",x0=0,y0=0,x1=1,y1=1,line=dict(color="#2563EB",width=2),fillcolor="rgba(0,0,0,0)")])
            st.plotly_chart(fig)

            #top dropout states
            year = st.sidebar.selectbox("Select Year",sorted(df1["year"].unique()))
            # top_n = st.sidebar.slider("Select Top N States", 5, 20, 10)
            year= df1[df1["year"] == year]
            top_df = year.sort_values(by=s, ascending=False).head(top_n)
            fig = px.bar(top_df,x="State_UT",y=s,color="State_UT",title=f"Top {top_n} States with Highest {s} Dropout Rate")
            fig.update_layout(paper_bgcolor="white",plot_bgcolor="white",margin=dict(l=20,r=20,t=60,b=20),shapes=[dict(type="rect",xref="paper",yref="paper",x0=0,y0=0,x1=1,y1=1,line=dict(color="#2563EB",width=2),fillcolor="rgba(0,0,0,0)")])
            st.plotly_chart(fig, use_container_width=True)

            c1,c2=st.columns(2)
            with c1:

                #pie between girls and boys
                boys = (df1["Primary_Boys"].mean() +df1["Upper Primary_Boys"].mean() +df1["Secondary _Boys"].mean() +df1["HrSecondary_Boys"].mean())
                girls = (df1["Primary_Girls"].mean() +df1["Upper Primary_Girls"].mean() +df1["Secondary _Girls"].mean() +df1["HrSecondary_Girls"].mean() )
                pie_df1 = pd.DataFrame({"Category": ["Boys", "Girls"],"Dropout": [boys, girls]})
                fig = px.pie(pie_df1,names="Category",values="Dropout",title="Overall Average Dropout Distribution : Boys vs Girls",hole=0.4)
                fig.update_layout(paper_bgcolor="white",plot_bgcolor="white",margin=dict(l=20,r=20,t=60,b=20),shapes=[dict(type="rect",xref="paper",yref="paper",x0=0,y0=0,x1=1,y1=1,line=dict(color="#2563EB",width=2),fillcolor="rgba(0,0,0,0)")])
                st.plotly_chart(fig,use_container_width=True)
            with c2:

                #bar for educational level
                level_df = pd.DataFrame({ "Education Level": ["Primary","Upper Primary","Secondary","Higher Secondary"],"Average Dropout Rate": [ df1["Primary_Total"].mean(),df1["Upper Primary_Total"].mean(),df1["Secondary _Total"].mean(),df1["HrSecondary_Total"].mean()]})

                fig = px.bar(level_df,x="Education Level",y="Average Dropout Rate",color="Education Level",title="Average Dropout Rate Across Education Levels")
                fig.update_layout(paper_bgcolor="white",plot_bgcolor="white",margin=dict(l=20,r=20,t=60,b=20),shapes=[dict(type="rect",xref="paper",yref="paper",x0=0,y0=0,x1=1,y1=1,line=dict(color="#2563EB",width=2),fillcolor="rgba(0,0,0,0)")])
                st.plotly_chart(fig, use_container_width=True)

           
            
            # year= df1[df1["year"] == year]
            box_df = year.melt(value_vars=["Primary_Total","Upper Primary_Total","Secondary _Total","HrSecondary_Total"],var_name="Education Level",value_name="Dropout Rate")
            fig = px.box(box_df,x="Education Level",y="Dropout Rate",color="Education Level", points="outliers", title="Dropout Rate Distribution Across Education Levels by year")
            fig.update_layout(paper_bgcolor="white",plot_bgcolor="white",margin=dict(l=20,r=20,t=60,b=20),shapes=[dict(type="rect",xref="paper",yref="paper",x0=0,y0=0,x1=1,y1=1,line=dict(color="#2563EB",width=2),fillcolor="rgba(0,0,0,0)")])
            st.plotly_chart(fig, use_container_width=True)
             
            fig = px.bar(df1,x="State_UT",y=["Primary_Boys", "Primary_Girls"],barmode="group",title="Primary Boys vs Girls Dropout Rate by State",labels={"value": "Dropout Rate","State_UT": "States","variable": "Category"}) 
            fig.update_layout(paper_bgcolor="white",plot_bgcolor="white",margin=dict(l=20,r=20,t=60,b=20),shapes=[dict(type="rect",xref="paper",yref="paper",x0=0,y0=0,x1=1,y1=1,line=dict(color="#2563EB",width=2),fillcolor="rgba(0,0,0,0)")])
            st.plotly_chart(fig, use_container_width=True)

            
            
            # filtered_df = df1[df1["State_UT"].isin(states)]
            fig = px.line(filtered_df,x="year",y=s,color="State_UT",markers=True,title=f"{s} Dropout Trend by state wise")
            fig.update_layout(paper_bgcolor="white",plot_bgcolor="white",margin=dict(l=20,r=20,t=60,b=20),shapes=[dict(type="rect",xref="paper",yref="paper",x0=0,y0=0,x1=1,y1=1,line=dict(color="#2563EB",width=2),fillcolor="rgba(0,0,0,0)")])
            st.plotly_chart(fig, use_container_width=True)
                
    elif select=="📚 Gross Enrollment Rate Analysis":
        level= st.sidebar.selectbox("Select Education Level",["Primary_Total","Upper_Primary_Total","Secondary_Total","Higher_Secondary_Total"])
        Year=st.sidebar.selectbox("select Year",sorted(df2["Year"].unique()))
        trend = df2[df2["Year"] == Year].sort_values(level, ascending=False).head()

        # fig = px.line(df2,x="Year",y=level,markers=True,title=f"{level.replace('_',' ')} Gross Enrollment Rate Trend")
        # fig.update_layout(xaxis_title="Year",yaxis_title="Gross Enrollment Rate",hovermode="x unified" )
        # st.plotly_chart(fig, use_container_width=True)  
        

        state = st.sidebar.multiselect("Select State", df2["State_UT"].unique(),default=["Punjab","Chandigarh","Arunachal Pradesh"])
        line_df = df2[df2["State_UT"].isin(state)]
        fig = px.line(line_df,x="Year",y=level,color="State_UT",markers=True)
        fig.update_layout(paper_bgcolor="white",plot_bgcolor="white",margin=dict(l=20,r=20,t=60,b=20),shapes=[dict(type="rect",xref="paper",yref="paper",x0=0,y0=0,x1=1,y1=1,line=dict(color="#2563EB",width=2),fillcolor="rgba(0,0,0,0)")])
        st.plotly_chart(fig, use_container_width=True)

        # level1 = st.selectbox("Select Education Level",["Primary_Total", "Upper_Primary_Total", "Secondary_Total", "Higher_Secondary_Total"],key="level1")
        boys = {"Primary_Total": "Primary_Boys","Upper_Primary_Total": "Upper_Primary_Boys","Secondary_Total": "Secondary_Boys","Higher_Secondary_Total": "Higher_Secondary_Boys"}
        girls = {"Primary_Total": "Primary_Girls","Upper_Primary_Total": "Upper_Primary_Girls","Secondary_Total": "Secondary_Girls","Higher_Secondary_Total": "Higher_Secondary_Girls"}
        fig = px.scatter(df2,x=boys[level],y=girls[level],color="State_UT",hover_name="State_UT",hover_data=["Year"],title=f"{level} Boys vs Girls Gross Enrollment Rate")
        fig.update_layout( xaxis_title="Boys GER",yaxis_title="Girls GER")
        fig.update_layout(paper_bgcolor="white",plot_bgcolor="white",margin=dict(l=20,r=20,t=60,b=20),shapes=[dict(type="rect",xref="paper",yref="paper",x0=0,y0=0,x1=1,y1=1,line=dict(color="#2563EB",width=2),fillcolor="rgba(0,0,0,0)")])
        st.plotly_chart(fig, use_container_width=True) 

        values = [df2["Primary_Total"].mean(),df2["Upper_Primary_Total"].mean(),df2["Secondary_Total"].mean(),df2["Higher_Secondary_Total"].mean()]
        labels = ["Primary","Upper Primary","Secondary","Higher Secondary"]
        fig = px.pie( names=labels,values=values,hole=0.4,title="Average Gross Enrollment Rate by Education Level")
        fig.update_layout(paper_bgcolor="white",plot_bgcolor="white",margin=dict(l=20,r=20,t=60,b=20),shapes=[dict(type="rect",xref="paper",yref="paper",x0=0,y0=0,x1=1,y1=1,line=dict(color="#2563EB",width=2),fillcolor="rgba(0,0,0,0)")])
        st.plotly_chart(fig, use_container_width=True)

        level_avg = df2.groupby("Year")[["Primary_Total", "Upper_Primary_Total","Secondary_Total", "Higher_Secondary_Total"]].mean().reset_index()
        level_avg = level_avg.melt(id_vars="Year",var_name="Education Level",value_name="GER")
        fig = px.bar(level_avg,x="Year",y="GER",color="Education Level",barmode="group",title="Average Gross Enrollment Rate by Education Level Over Years")
        fig.update_layout(paper_bgcolor="white",plot_bgcolor="white",margin=dict(l=20,r=20,t=60,b=20),shapes=[dict(type="rect",xref="paper",yref="paper",x0=0,y0=0,x1=1,y1=1,line=dict(color="#2563EB",width=2),fillcolor="rgba(0,0,0,0)")])
        st.plotly_chart(fig, use_container_width=True)

        
        top = df2[df2["Year"] == Year].assign(Overall_GER=df2[["Primary_Total","Upper_Primary_Total","Secondary_Total","Higher_Secondary_Total"]].mean(axis=1)).sort_values("Overall_GER", ascending=False).head(top_n)
        fig = px.bar(top, x="Overall_GER", y="State_UT", color="Overall_GER", orientation="h", title=f"Top {top_n} States by Overall Gross Enrollment Rate ({Year})")
        fig.update_layout(paper_bgcolor="white",plot_bgcolor="white",margin=dict(l=20,r=20,t=60,b=20),shapes=[dict(type="rect",xref="paper",yref="paper",x0=0,y0=0,x1=1,y1=1,line=dict(color="#2563EB",width=2),fillcolor="rgba(0,0,0,0)")])
        st.plotly_chart(fig, use_container_width=True)
      






    elif select=="🏢Infrastructure Analysis":
        facility = ["Computers_All Schools","Electricity_All Schools","Water_All Schools","Boys_toilet_All Schools","Girls_Toilet_All Schools"]
        top = df3.assign(Overall_Infrastructure=df3[facility].mean(axis=1)).groupby("State_UT")["Overall_Infrastructure"].mean().sort_values(ascending=False).head(top_n).reset_index()
        fig = px.bar(top, x="Overall_Infrastructure", y="State_UT", color="Overall_Infrastructure", orientation="h", title=f"Top {top_n} States by Overall Infrastructure (Average of All Years)")
        fig.update_layout(paper_bgcolor="white",plot_bgcolor="white",margin=dict(l=20,r=20,t=60,b=20),shapes=[dict(type="rect",xref="paper",yref="paper",x0=0,y0=0,x1=1,y1=1,line=dict(color="#2563EB",width=2),fillcolor="rgba(0,0,0,0)")])
        st.plotly_chart(fig, use_container_width=True)
        
        fig = px.scatter(df3, x="Electricity_All Schools", y="Water_All Schools", color="State_UT", hover_name="State_UT", hover_data=["year"], title="Electricity vs Water Availability (All Years)")
        fig.update_layout(xaxis_title="Electricity Availability", yaxis_title="Water Availability")
        fig.update_layout(paper_bgcolor="white",plot_bgcolor="white",margin=dict(l=20,r=20,t=60,b=20),shapes=[dict(type="rect",xref="paper",yref="paper",x0=0,y0=0,x1=1,y1=1,line=dict(color="#2563EB",width=2),fillcolor="rgba(0,0,0,0)")])
        st.plotly_chart(fig, use_container_width=True)
        
        toilet = df3.groupby("year")[["Boys_toilet_All Schools","Girls_Toilet_All Schools"]].mean().reset_index()
        fig = px.bar(toilet, x="year", y=["Boys_toilet_All Schools","Girls_Toilet_All Schools"], barmode="group", title="Average Boys vs Girls Toilet Availability Over Years")
        fig.update_layout(paper_bgcolor="white",plot_bgcolor="white",margin=dict(l=20,r=20,t=60,b=20),shapes=[dict(type="rect",xref="paper",yref="paper",x0=0,y0=0,x1=1,y1=1,line=dict(color="#2563EB",width=2),fillcolor="rgba(0,0,0,0)")])
        st.plotly_chart(fig, use_container_width=True)

        trend = df3.groupby("year")[["Computers_All Schools","Electricity_All Schools","Water_All Schools","Boys_toilet_All Schools","Girls_Toilet_All Schools"]].mean().reset_index()
        fig = px.line(trend, x="year", y=["Computers_All Schools","Electricity_All Schools","Water_All Schools","Boys_toilet_All Schools","Girls_Toilet_All Schools"], markers=True, title="Infrastructure Facilities Trend Over Years")
        fig.update_layout(paper_bgcolor="white",plot_bgcolor="white",margin=dict(l=20,r=20,t=60,b=20),shapes=[dict(type="rect",xref="paper",yref="paper",x0=0,y0=0,x1=1,y1=1,line=dict(color="#2563EB",width=2),fillcolor="rgba(0,0,0,0)")])
        st.plotly_chart(fig, use_container_width=True)

        top = df3.groupby("State_UT")[["Computers_All Schools","Electricity_All Schools","Water_All Schools","Boys_toilet_All Schools","Girls_Toilet_All Schools"]].mean()
        top = top.assign(Overall=top.mean(axis=1)).sort_values("Overall", ascending=False).head(10).drop(columns="Overall")
        fig = px.imshow(top, text_auto=True, aspect="auto", title="Top 10 States Infrastructure Heatmap (Average of All Years)")
        fig.update_layout(paper_bgcolor="white",plot_bgcolor="white",margin=dict(l=20,r=20,t=60,b=20),shapes=[dict(type="rect",xref="paper",yref="paper",x0=0,y0=0,x1=1,y1=1,line=dict(color="#2563EB",width=2),fillcolor="rgba(0,0,0,0)")])
        st.plotly_chart(fig, use_container_width=True)

        sun = df3.assign(Overall=df3[["Computers_All Schools","Electricity_All Schools","Water_All Schools","Boys_toilet_All Schools","Girls_Toilet_All Schools"]].mean(axis=1))
        fig = px.sunburst(sun, path=["State_UT","year"], values="Overall", hover_data=["Computers_All Schools","Electricity_All Schools","Water_All Schools","Boys_toilet_All Schools","Girls_Toilet_All Schools"],title="Infrastructure Distribution by State and Year")
        fig.update_layout(width=600, height=600)
        fig.update_layout(paper_bgcolor="white",plot_bgcolor="white",margin=dict(l=20,r=20,t=60,b=20),shapes=[dict(type="rect",xref="paper",yref="paper",x0=0,y0=0,x1=1,y1=1,line=dict(color="#2563EB",width=2),fillcolor="rgba(0,0,0,0)")])
        st.plotly_chart(fig, use_container_width=True)

       


elif menu=="⚖️ Camparative analysis":   
    st.markdown("<div class='section-header'>📊 Infrastructure Score vs Overall Dropout</div>",unsafe_allow_html=True)  
    # df["Overall_Dropout"]=df[["Primary_Total_Dropout","Upper Primary_Total","Secondary _Total","HrSecondary_Total"]].mean(axis=1)
    # df["Overall_GER"]=df[["Primary_Total_GER","Upper_Primary_Total","Secondary_Total","Higher_Secondary_Total"]].mean(axis=1)
    # df["Infrastructure_Score"]=df[["Electricity_All Schools","Water_All Schools","Boys_toilet_All Schools","Girls_Toilet_All Schools","Computers_All Schools"]].mean(axis=1)
    # st.markdown("<div class='graph-box'>",unsafe_allow_html=True)
  
    df["Overall_Dropout"]=df[["Primary_Total_Dropout","Upper Primary_Total","Secondary_Total","HrSecondary_Total"]].mean(axis=1)
    df["Overall_GER"]=df[["Primary_Total_GER","Upper_Primary_Total","Secondary_Total","Higher_Secondary_Total"]].mean(axis=1)
    df["Infrastructure_Score"]=df[["Electricity_All Schools","Water_All Schools","Computers_All Schools","Boys_toilet_All Schools","Girls_Toilet_All Schools"]].mean(axis=1)
    
    year=st.sidebar.selectbox("Year",sorted(df["year"].unique()))
    df1=df[df["year"]==year]

    fig=px.scatter(df,x="Infrastructure_Score",y="Overall_Dropout",color="Overall_Dropout",hover_name="State_UT",hover_data=["year","Overall_GER"],color_continuous_scale="RdYlGn_r")
    fig.update_layout(title="Infrastructure Score vs Overall Dropout",title_x=0.5,height=600,plot_bgcolor="white",paper_bgcolor="white",font=dict(size=15))
    st.plotly_chart(fig,use_container_width=True)
    st.markdown("</div>",unsafe_allow_html=True)

    st.markdown("<div class='section-header'>🫧 Gross Enrollment vs Dropout (Bubble Chart)</div>",unsafe_allow_html=True)
    st.markdown("<div class='graph-box'>",unsafe_allow_html=True)
    fig=px.scatter(df,x="Overall_GER",y="Overall_Dropout",size="Infrastructure_Score",color="Infrastructure_Score",hover_name="State_UT",hover_data=["year"],color_continuous_scale="Blues",size_max=35)
    fig.update_layout(title="Gross Enrollment vs Overall Dropout",title_x=0.5,height=600,plot_bgcolor="white",paper_bgcolor="white",xaxis_title="Overall Gross Enrollment (%)",yaxis_title="Overall Dropout Rate (%)")
    st.plotly_chart(fig,use_container_width=True,config={"displayModeBar":False})
    st.markdown("</div>",unsafe_allow_html=True)

    st.markdown("<div class='section-header'>📊 Top 10 States Comparison</div>",unsafe_allow_html=True)
    st.markdown("<div class='graph-box'>",unsafe_allow_html=True)
    
    
    top10=df1.sort_values("Infrastructure_Score",ascending=False).head(10)
    fig=px.bar(top10,x="State_UT",y=["Infrastructure_Score","Overall_GER","Overall_Dropout"],barmode="group",color_discrete_sequence=["#001f54","#2E86DE","#E74C3C"])
    fig.update_layout(title="Top 10 States Based on Infrastructure Score",title_x=0.5,height=600,xaxis_title="State",yaxis_title="Value",plot_bgcolor="white",paper_bgcolor="white",legend_title="Indicators")
    st.plotly_chart(fig,use_container_width=True,config={"displayModeBar":False})
    st.markdown("</div>",unsafe_allow_html=True)

    st.markdown("<div class='section-header'>📦 Infrastructure Category vs Overall Dropout</div>",unsafe_allow_html=True)    
    df["Category"]=pd.qcut(df["Infrastructure_Score"],3,labels=["Low","Medium","High"])
    fig=px.box(df,x="Category",y="Overall_Dropout",color="Category")
    fig.update_layout(title="Overall Dropout by Infrastructure Category",title_x=0.5,height=550)
    st.plotly_chart(fig,use_container_width=True,config={"displayModeBar":False})

    st.markdown("<div class='section-header'>📊 Distribution of Infrastructure Score</div>",unsafe_allow_html=True)
    fig=px.histogram(df1,x="Infrastructure_Score",nbins=10,color="Infrastructure_Score")
    fig.update_layout(title="Infrastructure Score Distribution",title_x=0.5,height=550)
    st.plotly_chart(fig,use_container_width=True,config={"displayModeBar":False})

    st.markdown("<div class='section-header'>🌡️ Correlation Heatmap</div>",unsafe_allow_html=True)
    corr=df[["Overall_Dropout","Overall_GER","Infrastructure_Score"]].corr()
    fig=px.imshow(corr,text_auto=".2f",color_continuous_scale="RdBu_r",aspect="auto")
    fig.update_layout(title="Correlation Between Overall Dropout, GER and Infrastructure Score",title_x=0.5,height=500)
    st.plotly_chart(fig,use_container_width=True,config={"displayModeBar":False})

elif menu=="🔬 Key Insights":
    st.title("🔬 Key Insights")
    drop = df1.assign(Overall_Dropout=df1[["Primary_Total","Upper Primary_Total","Secondary _Total","HrSecondary_Total"]].mean(axis=1))
    highest_dropout = drop.groupby("State_UT")["Overall_Dropout"].mean().idxmax()
    lowest_dropout = drop.groupby("State_UT")["Overall_Dropout"].mean().idxmin()

    ger = df2.assign(Overall_GER=df2[["Primary_Total","Upper_Primary_Total","Secondary_Total","Higher_Secondary_Total"]].mean(axis=1))
    highest_ger = ger.groupby("State_UT")["Overall_GER"].mean().idxmax()
    lowest_ger = ger.groupby("State_UT")["Overall_GER"].mean().idxmin()

    infra = df3.assign(Overall_Infrastructure=df3[["Computers_All Schools","Electricity_All Schools","Water_All Schools","Boys_toilet_All Schools","Girls_Toilet_All Schools"]].mean(axis=1))
    best_state = infra.groupby("State_UT")["Overall_Infrastructure"].mean().idxmax()
    worst_state = infra.groupby("State_UT")["Overall_Infrastructure"].mean().idxmin()

    st.title("Dropout")
    st.markdown(f"<div class='box'>📈 <b>Highest Overall Dropout Rate:</b> {highest_dropout}</div>",unsafe_allow_html=True)
    st.markdown(f"<div class='box'>📉 <b>Lowest Overall Dropout Rate:</b> {lowest_dropout}</div>",unsafe_allow_html=True)
    st.markdown("<div class='box'>📌 Dropout rates are generally lower at the Primary level and increase at Secondary and Higher Secondary levels.</div>",unsafe_allow_html=True)
    st.markdown("<div class='box'>📌 Some states consistently recorded higher dropout rates across multiple years.</div>",unsafe_allow_html=True)
    st.markdown("<div class='box'>📌 Boys and girls show similar dropout patterns in most states.</div>",unsafe_allow_html=True)
    st.markdown("<div class='box'>📌 Several states have shown gradual improvement in reducing dropout rates over the years.</div>",unsafe_allow_html=True)
        
    st.title("Gross enrollment")
    st.markdown(f"<div class='box'>🏆 <b>Highest Overall Gross Enrollment Rate:</b> {highest_ger}</div>",unsafe_allow_html=True)
    st.markdown(f"<div class='box'>📉 <b>Lowest Overall Gross Enrollment Rate:</b> {lowest_ger}</div>",unsafe_allow_html=True)
    st.markdown("<div class='box'>📌 Primary education has the highest Gross Enrollment Rate among all education levels.</div>",unsafe_allow_html=True)
    st.markdown("<div class='box'>📌 Gross Enrollment Rate gradually decreases from Primary to Higher Secondary.</div>",unsafe_allow_html=True)
    st.markdown("<div class='box'>📌 Boys and girls have similar enrollment patterns in most states.</div>",unsafe_allow_html=True)
    st.markdown("<div class='box'>📌 Many states maintained consistently high enrollment rates across the three years.</div>",unsafe_allow_html=True)
        
    st.title("Infrastructure")
    st.markdown(f"<div class='box'>🏆 <b>Best Overall Infrastructure:</b> {best_state}</div>",unsafe_allow_html=True)
    st.markdown(f"<div class='box'>⚠ <b>Lowest Overall Infrastructure:</b> {worst_state}</div>",unsafe_allow_html=True)
    st.markdown("<div class='box'>📌 Electricity and drinking water facilities are available in most schools.</div>",unsafe_allow_html=True)
    st.markdown("<div class='box'>📌 Computer availability is comparatively lower than other infrastructure facilities.</div>",unsafe_allow_html=True)
    st.markdown("<div class='box'>📌 Availability of boys' and girls' toilets has improved over the years.</div>",unsafe_allow_html=True)
    st.markdown("<div class='box'>📌 Some states consistently performed better in providing school infrastructure across all three years.</div>",unsafe_allow_html=True)  
