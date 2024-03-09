import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cartopy.crs as ccrs
from netCDF4 import Dataset

# Load NetCDF data (replace 'your_data.nc' with the actual file name)
nc_file = 'test4.nc'
nc_data = Dataset(nc_file, 'r')

# Extract latitude, longitude, and cloud cover data
# lat = nc_data.variables['latitude'][:]
print(nc_data.variables)
print(len(nc_data.variables['latitude']))
lon = nc_data.variables['longitude'][:]
cloud_cover = nc_data.variables['ir_brightness_temperature'][:]

# Create a 3D plot with Cartopy projection
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection=ccrs.PlateCarree())

# # Plot the 3D surface with contourf
# contourf = ax.contourf(lon, lat, cmap='viridis', transform=ccrs.PlateCarree())

# # Add colorbar
# cbar = plt.colorbar(contourf, ax=ax, orientation='vertical', pad=0.1, aspect=16, shrink=0.8)
# cbar.set_label('Cloud Cover')

# # Add labels
# ax.set_xlabel('Longitude')
# ax.set_ylabel('Latitude')
# ax.set_title('3D Cloud Cover Plot on Map')

# # Show the plot
# plt.show()

# # Close the NetCDF file
nc_data.close()
