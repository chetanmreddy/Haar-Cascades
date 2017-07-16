# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 20:19:53 2017

@author: chetan
"""

import numpy as np
import cv2


img = cv2.imread('face-01.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('img',gray)