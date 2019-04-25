#-------------------------------------------------------------------------------
# Name:        Spatial Question Analysis
# Purpose:
#
# Author:      Schei008
#
# Created:     25-04-2019
# Copyright:   (c) Schei008 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import rdflib
import rdflib.plugins.sparql as sparql
import glob
#import RDFClosure
from rdflib.namespace import RDFS, RDF, OWL
from rdflib import URIRef, BNode, Literal
from rdflib import Namespace
#from urlparse import urlparse
import os


ADA = rdflib.Namespace("http://geographicknowledge.de/vocab/AnalysisData.rdf#")
SQO = rdflib.Namespace("http://geographicknowledge.de/vocab/SpatialQuestionOntology.rdf#")

"""Helper stuff"""
def load_rdf( g, rdffile, format='turtle' ):
    #print("load_ontologies")
        #print("  Load RDF file: "+fn)
    g.parse( rdffile, format = format )
    n_triples(g)
    return g

"""Reasoning stuff"""
def run_inferences( g ):
    #print('run_inferences')
    # expand deductive closure
    RDFClosure.DeductiveClosure(RDFClosure.OWLRL_Semantics).expand(g)
    RDFClosure.DeductiveClosure(RDFClosure.RDFS_Semantics).expand(g)
    n_triples(g)
    return g

def n_triples( g, n=None ):
    """ Prints the number of triples in graph g """
    if n is None:
        print( '  Triples: '+str(len(g)) )
    else:
        print( '  Triples: +'+str(len(g)-n) )
    return len(g)




def main():
    print 'Load questions!'
    output = rdflib.Graph()
    questions = load_rdf(rdflib.Graph(),'CombinedQuestions.ttl')
    for q in questions.subjects(SQO.hasSpatialExtent,None):
        print questions.value(q,RDFS.label)
        for c in questions.objects(q, RDF.type):
            print c


if __name__ == '__main__':
    main()
