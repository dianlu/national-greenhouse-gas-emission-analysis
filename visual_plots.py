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
    fig.update_layout(width=1200,height=1000)
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
    fig.update_layout(width=1200,height=1000)
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
    fig.update_layout(width=1200,height=1000)
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
    fig.update_layout(width=1200,height=1000)
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
    fig.update_layout(width=1200,height=1000)
    return fig