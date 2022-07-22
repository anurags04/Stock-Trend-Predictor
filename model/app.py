import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
import datetime as date
from keras.models import load_model
import streamlit as st
from sklearn.preprocessing import MinMaxScaler

st.title('Stock Trend Predictor')
ticker = st.text_input('Enter Stock Ticker', 'EICHERMOT.NS')
ticker.upper()

start = '2001-01-01'
last = date.datetime.today() - date.timedelta(days=1)
year = last.strftime("%Y")
month = last.strftime("%m")
day = last.strftime("%d")
end = year + "-" + month + "-" + day

df = data.DataReader(ticker, 'yahoo', start, end)

st.subheader('Data from 2001 - ' + year + "/"+ month + "/" + day)
st.write(df.describe())

st.subheader('Closing Price vs Time')
fig = plt.figure(figsize = (12,6))
plt.plot(df.Close, 'b')
st.pyplot(fig)

st.subheader('Closing Price vs Time with 100 MA')
ma_hundred = df.Close.rolling(100).mean()
fig = plt.figure(figsize = (12,6))
plt.plot(ma_hundred, 'r')
plt.plot(df.Close, 'b')
st.pyplot(fig)

st.subheader('Closing Price vs Time with 100 MA & 200 MA')
ma_twoh = df.Close.rolling(200).mean()
ma_hundred = df.Close.rolling(100).mean()
fig = plt.figure(figsize = (12,6))
plt.plot(ma_hundred, 'r')
plt.plot(ma_twoh, 'g')
plt.plot(df.Close, 'b')
st.pyplot(fig)

train_set = pd.DataFrame(df['Close'][0:int(len(df) * 0.80)])
test_set = pd.DataFrame(df['Close'][int(len(df) * 0.80): int (len(df))])

scaler = MinMaxScaler(feature_range = (0, 1))

train_list = scaler.fit_transform(train_set)

model = load_model('stocks_model.h5')

temp = train_set.tail(100)
test_final = temp.append(test_set, ignore_index = True)

input2 = scaler.fit_transform(test_final)

x_test = []
y_test = []

for i in range(100, input2.shape[0]):
    x_test.append(input2[i-100: i])
    y_test.append(input2[i, 0])

x_test, y_test = np.array(x_test), np.array(y_test)

y_predict = model.predict(x_test)

scale_factor = 1/(scaler.scale_[0])
scale_factor

y_predict *= scale_factor
y_test *= scale_factor

st.subheader('Prediction vs Original')
fig2 = plt.figure(figsize=(12,6))
plt.plot(y_test, 'b', label = 'Stock Price')
plt.plot(y_predict, 'r', label = 'Predicted Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
st.pyplot(fig2)

count = 0
lim = df['Close'].iloc[-1]
lim /=10

for i in range (0, len(y_test)):
    if(abs(y_test[i] - y_predict[i]) <= lim):
        count += 1
        
head = "Accuracy of stock prices within " + str(round(lim, 0))
st.header(head)
st.subheader(round((count/len(y_test) * 100), 3))