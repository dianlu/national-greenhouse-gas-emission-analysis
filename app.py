from flask import Flask, render_template, request
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
import visual_plots
import data_preprocess

app = Flask(__name__)

# Configuration options
app.config['STATIC_URL_TIMESTAMP'] = True
app.config['DEBUG'] = False
app.debug = False


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/raw_data')
def raw_data():
    # Get data
    emission_data=data_preprocess.fetch_and_process()
    # Visualise data
    raw_histogram_fig=visual_plots.raw_histogram(emission_data)
    raw_box=visual_plots.raw_box_plot(emission_data)
    # Convert the figure to html and pass it to the template  
    return render_template('data.html', plt1=raw_histogram_fig.to_html(full_html=False),
        plt2=raw_box.to_html(full_html=False))

@app.route('/data')
def data():
    # Get data
    emission_data=data_preprocess.fetch_and_process()
    # Visualise data
    share_pie_plot=visual_plots.share_pie_plot(emission_data)
    total_pie_plot=visual_plots.total_emission_pie_plot(emission_data)
    consumption_pie=visual_plots.net_energy_pie_plot(emission_data)
    # Convert the figure to html and pass it to the template  
    return render_template('data.html', plt1=share_pie_plot.to_html(full_html=False),
        plt2=total_pie_plot.to_html(full_html=False),plt3=consumption_pie.to_html(full_html=False))

@app.route('/heatmap')
def heatmap():
    # Get data
    emission_data=data_preprocess.fetch_and_process()
    # Visualise data
    consumption=visual_plots.consumption_heatmap(emission_data)
    emission=visual_plots.emission_heatmap(emission_data)
    least=visual_plots.least_efficient(emission_data)
    most=visual_plots.most_efficient(emission_data)
    # Convert the figure to html and pass it to the template  
    return render_template('data.html', plt1=consumption.to_html(full_html=False),
        plt2=emission.to_html(full_html=False),plt3=least.to_html(full_html=False),plt4=most.to_html(full_html=False))

@app.route('/relationship')
def relationship():
    # Get data
    emission_data=data_preprocess.fetch_and_process()
    # Visualise data
    scopes=visual_plots.scopes_scatter(emission_data)
    consumption_emission_scatter=visual_plots.consumption_emission_scatter(emission_data)
    # Convert the figure to html and pass it to the template  
    return render_template('data.html', plt1=scopes.to_html(full_html=False),
        plt2=consumption_emission_scatter.to_html(full_html=False))

if __name__ == '__main__':
    app.run(debug=False)
