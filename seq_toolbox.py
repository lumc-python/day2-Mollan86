import sys
import argparse


def calc_gc_percent(seq):
    at_count, gc_count = 0, 0
    for char in seq.upper():
        if char in ('A', 'T'):
            at_count += 1
        elif char in ('G', 'C'):
            gc_count += 1
        else:
        	raise ValueError(
        		"Unexpected charatcter found: {}. Only "
        		"ACTGs are allowed.".format(char))	

    try:
    	return gc_count * 100.0 / (gc_count + at_count)
    except ZeroDivisionError:
        return 0.0

# if __name__ == '__main__':
#     # Create our argument parser object.
#     parser = argparse.ArgumentParser()
#     # Add argument for the input type.
#     parser.add_argument(
#         'mode', type=str, choices=['file', 'text'],
#         help='Input type of the script')
#     # Add argument for the input value.
#     parser.add_argument(
#         'value', type=str,
#         help='Input value of the script')
#     # Do the actual parsing.
#     args = parser.parse_args()

#     message = "The sequence '{}' has a %GC of {:.2f}"

#     if args.mode == 'file':
#         try:
#             f = open(args.value, 'r')
#             for line in f:
#                 seq = line.strip()
#                 gc = calc_gc_percent(seq)
#                 print message.format(seq, gc)
#         finally:
#             f.close()
#     else:
#         seq = args.value
#         gc = calc_gc_percent(seq)
#         print message.format(seq, gc)



        