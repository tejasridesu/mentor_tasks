
 
Problem
 
When running "curl http://localhost:8080/health", I get a "Connection Refused" error.
 
Commands Used
 
systemctl status app-service
ss -tulnp
journalctl -u app-service
systemctl restart app-service
curl http://localhost:8080/health
 
Steps
 
1. Check whether the application is running using "systemctl status".
2. Check if port 8080 is listening using "ss -tulnp".
3. Check logs to find any startup errors.
4. Fix the issue if found.
5. Restart the service.
6. Run the curl command again and verify.
 
 
Solution
 
Find the reason why the application is not listening on port 8080, fix the issue, restart the service, and verify that the health check works.
 