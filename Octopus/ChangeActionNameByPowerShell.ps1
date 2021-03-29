$octopusServer = "https://TestOctopusURL" 
$octopusApiKey = "API-key" 
$octpusProjectNameID = "deploymentprocess-Projects-166"

$endPoint = New-Object Octopus.Client.OctopusServerEndpoint($octopusServer, $octopusApiKey);
$repo =  New-Object Octopus.Client.OctopusRepository($endPoint);
$deploymentProcess = $repo.DeploymentProcesses.Get($octpusProjectNameID);

$step = 0;
$subStep = 0;
foreach ($step  in $deploymentProcess.Steps)
{
    $step = $step + 1;
    Write-Host "Step $($step): $($step.Name) of project: $($project.Name)"
    foreach ($action in $step.Actions)
    {
        # use this number for unique action name
        $subStep = $subStep + 1 
        if ($step -eq 10){ # Specific Step
            # new action name
            $newName = -join($action.Name, " ", $subStep)
            echo "will update $($action.Name) to $($newName)"
            # Update Action Name
            $action.Name = $newName
            # Update DeploymentProcesses
            $repo.DeploymentProcesses.Modify($deploymentProcess)
        }
    }
}

