import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("/kaggle/input/gdp-of-all-countries19602020/gdp_1960_2020.csv")

df.head()

subset = df[df['country'].isin(["Malaysia"])]

subset.head()

subset.tail()

px.bar(subset, x="year", y= "gdp")

px.scatter(subset, x="year",y="gdp")

plt.scatter(subset ['year'],subset ['gdp'])

subset_2020 = df[df['year'].isin([2020])]

subset_2020_Asia = subset_2020[subset_2020['state'].isin(["Asia"])]
subset_2020_Africa = subset_2020[subset_2020['state'].isin(["Africa"])]
subset_2020_America = subset_2020[subset_2020['state'].isin(["America"])]
subset_2020_Europe = subset_2020[subset_2020['state'].isin(["Europe"])]
subset_2020_Oceania = subset_2020[subset_2020['state'].isin(["Oceania"])]

pie_data = [sum(subset_2020_Asia['gdp']),sum(subset_2020_Africa['gdp']),sum(subset_2020_America['gdp']),
            sum(subset_2020_Europe['gdp']),sum(subset_2020_Oceania['gdp'])];

mylabels = ["Asia", "Africa", "America", "Europe","Oceania"]
plt.pie(pie_data, labels = mylabels)

pie_df = {'Continent': mylabels,
        'GDP': pie_data}

px.pie(pie_df,values="GDP",names="Continent")

