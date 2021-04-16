import pandas as pd
import os


TMP = """
GLDBITEM Rainfall "{station}"
GLDBDATA R_TRAIN "Rainfall" "{station}" {len} {r_train}
GLDBDATA R_KTYPE "Rainfall" "{station}" 1 "1"
GLDBDATA R_RAIN "Rainfall" "{station}" {len} {r_rain}
GLDBDATA R_ROPT "Rainfall" "{station}" 1 "0"
GLDBDATA R_RMULTV "Rainfall" "{station}" 1 1.000
GLDBDATA R_KPREPV "Rainfall" "{station}" 1 "2"
GLDBDATA R_KTIMEV "Rainfall" "{station}" 1 "0"
GLDBDATA R_RAINSMTH "Rainfall" "{station}" 1 1
GLDBDATA R_RAINSYR "Rainfall" "{station}" 1 2021
GLDBDATA R_RAINSHR "Rainfall" "{station}" 1 0
GLDBDATA R_RAINSMIN "Rainfall" "{station}" 1 0
GLDBDATA R_RAINSSEC "Rainfall" "{station}" 1 0
GLDBDATA R_RAINSDAY "Rainfall" "{station}" 1 1
GLDBDATA R_DRAIN "Rainfall" "{station}" {len} {r_drain}

"""
def csv_to_rainfall_xpx(csv_path, xpx_path):
    """ csv format as below
STATION	R_TRAIN	R_DRAIN	R_RAIN
A	0	5	0.06
A	5	5	0.06
A	10	6	0.06

    """
    with open(xpx_path, 'w') as o:

        df = pd.read_csv(csv_path, dtype=object)
        for station in df['STATION'].unique():
            df2 = df.loc[df['STATION']==station]
            ct = len(df2['R_RAIN'])
            r_rain = ' '.join([str(x) for x in df2['R_RAIN']])
            r_train = ' '.join([str(x) for x in df2['R_TRAIN']])
            r_drain = ' '.join([str(x) for x in df2['R_DRAIN']])
            o.write(TMP.format(station=station, len=ct, r_train=r_train, 
            r_rain=r_rain, r_drain=r_drain))




if __name__ == '__main__':
    ws = r'C:\Users\Mel.Meng\Documents\GitHub\xpswmm\models\rainfall_xpx'
    csv_path = os.path.join(ws, 'sample_data.csv')
    xpx_path = os.path.join(ws, 'sampe_xpx.xpx')
    csv_to_rainfall_xpx(csv_path, xpx_path)


