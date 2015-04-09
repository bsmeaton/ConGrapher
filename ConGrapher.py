# import needed functions
import re
import os
import pylab as pl
import numpy as np
from matplotlib.legend_handler import HandlerLine2D

# ask user to describe input file name
print(" _________                   ________                    .__                  \n \_   ___ \  ____   ____    /  _____/___________  ______ |  |__   ___________ \n /    \  \/ /  _ \ /    \  /   \  __\_  __ \__  \ \____ \|  |  \_/ __ \_  __ \ \n \     \___(  <_> )   |  \ \    \_\  \  | \// __ \|  |_> >   Y  \  ___/|  | \/ \n  \______  /\____/|___|  /  \______  /__|  (____  /   __/|___|  /\___  >__|    \n         \/            \/          \/           \/|__|        \/     \/        \nBy BSmeaton \n")
log = input("Input log file name (e.g log_01.txt): ")
lines = open(log, "r" ).readlines()

# if output files exist delete it
if os.path.isfile("Ux_" + log):
        os.remove("Ux_" + log)
if os.path.isfile("Uy_" + log):
        os.remove("Uy_" + log)       
if os.path.isfile("Uz_" + log):
        os.remove("Uz_" + log)
if os.path.isfile("k_" + log):
        os.remove("k_" + log)
if os.path.isfile("w_" + log):
        os.remove("w_" + log)
if os.path.isfile("e_" + log):
        os.remove("e_" + log)
if os.path.isfile("p_" + log):
        os.remove("p_" + log)        
if os.path.isfile("time_" + log):
        os.remove("time_" + log)    
        
# search for specific parts of input file and paste in output file (loop)         
for line in lines:
    if re.search( r"Solving for Ux", line ):# Searching for Ux line in file
        if not os.path.isfile("Ux_" + log):# if there is not a Ux text file make one
            fileUx = open("Ux_" + log, 'w')
            fileUx.write('Ux \n')        
        start = 'Final residual = '
        end = ', No Iterations'
        Ux = line.split(start)[1].split(end)[0]# take residual as string between start and end
        fileUx.write(Ux + '\n')
        
    elif re.search( r"Solving for Uy", line ):
        if not os.path.isfile("Uy_" + log):
            fileUy = open("Uy_" + log, 'w')
            fileUy.write('Uy \n')        
        start = 'Final residual = '
        end = ', No Iterations'
        Uy = line.split(start)[1].split(end)[0]
        fileUy.write(Uy + '\n')
        
    elif re.search( r"Solving for Uz", line ):
        if not os.path.isfile("Uz_" + log):
            fileUz = open("Uz_" + log, 'w')
            fileUz.write('Uz \n')        
        start = 'Final residual = '
        end = ', No Iterations'
        Uz = line.split(start)[1].split(end)[0]
        fileUz.write(Uz + '\n')

    elif re.search( r"Solving for p", line ):
        if not os.path.isfile("p_" + log):
            filep = open("p_" + log, 'w')
            filep.write('p \n')        
        start = 'Final residual = '
        end = ', No Iterations'
        p = line.split(start)[1].split(end)[0]
        filep.write(p + '\n')
        
    elif re.search( r"Solving for omega", line ):
        if not os.path.isfile("w_" + log):
            filew = open("w_" + log, 'w')
            filew.write('w \n')        
        start = 'Final residual = '
        end = ', No Iterations'
        w = line.split(start)[1].split(end)[0]
        filew.write(w + '\n')
        
    elif re.search( r"Solving for k", line ):
        if not os.path.isfile("k_" + log):
            filek = open("k_" + log, 'w')
            filek.write('k \n')
        start = 'Final residual = '
        end = ', No Iterations'
        k = line.split(start)[1].split(end)[0]
        filek.write(k + '\n')

    elif re.search( r"Solving for epsilon", line ):
        if not os.path.isfile("e_" + log):
            filee = open("e_" + log, 'w')
            filee.write('e \n')
        start = 'Final residual = '
        end = ', No Iterations'
        e = line.split(start)[1].split(end)[0]
        filee.write(e + '\n')

    elif re.search( r"Time = ", line ):
        if not os.path.isfile("time_" + log):
            filetime = open("time_" + log, 'w')
            filetime.write('time \n')
        if not re.search( r"ClockTime =", line ):
            start = 'Time = '
            time = line.split(start)[1]
            filetime.write(time)
            
# if output files exist close them, then setup graph parameters by outputting list
if os.path.isfile("time_" + log):# if Ux file exists close it
        filetime.close()   
        datatime=np.genfromtxt("time_" + log , skiprows=2)# describes data for time
if os.path.isfile("Ux_" + log):
        fileUx.close()
        dataUx=np.genfromtxt("Ux_" + log , skiprows=2)
        line1, = pl.plot(datatime,dataUx,'',label = "Ux" ,linewidth=1)
if os.path.isfile("Uy_" + log):
        fileUy.close()       
        dataUy=np.genfromtxt("Uy_" + log , skiprows=2)
        line2, = pl.plot(datatime,dataUy,'',label = "Uy" ,linewidth=1)
if os.path.isfile("Uz_" + log):
        fileUz.close()
        dataUz=np.genfromtxt("Uz_" + log , skiprows=2)
        line3, = pl.plot(datatime,dataUz,'',label = "Uz" ,linewidth=1)
if os.path.isfile("p_" + log):
        filep.close()
        datap=np.genfromtxt("p_" + log , skiprows=2)
        line4, = pl.plot(datatime,datap,'',label = "p" ,linewidth=1)
if os.path.isfile("k_" + log):
        filek.close()
        datak=np.genfromtxt("k_" + log , skiprows=2)
        line5, = pl.plot(datatime,datak,'',label = "k" ,linewidth=1)
if os.path.isfile("w_" + log):
        filew.close()
        dataw=np.genfromtxt("w_" + log , skiprows=2)
        line6, = pl.plot(datatime,dataw,'',label = "w" ,linewidth=1)
if os.path.isfile("e_" + log):
        filee.close()
        datae=np.genfromtxt("e_" + log , skiprows=2)
        line6, = pl.plot(datatime,datae,'',label = "e" ,linewidth=1)
        
# plot graphs
pl.legend(handler_map={line1: HandlerLine2D(numpoints=6)}) # plots the legend

pl.title(log + "  OpenFOAM - Convergence Plot")
pl.xlabel("Time (s)")
pl.ylabel("Convergence Residual (Log Scale)")

pl.yscale('log')

pl.show()
