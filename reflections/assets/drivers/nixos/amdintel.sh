/etc/nixos/hardware-configuration.nix >> boot.initrd.kernelModules = [ "amdgpu" ];
services.xserver.enable = true; # to enable the xorg server
services.xserver.videoDrivers = [ "amdgpu" ]; # to load the amdgpu kernel module