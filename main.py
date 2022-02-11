import streamlit as st
import pickle
from sklearn.preprocessing import  StandardScaler
model= loaded_model = pickle.load(open("noscaled_house_prize_simple_lin_reg.pkl", 'rb'))
st.title("house price pridiction")

def predict_price(tra_date,house_age,dst_mrt,con_stores,latitude,longitude):


    prediction=model.predict([[tra_date,house_age,dst_mrt,con_stores,latitude,longitude]])
    return  prediction

def main():

    tra_date=st.number_input("transaction date")
    house_age=st.number_input("House age")
    dst_mrt=st.number_input("distance to the nearest MRT station")
    con_stores=st.number_input("number of convenience stores")
    latitude=st.number_input("latitude")
    longitude=st.number_input("longitude")
    result=""
    btn=st.button("pridict")
    if btn:
        result=predict_price(tra_date,house_age,dst_mrt,con_stores,latitude,longitude)
    st.success(f"The output is={result} ")

if __name__ == '__main__':
    main()