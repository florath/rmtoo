'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Generates the pricing graph

 (c) 2010,2017 by flonatel

 For licensing details see COPYING
'''
from __future__ import print_function

import sys
import csv

from rmtoo.lib.Encoding import Encoding


def parse_argv():
    """ Minimalistic (but working) way to parse the command line
    parameters and to be sure that two parameters are supplied.
    """
    if len(sys.argv) != 3:
        print("Usage: %s csvfile dotfile" % sys.argv[0])
        sys.exit(1)
    return sys.argv[1], sys.argv[2]


def main():
    """The main function for the pricing graph"""
    csvfilename, graphfilename = parse_argv()

    # The files must be saved according to this rules:
    #  delimiter must be a ','
    #  quotechar must be a '"'
    csvr = csv.reader(open(csvfilename, 'rb'),
                      delimiter=',', quotechar='"')

    # Open the output file and write out the header.
    graph_fd = open(graphfilename, "w")
    graph_fd.write("digraph reqdeps {\nrankdir=BT;\nmclimit=10.0;\n"
                   "nslimit=10.0;ranksep=1;\n")

    # Read in all the rows and store them: there is the need to run
    # multiple times and in different directions through this list.
    rows = []
    for row in csvr:
        rows.append(row)

    # This holds the dependent costs of a requirement.  If there is no
    # entry in this dictionary, there are no dependent costs.
    dep_costs = {}
    # Because the nodes are topoligical sorted, start at the end and go
    # until you reach the beginning.
    rows.reverse()
    for row in rows:

        # Colorize graph
        nodeparams = []
        if row[1] == 'none':
            nodeparams.append("color=red")
        elif row[1] == 'partial':
            nodeparams.append("color=orange")
        elif row[1] == 'fully':
            nodeparams.append("color=green")

        # Compute local costs (lcosts)
        # Sometimes a ',' is used to seperate 1000
        dayrate = float(Encoding.to_unicode(row[2])[:-2].replace(",", ""))
        days = float(row[3])
        material = float(Encoding.to_unicode(row[4])[:-2].replace(",", ""))
        lcosts = dayrate * days + material

        # Check if there are dependent costs (dcosts)
        dcosts = 0.0
        if row[0] in dep_costs:
            dcosts = dep_costs[row[0]]

        # Compute the overall costs
        ocosts = lcosts + dcosts

        # Write out node (attributes)
        nodeparams.append('label="%s\\n%9.2f\\n%9.2f"' %
                          (row[0], ocosts, lcosts))
        graph_fd.write("%s [%s];\n" % (row[0], ",".join(nodeparams)))

        # Add the current costs to the (possible existant) dep_costs
        acosts = 0.0
        if row[5] in dep_costs:
            acosts = dep_costs[row[5]]
        dep_costs[row[5]] = acosts + ocosts

    # Output all the existant edges
    for row in rows:
        if row[5] != '0':
            graph_fd.write("%s -> %s;\n" % (row[0], row[5]))

    graph_fd.write("}")
    graph_fd.close()


if __name__ == "__main__":
    main()
