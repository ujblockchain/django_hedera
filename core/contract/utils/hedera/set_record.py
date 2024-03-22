from contract.models import DeployedContract
from hedera import ContractExecuteTransaction, ContractFunctionParameters, ContractId, Hbar

from .create_contract import deploy_contract
from .get_client import client

# init contract id
contractId = ''
# check if a contract already exists
if DeployedContract.objects.all().count() > 0:
    # get record from db
    contractId = DeployedContract.objects.all()[0:1][0].contract_id
else:
    # if no contract exist, create one and refresh record from db
    deploy_contract()
    # get new contract
    contractId = DeployedContract.objects.all()[0:1][0].contract_id


# store record in hedera blockchain using solidity function
def get_receipt(message_id, name, subject, ref, message):
    resp = (
        ContractExecuteTransaction().setGas(200_000).setContractId(ContractId.fromString(contractId)).setFunction(
            'setRecord',
            ContractFunctionParameters().addString(message_id).addString(name).addString(subject).addString(ref).
            addString(message),
        ).setMaxTransactionFee(Hbar(2)).execute(client)
    )

    # get transaction receipt
    receipt = resp.getRecord(client)

    # get receipt
    return {'receipt_id': receipt.transactionId.toString()}
