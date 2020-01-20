sudo apt-get install network-manager -y

sudo apt purge openresolv dhcpcd5 -y

sudo systemctl disable NetworkManager-wait-online.service
sudo systemctl mask NetworkManager-wait-online.service
