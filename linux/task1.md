Problem
 
A client says the server is slow.
 
Commands Used
 
top
free -h
df -h
ps aux --sort=-%cpu | head
ps aux --sort=-%mem | head
 
Steps
 
1. Run "top" to check CPU usage.
2. Run "free -h" to check memory usage.
3. Run "df -h" to check disk usage.
4. Check which process is using more CPU.
5. Check which process is using more memory.
 
Solution
 
After finding the resource causing the issue, take the required action such as cleaning disk space, restarting a process, or investigating the application.