import streamlit as st
import pandas as pd
import geopandas as gpd
import numpy as np
import altair as alt
import pydeck as pdk
#import geopandas as gpd
from datetime import datetime
from datetime import time
from streamlit_folium import st_folium 
import folium as fo
import plotly.graph_objects as go
from datetime import date, timedelta   
import streamlit.components.v1 as components
import folium as fo
import random
import geopandas as gpd
from shapely.geometry import Polygon, Point

st.set_page_config(layout="wide")

col1_1 , col2_1 = st.columns((1,4))
with col2_1 :
     st.write("""
      # Aonic Operation Analysis Platform
     """)

@st.cache(allow_output_mutation=True)

def generate_chart(data,head) :
    fig = go.Figure(data=go.Scatterpolar(
          r=data.y,
          theta=data.x,
          fill='toself'))
    fig.update_layout( polar=dict(
            radialaxis=dict(
             visible=True
              ),
          ),
          showlegend=False
          )
    fig.update_layout(autosize=False,width=400,height=400,)
    return fig


def Mist_perf_chart(row) :
    data = pd.DataFrame({
        'x': ['Meet the customer needs', 'Working speed', 'Spraying performance', 'User friendly', 'Safety','variety of applications'],
        'y': [row["สามารถตอบโจทย์ความต้องการของลูกค้า"],row["ความรวดเร็วในการทำงาน"], row["ประสิทธิภาพการพ่น"], row["ง่ายต่อการใช้งานและการควบคุม"], 
              row["ความปลอดภัยในการทำงาน"],row["การใช้งานที่หลากหลาย พ่นปุ๋ย สารเคมี ยาฆ่าแมลง"]]
    })
    # Create bar chart
    chart = generate_chart(data,"Mist Product Performance")

    return chart

def Mist_factor_chart(row) :
    data = pd.DataFrame({
        'x': ['Price', 'Drone Performance', 'Spraying performance', 'User friendly', 'Safety','Giveaway','Brand image','Aftersale Service'],
        'y': [row["ราคา"],row["ประสิทธิภาพของโดรน"], row["ประสิทธิภาพการพ่น2"], row["ความง่ายต่อการใช้งาน"], 
              row["ความปลอดภัยในการทำงาน2"],row["การมีของแถม"],row["แบรนด์"],row["บริการหลังการขาย"]]
    })
    # Create bar chart
    chart = generate_chart(data,"Factor of purchasing Mist drones")

    return chart

def DJI_perf_chart(row) :
    data = pd.DataFrame({
        'x': ['Meet the customer needs', 'Working speed', 'drone performance', 'User friendly', 'camera quality','Controlling','Safety','variety of applications','Drone Accuracy / Precision'],
        'y': [row["สามารถตอบโจทย์ความต้องการของลูกค้า2"],row["ความรวดเร็วในการทำงาน2"], row["ประสิทธิภาพการทำงาน"], row["ง่ายต่อการใช้งาน"],row["คุณภาพของกล้อง"],row["การควบคุมโดรน"],
              row["ความปลอดภัยในการทำงาน3"],row["สามารถไปประยุกต์ใช้งานได้หลากหลาย"],row["ความแม่นยำของโดรน"]]
    })
    # Create bar chart
    chart = generate_chart(data,"DJI product Performance")

    return chart

def DJI_factor_chart(row) :
    data = pd.DataFrame({
        'x': ['Price', 'Drone Performance', 'Camera performance', 'User friendly', 'Safety','Giveaway','Brand image','Aftersale Service'],
        'y': [row["ราคา2"],row["ประสิทธิภาพของโดรน2"], row["ประสิทธิภาพของกล้อง"], row["ความง่ายต่อการใช้งาน2"], 
              row["ความปลอดภัยในการทำงาน4"],row["การมีของแถม2"],row["แบรนด์2"],row["บริการหลังการขาย2"]]
    })
    # Create bar chart
    chart = generate_chart(data,"Factor of purchasing DJI product")

    return chart

