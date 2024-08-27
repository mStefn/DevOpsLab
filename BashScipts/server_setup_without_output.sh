#!/bin/bash

# Define log file
LOGFILE="setup_log.txt"

# Start logging
echo "Starting server setup at $(date)" > "$LOGFILE"

# Update the package list
echo "Updating package list..." | tee -a "$LOGFILE"
sudo apt-get update -y >> "$LOGFILE" 2>&1

# Upgrade installed packages to the latest versions
echo "Upgrading installed packages..." | tee -a "$LOGFILE"
sudo apt-get upgrade -y >> "$LOGFILE" 2>&1

# Install basic server tools and applications
echo "Installing essential server applications..." | tee -a "$LOGFILE"

# Install utilities
sudo apt-get install -y curl wget git vim >> "$LOGFILE" 2>&1

# Install network tools
sudo apt-get install -y net-tools htop >> "$LOGFILE" 2>&1

# Install firewall
sudo apt-get install -y ufw >> "$LOGFILE" 2>&1

# Install SSH server (if not already installed)
sudo apt-get install -y openssh-server >> "$LOGFILE" 2>&1

# Install Apache (or another web server)
sudo apt-get install -y apache2 >> "$LOGFILE" 2>&1

# Install MySQL server (optional, for databases)
sudo apt-get install -y mysql-server >> "$LOGFILE" 2>&1

# Install PHP (optional, for dynamic web content)
sudo apt-get install -y php libapache2-mod-php php-mysql >> "$LOGFILE" 2>&1

# Clean up unnecessary packages and files
echo "Cleaning up..." | tee -a "$LOGFILE"
sudo apt-get autoremove -y >> "$LOGFILE" 2>&1
sudo apt-get clean >> "$LOGFILE" 2>&1

# Enable and start necessary services
echo "Enabling and starting services..." | tee -a "$LOGFILE"
sudo systemctl enable ssh >> "$LOGFILE" 2>&1
sudo systemctl enable apache2 >> "$LOGFILE" 2>&1
sudo systemctl start ssh >> "$LOGFILE" 2>&1
sudo systemctl start apache2 >> "$LOGFILE" 2>&1

# End logging
echo "Server setup complete at $(date)" | tee -a "$LOGFILE"

