import argparse

def f1():
    parser = argparse.ArgumentParser(description='test')
    parser.add_argument('--addresses',default="sipingroad", help = "The path of address")
    # parser.add_argument('--RUN', dest='RUN_MODE',
    #                     choices=['train', 'val', 'test'],
    #                     help='{train, val, test}',
    #                     type=str, required=True)

    # parser.add_argument('--MODEL', dest='MODEL',
    #                     choices=['small', 'large'],
    #                     help='{small, large}',
    #                     default='small', type=str)

    args = parser.parse_args()
    return args

args=f1()
print(args.addresses)