def Emlid_perf_chart(row) :
    data = pd.DataFrame({
        'x': ['Meet the customer needs', 'Working speed', 'performance', 'User friendly', 'Accuracy','How easy using with drones','variety of applications','Emlid Flow Application'],
        'y': [row["สามารถตอบโจทย์ความต้องการของลูกค้า3"],row["ความรวดเร็วในการทำงาน3"], row["ประสิทธิภาพการทำงาน2"], row["ง่ายต่อการใช้งาน2"],row["ความแม่นยำของอุปกรณ์"],row["ใช้งานร่วมกับโดรนได้ง่าย"],
              row["สามารถไปประยุกต์ใช้งานได้หลากหลาย2"],row["การควบคุมอุปกรณ์โดยใช้โทรศัพท์มือถือ"]]
    })
    # Create bar chart
    chart = generate_chart(data,"Emlid Performance")

    return chart

def Emlid_factor_chart(row) :
    data = pd.DataFrame({
        'x': ['Price', 'Able to do various methods (RTK,PPK,PPP,Static)', 'Accuracy', 'User friendly','Giveaway','Brand image','Aftersale Service','Emlid Flow App'],
        'y': [row["ราคา3"],row["รองรับการทำงานที่หลากหลาย RTK , PPK , Static , PPP"], row["ความแม่นยำ"], row["ความง่ายต่อการใช้งาน3"]
              ,row["การมีของแถม2"],row["แบรนด์2"],row["บริการหลังการขาย2"],row["การควบคุมอุปกรณ์โดยใช้โทรศัพท์มือถือ2"]]
    })
    # Create bar chart
    chart = generate_chart(data,"Factor of purchasing Emlid product")

    return chart

def Training_perf_chart(row) :
    data = pd.DataFrame({
        'x': ['Meet the customer needs', 'Course content', 'Time Slot , Agenda', 'Course materials', 'Knowledge of speakers','listeners understand easily.','Able to apply knowledge'],
        'y': [row["สามารถตอบโจทย์ความต้องการของลูกค้า4"],row["เนื้อหาเหมาะสม เข้าใจง่าย"], row["การจัดการเวลา"], row["สื่อการสอน รูปแบบการสอน"],row["ความรู้ความสามารถของวิทยากร"],row["วิทยากรสามารถสื่อสารให้ผู้ฟังเข้าใจได้ง่าย"],
              row["สามารถนำความรู้จากการสอนไปประยุกต์ใช้งานไดจริง"]]
    })
    # Create bar chart
    chart = generate_chart(data,"Training Course")

    return chart

def Training_factor_chart(row) :
    data = pd.DataFrame({
        'x': ['Price', 'Knowledge of speakers', 'Company profile', 'Professional of staff','Course Material'],
        'y': [row["ราคา4"],row["ความรู้ความสามารถของวิทยากร2"], row["ประวัติของบริษัท"], row["ความเป็นมืออาชีพ"]
              ,row["อุปกรณ์ที่ใช้ในการสอน"]]
    })
    # Create bar chart
    chart = generate_chart(data,"Factor of purchasing Training Course")

    return chart

def Service_chart(row) :

    data = pd.DataFrame({
        'x': ['Dress appropriately.', 'punctuality', 'Knowledge of Staff', 'meet the customers needs.'],
        'y': [row["การแต่งกายสุภาพเรียบร้อย"],row["ความตรงต่อเวลา"], row["ความรู้ความสามารถและความเชี่ยวชาญของพนักงาน"], row["การบริการของพนักงานสามารถตอบโจทย์ความต้องการของลูกค้าได้"]]
    })
    chart = generate_chart(data,"Service rating of our staff")

    return chart

def generate_pdf():
    pdf_file = "report.pdf"
    with open(pdf_file, "wb") as f:
        c = canvas.Canvas(f)
        c.drawString(72, 720, "Hello, world!")
        c.save()
    return pdf_file

def random_point_in_polygon(polygon):
    minx, miny, maxx, maxy = polygon.bounds
    while True:
        x = random.uniform(minx, maxx)
        y = random.uniform(miny, maxy)
        point = Point(x, y)
        if polygon.contains(point):
            return point

