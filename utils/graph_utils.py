
"""BAR_COLORS contant list containing the colors for the bars in graph"""

BAR_COLORS = ['#809FFF', "#FF875B", '#C0C0C0', '#FFBF00', '#0012C2', '#31BA00', '#0A277f', '#A42C00', '#525659']


def create_graph_indicator(graph_layout, timeseries_name=None, line=False):
    """
                            Create the colors indicators for the bars or lines in the graph
    :param graph_layout:
    :param timeseries_name:
    :param line:
    :return:
    """
    from PyQt5 import QtWidgets, QtCore
    graph_indicator_layout = QtWidgets.QHBoxLayout()

    if line:
        """
            Used in analysis module to create the line color indicator 
        """
        indicator_timeseries = QtWidgets.QLabel()
        indicator_timeseries.setText("             --o--")
        indicator_timeseries.setStyleSheet("color:red;")

        lbl_timeseries = QtWidgets.QLabel()
        lbl_timeseries.setText(timeseries_name+"\t\t")
        lbl_timeseries.setStyleSheet("color:black;")

        indicator_standard = QtWidgets.QLabel()
        indicator_standard.setText("--o--")
        indicator_standard.setStyleSheet("color:blue;")

        lbl_standard = QtWidgets.QLabel()
        lbl_standard.setText("standard"+"\t\t")
        lbl_standard.setStyleSheet("color:black;")

        graph_indicator_layout.addWidget(indicator_timeseries)
        graph_indicator_layout.addWidget(lbl_timeseries)
        graph_indicator_layout.addWidget(indicator_standard)
        graph_indicator_layout.addWidget(lbl_standard)
        graph_layout.addLayout(graph_indicator_layout)

    else:
        """
            Used in evaluation module to create the bar color indicator 
        """
        for index in range(9):

            lbl = QtWidgets.QLabel()
            lbl.setText("D" + str(index + 1))

            indicator = QtWidgets.QPushButton()
            indicator.setStyleSheet("background-color:" + BAR_COLORS[index] + ";")
            indicator.setObjectName("indicator" + str(index))

            graph_indicator_layout.addWidget(indicator)
            graph_indicator_layout.addWidget(lbl)

        graph_layout.addLayout(graph_indicator_layout)
