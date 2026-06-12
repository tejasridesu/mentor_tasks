 
Problem
 
A process is using 95% CPU.
 
Commands Used
 
top
ps -fp PID
journalctl -u service-name
kill PID
kill -9 PID
 
Steps
 
1. Run "top" to find the process using high CPU.
2. Note the PID of the process.
3. Run "ps -fp PID" to see what the process is doing.
4. Check logs if needed.
5. Find out if the high CPU usage is expected or not.
6. Take action based on the findings.
 
 
Solution
 
If the process is working normally, no action is needed. If it is stuck or causing issues, restart the service or stop the process. Use "kill -9" only as a last option.
 