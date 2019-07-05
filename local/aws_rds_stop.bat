:: This script invokes aws cli command(s) to stop an RDS instance after a veeam operation has completed.
:: This script is called by Veeam programmatically. Not to be executed directly.

:: 1. Pause for a reasonable time to allow Veeam to close connection to databases

sleep 1200

:: 2. Invoke aws command

aws rds stop-db-instance --db-instance-identifier rds_instance_name

:: 3. Exit

Exit