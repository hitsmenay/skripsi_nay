#skrip ini digunakan untuk melakukan regridding menjadi 0,05derajat

#import modul yang diperlukan
import pandas as pd 
import xarray as xr
from netCDF4 import Dataset
import numpy as np

ds = xr.open_dataset("tp.nc") #membuka file nc
ds


#menentukan longitude baru
new_lon = np.arange(ds.longitude[0], ds.longitude[-1], 0.05)  # 0.4 to 0.05

#menentukan latitude baru
new_lat = np.arange(ds.latitude[-1], ds.latitude[0], 0.05)
#melakukan regridding menggunakan interpolation
ds = ds.interp(latitude=new_lat, longitude=new_lon)  # Interpolation
# ds = ds.sel(latitude=latii,longitude=lonii,method="nearest")
# ds

#mengubah data menjadi tipe data frame
df = ds.to_dataframe()
#mengkonversi satuan seperti m ke mm, k ke c
#JANGAN LUPA # DI HAPUS 
df['tp'] = df['tp']*1000
#menyimpan data frame menjadi csv
df.to_csv("tp_arrange.csv")
