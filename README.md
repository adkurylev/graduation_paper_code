# Bitcoin Transactions Untangling

This study presents an analysis of bitcoin transactions from the very beginning of the blockchain. 
All transactions are classified into 4 classes: simple, separable, ambiguous, difficult. After the classification, an
analysis was made of the volume of transaction classes over time, what this distribution may be related
to and what is the dynamics of these classes. One of the goals of the study is to develop and publish an
algorithm for untangling Shared Send transactions. This requires transforming the transaction into a
graph, simplifying it, removing duplicate inputs and outputs, and recalculating values. Writing and testing
an algorithm for disentangling bitcoin transactions is accompanied by its publication in open sources.

In the course of this study, a pseudopolynomial untangling dynamic programming algorithm was developed, implemented and published. 
A local infrastructure has been created to unravel the transactions of the bitcoin blockchain network,
unraveling using Full Bitcoin Node, pre- and post-processing in Python and untangling in C++. 
Processed all transactions since 2009 (beginning of work bitcoin) until 2014, 
based on the results of computational experiments, we can conclude that
about 30% of confusing transactions in the bitcoin network, 93% of which can be 
untangled with an unambiguous way using the presented algorithm.
