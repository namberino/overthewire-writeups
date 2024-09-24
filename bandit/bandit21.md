Cron is a job scheduling utility present in Unix like systems. The `crond` daemon (A process which runs in the background, performs tasks, and is not interactive) enables cron functionality and runs in background. The cron reads the crontab (cron tables) for running predefined scripts. We can see the crontabs in `/etc/cron.d`:

```sh
cat /etc/cron.d/cronjob_bandit22
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
```

We cat the cron.d for bandit22. We could see that it runs the file `/usr/bin/cronjob_bandit22.sh` as bandit22. And this is what the asterisks mean:

```
 * * * * *  command to execute
 ┬ ┬ ┬ ┬ ┬
 │ │ │ │ │
 │ │ │ │ │
 │ │ │ │ └───── day of week (0 - 7) (0 to 6 are Sunday to Saturday, or use names; 7 is Sunday, the same as 0)
 │ │ │ └────────── month (1 - 12)
 │ │ └─────────────── day of month (1 - 31)
 │ └──────────────────── hour (0 - 23)
 └───────────────────────── min (0 - 59)
```

If we cat this script:

```bash
cat /usr/bin/cronjob_bandit22.sh
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```

This means it's changing the permission of `/tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv` and reading bandit22's password into that file. So we can get the password of bandit22 by reading that file:

```sh
cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```