'''
Created on 23 Sept 2022

This module contains code to perform automatic code testing. 

@author: ivo
'''
import os 
import pytest
from next_tools.output_comp import output_comp
import xarray as xr

file_dir = "/home/ivo/ICCS/output"
files = ["Moorings_2018m01_original.nc", "Moorings_2018m01_rerun.nc"]
files = [os.path.join(file_dir, file) for file in files]

def test_output_comp():
    """
    Test to see if output_comp flags different output as False. 
    """
    msg = "output_comp comparison failed."
    assert output_comp(files[0], files[1]), msg
    
test_output_comp()