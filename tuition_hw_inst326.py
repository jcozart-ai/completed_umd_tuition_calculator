from argparse import ArgumentParser
import sys
def calculate_tuition(credits=12, resident=True, dt=False):
    """ Calculates tuition and mandatory fees for one semester at UMD.

    Takes into consideration the number of credits the student is taking,
    whether they are a resident of Maryland, and whether they pay
    differential tuition.

    Args:
        credits (integer): the number of credits the student is taking
            (default: 12).
        resident (boolean): whether the student is considered a
            Maryland state resident for tuition purposes (default: True).
        dt (boolean): whether or not the student pays
            differential tuition (default: False).

    Raises:
        ValueError: credits must be non-negative.

    Returns:
        float: the student's combined tuition and mandatory fees.
    """
    if credits < 0:
       raise ValueError("credits must be non-negative")
    if credits == 0:
        return 0
    if credits >= 12:
        if resident:
            tuition = 4412.00 
        else:
            tuition = 17468.00 
    else:
        if resident:
            tuition = credits * 367.00 
        else:
            tuition = credits * 1456.00 
    if credits >= 9:
        tuition = tuition + 977.50
    else:
        tuition = tuition + 455.00    
    if dt:
        if credits >= 12:
            tuition = tuition + 1428.00
        else:
            tuition = tuition + credits * 118.00   
    return(tuition)
 

def parse_args(arglist):
     """ Parses command-line arguments.

    The following optional command-line arguments are defined:

    -c / --credits: the number of credits the student is taking
        (type: int, default: 12)
    -nr / --nonresident: indicates the student is not a Maryland
        resident (action: 'store_true')
    -dt / --differentialtuition: indicates the student pays differential
        tuition (action: 'store_true')

    Args:
        arglist (list of str): a list of command-line arguments.

    Returns:
        namespace: a namespace with variables credits, nonresident, and
        differentialtuition.
    """
     parser = ArgumentParser()
     parser.add_argument('-c', '--credits', type=int, default=12)
     parser.add_argument('-nr', '--nonresident', action='store_true')
     parser.add_argument('dt', 'differentialtiution', action='store_true')
     return parser.parser_args(arglist)



if __name__ == "__main__":
    arglist = sys.argv[1:]
    args = parse_args(arglist)
    tuition = calculate_tuition(
        args.credit, not args.nonresident, args.differentialtuition
    )
    print(f"Your tuition and fees total ${tuition}")