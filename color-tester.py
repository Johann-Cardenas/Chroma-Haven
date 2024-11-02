# ╔══════════════════════════════════════════════════════════════════════════════════╗
# ║███████╗███╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗ █████╗ ████████╗ ██████╗ ██████╗ ║
# ║██╔════╝████╗  ██║██╔════╝ ██║████╗  ██║██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗║
# ║█████╗  ██╔██╗ ██║██║  ███╗██║██╔██╗ ██║█████╗  ███████║   ██║   ██║   ██║██████╔╝║
# ║██╔══╝  ██║╚██╗██║██║   ██║██║██║╚██╗██║██╔══╝  ██╔══██║   ██║   ██║   ██║██╔══██╗║
# ║███████╗██║ ╚████║╚██████╔╝██║██║ ╚████║███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║║
# ║╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝║
# ╚══════════════════════════════════════════════════════════════════════════════════╝
# ╔══════════════════════════════════════════════════════════════════════════════════╗
#   Repository:  Chroma Haven                                                                                               
#   Description: Test graphically color palettes and choose your fighter.                                                             #
#   Author: Johann J Cardenas                                                   
#   Date: 11/01/2024        Version: v2.0.0                                              
# ╚══════════════════════════════════════════════════════════════════════════════════╝

import matplotlib.pyplot as plt
import numpy as np

# Define function to convert hex color to RGB
def hex_rgb(hex_color):
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
mumbay_hex = ['CDD5DC', 'F4F4F4', 'E0E0E0', 'B2B6BB']
panama_hex = ['4D4957', 'F4F4F4', 'E7E6E6', '9F9DA3']
managua_hex = ['2B2B2B', '898989', 'F8F8F8', 'E8E8E8']
cairo_hex = ['333333', '9BA8A8', 'EBEBE7', 'C8CEC4']
sanjose_hex = ['6F727F', 'EEEDED', 'AAA6B5', '866B7A']
asuncion_hex = ['5E5D5D', 'A7A5A5', 'EAE6E4', 'A4918E']
lima_hex = ['575965', 'C3C4C8', 'F8F8F6', '939498']

# Define color palettes (colorful)
stockholm_hex = ['F01159', 'DFF8FE', '82CDE5', '003458']
helsinki_hex = ['F7444E', 'F7F8F3', '78BCC4', '002C3E']
brusels_hex = ['043353', 'E44652', 'FAF8F0', 'E4DFCF']
berlin_hex = ['252324', 'FA3283', 'EAF7DF', '72EFD9']
cabo_hex = ['252324', 'FF2C82', 'EAF7DF', '72EFD9']
alienware = ['2C393F', '00C7C7', 'EDEDED', 'FFFFFF']
santiago_hex = ['2F404F', '3894A1', 'F0F1EE', 'C7DAD3']
sidney_hex = ['10455B', '2AA1AF', 'E2F0F1', 'FFFFFF']
buenosaires_hex = ['1F355D', 'FFFFFF', 'C0ECEC', '6FBEDB']
quito_hex = ['353755', 'FFFFFF', 'E0E4EE', '5BD3C7']
montevideo_hex = ['287094', 'D4D4CE', 'F6F6F6', '023246']
rio_hex = ['2C2627', 'BC2C3D', 'F8F3E6', 'EFD2BC']
bogota_hex = ['062639', 'E7301C', 'EDF4EA', 'C9D4C5']
tokyo_hex = ['2C3D63', 'ADDCCA', 'F7F8F3', 'FF6F5E']
illinois_hex = ['2E364F', '2D5D7C', 'F3F0E2', 'EF5939']
galicia_hex = ['182F53', 'F9EEE2', 'F57A4D', '9C3725']
barcelona_hex = ['3B4069', 'ECE0D5', 'F9F3EB', 'FF593E']
lisbon_hex = ['FF642E', 'F5F0E5', 'D4D7DB', '444C5E']
caracas_hex = ['25424C', 'FFA45B', 'FFEBDB', 'FB770D']

# User input
# ==============================================================================
# Define all color palettes in a list
palettes = {
    'Monochroma': monochroma_hex,
    'Monostyle': monostyle_hex,
    'Monolight': monolight_hex,
    'Monodark': monodark_hex,
    'Mumbay': mumbay_hex,
    'Panama City': panama_hex,
    'Managua': managua_hex,
    'Cairo': cairo_hex,
    'San Jose': sanjose_hex,
    'Asuncion': asuncion_hex,
    'Lima': lima_hex,
    'Stockholm': stockholm_hex,
    'Helsinki': helsinki_hex,
    'Brusels': brusels_hex,
    'Berlin': berlin_hex,
    'Punta Los Cabos': cabo_hex,
    'Alienware': alienware,
    'Santiago': santiago_hex,
    'Sidney': sidney_hex,
    'Buenos Aires': buenosaires_hex,
    'Quito': quito_hex,
    'Montevideo': montevideo_hex,
    'Rio': rio_hex,
    'Bogota': bogota_hex,
    'Tokyo': tokyo_hex,
    'Illinois': illinois_hex,
    'Galicia': galicia_hex,
    'Barcelona': barcelona_hex,
    'Lisbon': lisbon_hex,
    'Caracas': caracas_hex
}

# Prepare the figure to contain subplots for each palette
num_palettes = len(palettes)
fig, axs = plt.subplots(num_palettes, 2, figsize=(8, 3*num_palettes), dpi=300)

# Iterate over the dictionary to plot each palette
for idx, (palette_name, colors_hex) in enumerate(palettes.items()):
    colors_rgb = [hex_rgb(color) for color in colors_hex]
    # Call the function with specific axes
    create_plots(colors_rgb, axs[idx, 0], axs[idx, 1], palette_name)

plt.tight_layout()
plt.show()