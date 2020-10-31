from unittest import TestCase
import gauged_inflow
import math
import os
import pandas as pd
import matplotlib.pyplot as plt
import filecmp


class Test(TestCase):
    def test_transpose_csv(self):
        ws = './workspace/models/la_routing'
        csv_file = os.path.join(ws, 'la_flows.CSV')
        csv_out = os.path.join(ws, 'inflow.csv')
        start_date = '1/1/2014'
        gauged_inflow.transpose_csv(csv_file, csv_out, start_date, suffix='(Flow)', sec_field='TIME')

        df = pd.read_csv(csv_out, parse_dates=True)
        df['_dt'] = df.apply(lambda x: '%s %s' % (x['_date'], x['_time']), axis=1)
        df['_dt'] = pd.to_datetime(df['_dt'])

        df2 = df.loc[df['STATION'] == ' CBMHB1134', ['_dt', 'FLOW']]
        df2['FLOW'] = pd.to_numeric(df2['FLOW']) #, errors='ignore')
        # print(df2.describe())
        assert(math.fabs(df2['FLOW'].sum() - df2['FLOW'].sum()) < 0.01)
        print(df2['FLOW'].sum())
        df2.plot(x='_dt', y='FLOW')
        plt.show()

    def test_gauged_inflow_xpx(self):
        ws = './workspace/models/la_routing'
        xpx_file = os.path.join(ws, 'gauged_inflow.xpx')
        xpx_file_check = os.path.join(ws, 'gauged_inflow_check.xpx')
        file_path = r'c:\temp\inflow.csv'#os.path.join(ws, 'inflow.csv')
        node_name_field = 'STATION'
        file_format = 'INFLOW'
        gauged_inflow.gauged_inflow_xpx(xpx_file, node_name_field, file_path, file_format)
        assert(filecmp.cmp(xpx_file_check, xpx_file))
