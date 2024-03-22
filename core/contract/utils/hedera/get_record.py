from contract.models import DeployedContract
from hedera import ContractCallQuery, ContractFunctionParameters, Hbar

from .get_client import client

# get contract id
contractId = DeployedContract.objects.all()[0:1]


def get_blockchain_record(message_id):
    # get blockchain record
    # 600 < gas fee < 1000
    result = (
        ContractCallQuery().setGas(50000).setContractId(contractId).setFunction(
            'getRecord',
            ContractFunctionParameters().get_record(message_id)
        ).setQueryPayment(Hbar(1)).execute(client)
    )

    # check if there is an error
    if result.errorMessage:
        exit('error calling contract: ', result.errorMessage)
    # get record
    message = result.getString(0)
    # return record
    return {'message': message}
