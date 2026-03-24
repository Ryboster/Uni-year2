#!/bin/bash
. /etc/os-release

echo "Detecting distro ..."
case "$ID" in
    ubuntu|neon|linuxmint|pop|elementary|zorin)
        echo "... Detected Ubuntu or Ubuntu derivative"
        ./Drivers/ubuntu/ubuntu.sh
        os = "ubuntu"
        ;;
    opensuse-tumbleweed)
        echo "... Detected Tumbleweed"
        ./drivers/tumbleweed/tumbleweed.sh
        os = "tumbleweed"
        ;;
    nixos)
        echo "... Detected NixOS"
        os = "nixos"
        ./drivers/nixos/nixos.sh
        ;;
    *)
    echo "... Unsupported distro. Navigate to https://github.com/lutris/docs/blob/master/InstallingDrivers.md for instructions on how to install Vulkan."
    exit 0
esac

echo "Detecting GPU ..."
if echo $GPU_VENDOR | grep -qi nvidia; then
    echo "... NVIDIA detected"
    ./Drivers/"$os"/nvidia.sh

elif echo $GPU_VENDOR | grep -qi amd || echo $GPU_VENDOR | grep -qi intel; then
    echo "... AMD or INTEL detected"
    ./Drivers/"$os"/amdintel.sh

else
    echo "Unsupported GPU. Navigate to https://github.com/lutris/docs/blob/master/InstallingDrivers.md for instructions on how to install Vulkan."

fi
