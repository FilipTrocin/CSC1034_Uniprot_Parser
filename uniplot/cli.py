import argparse


from . import plot
from . import analysis
from . import parse


user_input = input("Enter the path of the file: ")

f = open(user_input,'r+')


LOCbig = "uniprot_receptor.xml.gz"
LOCsmall = "uniprot_sprot_small.xml.gz"

def average(args):
    """Printing the average length of large and small set"""
    print("Average Length of that set is {}".format(
        analysis.average_len(parse.uniprot_seqrecords(user_input))))


def dump(args):
    """Returns data of the proteins"""
    for record in parse.uniprot_seqrecords(user_input):
        print(record)

def names(args):
    """Returns names of the proteins"""
    for record in parse.uniprot_seqrecords(user_input):
        print(record.name)

def plot_average_by_taxa_bar_chart(args):
    """Returns the average length of top-level taxas using bar chart"""
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(user_input))
    plot.plot_bar_show(av)

def plot_average_by_taxa_pie_chart(args):
    """Returns the average length of top-level taxas using pie chart"""
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(user_input))
    plot.plot_pie_show(av)

def cli():
    """Assigning commands to the particular functions"""
    parser = argparse.ArgumentParser(prog="uniplot")

    subparsers = parser.add_subparsers(help="Sub Command Help")

    subparsers.add_parser("dump", help="showing all data about proteins").set_defaults(func=dump)
    subparsers.add_parser("list", help="showing list of proteins names").set_defaults(func=names)
    subparsers.add_parser("average", help="showing average length of proteins").set_defaults(func=average)
    subparsers.add_parser("plot-average-by-taxa-bar-chart", help="showing bar graph for the average length of proteins")\
        .set_defaults(func=plot_average_by_taxa_bar_chart)
    subparsers.add_parser("plot-average-by-taxa-pie-chart", help="showing pie chart for the average length of proteins")\
        .set_defaults(func=plot_average_by_taxa_pie_chart)

    args = parser.parse_args()

    args.func(args)

f.close()


