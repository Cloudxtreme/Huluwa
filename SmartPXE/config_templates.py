# below is templates for DHCP server config

DHCPServerConfigPath = "/etc/dhcp/dhcpd.conf"

DHCPConfigTemplate = """
option domain-name-servers 8.8.8.8, 8.8.4.4;
option routers 192.168.111.1;
option broadcast-address 192.168.111.255;
default-lease-time 600;
max-lease-time 7200;
filename "pxelinux.0";
deny unknown-clients;

subnet 192.168.111.0 netmask 255.255.255.0 {
    range 192.168.111.100 192.168.111.200;
    
    {{ hosts }}
}
"""

DHCPHostEntryTemplate = """
host {{ hostname }} {
    hardware ethernet {{ mac_address }};
}
"""

# below is templates for PXE server config

PXEConfigPath = "/var/lib/tftpboot/pxelinux.cfg/default"

PXEConfigTemplate= """
default menu.c32
prompt 0
timeout 5
ONTIMEOUT 1

menu title ########## Huluwa PXE Boot Menu ##########

{{ entries }} 
"""

PXEOSEntryTemplate = """
label 1
menu label ^1) {{ display_name }}
menu default
kernel {{ os_name }}/vmlinuz
append initrd={{ os_name }}/initrd.img method=http://{{ tftp_ip }}/{{ os_name }} ks=http://{{ tftp_ip }}/kickstart/ks_{{ os_name }}.cfg devfs=nomount
"""


