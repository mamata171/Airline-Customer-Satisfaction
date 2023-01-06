import streamlit as st
import pickle

pickle_in = open('classifier.pkl',"rb")
classifier1 = pickle.load(pickle_in)

st.title("Airline Customer Satisfaction")

def Prediction(customer_Type,On_board_service,Age,Leg_room_service,Flight_Distance,
                Ease_of_Online_booking,Inflight_entertainment,Class,
                Type_of_Travel,Online_boarding):
    
    if customer_Type == "Loyal Customer":
        customer_Type = 0
    else :
        customer_Type = 1

    if Class == "Bussiness":
        Class = 0
    elif Class == "Eco":
        Class = 1
    else:
        Class = 2

    if Type_of_Travel == "Business travel":
        Type_of_Travel = 0
    else :
        Type_of_Travel = 1



    
    prediction = classifier1.predict([[customer_Type,On_board_service,Age,
                    Leg_room_service,Flight_Distance,Ease_of_Online_booking,
                    Inflight_entertainment,Class,Type_of_Travel,Online_boarding]])
    return prediction

def main():
    col1,col2 = st.columns(2)

    with col1:
        customer_Type = st.selectbox("Select Type of customer", ('Loyal Customer','disloyal Customer')) 
        On_board_service = st.text_input('Enter rating for board service(5-high 1-least)')
        Age = st.text_input("Enter Age of customer")
        Leg_room_service = st.text_input("Enter rating for Leg Room service Rating(5-high 1-least)")
        Flight_Distance = st.text_input("Enter the flight distance")
    with col2:
        Ease_of_Online_booking = st.text_input("Enter Rating for ease of online booking(5-high 1-least)")
        Inflight_entertainment = st.text_input("Enter Rating for Inflight entertainment(5-high 1-least)")
        Class = st.selectbox("Select Type class of customer", ('Bussiness','Eco',"Eco Plus")) 
        Type_of_Travel = st.selectbox("Select type of travel of customer",('Bussiness Travel','Personal Travel'))
        Online_boarding = st.text_input("Enter Rating for online boarding(5-high 1-least)")

    result = ""
    if st.button("Predict"):
        result = Prediction(customer_Type,On_board_service,Age,Leg_room_service,Flight_Distance,
                Ease_of_Online_booking,Inflight_entertainment,Class,
                Type_of_Travel,Online_boarding)

        if result==0:
            st.success('Customer is neutral or dissatisfied'.format(result))

        else:
            st.success('Customer is satisfied'.format(result))

if __name__ == "__main__":
    main()
