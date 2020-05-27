# dashboard

This is a collection of telegraf configuration files (`*.conf`) and a couple other scripts that I use to collect data for my Grafana dashboard and push to InfluxDB. The .conf files are straight from my telegraf directory (`/etc/telegraf/telegraf.d/`) edited only to remove passwords and other private information. They may lack comments and may not formatted to be user friendly for portable use. These files are supplied for reference for others to use to determine the proper OIDs for their own telegraf configurations.

Description:

1. **airvpn.conf**: For use with AirVPN to get expiration date and public IP address
2. **cisco.conf**: Uptime for Cisco Small Business switches
3. **cisco500.conf**: Data transfer information for four ports of interest. Polled every 60s instead of 15s because it takes a while for telegraf to grab this data
4. **cyberpower.conf**: For use with RMCARD205 for CyberPower UPS
5. **edgerouter.conf**: For Ubiquiti EdgeRouter series of internet routers
6. **edgeswitch.conf**: For Ubiquiti EdgeSwitch series but works on Unifi switches
7. **esxi.conf**: Metrics from VMWare ESXi
8. **generic.conf**: Uptime and system name metrics from various devices
9. **idrac.conf**: For use with Dell iDRAC7 (using with Dell R720xd)
10. **idrac6.conf**: For use with Dell iDRAC6 (using with Dell R510 & R310)
11. **synology.conf**: For use with Synology NAS devices
12. **unifiap.conf**: For use with Ubiquiti access points
13. **vcenter.conf**: Collect data from VMWare vCenter (using with v6.7)
14. **weather.conf**: Weather information from openweathermap.org. You'll need to sign up to get your personal API key.
15. **updateip.sh**: Runs as a cronjob in Ubuntu to push the machine's IP address to the database. I use this on my OpenVPN VM to get the VPN public IP address and on my data aggregation VM for my public IP.
16. **readtemp.py**: Python script running as a cron job for Raspberry pi to gather data from DS18B20 temperature sensors and push to database

Not included in the list above:
1. Data collection from Plex and Tautulli. See https://github.com/Boerderij/Varken
2. WAN in/out speeds and total data used is collected from PRTG which I have running in a VM to collect data from my EdgeRouter 4. See https://github.com/neuralfraud/grafana-prtg

In Grafana you can import my dashboard with ID `12370`
