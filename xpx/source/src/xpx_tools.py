import pandas as pd
import numpy as np
import datetime
import os


def read_hydrograph(csv_path, datetime_fld='datetime', date_format='%d%b%Y  %H%M'):
    df = pd.read_csv(csv_path)
    df['dt'] = df[datetime_fld].apply(lambda x: datetime.datetime.strptime(x, date_format))
    t0 = min(df['dt'].values)
    df['hour'] = df['dt'].apply(lambda x: (x - t0).days * 24 + (x - t0).seconds / 3600.0)
    del df['dt']
    return df


def import_hydrograph(hydro_csv, xpx_path, datetime_fld='datetime', date_format='%d%b%Y  %H%M'):
    df = read_hydrograph(hydro_csv, datetime_fld, date_format)
    hours = df['hour'].values
    ct = len(hours)
    hours_list = ' '.join([str(x) for x in hours])
    with open(xpx_path, 'w') as o:
        for fld in df.columns:
            if fld in ['dt', datetime_fld]:
                pass
            else:
                values = df[fld].values
                values = ' '.join([str(x) for x in values])

                o.write('DATA INQ "%s" 0 1 1\n' % fld)
                o.write('DATA TEO "%s" 0 %s %s\n' % (fld, ct, hours_list))
                o.write('DATA QCARD "%s" 0 %s %s\n' % (fld, ct, values))


if __name__ == '__main__':
    # for help: https://medium.com/@mel.meng.pe/batch-hydrographs-into-xpswmm-a9303df7a46b
    # the hydrograph csv file path, e.g. c:\temp\hydrograph.csv
        # first column should be datetime and the date format is: 01Jun2007  0010
        # other columns should have the node name in XPSWMM/XPSTORM as the header
        # datetime,Node1,Node2,Node3
        # 01Jun2007  0000,0,0,0
        # 01Jun2007  0005,0.023,0.04,0.014
        # 01Jun2007  0010,0.107,0.17,0.065
        # 01Jun2007  0015,0.268,0.45,0.162

    hydrograph_csv = r'C:\Users\Mel.Meng\Documents\GitHub\xpswmm\xpx\source\test\data\sample_output.csv'
    # the frist column name
    date_fld = 'datetime'
    # date time format , for more information: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
    date_format = '%d%b%Y  %H%M'

    # path to the xpx file, which will be used to import the time series into XPSWMM
    output_xpx = r'C:\Users\Mel.Meng\Documents\GitHub\xpswmm\xpx\source\test\data\sample.xpx'


    import_hydrograph(hydrograph_csv, output_xpx, date_fld, date_format)

