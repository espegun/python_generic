# How to Tkinter 

## Understanding the grid manager
[Grid manager tutorial](https://www.pythontutorial.net/tkinter/tkinter-grid/)  

* The intersection of a row and column is called a *cell*. Every cell can only contain one *widget*, but this could be a *Frame*, which could have sub-widgets.
* The height of a row and width of a column depends on highest and widest widget in it, respectively.
* Using `rowspan` or `columnspan` > 1, cells can span more than one row/column.

*Is this the actual algorithm*.
1. Specify the `height`and `width` for those widgets which needs it specified.
2. Specify the `weight` of each row and column, determining their relative height and width.
3. Given the above, the Geometry manager will calculate the actual height and width of each row and column (and the cells in their intersections).
4. Then all the widgets should be placed in their cells. Always specify `sticky` for the alignment of the width within the cell. `ns` and `ew` will stretch the widget to fill the cell, vertically and horizontally. 


## Sources
[Tkinter tutorial @ RealPython](https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter)  
[Tkinter @ Tutorialspoint](https://www.tutorialspoint.com/python/python_gui_programming.htm) Very structured when looking up colors, widgets, geometry managers.  
[Tkinter topic by topic](https://python-course.eu/tkinter/)  
[Tkinter event types](https://python-course.eu/tkinter/events-and-binds-in-tkinter.php)  

