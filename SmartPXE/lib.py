import subprocess
from SmartPXE.config_templates import *
from jinja2 import Template


def generate_pxe_os_entry(os):
    t = Template(PXEOSEntryTemplate)
    return t.render(
        display_name=os.display_name,
        os_name=os.name,
        tftp_ip=os.tftp_ip
        )


def generate_pxe_conf(content):
    t = Template(PXEConfigTemplate)
    return t.render(entries=content)


def generate_dhcp_client_entry(client):
    t = Template(DHCPHostEntryTemplate)
    return t.render(
        hostname=client.hostname,
        mac_address=client.mac
    )


def generate_dhcp_conf(content):
    t = Template(DHCPConfigTemplate)
    return t.render(hosts=content)


def _overwrite(path, content):
    try:
        with open(path, 'w') as f:
            f.write(content)
    except:
        return False
    return True


def update_dhcp_conf(content):
    return _overwrite(DHCPServerConfigPath, content)


def update_pxe_conf(content):
    return _overwrite(PXEConfigPath, content)


def restart_dhcpd():
    if subprocess.call(["systemctl", "restart", "dhcpd"]) == 0:
        return True
    return False
