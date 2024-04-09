import firefly_iii_client
from firefly_iii_client.models.account_array import AccountArray
from firefly_iii_client.models.account_type_filter import AccountTypeFilter
import monobank_api
import apscheduler
import logging
import datetime
import iso18245
import json

from firefly_iii_client.rest import ApiException

mono_base = monobank_api.BaseAPI()
mono_private = monobank_api.PersonalAPI(token=token)
access_token = ff_token
firefly_config = firefly_iii_client.configuration.Configuration(host="https://firefly.klyba.family/api",
                                                                access_token=access_token)

private_info = mono_private.get_client_info()
mono_accounts = private_info['accounts']
mono_jars = private_info['jars']

with firefly_iii_client.ApiClient(firefly_config) as ff_api_client:
    acc_api_instance = firefly_iii_client.AccountsApi(ff_api_client)
    acc_type = AccountTypeFilter(value='asset')

    # Store a new transaction
    acc_api_response = acc_api_instance.list_account(type=acc_type)
    for ff_account in acc_api_response.data:
        print(ff_account.attributes.notes)

# client_info = mono_private.get_client_info()
# statements = mono_private.get_statements(account='ZI8Cjv_mnaSatZeHiYJ1aw', date_from=datetime.datetime.now()-datetime.timedelta(days=1), date_to=datetime.datetime.now())
# print(client_info)
