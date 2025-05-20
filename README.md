# nvidia-info

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/araujofrancisco/nvidia-info)

A set of tools to obtain NVIDIA GPU information from multiple clients using SSH. The main tool is a Bash script that retrieves NVIDIA info (fan speed, temperature, power, memory usage, etc.) for a list of remote computers. There is also a Python script to save the collected data into a database.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)
- [Contributing](#contributing)
- [License](#license)

## Description

This project helps system administrators monitor NVIDIA GPUs across several remote machines. It uses SSH to connect to each client, gathers GPU statistics, and can store the results in a database for further analysis.

## Features

- Collects GPU fan speed, temperature, power usage, and memory stats.
- Works across multiple remote clients via SSH.
- Stores collected data in a database (optional, via Python script).

## Requirements

- SSH access to each client (default port 22).
- `nvidia-smi` installed on all client machines.
- Python 3.x (for database storage).
- Necessary permissions to SSH and run scripts on remote clients.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/araujofrancisco/nvidia-info.git
   cd nvidia-info
   ```
2. Ensure nvidia-smi is available on all clients.
3. Make the Bash script executable:
   ```bash
   chmod +x getinfo.sh
   ```
   
## Usage

Bash Script
Retrieve NVIDIA information from clients:
```bash
./getinfo.sh [-h|--header]
```
- -h or --header: Display header line with column names.

## Python Script
Save the collected information to a database:
```bash
python3 update_db.py
```

The Python program calls the Bash script and saves the information to a database, creating it if it does not exist.

## Example Output
```bash
fddev6   100% 68C P0 N/A / 52W   3929MiB / 4096MiB   100% Default
fddev8    36% 58C P2 101W / 102W 7245MiB / 12288MiB  100% Default
af4coin1  85% 66C P2 130W / 140W 5389MiB / 8192MiB   100% Default
af4coin1  65% 58C P2 121W / 140W 5256MiB / 8192MiB   100% Default
```

## Contributing
Contributions are welcome! Please follow these steps:

- Fork the repository.
- Create a new branch (git checkout -b feature-branch).
- Commit your changes (git commit -m "Add feature").
- Push to the branch (git push origin feature-branch).
- Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

