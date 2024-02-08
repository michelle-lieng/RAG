========================
Vector Database Summary
========================

A vector database (used interchangably with a vector store) is a storage system used for high-dimensional
vector data. A complex vector database includes functionalities for efficiently querying and managing vectors,
such as indexing. 

We apply embeddings to text captures the semantic and contextual information of the data and then 
store embeddings in a vector database so we can index it.

Indexing
========
An index is a structured way to organise data within a vector db to improve efficiency of query operations, 
especially for similarity searches. The index enables you to quickly retrieve vectors that are most similar
to a query vector, based on a specific distance or similarity metric (e.g. Euclidean distance (L2), cosine 
similarity).

Indexes can take various forms depending on the type of data they organise and the specific requirements for
search efficiency, scalability and accuracy. Common forms include spatial indexes (e.g. nearest neighbour),
inverted indexes (map from content keywords to their location in the db), etc.

FAISS
======
.. code-block:: python

    $pip install faiss-cpu 
    import faiss

Faiss (Facebook AI Similarity Search) is a library for efficient similarity search and clustering of dense 
vectors. It contains algorithms that search in sets of vectors of any size, up to ones that possibly do 
not fit in RAM. It also contains supporting code for evaluation and parameter tuning. 

Faiss contains several methods for similarity search. It assumes that the instances are represented as 
vectors and are identified by an integer, and that the vectors can be compared with L2 (Euclidean) distances 
or dot products. Vectors that are similar to a query vector are those that have the lowest L2 distance or the
highest dot product with the query vector. It also supports cosine similarity, since this is a dot product 
on normalized vectors.

Langchain's vector store 
=========================
.. code-block:: python
    
    $pip install langchain
    from langchain.vectorstores.faiss import FAISS

This is a free, open-source vector store option that can be run entirely on your local machine.
The FAISS vector database makes use of Facebook AI Similarity Search (FAISS) library.

A common way to store and search over unstructed data is to embed it and store resulting
embedding vectors. Then embed the unstructured query (query vector) and retrieve the 
embedding vectors that are most similar to the embedded query. A vector store takes care of
storing embedded data and performing vector search for you. 

This is different from Facebook's FAISS library as it doesn't take vectors as inputs - instead it takes
cleaned, chunked data and then turns those into embeddings and then creates an index and a vector db. Facebook's
FAISS library focuses on creating an index only.



