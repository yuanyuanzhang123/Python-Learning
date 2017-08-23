#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/23 19:38
# @Author  : Zhangyuanyuan
# @Site    : 
# @File    : linear_regression.py
# @Software: PyCharm Community Edition

import pandas
from sklearn.linear_model import LinearRegression

bmi_life_data = pandas.read_csv('bmi_and_life_expectancy.csv')
#print(bmi_life_data.head())
model = LinearRegression()
model.fit(bmi_life_data[['BMI']],bmi_life_data[['Life expectancy']])

#predict
bmi = 21.07931
predict_life =  model.predict(bmi)
print("BMI:%f predict life expectancy:%d"%(bmi,predict_life))
