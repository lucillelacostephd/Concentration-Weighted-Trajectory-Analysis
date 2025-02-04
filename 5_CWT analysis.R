library(readr)
library(openair)

# Choose dataset
selected_dataset <- "Canister"  # Switch to "PAMS" when needed

# Define datasets and sources
datasets <- list(
  PAMS = list(
    file = "C:/Users/LB945465/Desktop/Trajectories/Merged_Traj_PAMS.csv",
    sources = c(
      'Industrial_evaporation', 'Biogenic', 'Fuel_evaporation',
      'Industrial', 'Polymer_production', 'Vehicle_exhaust',
      'Diesel_emissions', 'Gasoline_emissions'
    )
  ),
  Canister = list(
    file = "C:/Users/LB945465/Desktop/Trajectories/Merged_Traj_canister.csv",
    sources = c(
      'Diesel_emissions', 'Fuel_evaporation', 'Biogenic',
      'Aldehyde_rich', 'MEK_rich', 'Vehicle_emissions',
      'Natural_gas', 'Background'
    )
  )
)

# Load the appropriate data and sources
merged_data <- read_csv(datasets[[selected_dataset]]$file)
sources <- datasets[[selected_dataset]]$sources

# Directory to save plots
output_dir <- "C:/Users/LB945465/Desktop/Trajectories/CWT_Plots/"

# Create output directory if it doesn't exist
if (!dir.exists(output_dir)) {
  dir.create(output_dir)
}

# Loop through each source and generate a plot
for (source in sources) {
  # Generate the CWT plot
  plot_file <- paste0(output_dir, source, "_CWT_plot.png")
  
  png(filename = plot_file, width = 1200, height = 800, res = 150)  # Adjust resolution and size if needed
  
  trajLevel(
    merged_data,
    lon = "lon",
    lat = "lat",
    pollutant = source,
    key.header = paste(source),
    fontsize = 15,
    statistic = "cwt",
    grid.col = "gray",
    col = c("skyblue", "yellow", "red"),
    #col = "increment",
    min.bin = 50,
    orientation = c(90, -100, 0),
    xlim = c(-100, -55), #Eastern US
    ylim = c(20, 60), #Eastern US
    #xlim = c(-85, -65),  # Zoomed out to cover more of eastern U.S.
    #ylim = c(30, 50),    # Wider vertical range from Florida to southern Canada
    #xlim = c(-75, -72),  # Longitude range near NYC
    #ylim = c(40, 42),    # Latitude range near NYC
    #resolution = 0.1,  # Increase grid detail with smaller resolution
    smooth = TRUE,
    key.footer = "ppbv"
  )
  
  dev.off()  # Close the PNG device
  
  print(paste("Plot saved for:", source))
}

