# Get Queue List
$queue = Get-MsmqQueue -Name "*" -QueueType Private
# Define Permissons
$rights = "DeleteQueue", "PeekMessage", "ReceiveMessage", "WriteMessage", "FullControl"
# Set the permisson to the queues
$rights | Foreach-Object { Set-MsmqQueueAcl -InputObject $queue -UserName "DOMAIN\user_name" -Allow $PSItem}

