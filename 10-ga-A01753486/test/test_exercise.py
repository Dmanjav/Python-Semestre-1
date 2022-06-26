#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 18:38:00 2020

@author: avmejia
"""

import pytest
import src.genetico


def test_crossover():
    assert src.genetico.cruzamiento([0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], 5) == [
        [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 0]]
    assert src.genetico.cruzamiento([0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], 1) == [
        [0, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0]]
