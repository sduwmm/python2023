import pyspedas
import os
#import pytplot
from pytplot import tplot_options
from pytplot import tplot
from pytplot import del_data
from pytplot import time_string
import matplotlib.pyplot as plt

figPath= 'C:/OneDrive - mail.sdu.edu.cn/ft_overview/'
fileName=open("C:/OneDrive - mail.sdu.edu.cn/ft_overview/tlist.txt",'r')


line = fileName.readline()
while line:
    #print(line, end = '')
    line = fileName.readline()
    print(line)
    year=line[0:4]
    #print(year)
    month=line[5:7]
    day =line[8:10]
    hour  =line[11:13]
    minute=line[14:16]
    #print(minute)
    second=line[17:19]
    second='00'
    timeSpan=2###in minutes
    minutePlus=str(int(minute)+timeSpan)
    if int(minute)+timeSpan >= 60:
        minutePlus = str(int(minute) + timeSpan -60)
        hourPlus   = str(int(hour) + 1)
    else:
        minutePlus = str(int(minute) + timeSpan)
        hourPlus   = hour
    '''
    '''
    trange=[year+'-'+month+'-'+day+'/'+hour+':'+minute+':'+second,\
            year+'-'+month+'-'+day+'/'+hourPlus+':'+minutePlus+':'+second]
    print(trange)

    tr=trange[0]

    pngName = figPath+'FT_{}{}{}_{}{}'.format(tr[0:4], tr[5:7], tr[8:10],tr[11:13],tr[14:16])
    probes = ['1']
    b_data_rate=['brst']
    p_data_rate=['brst']

    fgm_vars = pyspedas.mms.fgm(trange=trange, probe=probes, level='l2', data_rate=b_data_rate,time_clip=True)
    dis_moms_vars = pyspedas.mms.fpi(trange=trange, probe=probes, level='l2', data_rate='brst', datatype='dis-moms',time_clip=True)

    tplot_options('wsize', [1000, 500])
    tplot(['mms1_fgm_b_gse_brst_l2_bvec', \
                   'mms1_fgm_b_gse_brst_l2_btot', \
                   'mms1_dis_energyspectr_omni_brst', \
                   'mms1_dis_numberdensity_brst',\
                   'mms1_dis_bulkv_gse_brst'], \
                  xsize=16, \
                  ysize=9, \
                  save_png=(pngName),display=False)
    del_data('*')