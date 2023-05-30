## Utilization Analysis

This is small demonstration of a data pipeline that uses the `/data` folder with system log or `0_sim_log.csv` that contains information of system utilisations throughout a period of time and a supercomputer resource utilisation csv or `3_apst_03_2021.csv` that contains the actual system utilizations of that period in order to generate a simulation for resource utilisation of High Performance Computing (HPC) systems. 

The flow of data is expantiated in the diagrams below:

- First, the data is extracted from various HPC sources, for simplicity and demonstration purposes, the data is extracted from a single source, the `/data` folder. `0_sim_log.csv` contains the system utilisation of a system for a period of time and `3_apst_03_2021.csv` contains the actual system utilisation of that period. 
- Now, in order to transform these data files in to their respective dataframes, the `data-transformations` scripts and notebooks are used. These files are located in the `/src` and `notebooks` folder. The `data-transformations` scripts are used to transform the data into a dataframe that can be used for the simulation. The final dataframes are then stored in the `/data` folder as a csv.

![1st data flow](/figures/premiere-pipeline.png)

- The second data flow employs the final dataframes discussed above and uses them to generate a simulation of the system utilisation with a camparison with actual utilization of resources in the form of a graph or a plot. The `gen_ploy` notebook is used to compare the simulations with graphs using `plots.csv` in the `/data` folder. 

![2nd data flow](/figures/second-pipeline.png)

- Finally, the third data flow uses the `plot_utilization` Flask application to generate a simulation of the system utilisation with a camparison with actual utilization of resources in the form of a grapph using  `plotly-Dash` application. The `plot_utilization` Flask application is located in the `/src` folder and the result is a web application that can be accessed through the browser.

![3rd data flow](/figures/third-pipeline.png)