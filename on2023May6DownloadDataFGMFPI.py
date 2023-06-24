import pyspedas
import os
import pytplot
from pytplot import time_string

figPath= 'D:\OneDrive - mail.sdu.edu.cn/ft_overview/'
trange=['2017-11-13/13:50', '2017-11-13/13:53']#not FT
trange=['2015-12-28/04:27','2015-12-28/04:30']
trange=['2017-11-17/13:13:00','2017-11-17/13:14']
#trange=time_string([tr[0] - 60., tr[0] + 180.])

tr=trange[0]

pngName = figPath+'FT_{}{}{}_{}{}'.format(tr[0:4], tr[5:7], tr[8:10],tr[11:13],tr[14:16])
probes = ['1']
b_data_rate=['brst']
p_data_rate=['brst']

fgm_vars = pyspedas.mms.fgm(trange=trange, probe=probes, level='l2', data_rate=b_data_rate,time_clip=True)
dis_moms_vars = pyspedas.mms.fpi(trange=trange, probe=probes, level='l2', data_rate='brst', datatype='dis-moms',time_clip=True)

pytplot.tplot_options('wsize', [1000, 500])
pytplot.tplot(['mms1_fgm_b_gse_brst_l2_bvec', \
               'mms1_fgm_b_gse_brst_l2_btot', \
               'mms1_dis_energyspectr_omni_brst', \
               'mms1_dis_numberdensity_brst',\
               'mms1_dis_bulkv_gse_brst'], \
              save_png=(pngName))

pytplot.del_data('*')
