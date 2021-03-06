# -*- coding: utf-8 -*-
#
# This file is part of spectraplotpy.
#
# spectraplotpy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# spectraplotpy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with spectraplotpy.  If not, see <http://www.gnu.org/licenses/>.
#

"""
Created on Mon Mar 17 2014

@author: ariamania
"""

import spectraplotpy as spp
import numpy as np
import pytest as pt
from mock import MagicMock


def create_fake_dataset():
    ds = spp.Dataset()
    ds.x = np.array([1,2,3,4])
    ds.y = np.array([2,4,6,8])
    ds.error_y = np.array([1,1,1,1])    
    return ds 

def test_construction():
    ds = spp.Dataset()
    assert spp.Spectrum(ds)

def test_copy():
    ds = create_fake_dataset()
    s = spp.Spectrum(ds) 
    s1 = s.copy()
    
    assert all(s.dataset.x == s1.dataset.x)
    assert all(s.dataset.y == s1.dataset.y)
    
    s1.dataset.x[2] = 100
    assert not all(s.dataset.x == s1.dataset.x)

def test_Length_Error_exception():
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    ds1 = spp.Dataset()
    ds1.x = np.array([1,2,3])
    ds1.y = np.array([2,4,6])
    s1 = spp.Spectrum(ds1)
    
    with pt.raises(spp.LengthError):
        s + s1
        
    with pt.raises(spp.LengthError):
        s - s1
        
    
def test_add():
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    s1 = s.copy()
    s2 = s + s1
    s.add(s1)
    
    assert all(s.dataset.x == s2.dataset.x)
    assert all(s.dataset.y == s2.dataset.y)


def test_add_value():
    s_y_np = np.array([2,4,6,8])
    s_y_np1 = s_y_np.copy()
    s_y_np2 = s_y_np + s_y_np1
    
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    s1 = s.copy()
    
    assert all(s.dataset.y == s_y_np)
    
    s.add(s1)
    
    assert all(s.dataset.y == s_y_np2)
    
def test_sub():
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    s1 = s.copy()
    s2 = s - s1
    s.sub(s1)
    
    assert all(s.dataset.x == s2.dataset.x)
    assert all(s.dataset.y == s2.dataset.y)
    
def test_sub_value():
    s_y_np = np.array([2,4,6,8])
    s_y_np1 = s_y_np.copy()
    s_y_np2 = s_y_np - s_y_np1
    
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    s1 = s.copy()
    
    assert all(s.dataset.y == s_y_np)
    
    s.sub(s1)
    
    assert all(s.dataset.y == s_y_np2)
    
def test_mul():
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    s1 = s * 3.0
    s2 = 3.0 * s
    s.mul(3.0)
    
    assert all(s.dataset.x == s1.dataset.x)
    assert all(s.dataset.y == s1.dataset.y)
    assert all(s.dataset.x == s2.dataset.x)
    assert all(s.dataset.y == s2.dataset.y)
    
def test_mul_value():
    s_y_np = np.array([2,4,6,8])
    s_y_np1 = 3.0 * s_y_np
    
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    
    assert all(s.dataset.y == s_y_np)
    
    s1 =  3.0 * s 
    
    assert all(s1.dataset.y == s_y_np1)
    
def test_div():
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    with pt.raises(TypeError):
        3.0 / s
        
    s2 = s / 3.0    
    s.div(3.0)
    
    assert all(s.dataset.x == s2.dataset.x)
    assert all(s.dataset.y == s2.dataset.y)
    

def test_mock_plot():
    """
    create a mock test for the plot method
    """
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    
    mock_fig = MagicMock()
    mock_fig.plot = MagicMock()
    s.plot(mock_fig)
    mock_fig.plot.assert_called_once_with(s.dataset.x, s.dataset.y)
    
    
def test_errorbar():
    """
    create a mock test for the plot_errorbar method
    """
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    x_data = s.dataset.x
    y_data = s.dataset.y
    x_errors = s.dataset.errors_x
    y_errors = s.dataset.errors_y
    
    mock_fig = MagicMock()
    mock_fig.errorbar = MagicMock()
    s.errorbar(mock_fig)
    mock_fig.errorbar.assert_called_once_with(x_data, y_data, 
                                              y_errors, x_errors) 
    

