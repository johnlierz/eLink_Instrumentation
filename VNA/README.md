# VNA Data Processing

Input files: touchstone file (.s2p, .s4p) or VNA output file (.vna.txt)

## Setup

Certain python packages are required, so you will need to setup your python environment to use them.
The main package we will use is called scikit-rf with documentation [here](https://scikit-rf.readthedocs.io/en/latest/index.html) and installation instructions [here](https://scikit-rf.readthedocs.io/en/latest/tutorials/Installation.html).
I recommend creating a python environment using conda in order to install the necessary packages.
See the conda documentation [here](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html).
Also, for new Macs (2020 and later) that have an Apple M1 chip (which uses a new architecture), look [here](https://www.jimbobbennett.io/installing-scikit-learn-on-an-apple-m1/).

To install conda, go [here](https://docs.conda.io/projects/continuumio-conda/en/latest/user-guide/install/index.html), choose your operating system, and follow the instructions.
Once conda is installed, you can run these commands in your terminal (for Mac or Linux... I'm not sure about Windows!).
```
conda update -n base conda
conda config --set auto_activate_base false
```
Then you can create a new python environment.
```
conda create -n .venv python
```
To activate the environment, do
```
conda activate .venv
```
When the environment is active, install scikit-rf.
```
conda install -c conda-forge  scikit-rf
```
To list installed packages, do
```
conda list
```
To deactivate the environment, do
```
conda deactivate
```
You can now activate and deactivate your conda environment as needed.
You will need to activate it before running the scripts that use scikit-rf.

## Scripts

### VNADataInspection.py
Reads .s4p file

### readVNAData.py
Extracts Z-impedance parameters from input text files using self defined function

### readVNADataSKRF.py
Converts .txt files to .s2p files and analyzes S-parameter properties using skrf library

### create_all_s2p.py
Calls readVNADataSKRF.py on a list of files.
```
python3 python/create_all_s2p.py
```

### plotImpedance.py
Plots S11 and TD11 using .s2p input files

### plotVNAFeatures.py
Merge of the steps of creating .s2p files and plotting the S-parameters and Impedance in frequency and time domain. 

### draw_plots.py 
Driver script to plot all other S-parameters options such as S12 and S21 and execute 'plotVNAFeatures.py'. 

### input_cable_data.txt
The input for 'plotVNAFeatures.py' script which are set of measurements for all channels of a particular cable, with last file reserved to compare with the calibration data. 

