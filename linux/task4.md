
Problem
 
A service keeps restarting every few minutes.
 
Commands Used
 
systemctl status app-service
journalctl -u app-service
free -h
df -h
systemctl restart app-service
 
Steps
 
1. Check the service status.
2. Confirm that the service is restarting repeatedly.
3. Check logs to find the reason for the crash.
4. Check memory and disk usage if needed.
5. Fix the root cause.
6. Restart the service and verify.

 
Solution
 
Identify the root cause from logs or system resources, fix the issue, and then restart the service.
 