#!/usr/bin/env python

import subprocess

options = [
            # createS2p, inputDir, inputTxtFiles, cableName, cableLength, t1, t2, outputTouchstoneSubFile, SParamterComp
            [1, '../example_data', 'input_cable_data.txt',   '',                '35',  0.2,   0.4, '0', '11'], #S11
            [0, '../example_data', 'input_cable_data.txt',   '',                '35',  0.2,   0.4, '0', '12'], #S12
            [0, '../example_data', 'input_cable_data.txt',   '',                '35',  0.2,   0.4, '1', '21'], #S21
            [1, '../data',         'johncable3_2m.txt',      'johncable3_2m',  '200',  3.0,  15.0, '0', '11'], #S11
            [0, '../data',         'johncable3_2m.txt',      'johncable3_2m',  '200',  3.0,  15.0, '0', '12'], #S12
            [0, '../data',         'johncable3_2m.txt',      'johncable3_2m',  '200',  3.0,  15.0, '1', '21'], #S21
	  ]

command = 'python plotVNAFeatures.py --createS2p={0:<3.0f} --inputDir={1:s} --inputTxtFiles={2:s} --cableName={3:s} --cableLength={4:s} --t1={5:<3.2f} --t2={6:<3.2f} --outputTouchstoneSubFile={7:s} --SParamterComp={8:s}'

for opt in options:
    s = command.format(opt[0], opt[1], opt[2], opt[3], opt[4], opt[5], opt[6], opt[7], opt[8])
    print(s)
    subprocess.call( [s, ""], shell=True )	

