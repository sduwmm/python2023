'''
https://blog.csdn.net/whatday/article/details/108923273
'''
import pyspedas
import os
import pytplot


trange=['2022-01-16/11:59:55','2022-01-16/12:01:00']
trange=['2016-12-25T15:59:18','2016-12-25/16:20:20']
trange = ['2019-01-18/21:03:00', '2019-01-18/21:04:13']
trange=['2019-01-05/17:37:53','2019-01-05/17:41:53']
trange=['2023-01-23/03:17:33','2023-01-23/03:44:43']
trange = ['2015-10-16/13:05:40', '2015-10-16/13:07:25']#; Burch et al., Science event

trange=['2021-03-20/19:29:35','2021-03-20/19:29:50']
trange=['2015-10-07/11:44:13','2015-10-07/11:44:40']
trange=['2015-11-30/00:23:00','2015-11-30/00:25:00']
trange=['2017-10-24/08:25:00','2017-10-24/08:27:00']
trange=['2015-10-30/05:15:00','2015-10-30/05:16:00']
trange=['2023-01-23/03:00:00','2023-01-23/04:00:00']

###
Stime=trange[0]
pngDir='C:/2021_fb_hfa/'
if not os.path.exists(pngDir):
        os.makedirs(pngDir)
pngName=pngDir+'burst_all_mms1_summ_{}{}{}_{}{}{}'.format(Stime[0:4], Stime[5:7], Stime[8:10], Stime[11:13], Stime[14:16], Stime[17:19])
###

probe = ['1']
probes=['1','2','3','4']
#probes=['1']
b_data_rate=['brst','srvy']
p_data_rate=['brst','fast']

des_dist_vars = pyspedas.mms.fpi(trange=trange, probe=probes, level='l2', data_rate='brst', datatype='des-dist',time_clip=False)

pytplot.del_data('*')



