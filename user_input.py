# it gets user input

def get_user_input():
    '''collects user input for medication details '''

    name = input('Enter medication name')
    dose = input('Enter the medicine dose')
    frequency = input('Enter the frequency of medicine intake(daily/weekly)')
    time = input('Enter time for your medicine')


    return { 'Medicine name:' : name,
             "Medicine dose" : dose,
             'Frequency': frequency,
             'Time': time
    }


