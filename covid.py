import streamlit as st
import requests
import pandas as pd
from datetime import date
today = date.today()
date=today.strftime("%d-%m-%Y")

st.write("""
# Check covid vaccine availability using pincode and date
""")
user_input = st.text_input("Pincode", "143001")
date_input = st.text_input("Date",str(date))
st.subheader('Data information:')


data={
    "pincode":user_input ,
    "date": date_input
}

url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"
r=requests.get(url,params=data)
data2=r.json()
data1=pd.DataFrame(data2.get("centers"))
if data1.empty:
    st.write("No center available right now at your searched place")
else:
    df={"State":[data1["state_name"][0]],"District":[data1["district_name"][0]],"Block": [data1["block_name"][0]]}
    df=pd.DataFrame.from_dict(df)
    st.write(df)
    ind=0
    for name in data1["name"]:
        data2=data1["sessions"][ind]
        d=pd.DataFrame(data2)
        d=d.drop(["session_id"],axis=1)
        d=d.drop(["slots"],axis=1)
        #d=d.drop(["allow_all_age"],axis=1)
        st.write(name)
        st.write(d)
        ind+=1
#st.write(d)
#print(r.url)