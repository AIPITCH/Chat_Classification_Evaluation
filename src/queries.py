"""
LLM query templates.
"""

TAG_EVALUATION_QUERY = """
# Instructions
You are a Threat Intelligence specialist.
This is an excerpt of channel messages. 
You will Classify the channel using labels.

**Give 10 labels**. 

The label MUST be short, with one word maximum in english.
Label what is the most frequent.

When possible, use the following syntax of labels, but don't hesitate to give more custom and accurate labels.

- Law_enforcement: Related to channels of police/gvt and LE actions against threat actors.
- Carding: Related to selling, fraud, or illegal activities involving credit cards.
- Hacking_claim: revendication of threat actors about website compromises or pride in breaching systems.
- CredsDumps: Related to credential leaks for download or share.
- Leaks: Pertaining to company leaks after hacks, such as SQL database dumps.
- DDoS: Discussing DDoS activities, claims of attacks, or selling DDoS tools.
- Ponzi/Financial: Related to financial gain or investment schemes.
- Testimonial: Evidence of payments or proof that a service is legitimate. it does not includes greetings to groups.
- Hosting: if it talk about AWS, Azure, and Digital Ocean accounts, often at discounted prices.

You may add more label of your choice if you find them relevant.

IMPORTANT: Select labels to permit discrimination between channels containing valuable information or mostly hacking service advertisements.
It is also IMPORTANT to label if the channel deliver really leaks and credential dumping samples.
**IMPORTANT: Output only the labels as a csv, Don't forget the comma. Do not provide any additional text or commentary**
""".strip()



TAXONOMY_TAG_EVALUATION_QUERY = """
# Instructions
You are a Threat Intelligence specialist.
This is an excerpt of channel messages. 
Classify the channel with this custom taxonomy based on UUIDs labels.

IMPORTANT:
- Provide the output as a simple list of UUIDs.
- Select the most relevant tags.
- Output no more than 10 tags.
- Each UUID MUST be copied exactly from the allowed list below.
- Do not output UUIDs outside the allowed list.
- Do not add commentary, markdown, quotes, JSON, or extra text.
- The allowed list format is "uuid: tag: definition"; output only UUIDs.

Output Example: 
```
c0bef0db-be23-54f0-8e0f-2d53bd5ace87
0e992b11-d9ff-5207-b3be-255b8854d198
b1f66aec-a0fe-5a5f-8be3-e30965e82d82
```

Allowed tags:
{taxonomy_tags}
""".strip()

TAG_VALIDATION_QUERY = """
Following is messages collected on a telegram channel.

Validate if the classification is relevant. For each keyword give an explanation of what you have see in the text.

Take the following in consideration
No markdown.
No duplicate keys.
No explanations outside JSON.
Always issue ENGLISH text.

WARNING: The output should be in RAW JSON that should follow this format
{
  "channel_summary": {
    "description": "The Telegram channel description..."
  },
  "keyword_classifications": {
    "label1": {
      "justification": "Explanation why this classification...",
      "match": true
    },
    "label2": {
      "justification": "Explanation why this classification...",
      "match": false
    }
  }
}

The keyword that you have to justify are:
""".strip()

TAXONOMY_TAG_VALIDATION_CONTEXT = """
Taxonomy definitions for the keywords, no UUIDs:
{taxonomy_definitions}
""".strip()
