# Concentration-Weighted-Trajectory-Analysis

The Concentration Weighted Trajectory (CWT) analysis is a method used to identify potential source regions contributing to pollutant concentrations at a given monitoring site. It combines trajectory data (air mass back-trajectories) with measured pollutant concentrations to highlight areas associated with higher average concentrations.

How CWT Works:

1. Air mass trajectories are tracked to understand the pathways air traveled before reaching the monitoring site.
2. Each trajectory is assigned a weight based on the concentration of a target pollutant measured at the time the air mass arrived.
3. The result is a spatial plot showing regions that consistently contribute to high or low pollutant concentrations, enabling the identification of long-range and local sources.

In this project, the CWT analysis was applied using openair in R, generating plots for multiple pollutant sources from both PAMS and canister data for the New York City metropolitan area. The analysis provides insights into the spatial distribution of contributing sources across the eastern United States.
