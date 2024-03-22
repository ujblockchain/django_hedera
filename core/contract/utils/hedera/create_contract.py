import json

from contract.models import DeployedContract
from django.conf import settings
from hedera import ContractCreateTransaction, FileCreateTransaction, Hbar

from .get_client import OPERATOR_KEY, client


# set deploy  function
def deploy_contract():
    # init contract
    contractId = ''

    # check if a contract already exists
    if DeployedContract.objects.all().count() > 0:
        # get record from db
        contractId = DeployedContract.objects.all()[0:1][0].contract_id
    else:

        # set max transaction fee
        client.setMaxTransactionFee(Hbar(100))
        # set max query payment fee in hbar
        client.setMaxQueryPayment(Hbar(10))

        # open and read byte code file
        base_dir = settings.BASE_DIR
        byte_code_file = open(f'{base_dir}/contract/utils/solidity/byte_code.json')
        byte_code = json.load(byte_code_file)
        byte_code_file.close()

        # encode byte code
        byte_code = byte_code['object'].encode()

        # init file transaction
        file_transaction = FileCreateTransaction()

        # create file transaction for byte code
        file_transaction_response = (file_transaction.setKeys(OPERATOR_KEY).setContents(byte_code).execute(client))
        # transaction id
        fileId = file_transaction_response.getReceipt(client).fileId
        # init contract transaction
        blockchain_transaction = ContractCreateTransaction()
        # create hedera transaction
        blockchain_transaction_response = (
            blockchain_transaction.setGas(500_000).setBytecodeFileId(fileId).execute(client)
        )
        # get contract Id
        contractId = blockchain_transaction_response.getReceipt(client).contractId

        # save deployed contract id
        new_contract = DeployedContract(contract_id=contractId.toString())
        new_contract.save()

        # refresh record from db
        new_contract.refresh_from_db()

        # get new record
        contractId = DeployedContract.objects.all()[0:1][0].contract_id

    return contractId
