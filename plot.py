# usage: change names of files at bottom, check figure labels, etc.
# then run 'python plot.py'
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math

def plot_cv(figname):
    fig = plt.figure()
    for i in np.arange(len(cv_files)):
        data_in=np.loadtxt(cv_files[i],skiprows=1,usecols=(0,1))
        for j in np.arange(len(data_in)):
            data_in[:,0][j]=data_in[:,0][j]
        plt.plot(data_in[:,0][:100],data_in[:,1][:100],marker[i],label=fig_legend[i])

    plt.title("Velocity Autocorrelation Function")
    plt.xlabel("time (ps)")
    plt.ylabel("$C_{V}(t)$")
    plt.legend()
    plt.draw()
    plt.savefig(figname)

def plot_rc(figname):
    fig = plt.figure()
    for i in np.arange(len(rc_files)):
        data_in=np.loadtxt(rc_files[i],skiprows=1,usecols=(0,1))
        for j in np.arange(len(data_in)):
            data_in[:,0][j]=data_in[:,0][j]
        plt.plot(data_in[:,0],data_in[:,1],marker[i],label=fig_legend[i])

    plt.title("Occupation Time Distribution")
    plt.xlabel("time (ps)")
    plt.ylabel("$C_{R}(t)$")
    plt.legend()
    plt.draw()
    plt.savefig(figname)

def plot_msd(figname):
    fig = plt.figure()
    for i in np.arange(len(msd_files)):
        data_in=np.loadtxt(msd_files[i],skiprows=1,usecols=(0,1))
        for j in np.arange(len(data_in)):
            data_in[:,0][j]=data_in[:,0][j]
        plt.plot(data_in[:,0],data_in[:,1],marker[i],label=fig_legend[i])

    plt.title("Mean Square Displacement")
    plt.xlabel("time (ps)")
    plt.ylabel("$MSD (\AA)$")
    plt.legend()
    plt.draw()
    plt.savefig(figname)

def plot_thermo(figname):

    # set which columns to plot as y-axis (x-axis always time)
    plot_cols=[1,2,3,4,5,6,7]

    # read in headings from file
    file=open(thermo_files[0])
    line=file.readline()
    headers = line.split()
    file.close()

    for j in np.arange(len(plot_cols)):
        fig = plt.figure()
        for i in np.arange(len(thermo_files)):
            data_in=np.loadtxt(thermo_files[i],skiprows=1,usecols=(0,j))
            start=data_in[:,0][0]
            for k in np.arange(len(data_in[:,0])):
                data_in[:,0][k] = data_in[:,0][k] - start
            plt.plot(data_in[:,0],data_in[:,1],label=fig_legend[i])

        plt.title("{0}".format(headers[j]))
        plt.xlabel("timestep")
        plt.ylabel("{0}".format(headers[j]))
        plt.legend()
        plt.draw()
        plt.savefig('{0}-{1}'.format(headers[j],figname))

marker=['--',':']
fig_legend=['bulk','confined']
cv_files=['C_V_out_s0_m1000_t20000-neat','C_V_out_s0_m1000_t20000-confined']
plot_cv('C_V_compare.png')

msd_files=['MSD_out_s0_m1000_t20000-neat','MSD_out_s0_m1000_t20000-confined']
plot_msd('MSD_compare.png')

rc_files=['R_C_out_s0_m1000_t20000-neat','R_C_out_s0_m1000_t20000-confined']
plot_rc('R_C_compare.png')

# will plot different properties to separate image, multiple files to same plot
# plots must have the same layout of columns...
#thermo_files=['npt_6.8/C-walls_6.8_fix-rigid-npt_rst.o10814.log.PARSED','npt_13.0/C-walls_13.0_fix-rigid-npt_rst.o10737.log.PARSED'] # these are working
#thermo_files=['npt_6.8/C-walls_6.8_fix-rigid-npt_1fs.o10769.log.PARSED','npt_13.0/C-walls_13.0_fix-rigid-npt_1fs.o10735.log.PARSED'] # crashed
thermo_files=['../npt_13.0/C-walls_13.0_fix-rigid-npt_1atm_298K.o11117.log.PARSED'] # crashed
#plot_thermo('PPPM-o17777.png')
