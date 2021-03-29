$remoteCommand = {dir c:\};
$computerName = "Computer Name" # can be comma seperate list
Invoke-Command -ScriptBlock $remoteCommand -ComputerName $computerName

# https://docs.microsoft.com/en-us/powershell/scripting/learn/remoting/running-remote-commands?view=powershell-7.1#run-a-remote-command