def generate_map(df) :
    map = fo.Map(location = [13.75, 100.50], zoom_start = 6 )
    th_poly = gpd.read_file("https://data.opendevelopmentmekong.net/th/dataset/8f3fa1b8-cb5c-48c8-9fd7-d3c213ea23db/resource/1559cee4-fedc-4330-be9c-d8cf3dd75015/download/tha_admbnda_adm1_rtsd_20190221.zip")
    th_poly["ADM1_EN"] = th_poly["ADM1_EN"].str.replace("Chon Buri","Chonburi")
    #cen = th_poly["geometry"].centroid ; lat = cen.y ; lon = cen.x

    for _, row in th_poly.iterrows(): 
      sim_geo = gpd.GeoSeries(row['geometry']).simplify(tolerance=0.001)
      geo_j = sim_geo.to_json()
      geo_j = fo.GeoJson(data=geo_j,style_function=lambda x: {'fillColor': 'red','color': 'red','opacity': 0.5})
      fo.Popup(row['ADM1_EN']).add_to(geo_j)
      geo_j.add_to(map)

    gdf = pd.DataFrame()
    gdf["geometry"] = th_poly["geometry"]
    gdf["Province"] = th_poly["ADM1_EN"]
    merged_df = pd.merge(df, gdf, on='Province')
    merged_df['Point'] = merged_df['geometry'].apply(lambda x: random_point_in_polygon(x))

    for i,row in merged_df.iterrows() : 
      lat = row["Point"].y
      lon = row["Point"].x
      fo.Marker(location=[lat, lon],popup=fo.Popup('ID: {} <br> Date: {} <br> Product: {} <br> Service: {} <br> Customer: {} <br> Location: {}'.format(row['ops_id'],row['Date'],row['Product'],row['Service Type2'], row['Client / Customer'],row['Location']),max_width=200)
        ,icon=fo.Icon(color="gray", icon="info-sign"),).add_to(map)
      sim_geo = gpd.GeoSeries(row['geometry']).simplify(tolerance=0.001)
      geo_j = sim_geo.to_json()
      geo_j = fo.GeoJson(data=geo_j,style_function=lambda x: {'fillColor': 'red','color': 'red','opacity': 0.5})
      geo_j.add_to(map)

    return map

def find_branch(row) :
    BKK = ["Ton", "Punch", "Ned"]
    PTH = ["Kong","Boy"]
    KKC = ["Gatang","Benz","Nuch"]
    branch = list()
    if any(i in row for i in BKK):
      branch.append("BKK")
    if any(i in row for i in PTH):
      branch.append("PTH")
    if any(i in row for i in KKC):
      branch.append("KKC")
    a = ""
    for i in branch :
        a += str(i)+" ; "
    return str(a)

def filter(file) :
    df = file
    df['DJI Enterprise'] = df['DJI Enterprise'].str.replace('No;','') ; df['DJI Enterprise'] = df['DJI Enterprise'].str.replace(';','  ')
    df['Mist Drone'] = df['Mist Drone'].str.replace('No;','') ; df['Mist Drone'] = df['Mist Drone'].str.replace(';','')
    df['Software'] = df['Software'].str.replace('No;','') ; df['Software'] = df['Software'].str.replace(';','')
    df['Emlid GNSS'] = df['Emlid GNSS'].str.replace('No;','') ; df['Emlid GNSS'] = df['Emlid GNSS'].str.replace(';','')
    df['Team member'] = df['Team member'].str.replace(';',' / ')
    df['Service Type2'] = df['Service Type2'].str.replace(';','  ')
    return df

def first_filter(file) :
    df = file[['Date', 'Province', 'Client / Customer',
       'Description', 'Team member','Service Type2', 'Remark',
       'Mist Drone', 'DJI Enterprise','Emlid GNSS', 'Software']]
    df = filter(df)
    return df

