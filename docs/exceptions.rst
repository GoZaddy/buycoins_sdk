Exceptions and Exception Handling
===================================

| Buycoins SDK provides some Exception classes which can be found here: :doc:`buycoins_sdk.commons`
| These Exception classes allow developers to easily spot errors coming from the Buycoins SDK package and handle them appropriately.

| In this section, we will briefly discuss two important exceptions.

BuycoinsException
^^^^^^^^^^^^^^^^^^
This is the base exception class from which other classes inherit. Every exception raised by the Buycoins Python SDK will inherit this class and that makes it easier to spot Buycoins-related exceptions.

Also note that not every possible error that can be raised by the Buycoins SDK has a corresponding Exception class, only a select few do. However, other errors without an exception class will still raise a regular BuycoinsException.

BuycoinsHTTPException
^^^^^^^^^^^^^^^^^^^^^^^
| This exception is raised whenever an HTTP error is raised during the execution of the BuycoinsSDK.
| It has three fields:

    * status_code [int]: an integer representing the status code of the HTTPError
    * response [requests.Response]: the HTTP Response from the HTTPError
    * error_message [str]: the error message from the HTTPError

This exception is usually raised when you try to access the Buycoins API with incorrect or invalid API keys or when an internal server error occurs.

