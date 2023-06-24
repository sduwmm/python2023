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
trange=['2015-12-28/03:57:00','2015-12-28/03:58:00']
trange=['2017-12-01/14:40:33','2017-12-01/14:41:10']
trange=['2018-12-10/04:19:00','2018-12-10/04:20:00']
trange=['2018-01-09/08:34:23','2018-01-09/08:37:03']
trange=['2018-02-04/10:37:00','2018-02-04/10:43:40']
trange=['2019-01-18/21:03:13',        '2019-01-18/21:04:13']
trange=['2018-01-08/06:40:00','2018-01-08/06:43:00']
trange=['2017-12-18/12:36:00','2017-12-18/12:38:00']
trange=['2015-11-04/08:05:00','2015-11-04/08:06:00']
trange=['2017-12-01/14:39:00','2017-12-01/14:41:30']
trange=['2017-12-17/17:53:00','2017-12-17/17:54:00']
trange=['2023-01-23/03:00:00','2023-01-23/04:00:00']
trange=['2023-01-23/06:30:00','2023-01-23/07:30:00']
trange=['2023-01-23/06:00:00','2023-01-23/06:20:00']
trange=['2019-12-06/05:13:54','2019-12-06/05:13:54.700']

###
Stime=trange[0]
pngDir='C:/2021_fb_hfa/'
if not os.path.exists(pngDir):
        os.makedirs(pngDir)
pngName=pngDir+'burst_all_mms1_summ_{}{}{}_{}{}{}'.format(Stime[0:4], Stime[5:7], Stime[8:10], Stime[11:13], Stime[14:16], Stime[17:19])
###

probe = ['1']
probes=['1','2','3','4']
probes=['1']

mec_vars = pyspedas.mms.mec(trange=trange, probe=probes, datatype='epht89d', data_rate='srvy',time_clip=False)
#defatt=pyspedas.mms_load_state(trange=trange, probe=probes)

#brst
fgm_vars = pyspedas.mms.fgm(trange=trange, probe=probes, level='l2', data_rate='brst',time_clip=False)
scm_vars = pyspedas.mms.scm(trange=trange, probe=probes, level='l2', data_rate='brst', datatype='scb',time_clip=False)
#fsm_vars = pyspedas.mms.fsm(trange=trange, probe=probes, data_rate='brst', datatype='scb',time_clip=False)
edp_vars = pyspedas.mms.edp(trange=trange, probe=probes, level='l2', data_rate='brst', datatype='dce',time_clip=False)
dis_moms_vars = pyspedas.mms.fpi(trange=trange, probe=probes, level='l2', data_rate='brst', datatype='dis-moms',time_clip=False)
dis_dist_vars = pyspedas.mms.fpi(trange=trange, probe=probes, level='l2', data_rate='brst', datatype='dis-dist',time_clip=False)
des_moms_vars = pyspedas.mms.fpi(trange=trange, probe=probes, level='l2', data_rate='brst', datatype='des-moms',time_clip=False)


#fast
fgm_vars = pyspedas.mms.fgm(trange=trange, probe=probes, level='l2', data_rate='srvy',time_clip=False)
scm_vars = pyspedas.mms.scm(trange=trange, probe=probes, level='l2', data_rate='srvy', datatype='scsrvy',time_clip=False)
fsm_vars = pyspedas.mms.fsm(trange=trange, probe=probes, data_rate='srvy', datatype='scb',time_clip=False)
edp_vars = pyspedas.mms.edp(trange=trange, probe=probes, level='l2', data_rate='fast', datatype='dce',time_clip=False)
#dis_dist_vars = pyspedas.mms.fpi(trange=trange, probe=probes, level='l2', data_rate='fast', datatype='dis-dist',time_clip=False)
dis_moms_vars = pyspedas.mms.fpi(trange=trange, probe=probes, level='l2', data_rate='fast', datatype='dis-moms',time_clip=False)
des_moms_vars = pyspedas.mms.fpi(trange=trange, probe=probes, level='l2', data_rate='fast', datatype='des-moms',time_clip=False)


#electron dist
des_moms_vars = pyspedas.mms.fpi(trange=trange, probe=probes, level='l2', data_rate='brst', datatype='des-moms',time_clip=False)




mec_vars = pyspedas.mms.mec(trange=trange, probe=probes, data_rate='srvy', datatype='ephts04d',time_clip=False)
mec_vars = pyspedas.mms.mec(trange=trange, probe=probes, data_rate='brst', datatype='ephts04d',time_clip=False)
mec_vars = pyspedas.mms.mec(trange=trange, probe=probes, data_rate='srvy', datatype='epht89q',time_clip=False)
mec_vars = pyspedas.mms.mec(trange=trange, probe=probes, data_rate='brst', datatype='epht89q',time_clip=False)
mec_vars = pyspedas.mms.mec(trange=trange, probe=probes, data_rate='brst', datatype='epht89d',time_clip=False)



edi_vars = pyspedas.mms.edi(trange=trange, probe=probes, data_rate='brst',datatype='efield',time_clip=False)
edi_vars = pyspedas.mms.edi(trange=trange, probe=probes, data_rate='brst',datatype='amb',time_clip=False)

feeps_vars=pyspedas.mms.feeps(trange=trange, probe=probes, data_rate='brst',datatype='ion',time_clip=False)
feeps_vars=pyspedas.mms.feeps(trange=trange, probe=probes, data_rate='brst',datatype='electron',time_clip=False)

eis_vars = pyspedas.mms.eis(trange=trange, probe=probes, data_rate='brst',datatype='extof',time_clip=False)
eis_vars = pyspedas.mms.eis(trange=trange, probe=probes, data_rate='brst',datatype='phxtof',time_clip=False)
eis_vars = pyspedas.mms.eis(trange=trange, probe=probes, data_rate='brst',datatype='electronenergy',time_clip=False)

aspoc_vars=pyspedas.mms.aspoc(trange=trange,probe=probes,data_rate='brst',datatype='asp1')
aspoc_vars=pyspedas.mms.aspoc(trange=trange,probe=probes,data_rate='brst',datatype='asp2')
aspoc_vars=pyspedas.mms.aspoc(trange=trange,probe=probes,data_rate='brst',datatype='aspoc')


hpca_vars=pyspedas.mms.hpca(trange=trange,probe=probes,data_rate='brst',datatype='moments')
hpca_vars=pyspedas.mms.hpca(trange=trange,probe=probes,data_rate='srvy',datatype='moments')
hpca_vars=pyspedas.mms.hpca(trange=trange,probe=probes,data_rate='brst',datatype='ion')
hpca_vars=pyspedas.mms.hpca(trange=trange,probe=probes,data_rate='srvy',datatype='moments')


pytplot.del_data('*')



