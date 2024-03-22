from decouple import config
from hedera import AccountId, Client, PrivateKey

# init variables
OPERATOR_ID = AccountId.fromString(config('ACCOUNT_ID'))
OPERATOR_KEY = PrivateKey.fromString(config('DER_ENCODED_PRIVATE_KEY'))


def network():
    # set network, we are using testnet
    # using hedera testnet
    client = Client.forTestnet()
    return client


# init client, which in this case in group9ify
client = network().setOperator(OPERATOR_ID, OPERATOR_KEY)
