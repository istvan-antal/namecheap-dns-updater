# namecheap-dns-updater
Simple python script that can be used to update Namecheap DNS.

```bash
cp config.sample.json config.json
```

## Cron setup

```bash
CRONDTEXT=$(echo "*/5 * * * * $(whoami) $(pwd)/update.py > $(pwd)/update.log")
sudo /bin/sh -c "echo '$CRONDTEXT' > /etc/cron.d/namecheap-update"
```