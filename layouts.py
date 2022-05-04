#layouts.py
#Rhiannon MacCreadie
#04.05.2022
# Practice making layouts for class

# Initialising
import sys
from PySide6 import QtWidgets
from PySide6 import QtCore

app = QtWidgets.QApplication()

window = QtWidgets.QMainWindow()
window.setWindowTitle("Layouts")
window.setGeometry(600, 600, 200, 100)

window.setCentralWidget(QtWidgets.QWidget())

# Layout One
"""
# Define Layouts
hbox_layout = QtWidgets.QHBoxLayout()
# Sub Layout
vbox_layout = QtWidgets.QVBoxLayout()

# Set Main Layout
window.centralWidget().setLayout(hbox_layout)

# Define Widget
left_widget = QtWidgets.QWidget()
# Set Widget Layout
left_widget.setLayout(vbox_layout)

# Label and place top widget
top_left_widget = QtWidgets.QLabel('Widget 1')
vbox_layout.addWidget(top_left_widget)

# Label and place bottom widget
bottom_left_widget = QtWidgets.QLabel('Widget 2')
vbox_layout.addWidget(bottom_left_widget)

# Place vertical widgets into main widget
hbox_layout.addWidget(left_widget)

# Label and Place right Widget
right_widget = QtWidgets.QLabel('Widget 3')
hbox_layout.addWidget(right_widget)
"""

# Layout Two
"""
# Define Layouts
# Main Layout
hbox_layout = QtWidgets.QHBoxLayout()
# Sub Layout
top_layout = QtWidgets.QHBoxLayout()
left_layout = QtWidgets.QVBoxLayout()
right_layout = QtWidgets.QVBoxLayout()

# Set main alignment to centre
center = QtCore.Qt.AlignCenter
# Set main layout
window.centralWidget().setLayout(hbox_layout)

# Define Widgets
top_widget = QtWidgets.QWidget()
left_widget = QtWidgets.QWidget()
right_widget = QtWidgets.QWidget()

# Set Sub Layouts
top_widget.setLayout(top_layout)
left_widget.setLayout(left_layout)
right_widget.setLayout(right_layout)

# Left Side Widgets
# Top Left widgets
# Label and add top left widget
top_left_widget = QtWidgets.QLabel('Widget 1')
top_left_widget.setAlignment(center)
top_layout.addWidget(top_left_widget)

# Label and add top centre widget
top_centre_widget = QtWidgets.QLabel('Widget 2')
top_centre_widget.setAlignment(center)
top_layout.addWidget(top_centre_widget)

# Add widget to left side widgets
left_layout.addWidget(top_widget)

# Bottom Left Widget
# Label and add bottom left widget
bottom_left_widget = QtWidgets.QLabel('Widget 3')
bottom_left_widget.setAlignment(center)
left_layout.addWidget(bottom_left_widget)

# Add left side widgets to main widget
hbox_layout.addWidget(left_widget)

# Right Side Widgets
# Label and add top right widget
top_right_widget = QtWidgets.QLabel('Widget 4')
top_right_widget.setAlignment(center)
right_layout.addWidget(top_right_widget)

# Label and add bottom right widget
bottom_right_widget = QtWidgets.QLabel('Widget 5')
bottom_right_widget.setAlignment(center)
right_layout.addWidget(bottom_right_widget)

# Add right side widgets to main widget
hbox_layout.addWidget(right_widget)
"""
# Layout Three
"""
# Define Layouts
# Main Layout
hbox_layout = QtWidgets.QHBoxLayout()
# Sub Layouts
top_layout = QtWidgets.QHBoxLayout()
bottom_layout = QtWidgets.QHBoxLayout()
left_layout = QtWidgets.QVBoxLayout()
right_layout = QtWidgets.QVBoxLayout()

center = QtCore.Qt.AlignCenter
window.centralWidget().setLayout(hbox_layout)

# Define Widgets
top_widget = QtWidgets.QWidget()
left_widget = QtWidgets.QWidget()
bottom_widget = QtWidgets.QWidget()
right_widget = QtWidgets.QWidget()

# Set Widget Layouts
right_widget.setLayout(right_layout)
bottom_widget.setLayout(bottom_layout)
left_widget.setLayout(left_layout)
top_widget.setLayout(top_layout)

# Left Side Widgets
# Top left Widgets
top_left_widget = QtWidgets.QLabel('Widget 1')
top_left_widget.setAlignment(center)
top_layout.addWidget(top_left_widget)

top_centre_widget = QtWidgets.QLabel('Widget 2')
top_centre_widget.setAlignment(center)
top_layout.addWidget(top_centre_widget)

# Add Top left Widgets into Left side widget
left_layout.addWidget(top_widget)

# Bottom Left Widgets
bottom_left_widget = QtWidgets.QLabel('Widget 3')
bottom_left_widget.setAlignment(center)
bottom_layout.addWidget(bottom_left_widget)

bottom_center_widget = QtWidgets.QLabel('Widget 4')
bottom_center_widget.setAlignment(center)
bottom_layout.addWidget(bottom_center_widget)

# Add Bottom left Widgets into Left side widget
left_layout.addWidget(bottom_widget)

# Add Left Widgets into main widget
hbox_layout.addWidget(left_widget)

# Right Side Widgets
top_right_widget = QtWidgets.QLabel('Widget 5')
top_right_widget.setAlignment(center)
right_layout.addWidget(top_right_widget)

center_right_widget = QtWidgets.QLabel('Widget 6')
center_right_widget.setAlignment(center)
right_layout.addWidget(center_right_widget)

bottom_right_widget = QtWidgets.QLabel('Widget 7')
bottom_right_widget.setAlignment(center)
right_layout.addWidget(bottom_right_widget)

# Add Right Widgets into main widget
hbox_layout.addWidget(right_widget)
"""

# Output Code
window.show()

app.exec_()