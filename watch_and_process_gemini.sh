#!/bin/bash

# Define the paths to the numpy files
NUMPY_FILE="/contact_transfer/output_gemini/rgbd_image_new.npz"
PREDICTIONS_FILE="/contact_transfer/output_grasp/predictions_rgbd_image_new.npz"


# Define the line of code to execute
PROCESS_COMMAND="python contact_graspnet/inference.py --np_path=$NUMPY_FILE"

# Delete the files if they exist before entering the loop
if [ -f "$NUMPY_FILE" ]; then
  echo "Deleting existing $NUMPY_FILE..."
  rm "$NUMPY_FILE"
fi

if [ -f "$PREDICTIONS_FILE" ]; then
  echo "Deleting existing $PREDICTIONS_FILE..."
  rm "$PREDICTIONS_FILE"
fi

# Infinite loop to watch for the numpy file and execute the process
while true
do
  # Check if the numpy file exists
  if [ -f "$NUMPY_FILE" ]; then
    echo "File $NUMPY_FILE found. Processing..."

    # Execute the line of code
    $PROCESS_COMMAND --local_regions --filter_grasps

    # Check if the command was successful
    if [ $? -eq 0 ]; then
      echo "Processing complete. Deleting $NUMPY_FILE..."
      # Delete the numpy file
      rm "$NUMPY_FILE"
    else
      echo "Error during processing. Retrying..."
    fi
  else
    # File not found, wait and check again
    echo "Waiting for $NUMPY_FILE..."
  fi

  # Small sleep interval to prevent busy-waiting
  sleep 2
done
