from unittest import TestCase
import gauged_inflow
import os
import pandas as pd
import matplotlib.pyplot as plt

class Test(TestCase):
    def test_transpose_csv(self):
        ws = './workspace/models/la_routing'
        csv_file = os.path.join(ws, 'la_flows.CSV')
        csv_out = os.path.join(ws, 'inflow.csv')
        start_date = '1/1/2014'
        gauged_inflow.transpose_csv(csv_file, csv_out, start_date, suffix='(Flow)', sec_field='TIME')

        # df = pd.read_csv(csv_out, parse_dates=True)
        # df.index = df['_dt']
        # df[df['STATION'] == 'CBLAC0571'].plot()
        # plt.show()
        self.fail()
    def test_gauged_inflow_xpx(self):
        ws = './workspace/models/la_routing'
        xpx_file = os.path.join(ws, 'gauged_inflow.xpx')
        file_path = r'c:\temp\inflow.csv'#os.path.join(ws, 'inflow.csv')
        node_name_field = 'STATION'
        file_format = 'INFLOW'
        gauged_inflow.gauged_inflow_xpx(xpx_file, node_name_field, file_path, file_format)
        self.fail()
