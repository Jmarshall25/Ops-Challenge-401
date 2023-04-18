# Script: Ops 401 Class 01 Lab
# Author: Jordan Marshall
# Date of latest revision: 17Apr23
# Purpose: Screen Lock

# Main

# Set the screen lock timeout in seconds
$timeout = 60

# Start a loop to continuously check for user activity
while ($true) {
    # Get the last input time for the current user
    $lastInputTime = (Get-Process "winlogon" -IncludeUserName).UserName | ForEach-Object {$_.Split("\")[1]} | ForEach-Object {Get-CimInstance Win32_Session} | Where-Object {$_.UserName -eq $_} | Select-Object -ExpandProperty LastInputTime

    # Calculate the time since the last user activity in seconds
    $idleTime = (New-TimeSpan -Start $lastInputTime).TotalSeconds

    # If the user has been inactive for longer than the specified timeout, lock the screen
    if ($idleTime -ge $timeout) {
        # Lock the screen
        [void][DllImport('user32.dll','LockWorkStation')]

        # Wait for a few seconds before starting the loop again
        Start-Sleep -Seconds 5
    }

    # Wait for a few seconds before checking for user activity again
    Start-Sleep -Seconds 5
}

# End
