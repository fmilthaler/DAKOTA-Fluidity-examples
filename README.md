# DAKOTA-Fluidity-examples

This repository contains examples on how to use the optimisation framework DAKOTA in combination with Fluidity.

The following numerical experiments are shown:
 * Driven cavity,
 * Tsunami,
 * Flow past a cylinder,
which can be found in the appropriately named directories of this repository.

## How to run an example
First, DAKOTA needs to be installed on the machine. Read through the official instructions: [http://dakota.sandia.gov/content/install-linux-macosx](http://dakota.sandia.gov/content/install-linux-macosx). Once DAKOTA is installed, open the file `setvars.sh` and modify the first line of it, such that the env variable `DAKOTA` points to the basedir of the DAKOTA installation. You can then run `source setvars.sh` on the command-line to add DAKOTA relevant paths to your env variables. Since all examples are using Fluidity, the fluidity/bin directory needs to be added to your `PATH` env variable, and fluidity/python to the `PYTHONPATH` variable. Finally, `make` should then start the optimisation process using DAKOTA and Fluidity.

####`flow_past_cylinder-ls-inflow`:
This example uses nonlinear least squares to optimise the inflow boundary condition of the flow past a cylinder example. In this directory, you find among others the file `dakota_cylinder.in`. This file contains user set parameters to drive DAKOTA. Under `variables` you find how many variables are set, their min/max bounds, initial value, and their label. Under `interface`, you find the entry `analysis_driver = 'fluidity_cylinder.py'`, meaning DAKOTA will execute the file `fluidity_cylinder.py` at each iteration. In that Python script there are all pre- and postprocessing steps, e.g. substituting new parameters coming from DAKOTA into the next Fluidity run (usually by substitution to the .flml), as well as analysing Fluidity's output to return a value/an error back to DAKOTA.

## Questions
If you have questions, ask your colleagues at AMCG, and/or get in touch.
