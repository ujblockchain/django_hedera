import json

from hedera import ContractCallQuery, ContractFunctionParameters, ContractId, Hbar

from core.contract.models import DeployedContract

from .get_client import client

# get contract id
contractId_string = DeployedContract.objects.all()[0:1][0].contract_id
contractId = ContractId.fromString(contractId_string)


def get_blockchain_record(message_id):
    # get blockchain record
    # 600 < gas fee < 1000
    result = (
        ContractCallQuery().setGas(50000).setContractId(contractId).setFunction(
            'getRecord',
            ContractFunctionParameters().addString(message_id)
        ).setQueryPayment(Hbar(1)).execute(client)
    )

    # check if there is an error
    if result.errorMessage:
        exit('error calling contract: ', result.errorMessage)
    # get record
    message = result.getString(0)

    # convert to list
    # list is in [name, subject, reference, message]
    message_list = json.loads(message)

    # return record
    return message_list
