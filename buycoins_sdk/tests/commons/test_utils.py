from fixtures import *
from unittest import TestCase
from buycoins_sdk import utils


class TestUtils(TestCase):
    def test_is_valid_webhook_request(self):
        val = utils.is_valid_webhook_request(
            webhook_token=webhook_token,
            request_body=request_body,
            webhook_signature_header=signature_from_request
        )

        self.assertTrue(val, 'SHOULD BE TRUE')

        val = utils.is_valid_webhook_request(
            webhook_token=webhook_token,
            request_body="fake request",
            webhook_signature_header=signature_from_request
        )

        self.assertFalse(val, 'SHOULD BE FALSE')
