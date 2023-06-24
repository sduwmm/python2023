import pyspedas
import os
import pytplot
from pytplot import time_string
import matplotlib.pyplot as plt

figPath= 'C:/Users/20171/OneDrive - mail.sdu.edu.cn/AAA_worklog_2023/paper_whistler_figure/paperList/'
fileName=open('C:/Users/20171/OneDrive - mail.sdu.edu.cn/AAA_worklog_2023/paper_whistler_figure/paperList/list.txt','r')


line = fileName.readline()
while line:
    #print(line, end = '')
    line = fileName.readline()
    #print(line)
    print(type(line))
    print(line[8:29])
    '''
    '''
    trange=[line[9:28],line[31:51]]
    print(trange)

    tr=trange[0]

    pngName = figPath+'FT_{}{}{}_{}{}'.format(tr[0:4], tr[5:7], tr[8:10],tr[11:13],tr[14:16])
    probes = ['1']
    b_data_rate=['brst']
    p_data_rate=['brst']

    fgm_vars = pyspedas.mms.fgm(trange=trange, probe=probes, level='l2', data_rate=b_data_rate,time_clip=True)
    dis_moms_vars = pyspedas.mms.fpi(trange=trange, probe=probes, level='l2', data_rate='brst', datatype='dis-moms',time_clip=True)

    pytplot.tplot_options('wsize', [1600, 900])
    pytplot.tplot(['mms1_fgm_b_gse_brst_l2_bvec', \
                   'mms1_fgm_b_gse_brst_l2_btot', \
                   'mms1_dis_energyspectr_omni_brst', \
                   'mms1_dis_numberdensity_brst',\
                   'mms1_dis_bulkv_gse_brst'], \
                  xsize=16,\
                  ysize=9,\
                  save_png=(pngName),display=False)
    #pytplot.tplot.close()
    #plt.close()
    pytplot.del_data('*')