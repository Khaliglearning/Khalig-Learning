import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn import metrics
from fbprophet import Prophet
from fbprophet.plot import add_changepoints_to_plot
from fbprophet.plot import plot_cross_validation_metric
from fbprophet.diagnostics import performance_metrics
from fbprophet.diagnostics import cross_validation


df = pd.read_csv("dados.csv")
df.rename(columns={'DT_MEDICAO':'ds', 'TEM_INS':'y'},inplace=True)
df


del df['HR_MEDICAO']
del df['UMD_INS']
del df['Unnamed: 0']
del df['VEN_VEL']


df


temperatura = df['y']
temperatura
data = df['ds']
data


temperatura.plot()


train_set = df.iloc[:-4759]
test_set = df.iloc[:-4000]


model_mensal = Prophet()


model_mensal.fit(train_set)


y_pred = model_mensal.predict(test_set)


y_pred


model_mensal.plot(y_pred)


y_pred['yhat'].values


print('MAE: {}'.format(metrics.mean_absolute_error(test_set['y'].values, y_pred['yhat'].values)))
print('RMSE: {}'.format(metrics.mean_squared_error(test_set['y'].values, y_pred['yhat'].values, squared=False)))


components_mensal = model_mensal.plot_components(y_pred)
components_mensal


df_cv = cross_validation(model_mensal, horizon = '25 days')


df_cv


regression_report = performance_metrics (df_cv)


regression_report


fig = plot_cross_validation_metric(df_cv, metric='rmse')
