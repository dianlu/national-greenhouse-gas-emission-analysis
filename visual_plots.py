import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np

def raw_histogram(data):
    ''' 
    Overlay histogram of raw data.

    Parameter:
        data: Pandas dataframe, raw data
    Return:
        fig: Plotly figure
    '''

    fig = go.Figure()
    # Raw overlay histogram plot
    fig.add_trace(go.Histogram(x=data['Net energy consumed (GJ)'],name='Net energy consumed (GJ)'))
    fig.add_trace(go.Histogram(x=data['Total scope 1 emissions (t CO2-e)'],name='Total scope 1 emissions (t CO2-e)'))
    fig.add_trace(go.Histogram(x=data['Total scope 2 emissions (t CO2-e)'],name='Total scope 2 emissions (t CO2-e)'))
    # Overlay both histograms
    fig.update_layout(barmode='overlay')
    # Reduce opacity to see both histograms
    fig.update_traces(opacity=0.75)
    fig.update_layout(
    title_text="Distribution of Raw Data",
    xaxis=dict(
        rangeslider=dict(
            visible=True
        ),
    ))
    fig.update_layout(width=1200,height=900)
    return fig

def raw_box_plot(data):
    ''' 
    Overlay box plot of raw data.

    Parameter:
        data: Pandas dataframe, raw data
    Return:
        fig: Plotly figure
    '''
    fig = go.Figure()
    fig.add_trace(go.Box(x=data['Net energy consumed (GJ)'], name='Net energy consumed (GJ)'))
    fig.add_trace(go.Box(x=data['Total scope 1 emissions (t CO2-e)'],name='Total scope 1 emissions (t CO2-e)'))
    fig.add_trace(go.Box(x=data['Total scope 2 emissions (t CO2-e)'],name='Total scope 2 emissions (t CO2-e)'))
    fig.update_layout(
    title_text="Box Plot of Raw Data",
    xaxis=dict(
        rangeslider=dict(
            visible=True
        ),
    ))
    fig.update_layout(width=1200,height=900)
    return fig

def share_pie_plot(data):
    ''' 
    Pie plot of emission rate over consumption: total emission divided by consumption. 
    Organisations with < 30% emission rate are compressed.

    Parameter:
        data: Pandas dataframe, raw data
    Return:
        fig: Plotly figure
    '''
    data_pie=data[['Organisation name','share']]
    data_pie.loc[data_pie['share'] < 0.3, 'Organisation name'] = 'Organisations < 30% emission rate'
    fig = px.pie(data_pie, values='share', names='Organisation name', title='Least emission efficient organisation')
    fig.update_layout(width=1200,height=900)
    return fig

def total_emission_pie_plot(data):
    ''' 
    Pie plot of total emission.
    Organisations with < 3 Million total emission are compressed.

    Parameter:
        data: Pandas dataframe, raw data
    Return:
        fig: Plotly figure
    '''
    data_pie_total=data[['Organisation name','total emission']]
    data_pie_total.loc[data_pie_total['total emission'] < 3000000, 'Organisation name'] = 'Organisations with emission < 3M'
    fig = px.pie(data_pie_total, values='total emission', names='Organisation name', title='Total Emission Portions')
    fig.update_layout(width=1200,height=900)
    return fig

def net_energy_pie_plot(data):
    ''' 
    Pie plot of net energy consumption.
    Organisations with < 30 Million total consumption are compressed.

    Parameter:
        data: Pandas dataframe, raw data
    Return:
        fig: Plotly figure
    '''
    data_pie_consumption=data[['Organisation name','Net energy consumed (GJ)']]
    data_pie_consumption.loc[data_pie_consumption['Net energy consumed (GJ)'] < 30000000, 'Organisation name'] = 'Organisations with consumption < 30M'
    fig = px.pie(data_pie_consumption, values='Net energy consumed (GJ)', names='Organisation name', title='Net Energy Consumption Portions')
    fig.update_layout(width=1200,height=900)
    return fig

def scopes_scatter(data):
    ''' 
    Scatter plot of scope 1 and scope 2 emissions.

    Parameter:
        data: Pandas dataframe, raw data
    Return:
        fig: Plotly figure
    '''
    fig =px.scatter(data, x="Total scope 1 emissions (t CO2-e)", y="Total scope 2 emissions (t CO2-e)")
    fig.update_layout(
    title_text="Relationship between scope 1 and scope 2 emissions",
    xaxis=dict(
        rangeslider=dict(
            visible=True
        ),
    ))
    fig.update_layout(width=1200,height=900)
    return fig

