# nvidia-info
Bash script that retrieves nvidia info for a list of computers

This script requires ssh access on default port to the clients and each client need to have install nvidia-smi to been able to retrieve current status. To get the script working just needs to include a client name (computer) per line in <b>clients.txt</b> file.

Example output for execution:

fddev6 --></br>
|100%   69C    P0    N/A /  52W |   3636MiB /  4096MiB |    100%      Default |</br>
fddev8 --></br>
| 36%   57C    P2    59W / 102W |  11067MiB / 12288MiB |    100%      Default |</br>
af4coin1 --></br>
| 85%   65C    P2   129W / 140W |   5364MiB /  8192MiB |    100%      Default |</br>
| 65%   58C    P2   122W / 140W |   5224MiB /  8192MiB |    100%      Default |</br>
