from django.contrib.auth.decorators import login_required

from django.views.decorators.http import require_http_methods, require_POST

# FIXME: Requite token
@require_POST
@login_required
def request_activation(request):
    # parthner_id, customer_id, product_id, value_to_charge):
    # POST
    pass
