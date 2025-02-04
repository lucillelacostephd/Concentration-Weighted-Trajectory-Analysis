
library(readr)

# Load .rds file
traj_data <- readRDS("C:\Users\LB945465\Desktop\Trajectories\BronxTrajData.rds")

# Save as CSV
write_csv(traj_data, "C:\Users\LB945465\Desktop\Trajectories\BronxTrajData.csv")
