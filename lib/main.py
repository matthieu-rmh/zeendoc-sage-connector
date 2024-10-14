from core_logics import get_sage_receipt_lines, convert_receipt_lines

def main():
    '''
    Main thread of our logic, where we call the corresponding functions
    to call the APIs whether from Sage or Zeendoc
    '''

    raw_sage_receipt_lines = get_sage_receipt_lines()
    # print(str(type(raw_sage_receipt_lines)))
    converted_sage_receipt_lines = convert_receipt_lines(raw_sage_receipt_lines) 

    print(str(converted_sage_receipt_lines[0]))

    # this is a variable populated with mock data simulating receipt lines
    # receipts = get_sage_receipt_lines()

if __name__ == "__main__":
    main()
