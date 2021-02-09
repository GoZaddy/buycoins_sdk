"""
This module will contain some util functions that can be used by users
"""

import hmac
import hashlib


def is_valid_webhook_request(webhook_token: str, request_body: str, webhook_signature_header: str) -> bool:
    """This method verifies that requests to your Webhook URL are genuine and from Buycoins.

    Args:
        webhook_token: your webhook token
        request_body: the body of the request
        webhook_signature_header: the X-Webhook-Signature header from BuyCoins

    Returns:
        a boolean stating whether the request is valid or not

    """
    hmac_request_body = hmac.new(webhook_token.encode(), request_body.encode(), hashlib.sha1)
    return hmac.compare_digest(hmac_request_body.hexdigest(), webhook_signature_header)
