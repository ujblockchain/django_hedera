from hedera import ContractExecuteTransaction, ContractFunctionParameters, ContractId, Hbar

from .create_contract import deploy_contract
from .get_client import client

# init contract id
contractId = deploy_contract()


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
