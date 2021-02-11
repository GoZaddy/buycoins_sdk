Verifying Webhooks from Buycoins
=================================

| Buycoins uses webhooks to inform your app when certain events take place. You can learn more about this `here <https://developers.buycoins.africa/webhooks/introduction>`_.

| In this brief section, we will be looking at how to verify that requests being made to your webhook URL are genuine and from Buycoins using the Buycoins SDK.

.. note:: You will need to obtain a webhook token from Buycoins. Visit `here <https://developers.buycoins.africa/webhooks/introduction>`_ to learn how to do this.

The utils module
-----------------
The Buycoins SDK contains an utils module which houses a function called **is_valid_webhook_request**. Using this function, we can easily tell if a webhook request is genuine or not::

    >>> from buycoins_sdk import utils
    >>> import json
    >>> webhook_token = '...'  # should be gotten from Buycoins

    ....

    # if you are using flask:
    # (the process should be similar irrespective of your framework)
    >>> is_valid = utils.is_valid_webhook_request(
            webhook_token=webhook_token,
            webhook_signature_header=request.headers.get('X-Webhook-Signature'),
            request_body=json.dumps(request.get_json())
        )

If the webhook request is a valid one, we can then create an Event object using the Event class in the Buycoins SDK::

    >>> from buycoins_sdk import types
    >>> if is_valid:
            event = types.Event.from_request_body(request.get_json())
            print(event.event_type)  # EventType.COINS_INCOMING



