emojize = input('Please enter a string with a :) : ')

def main (emojize):
    x = emojize.replace(':)','🙂')
    x = emojize.replace(':(','🙁')
    print (x)
    
main(emojize)