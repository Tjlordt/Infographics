#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 00:12:53 2023

@author: tj
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

# Read data from the CSV file
df = pd.read_csv('uk_renewable_energy.csv')
year = df['Year']
fossil_energy = df['Total energy consumption of primary fuels and equivalents']
ren_energy = df['Energy from renewable & waste sources']
frac_ren = df['Fraction from renewable sources and waste']

# Set color palette
cp = sns.color_palette('colorblind')

# Create a new figure using gridspec
fig = plt.figure(figsize=(20, 24))
gs = GridSpec(nrows=4, ncols=2, figure=fig)

# Create top-left subplot
ax1 = fig.add_subplot(gs[0, 0])
sns.lineplot(x=year, y=fossil_energy, linewidth=4, color=cp[5], ax=ax1)
sns.lineplot(x=year, y=ren_energy, linewidth=4, color=cp[2], ax=ax1)
ax1.set_title('Yearly Energy Consumption from Two Sources')
ax1.set_ylabel('Energy Consumption (mtoe)')
ax1.legend(['Primary fuels and equivalent', 'Renewables and waste'], loc='upper right')

# Create top-right subplot
ax2 = fig.add_subplot(gs[0, 1])
sns.lineplot(x=year, y=frac_ren, linewidth=4, color=cp[6], ax=ax2)
ax2.set_title('Fraction of Energy Consumption from Renewable and Waste Sources')
ax2.set_ylabel('Fraction (no units)')
ax2.legend(['Fraction from renewable sources and waste'], loc='upper right')

# Create middle-left subplot
ax3 = fig.add_subplot(gs[1, 0])
ax3.bar(df.index, df['Energy from renewable & waste sources'], color='green')
ax3.set_xlabel('Year')
ax3.set_ylabel('Energy from renewable & waste sources')
ax3.set_title('Renewable & Waste Energy Consumption')
ax3.legend(['Energy'])

# Create middle-right subplot
ax4 = fig.add_subplot(gs[1, 1])
ax4.plot(df.index, df['Fraction from renewable sources and waste'], color='blue')
ax4.set_xlabel('Year')
ax4.set_ylabel('Fraction from renewable sources and waste')
ax4.set_title('Renewable Energy Fraction')
ax4.legend(['Fraction'])

# Create bottom-left subplot
ax5 = fig.add_subplot(gs[2, 0])
sns.histplot(data=df, x='Fraction from renewable sources and waste', color='orange', bins=10, ax=ax5)
ax5.set_xlabel('Fraction from renewable sources and waste')
ax5.set_ylabel('Frequency')
ax5.set_title('Fraction from Renewable Sources and Waste')
ax5.legend(['Frequency'])

# Create bottom-right subplot
ax6 = fig.add_subplot(gs[2, 1])
ax6.scatter(df['Total energy consumption of primary fuels and equivalents'], df['Fraction from renewable sources and waste'], color='purple')
ax6.set_xlabel('Total energy consumption of primary fuels and equivalents')
ax6.set_ylabel('Fraction from renewable sources and waste')
ax6.set_title('Energy Consumption vs Renewable Energy Fraction')
ax6.legend(['Energy-Fraction'])
# Add text annotation
ax7 = fig.add_subplot(gs[3, :])
infographic_text = "This code generates an infographic that displays the trend ofclimate renewable energy consumption and fraction in the UK from 1990 to 2020. The infographic consists of seven subplots arranged in a grid using matplotlib's GridSpec module. The subplots use different types of plots such as line plots, bar plots, scatter plots, and histograms to display various aspects of the data. Multiple Python libraries, including Pandas, Seaborn, Matplotlib, Matplotlib's GridSpec, and NumPy, are used for data analysis and visualization. The first subplot shows the yearly energy consumption from primary fuels and renewable sources plotted as line charts, with the two lines representing renewable and waste energy and primary fuels and equivalents, respectively. The top-right subplot displays the fraction of renewable energy in the total energy consumption, while the middle-left subplot displays the renewable energy consumption over the years plotted as a bar chart. The middle-right subplot displays the fraction of renewable energy over the years plotted as a line chart, and the bottom-left subplot displays the frequency of different renewable energy fractions plotted as a histogram. The bottom-right subplot displays the relationship between the total energy consumption and the renewable energy fraction plotted as a scatter plot. Finally, a text annotation is added in the last subplot at the bottom of the infographic, providing a brief description of the infographic's contents and purpose. The infographic is visually appealing, with a color palette that effectively differentiates the different types of data. The use of multiple subplots allows easy comparison of different aspects of the data, and the addition of the text annotation provides context and makes the infographic more informative. The infographic can be useful for individuals or organizations interested in the UK's energy consumption trends and policies related to renewable energy, and it can also serve as an educational tool for students or individuals interested in renewable energy and environmental issues."

ax7.text(0.5, 0.5, infographic_text, ha='center', va='center', fontsize=17, wrap=True, linespacing=1.0)
ax7.set_axis_off()

# Adjust the layout and spacing of the subplots
fig.tight_layout()
plt.savefig('infographic.png', dpi=300, bbox_inches='tight')

# Show the final infographic
plt.show()
