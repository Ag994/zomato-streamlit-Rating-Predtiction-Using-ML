import streamlit as st

import numpy as np
import pandas as pd
import joblib 

model= joblib.load('modelA.joblip')

st.title('How They Rate :pizza:')

online_order= st.selectbox('online order option',('Yes','No'))
book_table= st.selectbox('Book table option',('Yes','No'))
votes= st.number_input('how many votes the resturant have',0)
cuisines= st.selectbox('what type cuisines the resturant serve',('Indian','Italian','Desserts','Chinese',
                                                                    'Thai','fastfood','other'))
type= st.selectbox('what type of the resturant',('Buffet','Cafes','Delivery','Desserts',
                                                 'Bars','Drinks & nightlife','Dine_out'))
review= st.select_slider('the rate of review from 1 to 5',[1,2,3,4,5])
num_of_serving_area= st.select_slider('how many area the resturant serveing',[1,2])
correct_address= st.selectbox('Does the resturant have the right address',('correct','false'))
approx_cost_for_one= st.number_input('approx cost for one',0)

columns= ['online_order', 'book_table', 'votes', 'cuisines', 'type', 'review',
          'num_of_serving_area', 'correct_address', 'approx_cost_for_one']

def predict():
    col= np.array([online_order,book_table,votes,cuisines,type,review,num_of_serving_area,correct_address,approx_cost_for_one])
    data= pd.DataFrame([col], columns=columns)
    prediction= model.predict(data)[0]

    if prediction == 1:
        st.success('High Rated Resturant:thumbsup:')
    else:
        st.error('Low Rated Resturant:thumbsdown:')


st.button('Predict', on_click=predict)






