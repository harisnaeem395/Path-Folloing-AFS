# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 20:02:50 2022

@author: Haris
"""

import unittest
from Path_following_task import getpoints

class TestPoints (unittest.TestCase):
    
    def test_point_int (self):
        
        self.assertAlmostEqual(getpoints(10,20), 21.6)
        self.assertAlmostEqual(getpoints(0,0), 0)
        
    def test_values(self):
        self.assertRaise(ValueError, getpoints, (-2,-4))
        self.assertRaise(ValueError, getpoints, (2+j,-4-j))
        
        
        #self.assertAlmostEqual(getpoints(-1,-2), 0)
        
    #def test_point_

if __name__== "__main__":    
    unittest.main()