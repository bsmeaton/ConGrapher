# ConGrapher
Exports residual convergence data from an OpenFOAM log file, and graphs it.

Instructions for use:

Program requires Python 3.4, numpy, matplotlib it is recommended to use an engineering package such as Anaconda3.

Requires a log file of the OpenFOAM solve, for example the log file generated from the command (simpleFoam > log_01.txt) in windows.

1. Place the program ConGrapher.py in the same directory as log file.
2. Run program using python cmd line.
3. input logfile name and press enter

Program should output log graph and associated files with convergence residuals for (Ux, Uy, Uz, p and k, omega and epsilon)

