import sys
import os
import readgedcom

# Display the family/families with the most children, grandchildren, ...
# Given a GED file as the input paeameter. '''
#
# Copyright (c) 2022 John A. Andrea
# MIT License
#
# v1.0


def show_desc_label( g ):
    result = 'children'
    if g == 2:
       result = 'grandchildren'
    if g > 2:
       result = 'g' * (g-2) + '-grandchildren'
    return result


def get_descendant_count( ancestor, fam, gen ):
    # Some families might get visited more than once,
    # that's ok, code clarity is more important than performance.

    global counts

    counts[ancestor][gen] = 0

    for child in data[f_key][fam]['chil']:
        counts[ancestor][gen] += 1

        if 'fams' in data[i_key][child]:
           for child_fam in data[i_key][child]['fams']:
               get_descendant_count( ancestor, child_fam, gen+1 )


def show_parents( fam ):
    result = ''
    space = ''
    for parent in ['wife','husb']:
        if parent in data[f_key][fam]:
           indi = data[f_key][fam][parent][0]
           result += space + data[i_key][indi]['name'][0]['display']
           space = ' + '
    return result


if len(sys.argv) < 2:
   print( 'Usage: program-name input-file', file=sys.stderr )
   print( 'Where the input is a GEDCOM file', file=sys.stderr )
   print( 'Output is to standard-out', file=sys.stderr )
   sys.exit(1)
if not os.path.isfile(sys.argv[1]):
   print( 'Input file not found', file=sys.stderr )
   sys.exit(1)


options = { 'display-gedcom-warnings': False, 'show-settings': False }

data = readgedcom.read_file( sys.argv[1], options )
i_key = readgedcom.PARSED_INDI
f_key = readgedcom.PARSED_FAM


# get counts of the number of individuals descendant from every family
# keyed by the descendant generations
# counts[fam-id] = [ gen1: count-at-gen1, gen2: count-at-gen2, ... ]

counts = dict()

for fam in data[f_key]:
    counts[fam] = dict()
    get_descendant_count( fam, fam, 1 )

# how many generations were scanned
max_gen = 0
for fam in counts:
    max_gen = max( max_gen, max(list(counts[fam].keys())) )

# output per generation
for i in range( max_gen ):
    gen = i + 1
    print( show_desc_label( gen ) )

    # start at 1 so that counts of zero will be ignored
    max_count = 1
    for fam in counts:
        if gen in counts[fam]:
           max_count = max( max_count, counts[fam][gen] )

    # each of the families matching the maximum
    for fam in counts:
        if gen in counts[fam] and counts[fam][gen] == max_count:
           print( max_count, show_parents( fam ) )

    print()
