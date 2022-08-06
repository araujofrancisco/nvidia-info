# nvidia-info
A set of tools to obtain nvidia information from clients using ssh to retrieve the data. There is a main Bash script that retrieves nvidia info (fan speed, temperature, power and memory) for a list of computers and a python program that can create and update a database to keep a record of the information, designed to be used with a cron job to record in regular intervals the data.

The Bash script requires ssh access on default port to the clients and each client need to have install nvidia-smi to been able to retrieve current status. To get the script working just needs to include a client name (computer) per line in <b>clients.txt</b> file.

usage: getinfo.sh [-h|--header]

Example output for execution:

fddev6 100% 68C P0 N/A / 52W  3929MiB / 4096MiB  100% Default</br>
fddev8  36% 58C P2 101W / 102W  7245MiB / 12288MiB  100% Default</br>
af4coin1  85% 66C P2 130W / 140W  5389MiB / 8192MiB  100% Default</br>
af4coin1 65% 58C P2 121W / 140W  5256MiB / 8192MiB  100% Default</br>

The python program just calls the Bash script and save information to the database, creating it if it does not exists.

usage: python3 update_db.py
