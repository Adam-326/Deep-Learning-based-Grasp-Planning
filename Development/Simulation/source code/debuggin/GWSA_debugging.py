# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:28:27 2019

@author: Adam Syammas Zaki P
"""
import numpy as np
import scipy.spatial as ss
from pyhull.convex_hull import ConvexHull


wrenches = np.array([[ 0.5       ,  0.35355339, -0.35355339, -0.03535534, -0.30355339, -0.35355339],
           [ 0.5       ,  0.48296291,  0.12940952, -0.04829629,  0.17940952,-0.48296291],
           [ 0.5       ,  0.12940952,  0.48296291, -0.01294095,  0.53296291, -0.12940952],
           [ 0.5       , -0.35355339,  0.35355339,  0.03535534,  0.40355339, 0.35355339],
           [ 0.5       , -0.48296291, -0.12940952,  0.04829629, -0.07940952, 0.48296291],
           [ 0.5       , -0.12940952, -0.48296291,  0.01294095, -0.43296291, 0.12940952],
           [-0.5       , -0.35355339,  0.35355339,  0.03535534, -0.40355339, -0.35355339],
           [-0.5       ,  0.12940952,  0.48296291, -0.01294095, -0.53296291, 0.12940952],
           [-0.5       ,  0.48296291,  0.12940952, -0.04829629, -0.17940952, 0.48296291],
           [-0.5       ,  0.35355339, -0.35355339, -0.03535534,  0.30355339, 0.35355339],
           [-0.5       , -0.12940952, -0.48296291,  0.01294095,  0.43296291, -0.12940952],
           [-0.5       , -0.48296291, -0.12940952,  0.04829629,  0.07940952, -0.48296291]])

Hull = ConvexHull(wrenches)