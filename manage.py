import os
import sys
from dotenv import load_dotenv
import django.db.models.signals
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


load_dotenv()  # Charge automatiquement le fichier .env

sentry_sdk.init(
    dsn=os.getenv("dsn"),
    integrations=[
        DjangoIntegration(
            transaction_style='url',
            middleware_spans=True,
            signals_spans=True,
            signals_denylist=[
                django.db.models.signals.pre_init,
                django.db.models.signals.post_init,
            ],
            cache_spans=False,
            http_methods_to_capture=("GET",),
        ),
    ],
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    traces_sample_rate=1.0,  # Active la collecte de performance (1.0 = 100% des traces)
    send_default_pii=True,
)


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