def addprov(data) :
    Prov_ls = list(['Bangkok','Amnat Charoen','Ang Thong','Bueng Kan','Buriram','Chachoengsao','Chai Nat','Chaiyaphum','Chanthaburi',
  'Chiang Mai','Chiang Rai','Chonburi','Chumphon','Kalasin','Kamphaeng Phet','Kanchanaburi','Khon Kaen','Krabi','Lampang','Lamphun',
  'Loei','Lopburi','Mae Hong Son','Maha Sarakham','Mukdahan','Nakhon Nayok','Nakhon Pathom','Nakhon Phanom','Nakhon Ratchasima',
  'Nakhon Sawan','Nakhon Si Thammarat','Nan','Narathiwat','Nong Bua Lamphu','Nong Khai','Nonthaburi','Pathum Thani','Pattani','Phang Nga',
  'Phatthalung','Phayao','Phetchabun','Phetchaburi','Phichit','Phitsanulok','Phra Nakhon Si Ayutthaya','Phrae','Phuket','Prachinburi',
  'Prachuap Khiri Khan','Ranong','Ratchaburi','Rayong','Roi Et','Sa Kaeo','Sakon Nakhon','Samut Prakan','Samut Sakhon','Samut Songkhram',
  'Sara buri','Satun','SingBuri','Sisaket','Songkhla','Sukhothai','Suphan Buri','Surat Thani','Surin','Tak','Trang','Trat',
  'Ubon Ratchathani','Udon Thani','Uthai Thani','Uttaradit','Yala','Yasothon'])
    for i,row in data.iterrows() :
        Prov_ls.append(str(row["Province"]))
    result = [] 
    for i in Prov_ls : 
      if i not in result: 
        result.append(i)
    return result

def addteam(data) :
    Team_mem = list(['Punch','Ned','Ton','Bass','Boy','Kong','Gatang','Benz'])
    for i,row in data.iterrows() :
        Team_mem.append(str(row["Team member"]))
    result = [] 
    for i in Team_mem : 
      if i not in result: 
        result.append(i)
    return result

Serv_list = ['Demo','Repair','Mapping Service','Spray Service','Training','Consults']

Prod_list = ['Mist Pro','Mist Max','Matrice 30 T','Matrice 300 RTK','Mavic 3 Enterprise','Mavic 3 Thermal','Phantom 4 RTK'
  ,'Phantom 4 Multispectral' , 'Mavic 2 Enterprise Advance','Zenmuse L1','Zenmuse P1','Zenmuse H20 T','Zenmuse H20 N','Emlid RS2'
  ,'Emlid RS2+','Emlid RS+','Pix4D Mapper','DJI Terra','LiDAR 360']

def customer_list(data) :
    cus_ls = list()
    for i,row in data.iterrows() :
        cus_ls.append(str(row["Client / Customer"]))
    result = [] 
    for i in cus_ls : 
      if i not in result: 
        result.append(i)
    return result

def ops_id(df) :
  ids = list()
  for i,row in df.iterrows() :
    if row.ID < 100 :
      rep_id = "TH-OPS-00"+str(row.ID)
    else :
      rep_id = "TH-OPS-0"+str(row.ID)
    ids.append(rep_id)
  df['ops_id'] = ids
  return df

Graph_list = ['Mist','DJI','Emlid','Training','Service']

url = "https://docs.google.com/spreadsheets/d/1FPd61a1anjNTP-5sWHB_XXiAwUahXgeE/edit?usp=share_link&ouid=106465555471870500346&rtpof=true&sd=true"
File = 'https://drive.google.com/uc?id=' + url.split('/')[-2]
File = r'Data/Operation Form(1-126).xlsx'
#uploaded_file = st.file_uploader("Choose a Operation Excel file")
#engine='openpyxl'

