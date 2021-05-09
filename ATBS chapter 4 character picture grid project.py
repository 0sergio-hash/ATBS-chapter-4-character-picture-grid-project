#!/usr/bin/env python
# coding: utf-8

# # Instructions for this project at the Automate the boring stuff with python [website](https://automatetheboringstuff.com/2e/chapter4/).

# **The purpose of this project was to print the provided grid column by column to show the pattern**

# In[1]:


# Practice project: Character picture grid

grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]

# Print picture in grid
try:
    for x in range(len(grid[:])):
        for y in range(len(grid)):
            print(grid[y][x], end = '')
        print()

# Previous code printed except it kept trying to go to index [0][6] or the 6th column that doesn't exist
# so the except statement ends the execution before that happens 
except: 
    pass


# In[ ]:




