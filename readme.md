# Data Visualization Web Application

This is a web application built with Python Flask that helps users understand National Greenhouse and Energy Reporting data better by visualisation. 

Under the National Greenhouse and Energy Reporting Act 2007 (NGER Act), entities that are required to report their energy use and greenhouse gas emissions must report to the Australian Government. The Australian Government Clean Energy Regulator published these entities in the National Greenhouse and Energy Reporting Registrar https://www.cleanenergyregulator.gov.au/NGER/National greenhouse and energy reporting data/Extract-of-National-Greenhouse-and-Energy-Register-by-year/national-greenhouse-and-energyregister-2021-22 This application loads data and shows an analysis of the National Greenhouse and Energy Register for 2021-22 reporting year using the publicly available data.

## Requirements

- Flask==1.1.2
- numpy==1.23.5
- pandas==1.5.3
- plotly==5.15.0

## Installation

1. Clone the repository
2. Install the required packages:
   
   `pip install -r requirements.txt `

## Usage

1. Navigate to the project directory

2. Start the Flask application in terminal:

    `python app.py`


## Dependencies

The following packages are used in this project:

- Flask: Web framework for building the application.
- Plotly: Visualization library for creating interactive charts.


## Dataset Used

In this application, we mainly focused on [Corporate emissions and energy data 2021-22 covered under the register](https://www.cleanenergyregulator.gov.au/NGER/National%20greenhouse%20and%20energy%20reporting%20data/Corporate%20emissions%20and%20energy%20data/corporate-emissions-and-energy-data-2021-22). It has 3 key attributes for each reporting organisations: Scope 1 emission, Scope 2 emission, net energy assumption.

### Scope 1 emissions

Scope 1 greenhouse gas emissions are the emissions released to the atmosphere as a direct result of an activity, or series of activities at a facility level. Scope 1 emissions are sometimes referred to as direct emissions. Examples are:

- emissions produced from manufacturing processes, such as from the manufacture of cement
- emissions from the burning of diesel fuel in trucks
- fugitive emissions, such as methane emissions from coal mines, or
- production of electricity by burning coal.

### Scope 2 emissions

Scope 2 greenhouse gas emissions are the emissions released to the atmosphere from the indirect consumption of an energy commodity. For example, 'indirect emissions' come from the use of electricity produced by the burning of coal in another facility.

Scope 2 emissions from one facility are part of the scope 1 emissions from another facility.

For example, a power station burns coal to power its generators and in turn creates electricity. Burning the coal causes greenhouse emissions to be emitted. These gases are attributed to the power station as scope 1 emissions. If the electricity is then transmitted to a car factory and used there to power its machinery and lighting, the gases emitted as a result of generating the electricity are then attributed to the factory as scope 2 emissions.

## Usage of this visualisation application

This tool has 4 main visualisation sections, leading through the process of Data analysis, to help users understand the highlights from the dataset.

In Raw Data Explore section, histogram and box plot were used to help understand the distribution of the dataset.

In Relationship Analysis section, scatter plot was used to understand the relationship between attributes. In this section, apart from raw emission/consumption, we also investigated efficiency of the organisations, and found that organisations made the most emission tend to have a high energy efficiency (low share of emission/consumption), whereas some smaller firms with low emissions are not focusing on increasing the energy efficiency even though the values of their net emissions seem low.

In Emission Analysis section, pie chart was used to understand how large firms are dominating the emission/consumption and the amount of smaller firms are also taking a considerable share.

In Organisational Analysis section, we used heatmap to visualise and understand the top organisations that made emission/consumption, as well as the most and least energy efficient organisations.

