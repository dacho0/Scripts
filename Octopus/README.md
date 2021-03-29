# Preconditions
* Install Octopus.Client library
```
Install-Package Octopus.Client -source https://www.nuget.org/api/v2 -SkipDependencies
$path = Join-Path (Get-Item ((Get-Package Octopus.Client).source)).Directory.FullName "lib/net452/Octopus.Client.dll"
Add-Type -Path $path
```

# If get Octopus Client Library Error message
* Add the below line to the first line of the PowerShell script

`Add-Type -Path 'C:\PathTo\Octopus.Client.dll'`

# Reference

https://octopus.com/docs/octopus-rest-api/octopus.client/getting-started


