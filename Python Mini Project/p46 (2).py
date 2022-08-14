# Treemap using Python
# A treemap is used to visualize hierarchical data as a set of nested rectangles. 
# It is a data visualization tool for displaying data structured in a tree structure using nested rectangles.

import plotly.graph_objects as go

fig = go.Figure(go.Treemap(
    labels = ["A","B", "C", "D", "E", "F", "G", "H", "I"],
    parents = ["", "A", "A", "C", "C", "A", "A", "G", "A"]
))

fig.show()