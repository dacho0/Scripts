# Start an admin powershell console, and paste in the following

# Generic bootstrap
Set-ExecutionPolicy Bypass -Scope Process -Force; 
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; 
. { iwr -useb http://boxstarter.org/bootstrapper.ps1 } | iex; get-boxstarter -Force

# Baseline
Install-BoxstarterPackage -PackageName https://gist.githubusercontent.com/gavinjoneslic/1fc89054ea7d4c3ebfbeaa0b60bfc291/raw/7f9c52c745229de0dad7641104c3b386f5f9ade4/base-installs.txt


install chocolately

# Base infra
# HyperV
Install-WindowsUpdate -AcceptEula
cinst Microsoft-Hyper-V -source windowsfeatures
cinst Microsoft-Hyper-V-Management-PowerShell -source windowsfeatures

# WSL2
cup -y wsl2 microsoft-windows-terminal

# Docker
cup -y docker-desktop dive

# Base tools
choco install -y git  nuget.commandline erlang rabbitmq nano aspnetmvc.install aspnetmvc4.install linkshellextension 
# nservicebus googledrive
choco install -y nodejs --version 10.20.1

# Base IDEs
cup -y vscode
