# 1D_Heterogeneous_GW_flow_model
third assignment for Andy's class

1D Heterogeneous Groundwater Flow Model

by Patrick O'Hara

All units are SI

The following script was written to solve for hydraulic head given boundary 
condition hydraulic head values for both ends of the model. 

Hydraulic Conductivity (k) can be set to different values for different
lengths of the model. Currently there are 3 zones of varying hydraulic
conductivity.

Porosity (n) can be set to different values for differnt lengths of the model.
Currently there are 3 zones of varying porosity.

Distance (x) is set by making a numpy array of intigers from 1 though 100 and 
and then multiplying each value in the array by the number needed to get desired 
distance when multiplied by 100.

Darcy's Law is used to solve for change in h for each time step.
