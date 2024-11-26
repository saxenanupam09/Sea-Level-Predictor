import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig = plt.figure(figsize=(12,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create first line of best fit
    lin1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series(range(1880, 2051))
    y_pred = lin1.slope*x_pred + lin1.intercept 
    plt.plot(x_pred, y_pred, 'yellow')
    
    # Create second line of best fit
    df2 = df[df['Year'] >= 2000]
    lin2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series(range(2000, 2051))
    y_pred = lin2.slope*x_pred + lin2.intercept
    plt.plot(x_pred, y_pred, 'blue')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()