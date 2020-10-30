import pandas as pd
import os
import logging
import datetime
FORMAT = '%(asctime)-15s %(lineno)s:  %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)



def transpose_csv(csv_file, csv_out, start_date, suffix='(Flow)', sec_field='TIME'):
    """
    convert the format of
    TIME, NODE1(Flow), NODE2(Flow)
    0, 0, 0
    60, 0.1, 0.2,
    120, 0.3, 0.1
    ...
    to
    TIME, STATION, FLOW
    0, NODE1, 0
    60, NODE1, 0.1
    120, NODE1, 0.3
    0, NODE2, 0
    60, NODE2, 0.2
    120, NODE2, 0.1

    :param csv_file:
    :param suffix:
    :param sec_field:
    :return:
    """
    df = pd.read_csv(csv_file)
    df['_dt'] = df.apply(lambda x: datetime.timedelta(seconds=x[sec_field]) + pd.to_datetime(start_date), axis=1)
    df['_date'] = df.apply(lambda x: x['_dt'].strftime('%m/%d/%Y'), axis=1)
    df['_time'] = df.apply(lambda x: x['_dt'].strftime('%H:%M'), axis=1)
    idx = df[sec_field]
    results = []
    for fld in df.columns:
        if fld in [sec_field, '_dt', '_date', '_time', sec_field]:
            continue

        node_name = fld.replace(suffix, '')
        logging.info('processing node: %s' % fld)
        if fld.startswith(suffix):
            logging.info('no node name, ignore: %s' % fld)
        else:
            df['STATION'] = node_name
            df['FLOW'] = df[fld]
            results.append(df.loc[:, ['_date','_time',  'STATION', 'FLOW']])

    pd.concat(results).to_csv(csv_out, index=False)
    logging.info('converted csv saved to: %s' % csv_out)



def gauged_inflow_xpx(xpx_file, node_name_field, file_path, file_format):

    tmp = """DATA UDFS_FILE "{node}" 0 1 "{file}" 
DATA R_UDFS_FMTNAME "{node}" 0 1 "{file_format}" 
DATA GINFLOW "{node}" 0 1 1
DATA UDFS_STN "{node}" 0 1 "{node}"
"""
    df = pd.read_csv(file_path)
    file_path = os.path.abspath(file_path)
    with open(xpx_file, 'w') as o:
        for node in df[node_name_field].unique():
            o.write(tmp.format(node=node, file=file_path, file_format=file_format))
            logging.info('write line for node: %s' % node)
    logging.info('xpx saved to: %s' % xpx_file)



if __name__ == '__main__':
    # step 1 run the run the LA hydrology and generate the *.syr runoff flow interface file
    # step 2 use the interface file to convert the sry to csv file
    # step 3 run the following scripts to generate the following file

    # this is the csv file converted from the interface file
    csv_file = r'c:\temp\la_routing\la_flows.csv'
    # this is the csv file used as the gauged inflow file
    csv_out = r'c:\temp\la_routing\inflow.csv'
    start_date = '1/1/2014'

    # this script will convert the csv to a date, time station flow csv file
    transpose_csv(csv_file, csv_out, start_date, suffix='(Flow)', sec_field='TIME')
    # step 4 set up the INFLOW format for the gauged inflow file in the model
    # step 5 generate the xpx file to setup the gauged inflow

    xpx_file = r'c:\temp\la_routing\gauged_inflow.xpx' # xpx file path
    file_path = r'c:\temp\la_routing\inflow.csv' # gauged inflow path
    node_name_field = 'STATION' # the field name in the gauged inflow for node name
    file_format = 'INFLOW' # the format setup in the XP model
    gauged_inflow_xpx(xpx_file, node_name_field, file_path, file_format)