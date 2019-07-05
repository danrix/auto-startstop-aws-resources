# auto-startstop-aws-resources

Auto Start and Stop certian AWS resources to better match production/development schedules and realize savings.

Currently we auto start/stop instances, both RDS and EC2.

The system uses CloudWatch Event Rules, lambda functions and local python and batch (Windows) scripts. Results are logged to CloudWatch.

Future: use SNS to notify of anomalies.