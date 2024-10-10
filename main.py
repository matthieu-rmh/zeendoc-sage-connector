from sage_calls import get_receipts
    
def convert_receipt_lines(receipts):
    '''
    Convert receipts into usable lines to be sent to Zeendoc
    '''
    return receipts


def main():
    '''
    Main thread of our logic, where we call the corresponding functions
    to call the APIs whether from Sage or Zeendoc
    '''

    # this is a variable populated with mock data simulating receipt lines
    receipts = get_receipts()
    
    converted_receipts = convert_receipt_lines()

    print(str(receipts))

if __name__ == "__main__":
    main()
