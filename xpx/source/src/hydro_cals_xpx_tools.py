import pandas as pd
import numpy as np
import datetime
import os


def read_csv(f):
    df = pd.read_csv(f, skiprows=9).dropna()
    df['hour'] = pd.to_numeric(df['Time (min)'])/60.0
    df['data'] = df['Clear Peak Flow Rate (cfs)']
    df.index = df['hour']
    return df.loc[:, ['data']]

def scan_csv(root, out_csv):
    rows = []
    for root, dirs, files in os.walk(root):
        for f in files:
            a, b = os.path.splitext(f)
            if b.lower() == '.csv':
                node_name = a.split('-')[2]
                full_path = os.path.join(root, f)
                rows.append([node_name, full_path])
    pd.DataFrame(rows, columns=['node_name', 'file_path']).to_csv(out_csv)

def merge_csv(root, out_csv):
    df_join = None
    for root, dirs, files in os.walk(root):
        for f in files:
            a, b = os.path.splitext(f)
            if b.lower() == '.csv':
                
                node_name = a.split('-')[2]
                df = read_csv(os.path.join(root, f))
                df[node_name] = df['data']
                del df['data']
                if df_join is None:
                    df_join = df
                else:
                    df_join = df_join.join(df, lsuffix='l')
                
    
    df_join.to_csv(out_csv, index_label='hour')
        


def read_hydrograph(csv_path, datetime_fld='datetime', date_format='%d%b%Y  %H%M'):
    df = pd.read_csv(csv_path)
    df['dt'] = df[datetime_fld].apply(lambda x: datetime.datetime.strptime(x, date_format))
    t0 = min(df['dt'].values)
    df['hour'] = df['dt'].apply(lambda x: (x - t0).days * 24 + (x - t0).seconds / 3600.0)
    del df['dt']
    return df


def import_hydrograph(hydro_csv, xpx_path):
    df = pd.read_csv(hydro_csv)
    hours = df['hour'].values
    ct = len(hours)
    hours_list = ' '.join([str(x) for x in hours])
    with open(xpx_path, 'w') as o:
        for fld in df.columns:
            if fld in ['hour']:
                pass
            else:
                values = df[fld].values
                values = ' '.join([str(x) for x in values])

                o.write('DATA INQ "%s" 0 1 1\n' % fld)
                o.write('DATA TEO "%s" 0 %s %s\n' % (fld, ct, hours_list))
                o.write('DATA QCARD "%s" 0 %s %s\n' % (fld, ct, values))


if __name__ == '__main__':
   
    # the root folder where all the CSV files are
    root = r'C:\temp\support\00416850\To MEL'
    # the csv file with all the time series in it
    out_csv = r'C:\temp\support\00416850\merged.csv'
    merge_csv(root, out_csv)

    # out_csv = r'C:\temp\support\00416850\file_list.csv'
    # scan_csv(root, out_csv)
    hydro_csv = out_csv
    # the xpx file converted from the csv file
    xpx_path = r'C:\temp\support\00416850\merged.xpx'
    import_hydrograph(hydro_csv, xpx_path)
    

