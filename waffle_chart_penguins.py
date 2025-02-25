import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pywaffle import Waffle

# Load the penguin dataset
penguins = sns.load_dataset('penguins')

# Drop rows with missing species data
penguins = penguins.dropna(subset=['species'])

# Count the number of occurrences of each species
species_counts = penguins['species'].value_counts()

number_of_bars = len(species_counts)  # One plot per species
fig, axs = plt.subplots(
    nrows=number_of_bars,  # One row for each species
    ncols=1,  # One column for each subplot
    figsize=(12, 6)
)


# Set background color for the figure
fig.patch.set_facecolor("#F4F4F9")


# Iterate over each species and create a waffle chart for each one
for i, (species, count) in enumerate(species_counts.items()):
    # Each waffle will represent the number of penguins of that species
    percentage = (count / sum(species_counts)) * 100
    values = [count, sum(species_counts) - count]  # The count of that species vs the rest
    
    # Plot a waffle chart for each species
    Waffle.make_waffle(
        ax=axs[i],
        rows=4,  
        columns=25, 
        values=values,
        colors = ["#72874E","#A4BED5"]
      
      
        
    )
    
   
    
    axs[i].text(
     -0.3, 0.5,  # Adjust position above the charts
     f"{species}\n{percentage:.1f}%",
     ha='center', va='center',  
     fontsize=12, color="#2E4A58", 
     rotation=90
)

    
    

fig.suptitle(
    "Palmer Penguins Species Distribution",  # Title text
    fontsize=25,  # Font size
    fontweight='bold',  
    color="#476F84",  
    fontname="Arial Rounded MT Bold",  
    ha='center', 
    va='top',
    y=0.96,
    x=0.35);


fig.text(
    0.04,  # Horizontal position (centered)
    0.01,  # Vertical position (close to the bottom)
    "Data Palmer Penguins | Plot Sara Maras",  # Name text
    ha='left',  # Center horizontally
    va='bottom',  # Align text to the bottom
    fontsize=9,  # Font size for the name
    fontweight='normal',  
    color="#476F84",  # Color of the name (matching the title)
    fontname="Arial Rounded MT Bold"  # Same font as the title
);

# Save the plot as a PNG file
fig.savefig('palmer_penguins_species.png', dpi=500, bbox_inches='tight')