#!/usr/bin/python

########################################################
# This is an automatically generated MDANSE run script #
########################################################

from MDANSE import REGISTRY

################################################################
# Job parameters                                               #
################################################################

parameters = {}
parameters['atom_selection'] = None
parameters['atom_transmutation'] = [[u'waterL_sel_H', u'h2']]
parameters['frames'] = (0, 1000, 1)
parameters['instrument_resolution'] = ('gaussian', {'mu': 0.0, 'sigma': 0.1})
parameters['output_files'] = (u'/home/tofhr/gonzalezm/MDANSE2018/MDANSE_Case2/DCSF_D2O_waterL', (u'netcdf',))
parameters['q_vectors'] = 'SphLatt_3_21_2'
parameters['running_mode'] = ('monoprocessor',)
parameters['trajectory'] = u'/home/tofhr/gonzalezm/MDANSE2018/MDANSE_Case2/waterL_traject.nc'
parameters['weights'] = u'b_coherent'

################################################################
# Setup and run the analysis                                   #
################################################################

dcsf = REGISTRY['job']['dcsf']()
dcsf.run(parameters,status=True)