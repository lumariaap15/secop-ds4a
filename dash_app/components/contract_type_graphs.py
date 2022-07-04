from dataframes.data import df2

import plotly.express as px

df = df2.groupby(['Tipo de Contrato']).size().reset_index(name='counts')

contract_type_count_pie_chart = px.pie(df, values='counts', names='Tipo de Contrato')

contract_type_count_pie_chart.update_traces(textposition = 'inside' , textinfo = 'label', showlegend=False)