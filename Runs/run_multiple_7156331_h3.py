from run_experiment import createFolder, run_experiment
import subprocess as sp
import pandas as pd
import numpy as np
import pickle
from matplotlib import pyplot as plt
import os

path = '/home/kyoko/デスクトップ/Develop/ActualCausation/MABE/MABE_contents/'
os.chdir(path)

experiment_path = 'Experiments/190822_7_15_63_31_h3/'
cmd = [experiment_path + 'test_7156331_h3.cfg',
       experiment_path + 'activity_7156331_h3.cfg',#,
       experiment_path + 'genome_7156331_h3.cfg'] # change here to the name of setting files
datafile = path + 'Experiments/190822_7_15_63_31_h3/190822_7156331_h3_LOD_data.csv' # change to the expected generated file
genomefile = path + 'Experiments/190822_7_15_63_31_h3/190822_7156331_h3_LOD_organisms.csv'
activityfile = path + 'Experiments/190822_7_15_63_31_h3/markov_IO_map_190822_7156331_h3.csv' #change to the expected generated file
# TPMjoryfile = path + 'Experiments/kyoko/new_snapshot_data_0.csv'
data = []
genome = []
activity = []
# TPM_jory = []

runs = 10

for r in list(range(0,runs)):
	print(['run number ' + str(r)])
	# Running experiment
	run_experiment(cmd[0])
	# Getting data from file
	data.append(pd.read_csv(datafile))
	genome.append(pd.read_csv(genomefile))
	# Running recorders
	run_experiment(cmd[1])
	run_experiment(cmd[2])
	print(['success!!!'])
	# Getting recordings from file
	activity.append(pd.read_csv(activityfile))
	# TPM_jory.append(pd.read_csv(TPMjoryfile))

	with open('Experiments/190822_7_15_63_31_h3/190822_7156331_h3_LOD_data.pkl', 'wb') as f: # change
	    pickle.dump(data, f)

	with open('Experiments/190822_7_15_63_31_h3/190822_7156331_h3_genome.pkl', 'wb') as f:
	    pickle.dump(genome, f)

	with open('Experiments/190822_7_15_63_31_h3/190822_7156331_h3_activity.pkl', 'wb') as f: # change
	    pickle.dump(activity, f)

	#with open('Experiments/deterministic/TPM_jory.pkl', 'wb') as f:
	#    pickle.dump(TPM_jory, f)
