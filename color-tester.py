
import matplotlib.pyplot as plt
import numpy as np

# Define function to convert hex color to RGB
def hex_rgb(hex_color):
    """
    Convert a hex color string to an RGB tuple.

    Parameters:
    - hex_color: A string representing a hex color, e.g., '9CA1B3'

    Returns:
    - A tuple of integers representing the RGB values, e.g., (156, 161, 179)
    """
    hex_color = hex_color.lstrip('#')  # Remove '#' if it's there
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


# Function to create line and bar plots for a given color palette
def create_plots(colors_rg, ax1, ax2, palette_name):
    # Generate random data for visualization
    np.random.seed(4)  # For reproducibility
    data_line = np.random.rand(4, 8)  # Generate 4 datasets
    data_bar = np.random.rand(4, 4)  # Generate 4 datasets
    markers = ['o', 'o', 'o', 'o']

    # Line plot with markers
    for i in range(data_line.shape[0]):
        ax1.plot(data_line[i], marker=markers[i], linestyle='-', color=[c/255. for c in colors_rgb[i]], 
                 markeredgecolor='black', markeredgewidth=0.5, markersize=5, label=f'D{i+1}')
    ax1.set_title(f'{palette_name} - Line Plot', fontweight='bold')
    ax1.set_xlabel('X axis', fontweight='bold')
    ax1.set_ylabel('Y axis', fontweight='bold')
    ax1.grid(True, linestyle='--', linewidth=0.5, color='lightgray')
    ax1.legend(loc='best')
        

    # Bar chart plot
    bar_width = 0.2
    index = np.arange(data_bar.shape[1])
    for i in range(data_bar.shape[0]):
        ax2.bar(index + i*bar_width, data_bar[i], bar_width, color=[c/255. for c in colors_rgb[i]], 
                label=f'D{i+1}', edgecolor='black', linewidth=0.5)
    ax2.set_xticks(index + bar_width / 2)
    ax2.set_xticklabels(index)
    ax2.set_title(f'{palette_name} - Bar Chart', fontweight='bold')
    ax2.set_xlabel('X axis', fontweight='bold')
    ax2.set_ylabel('Y axis', fontweight='bold')
    ax2.legend(loc='best')
    ax2.grid(True, axis='y', linestyle='--', linewidth=0.5, color='lightgray')



# Define color palettes (black and white)
monochroma_hex = ['9CA1B3', 'CFD1FA', 'EBECEF', '58586F']
monostyle_hex = ['444251', '8D89A3', 'E4E3E5', 'CBCBCF']
monolight_hex = ['BEBCCB', 'F1EFF2', 'DDD7DC', 'A994A7']
monodark_hex = ['56514B', 'E7E5DD', 'BDBBAD', '999990']
lima_hex = ['575965', 'C3C4C8', 'F8F8F6', '939498']

# Define color palettes (colorful)
stockholm_hex = ['F01159', 'DFF8FE', '82CDE5', '003458']
tokyo_hex = ['2C3D63', 'ADDCCA', 'F7F8F3', 'FF6F5E']
berlin_hex = ['252324', 'FA3283', 'EAF7DF', '72EFD9']
santiago_hex = ['2F404F', '3894A1', 'F0F1EE', 'C7DAD3']
rio_hex = ['2C2627', 'BC2C3D', 'F8F3E6', 'EFD2BC']
bogota_hex = ['062639', 'E7301C', 'EDF4EA', 'C9D4C5']
illinois_hex = ['2E364F', '2D5D7C', 'F3F0E2', 'EF5939']

# User input
# ==============================================================================
# Define all color palettes in a list
palettes_hex =  [monochroma_hex,
                 monostyle_hex,
                 monolight_hex,
                 monodark_hex,
                 lima_hex, 
                 stockholm_hex, 
                 tokyo_hex, 
                 berlin_hex, 
                 santiago_hex, 
                 rio_hex, 
                 bogota_hex, 
                 illinois_hex]

palette_names = ['Monochroma',
                 'Monostyle',
                 'Monolight',
                 'Monodark',
                 'Lima', 
                 'Stockholm', 
                 'Tokyo', 
                 'Berlin', 
                 'Santiago', 
                 'Rio', 
                 'Bogota', 
                 'Illinois']
# ==============================================================================

# Prepare the figure to contain subplots for each palette
num_palettes = len(color_palettes)
fig, axs = plt.subplots(num_palettes, 2, figsize=(8, 3*num_palettes), dpi=300)

for idx, (palette_name, colors_hex) in enumerate(zip(palette_names, palettes_hex)):
    colors_rgb = [hex_rgb(color) for color in colors_hex]
    # Call the function with specific axes
    create_plots(colors_rgb, axs[idx, 0], axs[idx, 1], palette_name)

plt.tight_layout()
plt.show()


# # Create pie chart
# plt.figure(figsize=(4, 3), dpi=300)
# normalized_colors = [(r/255., g/255., b/255.) for (r, g, b) in colors_rgb]
# slices, texts, autotexts = plt.pie([1, 2, 3, 4], colors=normalized_colors, 
#                                    autopct='%1.1f%%', startangle=140, 
#                                    wedgeprops={'edgecolor': 'black', 'linewidth': 0.5})

# for autotext in autotexts:
#     autotext.set_color('black')  # Change color to make percentage labels more visible if needed
#     autotext.set_bbox(dict(facecolor='white', alpha=0.6, edgecolor='none', boxstyle='round,pad=0.2'))
    
# plt.title('Pie Chart', fontweight='bold')
# plt.legend(slices, [f'D{i+1}' for i in range(4)], title="Datasets", loc="upper center", bbox_to_anchor=(0.50, 0.05), ncol=4)
# plt. tight_layout()
# # Comment
# plt.show()

# ______________________________________________________