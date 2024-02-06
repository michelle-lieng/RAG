# RAG
Implementing RAG with Langchain and OpenAI API. PDF in data file is the AMEX Ultimate Card Travel Insurance terms and conditions. You can view pdf [here](https://www.americanexpress.com/content/dam/amex/au/pdfs/credit-cards/pds_ultimatecard.pdf).

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

Note:

$ python --version

Python 3.11.0