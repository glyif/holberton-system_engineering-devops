# Load Balance Outage (Issue #214)

By the production deployment team

### Issue Summary
At 11:23:45 PM PST on Monday (August 28, 2017), during a schedule code deployment and launch of a new intranet feature, a bad script brought down our loadbalancers. The outage lasted for 10 min and 23 seconds bringing the ending of the outage at 11:34:08 PM PST on Monday (August 28, 2017). Luckly, because of the time we deployed the outage the impact of our sales were minimal. Our assesment team marked the loss at around $10,000 and around 1.5% of our users were affects.

### Timeline
- Issue #214 was detected by our monitoring service almost immediately at 10:24:00 PM PST
- After the systems were reverted, our team did a review of the script and found the issue quite quickly. We hypothesize the engineer who wrote the script copy and pasted from a previous script and forgot to delete a line of code.
- Issue #214 was very straightforward and was fixed in a timely manner.
- Issue #214 was taken up with the engineer who wrote the script and he resolved the issue quickly.

### Detailed Analysis
A script installed nginx on all of our load balancers causing the load balancers to fail to restart because nginx was already running on the port. The script first killed the load balancer's process, then went to install new dependencies and update configurations, then finally it restarted the load balancer. While the load balancer was shutdown, nginx was installed and when the load balancer tried to start up again it failed to do so because nginx was already running on that port. The outage was quickly detected by our monitoring service and immediately reverted to the last stable back up which was made right before the code deployment. Our CDNs allowed the static site to be displayed but during the outage we were not able to take any new orders. Luckly, because of the time we deployed the outage the impact of our sales were minimal. After looking at the script, it was very noticiable the issue. The issue was quickly resolved by taking out one line of script that installed nginx.

### Next Steps
The incident itself was caused by a very mundane and careless mistake, however this outage revealed a bigger problem in our workflow. We have had code review for our engineering team from the beginner but we have not been as diligent with our dev ops. A similiar event happened (Issue #398) a year ago that brought caused few number of servers to shutdown. Since that incident, we have not improved our dev ops review process. Since Issue #214, a meeting was held with all of the lead in the Dev Ops team, all of the leads in the sys admin team, and the Director of Engineering to come up with a more comprehensive code review process for the dev ops team. They are currently still finalizing but they will have a new system implemented by the end of this working week.
