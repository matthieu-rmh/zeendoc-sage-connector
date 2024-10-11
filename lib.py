from sage_calls import get_receipts

def get_sage_receipt_lines():
    return get_receipts()

def convert_receipt_lines(receipts):
    '''
    Convert receipts into usable lines to be sent to Zeendoc
    '''
    return receipts
