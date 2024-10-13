from core_logics import get_sage_receipt_lines

def main():
    '''
    Main thread of our logic, where we call the corresponding functions
    to call the APIs whether from Sage or Zeendoc
    '''
    print(str(get_sage_receipt_lines()))

    # this is a variable populated with mock data simulating receipt lines
    # receipts = get_sage_receipt_lines()

if __name__ == "__main__":
    main()
