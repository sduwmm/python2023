import pyspedas
import os
#import pytplot
from pytplot import tplot_options
from pytplot import tplot
from pytplot import del_data
from pytplot import time_string
import matplotlib.pyplot as plt
from pyspedas import time_double
from pytplot import options, xlim, ylim, zlim, tplot,tplot_options

figPath= 'C:/OneDrive - mail.sdu.edu.cn/ft_overview/'
trange=['2015-10-07/11:44:13','2015-10-07/11:44:40']
trange=['2015-10-07/11:44:13','2015-10-07/11:45:10']
trange=['2015-10-07/11:44:39','2015-10-07/11:44:43']

print(trange)

tr=trange[0]

#pngName = figPath+'FT_{}{}{}_{}{}'.format(tr[0:4], tr[5:7], tr[8:10],tr[11:13],tr[14:16])
probes = ['1']
b_data_rate=['brst']
p_data_rate=['brst']

fgm_vars = pyspedas.mms.fgm(trange=trange, probe=probes, level='l2', data_rate=b_data_rate,time_clip=True)
dis_moms_vars = pyspedas.mms.fpi(trange=trange, probe=probes, level='l2', data_rate='brst', datatype='dis-moms',time_clip=True)
edp_vars = pyspedas.mms.edp(trange=trange, probe=probes, level='l2', data_rate=b_data_rate, datatype='dce',time_clip=True)
dis_dist_vars = pyspedas.mms.fpi(trange=trange, probe=probes, level='l2', data_rate='brst', datatype='dis-dist',time_clip=False)

tplot_options('wsize', [5000, 500])
tplot(['mms1_fgm_b_gse_brst_l2_bvec', \
                'mms1_fgm_b_gse_brst_l2_btot', \
                'mms1_dis_energyspectr_omni_brst', \
                'mms1_dis_numberdensity_brst',\
                'mms1_dis_bulkv_gse_brst',\
                'mms1_edp_dce_gse_brst_l2'], \
                xsize=16, \
                ysize=9, \
                save_png=('prl'),display=True)
xlim(time_double(trange[0]),time_double(trange[1]))
del_data('*')

