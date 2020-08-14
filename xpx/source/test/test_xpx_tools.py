from src import xpx_tools
import math


class TestXpx_tools:
    def test_read_hydrograph(self):
        f = './../test/data/sample_output.csv'
        date_fld = 'datetime'
        df = xpx_tools.read_hydrograph(f, date_fld)
        assert (math.fabs(max(df['hour'].values) - 23.916666666666) < 0.001)

    def test(self):
        f = './../test/data/sample_output.csv'
        date_fld = 'datetime'
        xpx = './../test/data/sample.xpx'

        xpx_tools.import_hydrograph(f, xpx, date_fld)
        assert False
