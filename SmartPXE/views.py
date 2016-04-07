from django.shortcuts import render
from django.views.generic import View
from SmartPXE.forms import XForm
from SmartPXE.models import Client, OS
from django.http import JsonResponse


class XView(View):

    def get(self, request, *args, **kwargs):
        form = XForm()
        return render(request, 'SmartPXE/index.html', {"form": form})


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
