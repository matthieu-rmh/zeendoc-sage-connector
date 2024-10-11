from lib import get_sage_receipt_lines

def main():
    '''
    Main thread of our logic, where we call the corresponding functions
    to call the APIs whether from Sage or Zeendoc
    '''

    # this is a variable populated with mock data simulating receipt lines
    receipts = get_sage_receipt_lines()

    print(str(receipts))

if __name__ == "__main__":
    main()
