===========
Self Notes
===========

Original code inspiration: https://github.com/avrabyt/RAG-Chatbot

Next Steps (Debugging & Experimental)
=====================================

* Find a way to minimise tokens (use package I read about)
* Fix filename metadata > new problems: the page number is a count from beginning so doesn't always match pdf
* Upgrade system prompt so that the structure of response is better and it utilises previous chat history
* Play around with whisper to ask questions
* Improve RAG with keywords and cosine similarity
* Update the readme file
* Add a way to minimize token length of chat history as the conversation gets longer
* Check if information extracted from tables in the pdf is correct e.g. key_facts.pdf 
* Figure out how to set api to environment variable
* Understand BytesIO
* Add more AMEX cards to compare them - ultimate goal the chatbot can compare which credit card is best in australia

Completed Changes
=================
* Added chat history 7/2/24
* Added more pdf files into data folder and fixed code 8/2/24
* Add a token counter 12/2/24

Notes 
=====
12/2/24
Fixed the metadata to show at bottom of file but noticed that the page number is a count from beginning 
so doesn't always match pdf. Also need to look at how much content is being sent to the system prompt - I think
I can reduce this number. No longer just sending page content to the pdf extract but also the metadata.

Also moved the vectordb function out of the loop in conversation function to reduce calls to the API.
