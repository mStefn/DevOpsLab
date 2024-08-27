#!/bin/bash

# Check if the script is run as root
if [ "$(id -u)" -ne "0" ]; then
  echo "This script must be run as root." >&2
  exit 1
fi

echo "Welcome to the user creation tool."
echo "Type 'exit' to finish entering users."

while true; do
  # Prompt for the username
  read -p "Enter the username to create: " username

  # Check if the user wants to exit
  if [ "$username" = "exit" ]; then
    echo "Ending user creation process."
    break
  fi

  # Check if the username is not empty
  if [ -z "$username" ]; then
    echo "Username cannot be empty. Please try again."
    continue
  fi

  # Prompt for the group name
  read -p "Enter the group name to add the user to (or leave blank if not needed): " groupname

  # Check if the user already exists
  if id "$username" &>/dev/null; then
    echo "User '$username' already exists."
  else
    # Create the new user
    useradd "$username"
    
    if [ $? -eq 0 ]; then
      echo "User '$username' has been successfully created."
    else
      echo "An error occurred while creating user '$username'."
      continue
    fi
  fi

  # Handle group addition
  if [ -n "$groupname" ]; then
    if getent group "$groupname" &>/dev/null; then
      echo "Group '$groupname' already exists."
    else
      # Create the new group
      groupadd "$groupname"
      
      if [ $? -eq 0 ]; then
        echo "Group '$groupname' has been successfully created."
      else
        echo "An error occurred while creating group '$groupname'."
        continue
      fi
    fi

    # Add the user to the group
    usermod -aG "$groupname" "$username"

    if [ $? -eq 0 ]; then
      echo "User '$username' has been added to group '$groupname'."
    else
      echo "An error occurred while adding user '$username' to group '$groupname'."
    fi
  fi
done

echo "User creation process completed."

