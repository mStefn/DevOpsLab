#!/bin/bash

# Update the package list
echo "Updating package list..."
sudo apt-get update -y

# Upgrade installed packages to the latest versions
echo "Upgrading installed packages..."
sudo apt-get upgrade -y

# Install basic server tools and applications
echo "Installing essential server applications..."

# Install utilities
sudo apt-get install -y curl wget git vim

# Install network tools
sudo apt-get install -y net-tools htop

# Install firewall
sudo apt-get install -y ufw

# Install SSH server (if not already installed)
sudo apt-get install -y openssh-server

# Install Apache (or another web server)
sudo apt-get install -y apache2

# Install MySQL server (optional, for databases)
sudo apt-get install -y mysql-server

# Install PHP (optional, for dynamic web content)
sudo apt-get install -y php libapache2-mod-php php-mysql

# Clean up unnecessary packages and files
echo "Cleaning up..."
sudo apt-get autoremove -y
sudo apt-get clean

# Enable and start necessary services
echo "Enabling and starting services..."
sudo systemctl enable ssh
sudo systemctl enable apache2
sudo systemctl start ssh
sudo systemctl start apache2

echo "Server setup complete."

