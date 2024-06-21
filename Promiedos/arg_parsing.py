import argparse

def arguments_parsing():
    parser = argparse.ArgumentParser(
                    prog='Football Useless Data',
                    description='Gather info but nothing important')
    
    parser.add_argument('--working-directory', "-wc", required= True)
    args = parser.parse_args() 
    return args