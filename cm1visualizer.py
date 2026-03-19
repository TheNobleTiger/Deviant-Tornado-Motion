# -----------------------------------------------------------
# Reflectivity Visualization for CM1 Model Output
# Author: Isaac Langan
# College of DuPage
# Purpose: Load CM1 netCDF outputs, visualize reflectivity
#          as an interactive slider plot, optionally save
#          timesteps as images (SAVESTATE mode).
# Input: NetCDF files in 'directory' (change below)
# Output: Interactive plot or saved images per timestep
# Dependencies: xarray, netCDF4, numpy, matplotlib, os, glob
# -----------------------------------------------------------

import os
import xarray as xr
from netCDF4 import Dataset
import glob
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib.colors import ListedColormap, BoundaryNorm, LinearSegmentedColormap

#Some items below are listed, I will be looking to add these however I have been having trouble with some of them. They will hopefully come at a later date
# ------------------ USER CONFIGURABLE PARAMETERS -------------------
SAVESTATE = False       # Set True to save all timesteps as images instead of opening interactive plot
PRESSURE_CONTOURS = False # Not coded in yet  # Set True to overlay pressure contours on reflectivity
REFLECTIVITY = True         # Set True to display reflectivity
WINDVECTORS = False # Not Coded in yet        # Set True to display wind vectors
WINDBARBS = False # Not coded in yet
directory = "/home/isaac/cm1-output/elreno"  # Change this path to your CM1 output directory or the location you store run files
# ------------------------------------------------------------------

files = sorted(glob.glob(f"{directory}/cm1out_*.nc")) # Sort files in order of timestep (first to last)
print(f"Found {len(files)} files.") # For debugging purposes, see how many files loaded

ds = Dataset(files[0])

# This and the following list are for loading RadarscopeBR values, torn out from a .pal file
dbz_vals = [
    -32.0, -31.5, -31.0, -30.5, -30.0, -29.5, -29.0, -28.5, -28.0, -27.5,
    -27.0, -26.5, -26.0, -25.5, -25.0, -24.5, -24.0, -23.5, -23.0, -22.5,
    -22.0, -21.5, -21.0, -20.5, -20.0, -19.5, -19.0, -18.5, -18.0, -17.5,
    -17.0, -16.5, -16.0, -15.5, -15.0, -14.5, -14.0, -13.5, -13.0, -12.5,
    -12.0, -11.5, -11.0, -10.5, -10.0, -9.5, -9.0, -8.5, -8.0, -7.5,
    -7.0, -6.5, -6.0, -5.5, -5.0, -4.5, -4.0, -3.5, -3.0, -2.5,
    -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5,
    3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5,
    8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5,
    13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5,
    18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5,
    23.0, 23.5, 24.0, 24.5, 25.0, 25.5, 26.0, 26.5, 27.0, 27.5,
    28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0, 32.5,
    33.0, 33.5, 34.0, 34.5, 35.0, 35.5, 36.0, 36.5, 37.0, 37.5,
    38.0, 38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0, 42.5,
    43.0, 43.5, 44.0, 44.5, 45.0, 45.5, 46.0, 46.5, 47.0, 47.5,
    48.0, 48.5, 49.0, 49.5, 50.0, 50.5, 51.0, 51.5, 52.0, 52.5,
    53.0, 53.5, 54.0, 54.5, 55.0, 55.5, 56.0, 56.5, 57.0, 57.5,
    58.0, 58.5, 59.0, 59.5, 60.0, 60.5, 61.0, 61.5, 62.0, 62.5,
    63.0, 63.5, 64.0, 64.5, 65.0, 65.5, 66.0, 66.5, 67.0, 67.5,
    68.0, 68.5, 69.0, 69.5, 70.0, 70.5, 71.0, 71.5, 72.0, 72.5,
    73.0, 73.5, 74.0, 74.5, 75.0, 75.5, 76.0, 76.5, 77.0, 77.5,
    78.0, 78.5, 79.0, 79.5, 80.0, 80.5, 81.0, 81.5, 82.0, 82.5,
    83.0, 83.5, 84.0, 84.5, 85.0, 85.5, 86.0, 86.5, 87.0, 87.5,
    88.0, 88.5, 89.0, 89.5, 90.0, 90.5, 91.0, 91.5, 92.0, 92.5,
    93.0, 93.5, 94.0, 94.5
]

