# DSML - Predict Ride-Hailing Tipping

## Setup
conda env create -f environment.yml  
conda activate almost-turkish

## Run
jupyter notebook

## Adding new packages
After adding new packages to env, run:  
conda env update --file environment.yml --prune


## Columns in 2019_03  
Trip ID,Trip Miles,Trip Start Timestamp,Trip End Timestamp,Pickup Census Tract,Pickup Centroid Location,Dropoff Census Tract,Dropoff Centroid Location,Shared Trip Authorized,Trips Pooled,Trip Total,Fare,Additional Charges,Tip