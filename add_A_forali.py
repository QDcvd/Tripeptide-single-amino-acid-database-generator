# -*- coding: utf-8 -*-
"""
Created on *********

@author: 了不起的田所李
"""
from pymol import cmd
import sys

filename = sys.argv[1]


def addh(pdbfilename):  # 给pdb文件加氢
    cmd.load(pdbfilename + '.pdb')
    cmd.h_add(pdbfilename)
    cmd.sort(pdbfilename + 'extend 1')
    cmd.save(pdbfilename + '_addh.pdb')


if __name__ == '__main__':
    addh(filename)