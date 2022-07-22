# Stock-Trend-Predictor
I have created this Python model which can be used to predict stock trends. The data used is from 1 January 2001 till the previous day the app is run on the system. Like i have run the app on 22nd July 2022, the model will take data from 1st Jan 2001 till 21st July 2002. 
To run the app on your local machine simply enyter the command "streamlit run app.py" in termnal(without the inverted commas).
I have used EICHERMOT.NS as the default ticker. You can predict the stocks of various companies, simply enter the ticker and run.
Also, the accuracy measured in on the basis of the current stock closing price and the predicted value about that. The distribution is taken as absolute difference of the actual stock price and the predicted stock price and if the difference is lessa than 1/10th of the closing price, prediction is considered true.
That's it. Have a nice day!!
Thank You :)
