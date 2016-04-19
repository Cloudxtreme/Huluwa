from django.shortcuts import render
from django.views.generic import View
from SmartPXE.forms import XForm
from SmartPXE.models import Client, OS
from django.http import JsonResponse
from SmartPXE.lib import restart_dhcpd, generate_pxe_os_entry, \
    generate_pxe_conf, generate_dhcp_client_entry, generate_dhcp_conf, \
    update_pxe_conf, update_dhcp_conf


class XView(View):

    def get(self, request, *args, **kwargs):
        form = XForm()
        return render(request, 'SmartPXE/index.html', {"form": form})

    def post(self, request, *args, **kwargs):
        form = XForm(request.POST)
        import ipdb; ipdb.set_trace()
        if form.is_valid():
            # generate PXE and DHCP config
            # then restart DHCP service
            try:
                os = OS.objects.get(pk=form.cleaned_data['os'])
                client = Client.objects.get(pk=form.cleaned_data['client'])
            except:
                return render(request, 'SmartPXE/resource_does_not_exist.html')
            # generate PXE conf
            os_entry = generate_pxe_os_entry(os)
            pxe_conf = generate_pxe_conf(os_entry)

            # generate dhcpd conf
            client_entry = generate_dhcp_client_entry(client)
            dhcpd_conf = generate_dhcp_conf(client_entry)

            if not update_pxe_conf(pxe_conf):
                return render(request, 'SmartPXE/error.html')
            if not update_dhcp_conf(dhcpd_conf):
                return render(request, 'SmartPXE/error.html')
            if not restart_dhcpd():
                return render(request, 'SmartPXE/error.html')

            return render(request, 'SmartPXE/success.html')
        return render(request, 'SmartPXE/error.html')



def get_client_list(request):
    # TODO filter the client object by string from user
    data = {
        "total_count": Client.objects.count(),
        "items": []
    }
    for x in Client.objects.all():
        data["items"].append({
            "id": x.id,
            "full_name": x.hostname
            }
        )
    return JsonResponse(data)


def get_os_list(request):
    # TODO filter the os object by string from user
    data = {
        "total_count": OS.objects.count(),
        "items": []
    }
    for x in OS.objects.all():
        data["items"].append({
            "id": x.id,
            "full_name": x.display_name
            }
        )
    return JsonResponse(data)