def share_scatter(data):
    ''' 
    Scatter plot of total emission and share (energy efficiency).

    Parameter:
        data: Pandas dataframe, raw data
    Return:
        fig: Plotly figure
    '''
    fig =px.scatter(data, x="share", y="total emission")
    fig.update_layout(
    title_text="Relationship between total emission and energy efficiency",
    xaxis=dict(
        rangeslider=dict(
            visible=True
        ),
    ))
    fig.update_layout(width=1200,height=900)
    return fig

def consumption_emission_scatter(data):
    ''' 
    Scatter plot of total emission and net energy consumption.

    Parameter:
        data: Pandas dataframe, raw data
    Return:
        fig: Plotly figure
    '''
    fig =px.scatter(data, x="total emission", y="Net energy consumed (GJ)")
    fig.update_layout(
    title_text="Relationship between total emission and net energy consumption",
    xaxis=dict(
        rangeslider=dict(
            visible=True
        ),
    ))
    fig.update_layout(width=1200,height=900)
    return fig

def emission_heatmap(data):
    ''' 
    Heatmap plot of top 9 emissions.

    Parameter:
        data: Pandas dataframe, raw data
    Return:
        fig: Plotly figure
    '''
    sorted_data = data.sort_values('total emission', ascending=False)
    top_9 = sorted_data.head(9)
    value = np.reshape(top_9['total emission'].values, (3, 3))
    reshaped_matrix = np.reshape(top_9['Organisation name'].values, (3, 3))
    fig=px.imshow(value,color_continuous_scale=px.colors.sequential.Viridis,text_auto=True)
    fig.update(data=[{'customdata': reshaped_matrix,
        'hovertemplate': "%{customdata}<br>"}])
    fig.update_layout(
        title_text="Top 9 Total Emissions")
    fig.update_layout(width=1200,height=900)
    return fig

def consumption_heatmap(data):
    ''' 
    Heatmap plot of top 9 net energy consumptions.

    Parameter:
        data: Pandas dataframe, raw data
    Return:
        fig: Plotly figure
    '''
    sorted_data = data.sort_values('Net energy consumed (GJ)', ascending=False)
    top_9 = sorted_data.head(9)
    value = np.reshape(top_9['Net energy consumed (GJ)'].values, (3, 3))
    reshaped_matrix = np.reshape(top_9['Organisation name'].values, (3, 3))
    fig=px.imshow(value,color_continuous_scale=px.colors.sequential.Viridis,text_auto=True)
    fig.update(data=[{'customdata': reshaped_matrix,
        'hovertemplate': "%{customdata}<br>"}])
    fig.update_layout(
        title_text="Top 9 Energy Consumptions")
    fig.update_layout(width=1200,height=900)
    return fig
    
def most_efficient(data):
    ''' 
    Heatmap plot of top 9 mist efficent organisations.

    Parameter:
        data: Pandas dataframe, raw data
    Return:
        fig: Plotly figure
    '''
    sorted_data = data.sort_values('share', ascending=True)
    top_9 = sorted_data.head(9)
    value = np.reshape(top_9['share'].values, (3, 3))
    reshaped_matrix = np.reshape(top_9['Organisation name'].values, (3, 3))
    fig=px.imshow(value,color_continuous_scale=px.colors.sequential.Viridis,text_auto=True)
    fig.update(data=[{'customdata': reshaped_matrix,
        'hovertemplate': "%{customdata}<br>"}])
    fig.update_layout(
        title_text="Top 9 Most Energy Efficient Organisations")
    fig.update_layout(width=1200,height=900)
    return fig

def least_efficient(data):
    ''' 
    Heatmap plot of top 9 least efficient organisations.

    Parameter:
        data: Pandas dataframe, raw data
    Return:
        fig: Plotly figure
    '''
    sorted_data = data.sort_values('share', ascending=False)
    top_9 = sorted_data.head(9)
    value = np.reshape(top_9['share'].values, (3, 3))
    reshaped_matrix = np.reshape(top_9['Organisation name'].values, (3, 3))
    fig=px.imshow(value,color_continuous_scale=px.colors.sequential.Viridis,text_auto=True)
    fig.update(data=[{'customdata': reshaped_matrix,
        'hovertemplate': "%{customdata}<br>"}])
    fig.update_layout(
        title_text="Top 9 Least Energy Efficient Organisations")
    fig.update_layout(width=1200,height=900)
    return fig