rgb_vals = [
    (115,77,172),(115,78,168),(115,79,165),(115,81,162),(116,82,158),
    (116,84,155),(116,85,152),(117,86,148),(117,88,145),(117,89,142),
    (118,91,138),(118,92,135),(118,94,132),(119,95,128),(119,96,125),
    (119,98,122),(120,99,118),(120,101,115),(120,102,112),(121,103,108),
    (121,105,105),(121,106,102),(122,108,98),(122,109,95),(122,111,92),
    (123,112,88),(123,113,85),(123,115,82),(124,116,78),(124,118,75),
    (124,119,72),(125,121,69),(127,123,72),(129,125,75),(131,127,79),
    (133,130,82),(135,132,85),(137,134,89),(139,137,92),(141,139,96),
    (144,141,99),(146,144,102),(148,146,106),(150,148,109),(152,151,113),
    (154,153,116),(156,155,119),(158,158,123),(161,160,126),(163,162,130),
    (165,165,133),(167,167,136),(169,169,140),(171,172,143),(173,174,147),
    (175,176,150),(178,179,154),(173,175,153),(168,171,152),(163,167,151),
    (158,163,150),(154,159,149),(149,155,148),(144,151,147),(139,147,146),
    (135,144,145),(130,140,144),(125,136,143),(120,132,142),(115,128,142),
    (111,124,141),(106,120,140),(101,116,139),(96,112,138),(92,109,137),
    (87,105,136),(82,101,135),(77,97,134),(73,93,133),(68,89,132),
    (63,85,131),(58,81,130),(54,78,130),(55,81,132),(57,85,134),
    (59,89,136),(61,93,138),(63,97,141),(65,101,143),(67,105,145),
    (69,109,147),(71,113,149),(73,117,152),(74,121,154),(76,125,156),
    (78,129,158),(80,133,160),(82,137,163),(84,141,165),(86,145,167),
    (88,149,169),(90,153,171),(92,157,174),(76,165,142),(60,173,110),
    (45,182,78),(42,175,72),(39,169,67),(37,163,62),(34,156,56),(31,150,51),
    (29,144,46),(26,137,40),(24,131,35),(21,125,30),(18,118,24),(16,112,19),
    (13,106,14),(11,100,9),(35,115,8),(59,130,7),(83,145,6),(107,161,5),
    (131,176,4),(155,191,3),(179,207,2),(203,222,1),(227,237,0),(252,253,0),
    (248,248,0),(244,243,0),(241,238,0),(237,233,0),(233,228,0),(230,223,0),
    (226,218,0),(222,213,0),(219,208,0),(215,203,0),(211,198,0),(208,193,0),
    (204,188,0),(200,183,0),(197,179,0),(250,148,0),(246,144,0),(242,141,1),
    (238,138,1),(234,135,2),(231,132,3),(227,129,3),(223,126,4),(219,123,5),
    (215,120,5),(212,116,6),(208,113,6),(204,110,7),(200,107,8),(196,104,8),
    (193,101,9),(189,98,10),(185,95,10),(181,92,11),(178,89,12),(249,35,11),
    (242,35,12),(236,35,13),(230,35,14),(223,36,15),(217,36,16),(211,36,17),
    (205,36,18),(198,37,19),(192,37,20),(186,37,22),(180,37,23),(173,38,24),
    (167,38,25),(161,38,26),(155,38,27),(148,39,28),(142,39,29),(136,39,30),
    (130,40,32),(202,153,180),(201,146,176),(201,139,173),(200,133,169),(200,126,166),
    (199,120,162),(199,113,159),(199,106,155),(198,100,152),(198,93,148),(197,87,145),
    (197,80,141),(196,74,138),(196,67,134),(196,60,131),(195,54,127),(195,47,124),
    (194,41,120),(194,34,117),(194,28,114),(154,36,224),(149,34,219),(144,33,215),
    (139,32,210),(134,31,206),(129,30,201),(124,29,197),(120,28,193),(115,27,188),
    (110,26,184),(105,24,179),(100,23,175),(95,22,170),(91,21,166),(86,20,162),
    (81,19,157),(76,18,153),(71,17,148),(66,16,144),(62,15,140),(132,253,255),
    (128,245,249),(125,238,243),(121,231,237),(118,224,231),(115,217,225),(111,210,219),
    (108,203,213),(105,196,207),(101,189,201),(98,181,196),(94,174,190),(91,167,184),
    (88,160,178),(84,153,172),(81,146,166),(78,139,160),(74,132,154),(71,125,148),
    (68,118,141),(66,111,136),(63,104,130),(60,97,124),(57,90,118),(55,83,113),
    (52,76,107),(49,69,101),(46,62,95),(43,55,90),(40,48,84),(37,41,79),(34,34,73)
]

# Normalize RGB values to 0-1 range for matplotlib and numpy functions
colors = [(r/255, g/255, b/255) for r,g,b in rgb_vals]
dbz_min, dbz_max = min(dbz_vals), max(dbz_vals)
norm_dbz = [(v - dbz_min) / (dbz_max - dbz_min) for v in dbz_vals]
cmap = LinearSegmentedColormap.from_list("RadarScope_BR", list(zip(norm_dbz, colors)))
norm = BoundaryNorm(dbz_vals, ncolors=len(dbz_vals), clip=True)

cref_list=[]
pressure_list=[]
vector_list=[]
time_list=[]

print(ds.variables.keys())

# Assuming the variables are named 'dx', 'dy', 'dz', and 'reflectivity'
x = np.array(ds.variables['xh'][:])
y = np.array(ds.variables['yh'][:])
reflectivity = ds['cref'][0,:,:]  #Take the lowest level only (Z-slicing)

