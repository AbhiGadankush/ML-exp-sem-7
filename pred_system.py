import numpy as np
import pickle

loaded_model = pickle.load(open('C:/Users/ABHISHEK/Music/Coding/House pred trained_model (1).sav', 'rb'))

input_data =[-122.23,37.88,41,880,129,322,126,8.3252]

input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print('Price of the house: ', prediction[0])