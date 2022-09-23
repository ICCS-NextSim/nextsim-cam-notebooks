"""
This module contains tests to check that NextSim output is valid.
"""

import numpy as np
import xarray as xr

def output_comp(file1, file2, eps=1e-2):
    """
    Load a pair of netcdf model outputs and run a sequence
    of comparison tests.

    Parameters
    ----------
    file1 : str
        Filename of first model output
    file2 : str
        Filename of second model output
    eps : float
        Maximum relative error
    """
    
    def compare_field(data1, data2):
        """
        This function compares one field

        Parameters
        ----------
        data1, data2 : numpy array 
            Data arrays that should be equal. 
            

        Returns
        -------
        Bool if fields are equal.

        """
        return np.nanmax(np.abs(data1-data2)) < eps * np.nanmax(np.abs(data1))
        
    data1 = xr.open_dataset(file1)
    data2 = xr.open_dataset(file2)

    fields = ["sit", "sic"]

    
    for field in fields: 
        data1 = getattr(data1, field).data
        data2 = getattr(data2, field).data
        is_match = compare_field(data1, data2)
        
        if not is_match:
            msg = "Difference field " + field + " is too large."
            print(msg)
            return False
            
    return True
        
        