# All debugging statements, tells the user the grid spacing being used
print("Grid spacing in x:", x[1] - x[0], "km")
print("Grid spacing in y:", y[1] - y[0], "km")
print(f"x range: {x.min()} km to {x.max()} km")
print(f"y range: {y.min()} km to {y.max()} km")

# Loop through each netCDF file to load reflectivity data
for f in files:
        ds = Dataset(f) # Open netCDF file
        cref_list.append(ds.variables['cref'][0,:,:]) # Take first vertical level (lowest altitude)
        time_minutes = ds.variables['time'][0]/60 # Convert simulation time from seconds to minutes
        time_list.append(time_minutes)
        ds.close() # Close file to free memory

# Another debugging message to see if cref is loading correctly
print(f"Loaded reflectivity data for {len(cref_list)} timesteps.")

# SAVESTATE MODE:
# If enabled, saves all timesteps as individual PNG images to a folder
# Does not open interactive slider UI
if SAVESTATE:
    parent_folder = os.path.join(os.getcwd(), "savestates") # Parent folder to all saved output files, feel free to change the name
    os.makedirs(parent_folder, exist_ok=True)
    folder_name = input("Enter savestate folder name: ").strip()
    if folder_name == "":
        folder_name = "unnamed-cm1-pngs" # Default folder if user enters nothing, feel free to change this
    save_path = os.path.join(parent_folder, folder_name)
    os.makedirs(save_path, exist_ok=True) # Create a folder if it does not already exist
    print(f"Saving images to: {save_path}")

    for i in range(len(cref_list)):
        fig_save, ax_save = plt.subplots()
        im_save = ax_save.imshow(
            cref_list[i],
            cmap=cmap,
            origin='lower',
            norm=norm,
            extent=[x.min(), x.max(), y.min(), y.max()],
            aspect='equal'
        )
        ax_save.set_title(f"Timestep {i+1} - Time: {time_list[i]:.1f} min")
        ax_save.set_xlim(x.min(), x.max())
        ax_save.set_ylim(y.min(), y.max())
        cbar = fig_save.colorbar(im_save, ax=ax_save)
        cbar.set_label('dBZ')
        filename = os.path.join(save_path, f"timestep_{i+1}.png")
        plt.savefig(filename, dpi=150)
        plt.close(fig_save)
        print(f"Saved {filename}")

    print("Savestate complete.")
    exit()

# Create figure and axis for plotting
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2) # Feel free to adjust this to your comfort level to leave enough room between the chart and slider
# Sets a defualt of plotting the first timestep
im = ax.imshow(
        cref_list[0],
        cmap = cmap,
        origin = 'lower',
        norm = norm,
        interpolation = 'nearest',
        extent = [x.min(), x.max(), y.min(), y.max()],
        aspect = 'equal',
        )

ax.set_title(f"Timestep 1 - Time: {time_list[0]} min")

# Set colorbar and label
cbar = fig.colorbar(im, ax=ax)
cbar.set_label('dBZ')
ax.set_xlim(x.min(), x.max())
ax.set_ylim(y.min(), y.max())

# Old functions still here for debugging and testing future product plotting
#plt.pcolormesh(x, y, reflectivity, shading = 'auto', cmap = cmap, norm=norm)
#plt.colorbar(label = 'Reflectivity (dBZ)')
#plt.xlabel('X (km)')
#plt.ylabel('Y (km)')
#plt.title('Reflectivity at first time step')
#plt.show()

# Provides enough space for positioning buttons and a slider, then defines axis
plt.subplots_adjust(bottom = 0.2)
ax_slider = plt.axes([0.2, 0.1, 0.65, 0.03])
slider = Slider(ax_slider, 'Timestep', 0, len(cref_list)-1, valinit=0, valstep=1)

# Slider update function
def update(val):
        timestep = int(slider.val)
        im.set_data(cref_list[timestep])
        ax.set_title(f"Timestep {timestep+1} - Time: {time_list[timestep]:.1f} min")
        fig.canvas.draw_idle()
slider.on_changed(update)

# Set a function to be called on when buttons/keys are pressed for moving forward 1 timestep
def step_forward(event=None):
    timestep = int(slider.val)
    if timestep < len(cref_list)-1:
        slider.set_val(timestep + 1)

# Same as above function but this time for moving backwards
def step_backward(event=None):
    timestep = int(slider.val)
    if timestep > 0:
        slider.set_val(timestep - 1)

ax_prev = plt.axes([0.1, 0.05, 0.1, 0.04]) # Positions a button on the bottom left
ax_next = plt.axes([0.8, 0.05, 0.1, 0.04]) # Positions a button on the bottom right
btn_prev = Button(ax_prev, '<< Prev') # Actually creates
btn_next = Button(ax_next, 'Next >>') # Actually creates
btn_next.on_clicked(step_forward) # Allows the button on the right to go forward when clicked
btn_prev.on_clicked(step_backward) # Allows the button on the left to go backwards when clicked

# Make arrow keys also function for moving forward/backwards timesteps
def on_key(event):
    if event.key == 'right':
        step_forward()
    elif event.key == 'left':
        step_backward()

# Connect key presses to the on_key function
fig.canvas.mpl_connect('key_press_event', on_key)


plt.show()
