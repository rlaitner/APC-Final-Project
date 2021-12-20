# APC 524 Final Project

![Tests](https://github.com/rlaitner/APC-Final-Project/actions/workflows/tests.yml/badge.svg)

This library can be installed with
```pip install -e .```
from the top directory if already cloned. Otherwise, use: 
``` pip install git+https://github.com/rlaitner/APC-Final-Project.git ```



# README 

## About 

This software package aims to enable users to explore the trade-offs of utilizing
different path-planning algorithms with different vehicles in both static and
dynamic environment.

## Contents of this Library: 
1. Main Code
	1. Path-Finding Algorithms
	2. Obstacle Class
	3. Vehicle Class
	4. Agent Class
	5. Environment Class
	6. Simulator Class    
2. Automated Testing 
3. Sample Config Files 
4. Documentation 
	1. See /docs for Sphinx 

## Usage 
User provides config file with adjusted parameters. 

 
## Build Sphinx Documentation 
If you do not already have Sphinx installed please see [Sphinx Installation](https://www.sphinx-doc.org/en/master/usage/installation.html)
for installation directions for your operating system. 

Ensure you are located in the ``doc`` directory and choose either ``make html``
or ``make latexpdf`` for output options. Output will be located in the ``build``
directory.   

## Project Status

Version 1.0

## More Info: 
- See Sphinx documentation for more in-depth review of contents
- Access our report [here](https://www.overleaf.com/read/nrsvyhfggrbr)
 
