#!/bin/bash

# Get the current date and time
current_date=$(date)

# Display system information
system_info=$(uname -a)

# Display disk usage information
disk_usage=$(df -h)

# Display RAM usage information
ram_usage=$(free -h)

# Output the results
echo "Date and time: $current_date"
echo "System information:"
echo "$system_info"
echo ""
echo "Disk usage:"
echo "$disk_usage"
echo ""
echo "RAM usage:"
echo "$ram_usage"

