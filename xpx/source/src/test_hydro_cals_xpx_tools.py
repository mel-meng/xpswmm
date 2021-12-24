from hydro_cals_xpx_tools import *


def test_look_csv():
    root = r'C:\Users\Mel.Meng\Documents\GitHub\xpswmm\xpx\source\test\data\csv_folder\csv_results'
    look_csv(root)

def test_read_csv():
    root = r'C:\Users\Mel.Meng\Documents\GitHub\xpswmm\xpx\source\test\data\csv_folder\csv_results'
    f = os.path.join(root, 'Rubio Wash - DA -0- 50YR.csv')
    df = read_csv(f)
    print(df)
    assert False
