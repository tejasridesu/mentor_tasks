
Problem
 
An application's memory usage keeps increasing over time.
 
Commands Used
 
free -h
ps aux --sort=-%mem | head
watch free -h
journalctl -u app-service
systemctl restart app-service
 
Steps
 
1. Check current memory usage using "free -h".
2. Identify the process using the most memory.
3. Monitor memory usage over time.
4. Check logs for memory-related errors.
5. Determine if there is a memory leak.
6. Restart the application if required.
 
Solution
 
Identify the application causing the issue, monitor its memory usage, check logs, and restart it if necessary. A permanent fix may require code changes.
 