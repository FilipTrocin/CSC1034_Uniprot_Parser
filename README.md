Overview
====================
I have realised that project as a part of my univeristy course in the first year as an introduction to biocomputing.

This package allows you analyse proteins sequences from uniprot.org and count the 
average number of a single protein. Moreover, it can produce a bar chart and 
pie chart using matplotlib.


PREREQUISITES
=============
Make sure you use Python in version 3.7

In order to make it running you have to install the following packages:

*  pipenv
*  biopython
*  matplotlib



INSTALLING PACKAGES
===================
1. Open PyCharm
2. On the very bottom in the right corner click on the Python version (should be 
   Python 3.7), then select "Interpreter Settings"
3. So as to add the package, click on the plus icon which should be located next 
   to the "Project Interpreter" section
4. In the search window on the top write desirable package
5. Select it
6. Install it using "Install Package" button


Every package is been installed in the same way as the above example provided

RUNNING
=======

1. Open Terminal
2. In terminal window type: "pipenv run python uniplot.py (here comes function)"
3. Swap "(here comes function)" expression onto the real function such as: "-h" or "--help", "dump", "list", "average", "plot-average-by-taxa-bar-chart", "plot-average-by-taxa-pie-chart"
4. Press enter
5. Enter the file path
6. Press enter again
