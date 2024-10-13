from sage.api_calls import get_receipt_lines

def get_sage_receipt_lines():
    return get_receipt_lines()

def convert_receipt_lines(receipts):
    '''
    Convert receipts into usable lines to be sent to Zeendoc
    '''
    return receipts
