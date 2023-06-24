from pyspedas import themis
from pyspedas import time_double
from pytplot import options, xlim, ylim, zlim, tplot,tplot_options
from pytplot import tplot_names, get_data, store_data, del_data
from pyspedas.mms.fpi.mms_get_fpi_dist import mms_get_fpi_dist
from pyspedas.particles.spd_slice2d.slice2d import slice2d
from pyspedas.mms import fpi
#print(tplot.__doc__)
#help(tplot)
figPath= 'C:/OneDrive - mail.sdu.edu.cn/AAA_worklog_2023/paper_whistler_figure/FT_formation/'
trange=['2018-12-10/04:00:00', '2018-12-10/05:00:00']
tr=trange[0]
pngName = figPath + 'FT_{}{}{}_{}{}'.format(tr[0:4], tr[5:7], tr[8:10], tr[11:13], tr[14:16])

#fgm_vars = themis.fgm(probe=['b','c'], trange=trange,time_clip=True)
#fgm_vars = themis.fgm(probe=['b'], trange=trange,time_clip=True)
#tplot(['thb_fgs_btotal', 'thb_fgs_gse'])
'''
tplot_options('wsize', [300, 500])
xlim(time_double(trange[0]),time_double(trange[1]))
ylim('thb_fgs_btotal',0.,5)
ylim('thb_fgs_gse',-4,4)
'''
'''
tplot(['thb_fgs_btotal', \
               'thb_fgs_gse'], \
              xsize=16, \
              ysize=9, \
              save_png=(pngName), display=True)

del_data('*')
'''

'''
trange=['2018-12-10/04:40:00', '2018-12-10/04:41:00']

fpi(trange=trange, probe='1', level='l2', data_rate='brst', datatype='dis-dist',
                                 time_clip=True)

dists = mms_get_fpi_dist('mms1_dis_dist_brst', probe='1')
the_slice=slice2d(dists,trange=trange)

slice2d(trange=None, time=None, samples=None, window=None,
        center_time=False,
        erange=None,
        thetarange=None,
        zdirrange=None,
        average_angle=None,
        sum_angle=None,
        energy=False,
        log=False,
        rotation='xy',
        custom_rotation=None,
        slice_x=None,
        subtract_bulk=False,
        resolution=None,
        interpolation='geometric',
        smooth=None)
'''