from django.shortcuts import render

from .config_product import ENABLE_NOTIFICATIONS, ENABLE_REPORTS


def inicio(request):
    return render(
        request,
        'core/inicio.html',
        {
            'enable_reports': ENABLE_REPORTS,
            'enable_notifications': ENABLE_NOTIFICATIONS,
        },
    )