if 0 < 1 :
    #bytes_data = uploaded_file.read()
    st.write("filename: OPS-DATA")
    df = pd.read_excel(File,engine='openpyxl').sort_values(by=['Date'],ascending=False).reset_index()
    df = df.fillna("") ; #df = df.rename(columns = {"Service Type2":"Service type"}, inplace = True)
    df.Picture = df.Picture.str.replace(' ','')
    #df.Date = pd.to_datetime(df.Date).dt.date
    df['Date'] = df["Date"].dt.strftime('%d-%m-%Y')
    df.Date = pd.to_datetime(df.Date).dt.date
    df["Product"] = df['DJI Enterprise'].str.cat(df['Mist Drone'], sep = ' / ')
    df["Product"] = df["Product"].str.cat(df['Software'], sep = ' / ')
    df["Product"] = df["Product"].str.cat(df['Emlid GNSS'], sep = ' / ')
    df["Product"] = df["Product"].str.replace(';',' / ') ; df["Product"] = df["Product"].str.replace('No','') 
    df["Product"] = df["Product"].str.replace('/  /  /  /  /  /  / ','') ;df["Product"] = df["Product"].str.replace('/  /  /  /  ','') 
    df["Product"] = df["Product"].str.replace('/  /','')
    df["Service Type2"] = df["Service Type2"].str.replace(';',' / ')
    df = filter(df)
    df = ops_id(df)
    df2 = first_filter(df)
    Cust_list = customer_list(df2) ; Team_mem = addteam(df)
    Prov_list = addprov(df) ; Prod_list = Prod_list ; #Serv_list = addservice(df)

    r1col1 , r1col2 , r1col3 , r1col4  = st.columns([3,1,1,1])
    with r1col1 :
        st.write("Overall Operation Map")
        map = generate_map(df)
        st_folium(map,height=400 ,width=600)
    with r1col2 :
          today = pd.Timestamp.now()
          week_prior =  today - pd.Timedelta(weeks=1)
          df_last_week = df[df['Date'] <= week_prior]
          df_last_week = df[df['Date'] >= (pd.Timestamp.now() - pd.Timedelta(days=20))]
          r1col2.metric(label="Total Operation", value=len(df.index), delta=len(df_last_week))
    with r1col3 :
          today = date.today()
          week_prior =  today - timedelta(weeks=1) ; week_prior2 =  today - timedelta(weeks=2)
          df_last_week = df[df['Date'] < week_prior] ; df_last2_week = df[(df['Date'] < week_prior2) & (df['Date'] > week_prior)]
          r1col3.metric(label="Last Week Operation", value=len(df_last_week), delta=len(df_last2_week))

    expander = st.expander("Seach and Filter Here",expanded=True)
    col1, col2, col3, col4 = expander.columns(4)
    with col1 :
        Prov = col1.multiselect("Seach By Province", Prov_list,default=None,key="mtps")
        Day_cb = col1.checkbox("Search By Date",key="date")
        if Day_cb :
          Day = col4.date_input("Search By Date",disabled=False ,key="date2")
        else :
          Day = col4.date_input("Search By Date",disabled=True ,key="date2")

    with col2 :
        Cust = col2.multiselect("Search By Client / Customer Name", Cust_list ,key="cus")
        Team = col2.multiselect("Filter By Team member", Team_mem ,default=None,key="team")
    
    with col3 :
        Serv = col3.multiselect("Filter By Service Type", Serv_list ,default=None,key="serv")
        Prod = col3.multiselect("Filter By Product", Prod_list ,default=None,key="prod")
    
    with col4 :
        Month = col4.select_slider("Filter By Month", Serv_list ,key="month")
        
        if Prov:
            st.write("You entered: ", str(Prov))
            ck = col1.checkbox("Show all data", value=False, key="all")
        else :
            ck = col1.checkbox("Show all data", value=True, key="all")
    
    if st.session_state["all"] :
      main_df = df2
      main_df_ls = df
    else :
      main_df = pd.DataFrame()
      main_df_ls = main_df

    if st.session_state["date"] :
      main_df = df2[df.Date == Day]
      main_df_ls = df[df.Date == Day].reset_index()

    if st.session_state["mtps"] :
      main_df = df2[df.Province.isin(st.session_state["mtps"])]
      main_df_ls = df[df.Province.isin(st.session_state["mtps"])].reset_index()

    if st.session_state["cus"] :
      main_df = df2[df["Client / Customer"].isin(Cust)]
      main_df_ls = df[df["Client / Customer"].isin(Cust)].reset_index()

    if st.session_state["team"] :
      if len(Team) == 1 :
        team2 = str(Team[0])
      else :
        team2 = str(Team[0])
        for i in Team[1:] :
          team2 = team2+"|"+str(i)
      main_df = df2[df["Team member"].str.contains(team2)]
      main_df_ls = df[df["Team member"].str.contains(team2)].reset_index()

    if st.session_state["serv"] :
      if len(Serv) == 1 :
        serv2 = str(Serv[0])
      else :
        serv2 = str(Serv[0])
        for i in Serv[1:] :
          serv2 = serv2+"|"+str(i)
      st.write(serv2)
      main_df = df2.loc[df["Service Type2"].str.contains(serv2)]
      main_df_ls = df.loc[df["Service Type2"].str.contains(serv2)].reset_index()

    if st.session_state["prod"] :
      if len(Prod) == 1 :
        prod2 = str(Prod[0])
      else :
        prod2 = str(Prod[0])
        for i in Prod[1:] :
          prod2 = prod2+"|"+str(i)
      st.write(prod2)
      main_df = df2.loc[df["Product"].str.contains(prod2)]
      main_df_ls = df.loc[df["Product"].str.contains(prod2)].reset_index()

    if st.session_state["all"] :
      main_df = df2
      main_df_ls = df
    else :
      main_df = pd.DataFrame()
      main_df_ls = main_df

    st.dataframe(main_df)

    def download_pdf():
        pdf_binary_data = generate_pdf()
        with open(pdf_binary_data, "rb") as f:
              return f.read()
    
    download_pdf = '/content/drive/MyDrive/Operation_Report/TH-OPS-0017-14-11-2022.pdf'
    perf_chart = { 'Mist':Mist_perf_chart , 'DJI':DJI_perf_chart , 'Emlid':Emlid_perf_chart , 'Training':Training_perf_chart , 'Service':Service_chart}
    fact_chart = { 'Mist':Mist_factor_chart , 'DJI':DJI_factor_chart , 'Emlid':Emlid_factor_chart , 'Training':Training_factor_chart , 'Service':Service_chart}

    for i,row in main_df_ls.iterrows() :
        expander = st.expander(str(str(row.Date)+" / "+row.Province+" / "+row['Client / Customer']))
        checkbox_key_i = "Report_PDF"+str(i)
        checkbox_key2_i = "Slide_PNG"+str(i)
        Graph_key_i = "Graph"+ str(i)
        Graph2_key_i = "Graph2"+ str(i)
        col1, col2 , col3 = expander.columns([1,1,1])

        with col1 :
          chk = str(checkbox_key_i) ; chk2 = str(checkbox_key2_i)
          rep_pdf = col1.download_button("Download Report PDF",data=download_pdf ,key=chk)
          if rep_pdf :
            st.write("*** Download PDF ...")
          dft = main_df.iloc[i].T ; dft = pd.DataFrame(dft)
          c_name = dft.columns[0]
          dft.rename(columns = {c_name:'Detail'}, inplace = True)
          col1.dataframe(dft,use_container_width=True)

        with col2 :
          col2.write("Performance Graph")
          Graph = col2.selectbox("Please select Graph", Graph_list ,key=Graph_key_i)          
          fig = perf_chart[Graph](row)
          col2.write(fig)
          
        with col3 :
          col3.write("Factor Graph")   
          default_option = 'Mist'       
          Graph = col3.selectbox("Please select Graph", list(Graph) ,value=default_option,key=Graph2_key_i)          
          fig = fact_chart[Graph](row)
          col3.write(fig)
          
        expander.write("Work Description : "+str(main_df.iloc[i].Description))
        r2col1 , r2col2 , r2col3 = expander.columns(3)
        with r2col1 :
          pic = row.Picture.split(";")
          pic = list(pic)
          pic_len = len(pic)
          r2col1.image(pic,width=400)
