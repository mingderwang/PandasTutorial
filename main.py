import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])
#print(s)

california_housing_dataframe = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")
print(california_housing_dataframe.describe())
#california_housing_dataframe('longitude')

import matplotlib.pyplot as plt
plt.plot([1,2,3])
plt.show()