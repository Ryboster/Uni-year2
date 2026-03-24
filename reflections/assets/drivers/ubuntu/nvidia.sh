sudo add-apt-repository ppa:graphics-drivers/ppa
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install -y nvidia-driver-535 libvulkan1 libvulkan1:i386

./Drivers/finish.sh