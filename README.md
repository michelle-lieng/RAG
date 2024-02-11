# RAG
Implementing RAG with Langchain and OpenAI API. PDFs in data file are downloaded from the AMEX Ultimate Card policies listed under "Important Information" on [this page here.](https://www.americanexpress.com/au/credit-cards/qantas-ultimate-card/).

First try on the RAG chatbot - successful:

```python
print(chatbot("Who is eligible for travel insurance?"))
```

Returned:

```
To be eligible for travel insurance, you must meet the following criteria based on the information provided in the document "AMERICAN EXPRESS CREDIT CARD INSURANCE" on page 4:

1. For International Return Trips, you must:
   - Be going on an International Return Trip and pay the full amount of your outbound ticket for a Scheduled Flight or Scheduled Cruise leaving Australia on your American Express Card Account, corresponding American Express Membership Rewards points/Qantas Points/Velocity Points (where applicable), and/or Travel Benefit.
   - Hold an eligible American Express Card Account that is current (not cancelled or suspended).
   - Be 79 years of age or younger when you make your Qualifying Travel Purchase.

2. For Card Purchase Cover (Section H) and Card Refund Cover (Section I):
   - Be a Card Member or an Additional Card Member, or their spouse or dependent child.
   - Be a Resident of Australia.
   - Purchase an Eligible Item and pay the entire cost using your American Express Card Account and/or corresponding Qantas Points/Velocity Points (where applicable).
   - Hold an eligible American Express Card Account that is current (not cancelled or suspended).

Please note that the eligibility criteria may vary depending on the specific insurance policy. It is recommended to read the full policy document for complete information. (AMERICAN EXPRESS CREDIT CARD INSURANCE, page 4)
```

Have now enabled conversation with the chatbot in conversation.py. Currently debugging error with unknown filename metadata.

```python
conversation()
```

Returned:

```
Ask anything: Who can I call if my card gets lost?


This is the chatbot response:
-----------------------------
You can call us immediately on 1300 132 639 (or if overseas by reverse charges on +61 2 9271 8666) to report a lost card. (filename: unknown, page: 13)


This is the chat history:
-------------------------
{
    "role": "user",
    "content": "Who can I call if my card gets lost?"
}
{
    "role": "assistant",
    "content": "You can call us immediately on 1300 132 639 (or if overseas by reverse charges on +61 2 9271 8666) to report a lost card. (filename: unknown, page: 13)"
}


This is the token count:
-------------------------
541 prompt tokens counted by the OpenAI API.
You have 3556 remaining tokens for the gpt-3.5-turbo model.
Ask anything: Are there any countries that I will not be covered for if I travel to?


This is the chatbot response:
-----------------------------
Yes, if an Australian State or Territory or the Australian Federal Government or an Australian government agency (such as DFAT) have issued a travel advisory warning, advising you to 'Do Not Travel' or that borders are closed, for the destination you planned to travel to, you will not be covered. Please refer to who.int, smartraveller.gov.au, dfat.gov.au, or other government sites for further information. This exclusion applies even if you have been granted a travel exemption by an Australian State or Territory, the Australian Federal Government, or an Australian government agency (such as DFAT) to travel. (filename: unknown, page: 8)


This is the chat history:
-------------------------
{
    "role": "user",
    "content": "Who can I call if my card gets lost?"
}
{
    "role": "assistant",
    "content": "You can call us immediately on 1300 132 639 (or if overseas by reverse charges on +61 2 9271 8666) to report a lost card. (filename: unknown, page: 13)"
}
{
    "role": "user",
    "content": "Are there any countries that I will not be covered for if I travel to?"
}
{
    "role": "assistant",
    "content": "Yes, if an Australian State or Territory or the Australian Federal Government or an Australian government agency (such as DFAT) have issued a travel advisory warning, advising you to 'Do Not Travel' or that borders are closed, for the destination you planned to travel to, you will not be covered. Please refer to who.int, smartraveller.gov.au, dfat.gov.au, or other government sites for further information. This exclusion applies even if you have been granted a travel exemption by an Australian State or Territory, the Australian Federal Government, or an Australian government agency (such as DFAT) to travel. (filename: unknown, page: 8)"
}


This is the token count:
-------------------------
510 prompt tokens counted by the OpenAI API.
You have 3587 remaining tokens for the gpt-3.5-turbo model.
Ask anything: How long can I be covered for while travelling?


This is the chatbot response:
-----------------------------
Cover automatically ends for all trips at 180 days. (filename: unknown, page: 8)


This is the chat history:
-------------------------
{
    "role": "user",
    "content": "Who can I call if my card gets lost?"
}
{
    "role": "assistant",
    "content": "You can call us immediately on 1300 132 639 (or if overseas by reverse charges on +61 2 9271 8666) to report a lost card. (filename: unknown, page: 13)"
}
{
    "role": "user",
    "content": "Are there any countries that I will not be covered for if I travel to?"
}
{
    "role": "assistant",
    "content": "Yes, if an Australian State or Territory or the Australian Federal Government or an Australian government agency (such as DFAT) have issued a travel advisory warning, advising you to 'Do Not Travel' or that borders are closed, for the destination you planned to travel to, you will not be covered. Please refer to who.int, smartraveller.gov.au, dfat.gov.au, or other government sites for further information. This exclusion applies even if you have been granted a travel exemption by an Australian State or Territory, the Australian Federal Government, or an Australian government agency (such as DFAT) to travel. (filename: unknown, page: 8)"
}
{
    "role": "user",
    "content": "How long can I be covered for while travelling?"
}
{
    "role": "assistant",
    "content": "Cover automatically ends for all trips at 180 days. (filename: unknown, page: 8)"
}


This is the token count:
-------------------------
662 prompt tokens counted by the OpenAI API.
You have 3435 remaining tokens for the gpt-3.5-turbo model.
Ask anything: end
```

Example questions to ask for AMEX document:
- How long can I be covered for while travelling?
- Are there any countries that I will not be covered for if I travel to?
- Who is eligible for travel insurance?
- What am I covered for?
- What ages can I be covered by travel insurance?
- How much is the annual fee for the American Express Ultimate Card?
- Who can I call if my card gets lost?

Note:

$ python --version

Python 3.11.0