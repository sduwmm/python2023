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
b_data_rate=['brst','srvy']
p_data_rate=['brst','fast']
'''
defatt=pyspedas.mms_load_state(trange=trange, probe=probes)
fgm_vars = pyspedas.mms.fgm(trange=trange, probe=probes, level='l2', data_rate=b_data_rate,time_clip=False)
dis_moms_vars = pyspedas.mms.fpi(trange=trange, probe=probes, level='l2', data_rate='brst', datatype='dis-moms',time_clip=False)
dis_moms_vars = pyspedas.mms.fpi(trange=trange, probe=probes, level='l2', data_rate='fast', datatype='dis-moms',time_clip=False)

des_moms_vars = pyspedas.mms.fpi(trange=trange, probe=probes, level='l2', data_rate='brst', datatype='des-moms',time_clip=False)
des_moms_vars = pyspedas.mms.fpi(trange=trange, probe=probes, level='l2', data_rate='fast', datatype='des-moms',time_clip=False)

#pytplot.options('mms1_des_numberdensity_brst','yrange',[0,10])
#pytplot.options('mms1_fgm_b_gse_brst_l2_btot','yrange',[0,10])

pytplot.options('mms1_des_numberdensity_brst','color','m')
pytplot.options('mms1_des_numberdensity_brst','ylog',0)
pytplot.tplot(['mms1_dis_temppara_brst',\
              'mms1_des_temppara_brst',\
              'mms1_dis_energyspectr_omni_brst',\
              'mms1_des_energyspectr_omni_brst',\
              'mms1_dis_bulkv_gse_brst',\
              'mms1_fgm_b_gse_brst_l2_bvec',\
              'mms1_fgm_b_gse_brst_l2_btot',\
              'mms1_des_numberdensity_brst'],\
              save_png=(pngName))

dis_dist_vars = pyspedas.mms.fpi(trange=trange, probe=probes, level='l2', data_rate='brst', datatype='dis-dist',time_clip=False)

dis_dist_vars = pyspedas.mms.fpi(trange=trange, probe=probes, level='l2', data_rate='fast', datatype='dis-dist',time_clip=False)

#des_dist_vars = pyspedas.mms.fpi(trange=trange, probe=probes, level='l2', data_rate='brst', datatype='des-dist',time_clip=False)
des_dist_vars = pyspedas.mms.fpi(trange=trange, probe=probes, level='l2', data_rate='fast', datatype='des-dist',time_clip=False)
#scm_vars = pyspedas.mms.scm(trange=trange, probe=probes, level='l2', data_rate=b_data_rate, datatype='scb',time_clip=False)
#edp_vars = pyspedas.mms.edp(trange=trange, probe=probes, level='l2', data_rate=b_data_rate, datatype='dce',time_clip=False)
#fgm_vars = pyspedas.mms.fgm(trange=trange, probe=probes, level='l2', data_rate=b_data_rate,time_clip=False)
r_data_rate=['srvy','brst']
r_datatype=['ephts04d', 'epht89q','epht89d']

edp_vars = pyspedas.mms.edp(trange=trange, probe=probes, level='l2', data_rate=b_data_rate, datatype='dce',time_clip=False)

mec_vars = pyspedas.mms.mec(trange=trange, probe=probes, datatype='srvy', data_rate='ephts04d',time_clip=False)
mec_vars = pyspedas.mms.mec(trange=trange, probe=probes, datatype='brst', data_rate='ephts04d',time_clip=False)
mec_vars = pyspedas.mms.mec(trange=trange, probe=probes, datatype='srvy', data_rate='epht89q',time_clip=False)
mec_vars = pyspedas.mms.mec(trange=trange, probe=probes, datatype='brst', data_rate='epht89q',time_clip=False)
mec_vars = pyspedas.mms.mec(trange=trange, probe=probes, datatype='srvy', data_rate='epht89d',time_clip=False)
mec_vars = pyspedas.mms.mec(trange=trange, probe=probes, datatype='brst', data_rate='epht89d',time_clip=False)


fsm_vars = pyspedas.mms.fsm(trange=trange, probe=probes, data_rate='brst', datatype='scb',time_clip=False)
fsm_vars = pyspedas.mms.fsm(trange=trange, probe=probes, data_rate='srvy', datatype='scb',time_clip=False)

edi_vars = pyspedas.mms.edi(trange=trange, probe=probes, data_rate='brst',datatype='efield',time_clip=True)
edi_vars = pyspedas.mms.edi(trange=trange, probe=probes, data_rate='brst',datatype='amb',time_clip=True)

feeps_vars=pyspedas.mms.feeps(trange=trange, probe=probes, data_rate='brst',datatype='ion',time_clip=True)
feeps_vars=pyspedas.mms.feeps(trange=trange, probe=probes, data_rate='brst',datatype='electron',time_clip=True)

eis_vars = pyspedas.mms.eis(trange=trange, probe=probes, data_rate='brst',datatype='extof',time_clip=True)
eis_vars = pyspedas.mms.eis(trange=trange, probe=probes, data_rate='brst',datatype='phxtof',time_clip=True)
eis_vars = pyspedas.mms.eis(trange=trange, probe=probes, data_rate='brst',datatype='electronenergy',time_clip=True)
'''
aspoc_vars=pyspedas.mms.aspoc(trange=trange,data_rate='brst',datatype='asp1')
aspoc_vars=pyspedas.mms.aspoc(trange=trange,probes=probes,data_rate='brst',datatype='asp2')
aspoc_vars=pyspedas.mms.aspoc(trange=trange,probes=probes,data_rate='brst',datatype='aspoc')

h_datatype=['moments','ion']
h_data_rate=['brst','srvy']
hpca_vars=pyspedas.mms.hpca(trange=trange,probes=probes,data_rate='brst',datatype='moments')
hpca_vars=pyspedas.mms.hpca(trange=trange,probes=probes,data_rate='srvy',datatype='moments')
hpca_vars=pyspedas.mms.hpca(trange=trange,probes=probes,data_rate='brst',datatype='ion')
hpca_vars=pyspedas.mms.hpca(trange=trange,probes=probes,data_rate='srvy',datatype='moments')


pytplot.del_data('*')



