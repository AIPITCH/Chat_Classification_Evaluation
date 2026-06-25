# deepseek-r1:32b
elapsed_second_request: 30.43s

```json
{
  "channel_summary": {
    "description": "A Telegram channel focusing on news, politics, and social commentary, occasionally including promotional content."
  },
  "keyword_classifications": {
    "advertisements": {
      "justification": "Multiple posts promote products such as Apple Music subscriptions, Shiba Inu crypto, and an online store for children's items.",
      "match": true
    },
    "anti-entity": {
      "justification": "Content discusses political issues and corruption but does not express opposition to specific entities.",
      "match": false
    },
    "conflict-related": {
      "justification": "Mentions a gas explosion incident, but no broader conflict is discussed.",
      "match": false
    },
    "cryptocurrencies": {
      "justification": "Only one message discusses Shiba Inu price movement.",
      "match": false
    },
    "culture": {
      "justification": "Posts discuss lifestyle trends and social issues, such as fashion and gaming.",
      "match": true
    },
    "disinformation": {
      "justification": "No clear signs of false information; content is news-oriented.",
      "match": false
    },
    "economy": {
      "justification": "Discussions include economic policies and vaccine mandates affecting businesses.",
      "match": true
    },
    "extremist": {
      "justification": "No content promoting extremism or violent ideologies.",
      "match": false
    },
    "files": {
      "justification": "No sharing of files or documents beyond links provided.",
      "match": false
    },
    "fraud-scams": {
      "justification": "Several messages discuss corruption and scams, such as the case with Vladimir Barcakin.",
      "match": true
    },
    "gaming": {
      "justification": "One message about a World of Warcraft update is present.",
      "match": true
    },
    "hacking": {
      "justification": "No mentions or discussions of hacking activities.",
      "match": false
    },
    "health": {
      "justification": "Multiple posts discuss COVID-19 cases and health measures.",
      "match": true
    },
    "incident-response": {
      "justification": "Gas explosion incident mentioned, but no detailed response info provided.",
      "match": false
    },
    "money-laundering-cash-in-out": {
      "justification": "Corruption cases implied but not explicitly about money laundering.",
      "match": false
    },
    "news": {
      "justification": "Many messages are news articles or current events coverage.",
      "match": true
    },
    "politics": {
      "justification": "Discussions include laws, regional conflicts, and government actions.",
      "match": true
    },
    "pro-entity": {
      "justification": "Content critiques rather than supports specific entities.",
      "match": false
    },
    "social": {
      "justification": "Includes social media interactions, memes, and community discussions.",
      "match": true
    },
    "threat-intelligence": {
      "justification": "No analysis of threats or actors is present.",
      "match": false
    }
  }
}
```

raw output:
```
```json
{
  "channel_summary": {
    "description": "A Telegram channel focusing on news, politics, and social commentary, occasionally including promotional content."
  },
  "keyword_classifications": {
    "advertisements": {
      "justification": "Multiple posts promote products such as Apple Music subscriptions, Shiba Inu crypto, and an online store for children's items.",
      "match": true
    },
    "anti-entity": {
      "justification": "Content discusses political issues and corruption but does not express opposition to specific entities.",
      "match": false
    },
    "conflict-related": {
      "justification": "Mentions a gas explosion incident, but no broader conflict is discussed.",
      "match": false
    },
    "cryptocurrencies": {
      "justification": "Only one message discusses Shiba Inu price movement.",
      "match": false
    },
    "culture": {
      "justification": "Posts discuss lifestyle trends and social issues, such as fashion and gaming.",
      "match": true
    },
    "disinformation": {
      "justification": "No clear signs of false information; content is news-oriented.",
      "match": false
    },
    "economy": {
      "justification": "Discussions include economic policies and vaccine mandates affecting businesses.",
      "match": true
    },
    "extremist": {
      "justification": "No content promoting extremism or violent ideologies.",
      "match": false
    },
    "files": {
      "justification": "No sharing of files or documents beyond links provided.",
      "match": false
    },
    "fraud-scams": {
      "justification": "Several messages discuss corruption and scams, such as the case with Vladimir Barcakin.",
      "match": true
    },
    "gaming": {
      "justification": "One message about a World of Warcraft update is present.",
      "match": true
    },
    "hacking": {
      "justification": "No mentions or discussions of hacking activities.",
      "match": false
    },
    "health": {
      "justification": "Multiple posts discuss COVID-19 cases and health measures.",
      "match": true
    },
    "incident-response": {
      "justification": "Gas explosion incident mentioned, but no detailed response info provided.",
      "match": false
    },
    "money-laundering-cash-in-out": {
      "justification": "Corruption cases implied but not explicitly about money laundering.",
      "match": false
    },
    "news": {
      "justification": "Many messages are news articles or current events coverage.",
      "match": true
    },
    "politics": {
      "justification": "Discussions include laws, regional conflicts, and government actions.",
      "match": true
    },
    "pro-entity": {
      "justification": "Content critiques rather than supports specific entities.",
      "match": false
    },
    "social": {
      "justification": "Includes social media interactions, memes, and community discussions.",
      "match": true
    },
    "threat-intelligence": {
      "justification": "No analysis of threats or actors is present.",
      "match": false
    }
  }
}
```
```

# devstral-2:latest
elapsed_second_request: 56.15s

```json
{
  "channel_summary": {
    "description": "The Telegram channel focuses on political, economic, and social issues in Russia, with recurring themes including corruption, regional governance conflicts, COVID-19 updates, and critiques of government actions."
  },
  "keyword_classifications": {
    "advertisements": {
      "justification": "There are promotional posts about discounts and products (e.g., Item 13).",
      "match": true
    },
    "anti-entity": {
      "justification": "Messages criticize government officials, regional policies, and corruption (e.g., Items 4, 6, 8, 17).",
      "match": true
    },
    "conflict-related": {
      "justification": "Discussions about regional political tensions and law enforcement conflicts (e.g., Item 1, 4, 5).",
      "match": true
    },
    "cryptocurrencies": {
      "justification": "Mention of cryptocurrency price updates (e.g., Item 26).",
      "match": true
    },
    "culture": {
      "justification": "Discussion about cultural figures and media trends (e.g., Item 10, 18, 24).",
      "match": true
    },
    "disinformation": {
      "justification": "No clear evidence of coordinated false information or deception.",
      "match": false
    },
    "economy": {
      "justification": "Discussions about economic policies, regional budgets, and corporate corruption (e.g., Items 8, 14, 29).",
      "match": true
    },
    "extremist": {
      "justification": "No promotion or glorification of extremist ideology or violence.",
      "match": false
    },
    "files": {
      "justification": "No evidence of file-sharing or document exchanges.",
      "match": false
    },
    "fraud-scams": {
      "justification": "Reports on fraudulent schemes and corruption (e.g., Items 4, 5, 28).",
      "match": true
    },
    "gaming": {
      "justification": "Mention of a game update (e.g., Item 22).",
      "match": true
    },
    "hacking": {
      "justification": "No evidence of unauthorized access or intrusion methods.",
      "match": false
    },
    "health": {
      "justification": "Updates on COVID-19 and public health measures (e.g., Items 2, 9, 15, 25).",
      "match": true
    },
    "incident-response": {
      "justification": "No evidence of cybersecurity incident discussions.",
      "match": false
    },
    "money-laundering-cash-in-out": {
      "justification": "Reports on financial misconduct and embezzlement (e.g., Items 8, 29).",
      "match": true
    },
    "news": {
      "justification": "Current events reporting on political, economic, and social issues (e.g., Items 1, 2, 9, 15).",
      "match": true
    },
    "politics": {
      "justification": "Extensive discussions about governance, regional conflicts, and political figures (e.g., Items 1, 6, 8, 20).",
      "match": true
    },
    "pro-entity": {
      "justification": "No clear support for any specific entity or ideology.",
      "match": false
    },
    "social": {
      "justification": "General social commentary and community updates (e.g., Items 3, 10).",
      "match": true
    },
    "threat-intelligence": {
      "justification": "No evidence of threat actor discussions or cybersecurity analysis.",
      "match": false
    }
  }
}
```

raw output:
```
```json
{
  "channel_summary": {
    "description": "The Telegram channel focuses on political, economic, and social issues in Russia, with recurring themes including corruption, regional governance conflicts, COVID-19 updates, and critiques of government actions."
  },
  "keyword_classifications": {
    "advertisements": {
      "justification": "There are promotional posts about discounts and products (e.g., Item 13).",
      "match": true
    },
    "anti-entity": {
      "justification": "Messages criticize government officials, regional policies, and corruption (e.g., Items 4, 6, 8, 17).",
      "match": true
    },
    "conflict-related": {
      "justification": "Discussions about regional political tensions and law enforcement conflicts (e.g., Item 1, 4, 5).",
      "match": true
    },
    "cryptocurrencies": {
      "justification": "Mention of cryptocurrency price updates (e.g., Item 26).",
      "match": true
    },
    "culture": {
      "justification": "Discussion about cultural figures and media trends (e.g., Item 10, 18, 24).",
      "match": true
    },
    "disinformation": {
      "justification": "No clear evidence of coordinated false information or deception.",
      "match": false
    },
    "economy": {
      "justification": "Discussions about economic policies, regional budgets, and corporate corruption (e.g., Items 8, 14, 29).",
      "match": true
    },
    "extremist": {
      "justification": "No promotion or glorification of extremist ideology or violence.",
      "match": false
    },
    "files": {
      "justification": "No evidence of file-sharing or document exchanges.",
      "match": false
    },
    "fraud-scams": {
      "justification": "Reports on fraudulent schemes and corruption (e.g., Items 4, 5, 28).",
      "match": true
    },
    "gaming": {
      "justification": "Mention of a game update (e.g., Item 22).",
      "match": true
    },
    "hacking": {
      "justification": "No evidence of unauthorized access or intrusion methods.",
      "match": false
    },
    "health": {
      "justification": "Updates on COVID-19 and public health measures (e.g., Items 2, 9, 15, 25).",
      "match": true
    },
    "incident-response": {
      "justification": "No evidence of cybersecurity incident discussions.",
      "match": false
    },
    "money-laundering-cash-in-out": {
      "justification": "Reports on financial misconduct and embezzlement (e.g., Items 8, 29).",
      "match": true
    },
    "news": {
      "justification": "Current events reporting on political, economic, and social issues (e.g., Items 1, 2, 9, 15).",
      "match": true
    },
    "politics": {
      "justification": "Extensive discussions about governance, regional conflicts, and political figures (e.g., Items 1, 6, 8, 20).",
      "match": true
    },
    "pro-entity": {
      "justification": "No clear support for any specific entity or ideology.",
      "match": false
    },
    "social": {
      "justification": "General social commentary and community updates (e.g., Items 3, 10).",
      "match": true
    },
    "threat-intelligence": {
      "justification": "No evidence of threat actor discussions or cybersecurity analysis.",
      "match": false
    }
  }
}
```
```

# gemma4:31b
elapsed_second_request: 56.41s

```json
{
  "channel_summary": {
    "description": "The channel serves as an aggregator of diverse content, including reports on government corruption in Russia, political analysis of power dynamics within the Russian State Duma and regional governments, current event news (such as COVID-19 measures and local accidents), social commentary, and various commercial advertisements."
  },
  "keyword_classifications": {
    "advertisements": {
      "justification": "The channel contains promotional posts for a children's store with promo codes (Item 13), an apartment rental listing (Item 16), and a promotion for Apple Music subscriptions (Item 27).",
      "match": true
    },
    "anti-entity": {
      "justification": "While the channel reports on corruption among specific officials, there is no evidence of systematic hostility or targeting of a specific country, government, or ideology as defined.",
      "match": false
    },
    "conflict-related": {
      "justification": "No mentions of current armed conflict, insurgency, or military escalation are present; Item 24 refers to historical events from 1945.",
      "match": false
    },
    "cryptocurrencies": {
      "justification": "Item 26 explicitly discusses the price and market capitalization of the meme-cryptocurrency Shiba Inu (SHIB).",
      "match": true
    },
    "culture": {
      "justification": "The content includes discussions on religious traditions (Item 3), commentary on LGBTQ+ trends in comic books and social norms (Item 10), and historical cultural figures (Item 24).",
      "match": true
    },
    "disinformation": {
      "justification": "There is no observable evidence of coordinated, false, or manipulated content intended to deceive the audience.",
      "match": false
    },
    "economy": {
      "justification": "Several items discuss corporate bankruptcies, large-scale debts (billions of rubles), and financial disputes involving companies like Ruspetro and SGEK (Items 28, 29, 30).",
      "match": true
    },
    "extremist": {
      "justification": "No content promoting or justifying political violence, terrorism, or extremist ideologies was found.",
      "match": false
    },
    "files": {
      "justification": "There are no posts sharing documents, archives, datasets, or file-sharing links.",
      "match": false
    },
    "fraud-scams": {
      "justification": "Items 4 and 5 describe a fraudster (Vladimir Bartsakin) who used forged documents to steal property; Item 28 mentions fraudulent deals involving fictitious loans.",
      "match": true
    },
    "gaming": {
      "justification": "Item 22 provides an update on the release date and new features for World of Warcraft: Shadowlands.",
      "match": true
    },
    "hacking": {
      "justification": "No mentions of unauthorized system access, intrusions, or technical exploitation are present.",
      "match": false
    },
    "health": {
      "justification": "Multiple items discuss the COVID-19 pandemic, including government restrictions (Items 9, 19, 25) and reports on the severity of the virus in Moscow (Item 15).",
      "match": true
    },
    "incident-response": {
      "justification": "No content related to cybersecurity incident triage or recovery is present.",
      "match": false
    },
    "money-laundering-cash-in-out": {
      "justification": "While corruption and luxury spending are mentioned, there is no specific evidence of the methods used to conceal or move illicit proceeds through financial systems.",
      "match": false
    },
    "news": {
      "justification": "The channel reports on various current events, including a gas explosion in Naberezhnye Chelny (Item 2), COVID-19 updates (Items 9, 15, 19, 25), and a theft attempt in Murmansk (Item 12).",
      "match": true
    },
    "politics": {
      "justification": "Items 1 and 20 analyze Russian legislative processes, regional power struggles, and internal dynamics within the State Duma and Presidential Administration.",
      "match": true
    },
    "pro-entity": {
      "justification": "No clear evidence of material expressing support for a specific country, government, or ideology was found.",
      "match": false
    },
    "social": {
      "justification": "The channel includes general social interactions such as morning greetings (Item 26), weather updates (Item 3), and commentary on societal trends (Item 10).",
      "match": true
    },
    "threat-intelligence": {
      "justification": "No collection or analysis of threat actor TTPs, indicators, or infrastructure is present.",
      "match": false
    }
  }
}
```

raw output:
```
{
  "channel_summary": {
    "description": "The channel serves as an aggregator of diverse content, including reports on government corruption in Russia, political analysis of power dynamics within the Russian State Duma and regional governments, current event news (such as COVID-19 measures and local accidents), social commentary, and various commercial advertisements."
  },
  "keyword_classifications": {
    "advertisements": {
      "justification": "The channel contains promotional posts for a children's store with promo codes (Item 13), an apartment rental listing (Item 16), and a promotion for Apple Music subscriptions (Item 27).",
      "match": true
    },
    "anti-entity": {
      "justification": "While the channel reports on corruption among specific officials, there is no evidence of systematic hostility or targeting of a specific country, government, or ideology as defined.",
      "match": false
    },
    "conflict-related": {
      "justification": "No mentions of current armed conflict, insurgency, or military escalation are present; Item 24 refers to historical events from 1945.",
      "match": false
    },
    "cryptocurrencies": {
      "justification": "Item 26 explicitly discusses the price and market capitalization of the meme-cryptocurrency Shiba Inu (SHIB).",
      "match": true
    },
    "culture": {
      "justification": "The content includes discussions on religious traditions (Item 3), commentary on LGBTQ+ trends in comic books and social norms (Item 10), and historical cultural figures (Item 24).",
      "match": true
    },
    "disinformation": {
      "justification": "There is no observable evidence of coordinated, false, or manipulated content intended to deceive the audience.",
      "match": false
    },
    "economy": {
      "justification": "Several items discuss corporate bankruptcies, large-scale debts (billions of rubles), and financial disputes involving companies like Ruspetro and SGEK (Items 28, 29, 30).",
      "match": true
    },
    "extremist": {
      "justification": "No content promoting or justifying political violence, terrorism, or extremist ideologies was found.",
      "match": false
    },
    "files": {
      "justification": "There are no posts sharing documents, archives, datasets, or file-sharing links.",
      "match": false
    },
    "fraud-scams": {
      "justification": "Items 4 and 5 describe a fraudster (Vladimir Bartsakin) who used forged documents to steal property; Item 28 mentions fraudulent deals involving fictitious loans.",
      "match": true
    },
    "gaming": {
      "justification": "Item 22 provides an update on the release date and new features for World of Warcraft: Shadowlands.",
      "match": true
    },
    "hacking": {
      "justification": "No mentions of unauthorized system access, intrusions, or technical exploitation are present.",
      "match": false
    },
    "health": {
      "justification": "Multiple items discuss the COVID-19 pandemic, including government restrictions (Items 9, 19, 25) and reports on the severity of the virus in Moscow (Item 15).",
      "match": true
    },
    "incident-response": {
      "justification": "No content related to cybersecurity incident triage or recovery is present.",
      "match": false
    },
    "money-laundering-cash-in-out": {
      "justification": "While corruption and luxury spending are mentioned, there is no specific evidence of the methods used to conceal or move illicit proceeds through financial systems.",
      "match": false
    },
    "news": {
      "justification": "The channel reports on various current events, including a gas explosion in Naberezhnye Chelny (Item 2), COVID-19 updates (Items 9, 15, 19, 25), and a theft attempt in Murmansk (Item 12).",
      "match": true
    },
    "politics": {
      "justification": "Items 1 and 20 analyze Russian legislative processes, regional power struggles, and internal dynamics within the State Duma and Presidential Administration.",
      "match": true
    },
    "pro-entity": {
      "justification": "No clear evidence of material expressing support for a specific country, government, or ideology was found.",
      "match": false
    },
    "social": {
      "justification": "The channel includes general social interactions such as morning greetings (Item 26), weather updates (Item 3), and commentary on societal trends (Item 10).",
      "match": true
    },
    "threat-intelligence": {
      "justification": "No collection or analysis of threat actor TTPs, indicators, or infrastructure is present.",
      "match": false
    }
  }
}
```

# gemma4:e4b
elapsed_second_request: 24.49s

```json
{
  "channel_summary": {
    "description": "The channel provides a mix of current events reporting and investigative journalism, focusing heavily on political scandals, corruption allegations against high-profile figures, and financial malfeasance within state corporations. It also covers public health updates (especially related to COVID-19), general news, and includes commercial advertisements."
  },
  "keyword_classifications": {
    "advertisements": {
      "justification": "Multiple posts contain explicit commercial promotions, discounts, and advertising for products or services (e.g., Item 3, Item 13, Item 27).",
      "match": true
    },
    "anti-entity": {
      "justification": "The content features material expressing opposition or challenge to central government authority and policies, such as regional dissatisfaction with federal legislation (Item 1).",
      "match": true
    },
    "conflict-related": {
      "justification": "No material about current armed conflict, civil unrest, or military escalation is present.",
      "match": false
    },
    "cryptocurrencies": {
      "justification": "One post explicitly discusses the price movement and market status of a specific meme cryptocurrency (Shiba Inu) and digital assets (Item 26).",
      "match": true
    },
    "culture": {
      "justification": "The channel includes discussions about popular culture, comics, entertainment trends, and historical cultural events (e.g., Item 10, Item 24).",
      "match": true
    },
    "disinformation": {
      "justification": "While many posts make strong accusations against public figures and institutions, the messages do not contain verifiable evidence or explicit statements confirming that the content is false, misleading, or coordinated disinformation.",
      "match": false
    },
    "economy": {
      "justification": "Several posts analyze complex financial matters, including corporate debt, bankruptcy proceedings, asset valuation, and wealth accumulation (e.g., Item 28, Item 30).",
      "match": true
    },
    "extremist": {
      "justification": "No material promotes or glorifies extremist ideologies, political violence, or anti-democratic movements.",
      "match": false
    },
    "files": {
      "justification": "No content involves the direct sharing of files, documents, or data sets.",
      "match": false
    },
    "fraud-scams": {
      "justification": "One post details a specific instance of fraud involving document forgery and theft from a widow (Item 4).",
      "match": true
    },
    "gaming": {
      "justification": "One post provides detailed information about an update release, features, and gameplay mechanics for a specific video game (World of Warcraft) (Item 22).",
      "match": true
    },
    "hacking": {
      "justification": "No material discusses unauthorized system access, intrusion techniques, or cyber exploitation.",
      "match": false
    },
    "health": {
      "justification": "Multiple posts provide updates and directives concerning public health issues, specifically related to COVID-19 outbreaks and necessary medical precautions (e.g., Item 2, Item 15).",
      "match": true
    },
    "incident-response": {
      "justification": "No material provides information regarding the technical steps for preparing for, containing, or recovering from a cybersecurity incident.",
      "match": false
    },
    "money-laundering-cash-in-out": {
      "justification": "Several posts describe methods used by corporate leadership to move or conceal funds through affiliated structures and fictitious loans (e.g., Item 28, Item 30).",
      "match": true
    },
    "news": {
      "justification": "The channel consistently provides current-event reporting and commentary on recent developments across political, legal, and social spheres.",
      "match": true
    },
    "politics": {
      "justification": "The content frequently analyzes political processes, governmental structures, legislative changes, and the relationship between regional and federal power (e.g., Item 1, Item 20).",
      "match": true
    },
    "pro-entity": {
      "justification": "The messages are primarily critical or investigative and do not contain material expressing explicit support for any specific country, government, or organization.",
      "match": false
    },
    "social": {
      "justification": "The channel includes posts related to personal updates, community discussions, and general social commentary on cultural or personal matters (e.g., Item 18).",
      "match": true
    },
    "threat-intelligence": {
      "justification": "The channel analyzes the professional backgrounds and alleged misconduct of powerful individuals, providing details that function as intelligence regarding corruption risks or compromised figures (e.g., Item 8).",
      "match": true
    }
  }
}
```

raw output:
```
{
  "channel_summary": {
    "description": "The channel provides a mix of current events reporting and investigative journalism, focusing heavily on political scandals, corruption allegations against high-profile figures, and financial malfeasance within state corporations. It also covers public health updates (especially related to COVID-19), general news, and includes commercial advertisements."
  },
  "keyword_classifications": {
    "advertisements": {
      "justification": "Multiple posts contain explicit commercial promotions, discounts, and advertising for products or services (e.g., Item 3, Item 13, Item 27).",
      "match": true
    },
    "anti-entity": {
      "justification": "The content features material expressing opposition or challenge to central government authority and policies, such as regional dissatisfaction with federal legislation (Item 1).",
      "match": true
    },
    "conflict-related": {
      "justification": "No material about current armed conflict, civil unrest, or military escalation is present.",
      "match": false
    },
    "cryptocurrencies": {
      "justification": "One post explicitly discusses the price movement and market status of a specific meme cryptocurrency (Shiba Inu) and digital assets (Item 26).",
      "match": true
    },
    "culture": {
      "justification": "The channel includes discussions about popular culture, comics, entertainment trends, and historical cultural events (e.g., Item 10, Item 24).",
      "match": true
    },
    "disinformation": {
      "justification": "While many posts make strong accusations against public figures and institutions, the messages do not contain verifiable evidence or explicit statements confirming that the content is false, misleading, or coordinated disinformation.",
      "match": false
    },
    "economy": {
      "justification": "Several posts analyze complex financial matters, including corporate debt, bankruptcy proceedings, asset valuation, and wealth accumulation (e.g., Item 28, Item 30).",
      "match": true
    },
    "extremist": {
      "justification": "No material promotes or glorifies extremist ideologies, political violence, or anti-democratic movements.",
      "match": false
    },
    "files": {
      "justification": "No content involves the direct sharing of files, documents, or data sets.",
      "match": false
    },
    "fraud-scams": {
      "justification": "One post details a specific instance of fraud involving document forgery and theft from a widow (Item 4).",
      "match": true
    },
    "gaming": {
      "justification": "One post provides detailed information about an update release, features, and gameplay mechanics for a specific video game (World of Warcraft) (Item 22).",
      "match": true
    },
    "hacking": {
      "justification": "No material discusses unauthorized system access, intrusion techniques, or cyber exploitation.",
      "match": false
    },
    "health": {
      "justification": "Multiple posts provide updates and directives concerning public health issues, specifically related to COVID-19 outbreaks and necessary medical precautions (e.g., Item 2, Item 15).",
      "match": true
    },
    "incident-response": {
      "justification": "No material provides information regarding the technical steps for preparing for, containing, or recovering from a cybersecurity incident.",
      "match": false
    },
    "money-laundering-cash-in-out": {
      "justification": "Several posts describe methods used by corporate leadership to move or conceal funds through affiliated structures and fictitious loans (e.g., Item 28, Item 30).",
      "match": true
    },
    "news": {
      "justification": "The channel consistently provides current-event reporting and commentary on recent developments across political, legal, and social spheres.",
      "match": true
    },
    "politics": {
      "justification": "The content frequently analyzes political processes, governmental structures, legislative changes, and the relationship between regional and federal power (e.g., Item 1, Item 20).",
      "match": true
    },
    "pro-entity": {
      "justification": "The messages are primarily critical or investigative and do not contain material expressing explicit support for any specific country, government, or organization.",
      "match": false
    },
    "social": {
      "justification": "The channel includes posts related to personal updates, community discussions, and general social commentary on cultural or personal matters (e.g., Item 18).",
      "match": true
    },
    "threat-intelligence": {
      "justification": "The channel analyzes the professional backgrounds and alleged misconduct of powerful individuals, providing details that function as intelligence regarding corruption risks or compromised figures (e.g., Item 8).",
      "match": true
    }
  }
}
```

# gpt-oss:120b
elapsed_second_request: 18.35s

```json
{
  "channel_summary": {
    "description": "The Telegram channel shares Russian‑language commentary on politics and corruption, news updates on COVID‑19, accidents and legal cases, occasional cultural references (religious holidays, comics, historical notes), promotional offers and discount codes, a gaming update, and brief mentions of cryptocurrency prices. The tone is often critical of government actions and officials."
  },
  "keyword_classifications": {
    "advertisements": {
      "justification": "Messages contain multiple commercial promotions such as product catalog discounts (Item 13), real‑estate rental ad (Item 16), a portal partnership call (Item 3) and free Apple Music subscription offer (Item 27).",
      "match": true
    },
    "anti-entity": {
      "justification": "Posts criticize the Russian federal centre, United Russia and Kremlin decisions, e.g., describing regional opposition as a \"direct challenge to the federal centre\" (Item 1) and questioning government measures (Items 19, 21).",
      "match": true
    },
    "conflict-related": {
      "justification": "No discussion of armed conflict, war, insurgency or military escalation is present; content focuses on politics, health and crime.",
      "match": false
    },
    "cryptocurrencies": {
      "justification": "Item 26 reports the price movement of meme‑coin Shiba Inu, a cryptocurrency market update.",
      "match": true
    },
    "culture": {
      "justification": "Posts reference Orthodox holiday traditions (Item 3), comic‑character commentary (Item 10) and WWII historical notes (Item 24).",
      "match": true
    },
    "disinformation": {
      "justification": "The messages do not contain demonstrably false or deliberately misleading information; they appear to be news, opinion or promotional content.",
      "match": false
    },
    "economy": {
      "justification": "Economic topics appear in corporate bankruptcy and lawsuit reports (Items 28‑30), discount promotions (Item 13), and cryptocurrency price mention (Item 26).",
      "match": true
    },
    "extremist": {
      "justification": "No content promotes extremist ideology, violence or terrorist recruitment.",
      "match": false
    },
    "files": {
      "justification": "The channel does not share documents, torrents, datasets or other file‑type resources.",
      "match": false
    },
    "fraud-scams": {
      "justification": "Promotional offers are presented as legitimate advertisements; there is no clear evidence of deceptive schemes to obtain money or data.",
      "match": false
    },
    "gaming": {
      "justification": "Item 22 announces a World of Warcraft update, which is explicitly about a video game.",
      "match": true
    },
    "hacking": {
      "justification": "No references to unauthorized access, intrusion techniques or hacking activities are found.",
      "match": false
    },
    "health": {
      "justification": "Several posts discuss COVID‑19 measures and case numbers (Items 9, 15, 19, 25), a gas explosion injury report (Item 2), and general pandemic updates (Item 20).",
      "match": true
    },
    "incident-response": {
      "justification": "The channel does not describe cybersecurity incident handling or response activities.",
      "match": false
    },
    "money-laundering-cash-in-out": {
      "justification": "There is no description of methods for concealing or moving illicit proceeds.",
      "match": false
    },
    "news": {
      "justification": "Most entries report recent events such as legal cases, COVID policies, explosions, and political developments, fitting a news‑type format.",
      "match": true
    },
    "politics": {
      "justification": "Extensive coverage of legislative proposals, regional opposition, corruption allegations and Kremlin actions (e.g., Items 1, 4, 8, 17, 20).",
      "match": true
    },
    "pro-entity": {
      "justification": "The channel does not express support for any specific country, government or organization; content is largely critical or neutral.",
      "match": false
    },
    "social": {
      "justification": "Posts include casual greetings and community‑style messages such as “Всем прекрасного доброго утра” (Item 26) and meme commentary on comics (Item 10).",
      "match": true
    },
    "threat-intelligence": {
      "justification": "No collection or analysis of cyber threat actors, tactics, techniques or indicators is present.",
      "match": false
    }
  }
}
```

raw output:
```
{
  "channel_summary": {
    "description": "The Telegram channel shares Russian‑language commentary on politics and corruption, news updates on COVID‑19, accidents and legal cases, occasional cultural references (religious holidays, comics, historical notes), promotional offers and discount codes, a gaming update, and brief mentions of cryptocurrency prices. The tone is often critical of government actions and officials."
  },
  "keyword_classifications": {
    "advertisements": {
      "justification": "Messages contain multiple commercial promotions such as product catalog discounts (Item 13), real‑estate rental ad (Item 16), a portal partnership call (Item 3) and free Apple Music subscription offer (Item 27).",
      "match": true
    },
    "anti-entity": {
      "justification": "Posts criticize the Russian federal centre, United Russia and Kremlin decisions, e.g., describing regional opposition as a \"direct challenge to the federal centre\" (Item 1) and questioning government measures (Items 19, 21).",
      "match": true
    },
    "conflict-related": {
      "justification": "No discussion of armed conflict, war, insurgency or military escalation is present; content focuses on politics, health and crime.",
      "match": false
    },
    "cryptocurrencies": {
      "justification": "Item 26 reports the price movement of meme‑coin Shiba Inu, a cryptocurrency market update.",
      "match": true
    },
    "culture": {
      "justification": "Posts reference Orthodox holiday traditions (Item 3), comic‑character commentary (Item 10) and WWII historical notes (Item 24).",
      "match": true
    },
    "disinformation": {
      "justification": "The messages do not contain demonstrably false or deliberately misleading information; they appear to be news, opinion or promotional content.",
      "match": false
    },
    "economy": {
      "justification": "Economic topics appear in corporate bankruptcy and lawsuit reports (Items 28‑30), discount promotions (Item 13), and cryptocurrency price mention (Item 26).",
      "match": true
    },
    "extremist": {
      "justification": "No content promotes extremist ideology, violence or terrorist recruitment.",
      "match": false
    },
    "files": {
      "justification": "The channel does not share documents, torrents, datasets or other file‑type resources.",
      "match": false
    },
    "fraud-scams": {
      "justification": "Promotional offers are presented as legitimate advertisements; there is no clear evidence of deceptive schemes to obtain money or data.",
      "match": false
    },
    "gaming": {
      "justification": "Item 22 announces a World of Warcraft update, which is explicitly about a video game.",
      "match": true
    },
    "hacking": {
      "justification": "No references to unauthorized access, intrusion techniques or hacking activities are found.",
      "match": false
    },
    "health": {
      "justification": "Several posts discuss COVID‑19 measures and case numbers (Items 9, 15, 19, 25), a gas explosion injury report (Item 2), and general pandemic updates (Item 20).",
      "match": true
    },
    "incident-response": {
      "justification": "The channel does not describe cybersecurity incident handling or response activities.",
      "match": false
    },
    "money-laundering-cash-in-out": {
      "justification": "There is no description of methods for concealing or moving illicit proceeds.",
      "match": false
    },
    "news": {
      "justification": "Most entries report recent events such as legal cases, COVID policies, explosions, and political developments, fitting a news‑type format.",
      "match": true
    },
    "politics": {
      "justification": "Extensive coverage of legislative proposals, regional opposition, corruption allegations and Kremlin actions (e.g., Items 1, 4, 8, 17, 20).",
      "match": true
    },
    "pro-entity": {
      "justification": "The channel does not express support for any specific country, government or organization; content is largely critical or neutral.",
      "match": false
    },
    "social": {
      "justification": "Posts include casual greetings and community‑style messages such as “Всем прекрасного доброго утра” (Item 26) and meme commentary on comics (Item 10).",
      "match": true
    },
    "threat-intelligence": {
      "justification": "No collection or analysis of cyber threat actors, tactics, techniques or indicators is present.",
      "match": false
    }
  }
}
```

# granite4.1:30b
elapsed_second_request: 28.56s

```json
{
  "channel_summary": {
    "description": "The Telegram channel 'Замотивируйся на лучшее' primarily shares news and commentary on Russian politics, governance, corruption scandals involving officials and state-owned enterprises, health updates related to COVID-19, and occasional promotional or commercial content. Recurring themes include regional autonomy disputes, high-profile corruption cases, pandemic response measures, and financial irregularities in energy and pharmaceutical sectors."
  },
  "keyword_classifications": {
    "advertisements": {
      "justification": "Only a few messages contain promotional elements (e.g., discount codes for Apple Music, gaming update), but they are not the channel's main focus.",
      "match": false
    },
    "anti-entity": {
      "justification": "Several posts criticize specific officials and entities (e.g., criticism of Putin's policies, corruption allegations against regional leaders), indicating opposition or hostility toward certain Russian governmental bodies.",
      "match": true
    },
    "conflict-related": {
      "justification": "No content discusses armed conflict, civil unrest, or military operations. The channel focuses on political and administrative issues rather than conflict zones.",
      "match": false
    },
    "cryptocurrencies": {
      "justification": "One message mentions the price surge of Shiba Inu (SHIB) cryptocurrency, but this is isolated and not a recurring theme.",
      "match": false
    },
    "culture": {
      "justification": "A few posts touch on cultural topics (e.g., comics character diversity, historical performance by Lydia Ruslanova), but they are minor compared to political content.",
      "match": false
    },
    "disinformation": {
      "justification": "While some messages contain sensational claims about corruption and health, there is no clear evidence of coordinated false narratives intended to deceive broadly.",
      "match": false
    },
    "economy": {
      "justification": "Multiple posts discuss economic issues: COVID-19's impact on business operations, energy sector debts, financial irregularities in state companies, and pandemic-related policy measures affecting the economy.",
      "match": true
    },
    "extremist": {
      "justification": "No content promotes extremist ideology, violence, or terrorism. The channel's focus is political critique rather than extremist advocacy.",
      "match": false
    },
    "files": {
      "justification": "The channel does not share documents, archives, images, or file-sharing links as a primary activity.",
      "match": false
    },
    "fraud-scams": {
      "justification": "Several messages detail alleged fraud and financial misconduct (e.g., corruption in energy companies, embezzlement cases, fraudulent salary payments), indicating a focus on fraud-related content.",
      "match": true
    },
    "gaming": {
      "justification": "Only one isolated message mentions an update for World of Warcraft, which is not a central theme.",
      "match": false
    },
    "hacking": {
      "justification": "No evidence of discussions about unauthorized access, system compromises, or cyber intrusion techniques.",
      "match": false
    },
    "health": {
      "justification": "Multiple posts cover COVID-19 developments, hospital admissions, vaccination policies, and public health measures, making health a significant recurring theme.",
      "match": true
    },
    "incident-response": {
      "justification": "While there are mentions of pandemic response actions (e.g., lockdowns, vaccination days), the channel does not detail cybersecurity incident handling or structured response frameworks.",
      "match": false
    },
    "money-laundering-cash-in-out": {
      "justification": "Some messages imply financial misappropriation and potential money laundering (e.g., embezzlement in energy firms, suspicious salary payments), but explicit methods of cash-in/out are not detailed.",
      "match": false
    },
    "news": {
      "justification": "The channel frequently posts news updates on political events, health crises, corruption scandals, and economic policies, aligning with a news dissemination purpose.",
      "match": true
    },
    "politics": {
      "justification": "A substantial portion of the content analyzes Russian political dynamics, governance disputes, regional autonomy issues, and policy decisions by officials, clearly indicating a political focus.",
      "match": true
    },
    "pro-entity": {
      "justification": "Although some messages mention Russian entities (e.g., Putin's directives), they are predominantly critical rather than supportive, lacking clear pro-entity advocacy.",
      "match": false
    },
    "social": {
      "justification": "Limited social interaction content; most posts are informational or analytical rather than personal updates or community chat.",
      "match": false
    },
    "threat-intelligence": {
      "justification": "No structured sharing of threat actor profiles, TTPs, indicators, or infrastructure analysis typical of threat intelligence. The channel's focus is on political and economic reporting.",
      "match": false
    }
  }
}
```

raw output:
```
{
  "channel_summary": {
    "description": "The Telegram channel 'Замотивируйся на лучшее' primarily shares news and commentary on Russian politics, governance, corruption scandals involving officials and state-owned enterprises, health updates related to COVID-19, and occasional promotional or commercial content. Recurring themes include regional autonomy disputes, high-profile corruption cases, pandemic response measures, and financial irregularities in energy and pharmaceutical sectors."
  },
  "keyword_classifications": {
    "advertisements": {
      "justification": "Only a few messages contain promotional elements (e.g., discount codes for Apple Music, gaming update), but they are not the channel's main focus.",
      "match": false
    },
    "anti-entity": {
      "justification": "Several posts criticize specific officials and entities (e.g., criticism of Putin's policies, corruption allegations against regional leaders), indicating opposition or hostility toward certain Russian governmental bodies.",
      "match": true
    },
    "conflict-related": {
      "justification": "No content discusses armed conflict, civil unrest, or military operations. The channel focuses on political and administrative issues rather than conflict zones.",
      "match": false
    },
    "cryptocurrencies": {
      "justification": "One message mentions the price surge of Shiba Inu (SHIB) cryptocurrency, but this is isolated and not a recurring theme.",
      "match": false
    },
    "culture": {
      "justification": "A few posts touch on cultural topics (e.g., comics character diversity, historical performance by Lydia Ruslanova), but they are minor compared to political content.",
      "match": false
    },
    "disinformation": {
      "justification": "While some messages contain sensational claims about corruption and health, there is no clear evidence of coordinated false narratives intended to deceive broadly.",
      "match": false
    },
    "economy": {
      "justification": "Multiple posts discuss economic issues: COVID-19's impact on business operations, energy sector debts, financial irregularities in state companies, and pandemic-related policy measures affecting the economy.",
      "match": true
    },
    "extremist": {
      "justification": "No content promotes extremist ideology, violence, or terrorism. The channel's focus is political critique rather than extremist advocacy.",
      "match": false
    },
    "files": {
      "justification": "The channel does not share documents, archives, images, or file-sharing links as a primary activity.",
      "match": false
    },
    "fraud-scams": {
      "justification": "Several messages detail alleged fraud and financial misconduct (e.g., corruption in energy companies, embezzlement cases, fraudulent salary payments), indicating a focus on fraud-related content.",
      "match": true
    },
    "gaming": {
      "justification": "Only one isolated message mentions an update for World of Warcraft, which is not a central theme.",
      "match": false
    },
    "hacking": {
      "justification": "No evidence of discussions about unauthorized access, system compromises, or cyber intrusion techniques.",
      "match": false
    },
    "health": {
      "justification": "Multiple posts cover COVID-19 developments, hospital admissions, vaccination policies, and public health measures, making health a significant recurring theme.",
      "match": true
    },
    "incident-response": {
      "justification": "While there are mentions of pandemic response actions (e.g., lockdowns, vaccination days), the channel does not detail cybersecurity incident handling or structured response frameworks.",
      "match": false
    },
    "money-laundering-cash-in-out": {
      "justification": "Some messages imply financial misappropriation and potential money laundering (e.g., embezzlement in energy firms, suspicious salary payments), but explicit methods of cash-in/out are not detailed.",
      "match": false
    },
    "news": {
      "justification": "The channel frequently posts news updates on political events, health crises, corruption scandals, and economic policies, aligning with a news dissemination purpose.",
      "match": true
    },
    "politics": {
      "justification": "A substantial portion of the content analyzes Russian political dynamics, governance disputes, regional autonomy issues, and policy decisions by officials, clearly indicating a political focus.",
      "match": true
    },
    "pro-entity": {
      "justification": "Although some messages mention Russian entities (e.g., Putin's directives), they are predominantly critical rather than supportive, lacking clear pro-entity advocacy.",
      "match": false
    },
    "social": {
      "justification": "Limited social interaction content; most posts are informational or analytical rather than personal updates or community chat.",
      "match": false
    },
    "threat-intelligence": {
      "justification": "No structured sharing of threat actor profiles, TTPs, indicators, or infrastructure analysis typical of threat intelligence. The channel's focus is on political and economic reporting.",
      "match": false
    }
  }
}
```

# igorls/gemma4-e4b-classifier:q8_0
elapsed_second_request: 19.27s

```json
{
  "channel_summary": {
    "description": "The channel functions as a news aggregator and political commentator, focusing heavily on domestic Russian current events. Recurring themes include high-level corruption investigations involving government officials and large corporations, analysis of federal vs regional politics, health updates (especially regarding COVID-19), local crime reports, and commercial promotions."
  },
  "keyword_classifications": {
    "advertisements": {
      "justification": "The channel contains multiple promotional posts, including a partner portal advertisement (Item 3), real estate listings (Item 16), and specific discount/promo code offers for retail goods (Item 13, Item 27).",
      "match": true
    },
    "anti-entity": {
      "justification": "The messages discuss internal political dissent from regions against federal legislation (Item 1), but do not contain material expressing hostility toward a specific external country or major entity.",
      "match": false
    },
    "conflict-related": {
      "justification": "While Item 24 mentions historical military contributions during WWII, there is no current material related to armed conflict, civil unrest, or wartime events.",
      "match": false
    },
    "cryptocurrencies": {
      "justification": "Item 26 reports on the price update and market performance of the meme cryptocurrency Shiba Inu (SHIB).",
      "match": true
    },
    "culture": {
      "justification": "Item 10 provides commentary on cultural trends in comics and fandoms, discussing archetypes like Cheburashka and Leo Polydor.",
      "match": true
    },
    "disinformation": {
      "justification": "No content is present that clearly meets the definition of false, misleading, or coordinated content intended to deceive audiences.",
      "match": false
    },
    "economy": {
      "justification": "Multiple items detail corporate financial issues, including bankruptcy proceedings (Item 28, Item 29, Item 30), debt accumulation, and large-scale business operations and contracts (Item 14).",
      "match": true
    },
    "extremist": {
      "justification": "No content promotes or glorifies extremist ideology or political violence.",
      "match": false
    },
    "files": {
      "justification": "There is no observable evidence of posts related to file sharing, torrents, or generic data exchange.",
      "match": false
    },
    "fraud-scams": {
      "justification": "Item 4 details a case where a scammer used document forgery to illegally seize property from an widow.",
      "match": true
    },
    "gaming": {
      "justification": "Item 22 announces the release date and features of an update for World of Warcraft: Shadowlands.",
      "match": true
    },
    "hacking": {
      "justification": "No material discusses unauthorized access, intrusion methods, or illicit exploitation of systems.",
      "match": false
    },
    "health": {
      "justification": "Items 2, 15, 19, and 25 report on the increase in COVID-19 cases and government mandates regarding vaccination and restrictions.",
      "match": true
    },
    "incident-response": {
      "justification": "No content is provided related to preparation for or recovery from cybersecurity incidents.",
      "match": false
    },
    "money-laundering-cash-in-out": {
      "justification": "Items 28 and 30 describe complex financial schemes involving the diversion of consumer funds into affiliated commercial structures and the use of offshore entities (MAANWENDE B.V) in corporate bankruptcy cases.",
      "match": true
    },
    "news": {
      "justification": "The channel consistently reports on current events, including political developments, crime incidents, health alerts, and business news.",
      "match": true
    },
    "politics": {
      "justification": "Items 1, 20, and 21 discuss legislative processes, regional autonomy challenges, and the internal power dynamics within the government structure.",
      "match": true
    },
    "pro-entity": {
      "justification": "The content is generally critical or investigative of powerful entities and individuals; there is no clear material expressing support for a specific entity.",
      "match": false
    },
    "social": {
      "justification": "Item 10 contains general social commentary on cultural trends, fitting community conversation and lifestyle discussion.",
      "match": true
    },
    "threat-intelligence": {
      "justification": "Items 8, 29, and 30 provide detailed analysis of systemic financial crimes, corporate malfeasance, and high-level corruption investigations involving specific actors and methods (TTPs).",
      "match": true
    }
  }
}
```

raw output:
```
{
  "channel_summary": {
    "description": "The channel functions as a news aggregator and political commentator, focusing heavily on domestic Russian current events. Recurring themes include high-level corruption investigations involving government officials and large corporations, analysis of federal vs regional politics, health updates (especially regarding COVID-19), local crime reports, and commercial promotions."
  },
  "keyword_classifications": {
    "advertisements": {
      "justification": "The channel contains multiple promotional posts, including a partner portal advertisement (Item 3), real estate listings (Item 16), and specific discount/promo code offers for retail goods (Item 13, Item 27).",
      "match": true
    },
    "anti-entity": {
      "justification": "The messages discuss internal political dissent from regions against federal legislation (Item 1), but do not contain material expressing hostility toward a specific external country or major entity.",
      "match": false
    },
    "conflict-related": {
      "justification": "While Item 24 mentions historical military contributions during WWII, there is no current material related to armed conflict, civil unrest, or wartime events.",
      "match": false
    },
    "cryptocurrencies": {
      "justification": "Item 26 reports on the price update and market performance of the meme cryptocurrency Shiba Inu (SHIB).",
      "match": true
    },
    "culture": {
      "justification": "Item 10 provides commentary on cultural trends in comics and fandoms, discussing archetypes like Cheburashka and Leo Polydor.",
      "match": true
    },
    "disinformation": {
      "justification": "No content is present that clearly meets the definition of false, misleading, or coordinated content intended to deceive audiences.",
      "match": false
    },
    "economy": {
      "justification": "Multiple items detail corporate financial issues, including bankruptcy proceedings (Item 28, Item 29, Item 30), debt accumulation, and large-scale business operations and contracts (Item 14).",
      "match": true
    },
    "extremist": {
      "justification": "No content promotes or glorifies extremist ideology or political violence.",
      "match": false
    },
    "files": {
      "justification": "There is no observable evidence of posts related to file sharing, torrents, or generic data exchange.",
      "match": false
    },
    "fraud-scams": {
      "justification": "Item 4 details a case where a scammer used document forgery to illegally seize property from an widow.",
      "match": true
    },
    "gaming": {
      "justification": "Item 22 announces the release date and features of an update for World of Warcraft: Shadowlands.",
      "match": true
    },
    "hacking": {
      "justification": "No material discusses unauthorized access, intrusion methods, or illicit exploitation of systems.",
      "match": false
    },
    "health": {
      "justification": "Items 2, 15, 19, and 25 report on the increase in COVID-19 cases and government mandates regarding vaccination and restrictions.",
      "match": true
    },
    "incident-response": {
      "justification": "No content is provided related to preparation for or recovery from cybersecurity incidents.",
      "match": false
    },
    "money-laundering-cash-in-out": {
      "justification": "Items 28 and 30 describe complex financial schemes involving the diversion of consumer funds into affiliated commercial structures and the use of offshore entities (MAANWENDE B.V) in corporate bankruptcy cases.",
      "match": true
    },
    "news": {
      "justification": "The channel consistently reports on current events, including political developments, crime incidents, health alerts, and business news.",
      "match": true
    },
    "politics": {
      "justification": "Items 1, 20, and 21 discuss legislative processes, regional autonomy challenges, and the internal power dynamics within the government structure.",
      "match": true
    },
    "pro-entity": {
      "justification": "The content is generally critical or investigative of powerful entities and individuals; there is no clear material expressing support for a specific entity.",
      "match": false
    },
    "social": {
      "justification": "Item 10 contains general social commentary on cultural trends, fitting community conversation and lifestyle discussion.",
      "match": true
    },
    "threat-intelligence": {
      "justification": "Items 8, 29, and 30 provide detailed analysis of systemic financial crimes, corporate malfeasance, and high-level corruption investigations involving specific actors and methods (TTPs).",
      "match": true
    }
  }
}
```

# mistral-medium-3.5:latest
elapsed_second_request: 87.29s

```json
{
  "channel_summary": {
    "description": "The Telegram channel focuses on Russian political, economic, and social news, including corruption scandals, regional governance disputes, COVID-19 updates, cultural commentary, and investigative journalism. It also shares promotional content, advertisements, and occasional off-topic posts (e.g., gaming, weather). Themes include anti-corruption critiques, pro-government narratives, conflict-related discussions, and disinformation risks."
  },
  "keyword_classifications": {
    "advertisements": {
      "justification": "Messages 3, 13, 16, and 27 contain explicit promotional content: weather updates with partner portals (Item 3), discount codes for children's products (Item 13), real estate listings (Item 16), and free subscription promos (Item 27).",
      "match": true
    },
    "anti-entity": {
      "justification": "Messages 4, 5, 6, 8, 17, 20, 23, 28, and 29 criticize specific entities (e.g., law enforcement officers like Colonel Arkalov, Vitaly Borodin’s anti-corruption project, Rostech appointees, Rosseti Ural’s management). These posts express opposition to or expose wrongdoing by individuals/organizations.",
      "match": true
    },
    "conflict-related": {
      "justification": "Message 1 discusses regional political friction (Tatarstan vs. federal center) over a draft law, which touches on governance conflicts but lacks direct armed conflict or military escalation themes. No other messages explicitly cover armed conflict.",
      "match": false
    },
    "cryptocurrencies": {
      "justification": "Message 26 mentions the price surge of Shiba Inu (SHIB) cryptocurrency, explicitly referencing its market performance and ranking.",
      "match": true
    },
    "culture": {
      "justification": "Messages 10 and 24 discuss cultural topics: LGBTQ+ trends in comics (Item 10) and historical cultural figures like Lidya Ruslanova (Item 24).",
      "match": true
    },
    "disinformation": {
      "justification": "No explicit evidence of coordinated false or misleading content intended to deceive. While some posts (e.g., Item 1, 20) may contain biased narratives, they lack clear disinformation intent per the taxonomy.",
      "match": false
    },
    "economy": {
      "justification": "Messages 8, 14, 17, 23, 28, and 29 discuss economic themes: corporate corruption (Rostech, Ruspetro), financial mismanagement, embezzlement, and asset disputes. These directly relate to economic conditions and business practices.",
      "match": true
    },
    "extremist": {
      "justification": "No messages promote, justify, or glorify extremist ideology, political violence, or terrorism. Criticism of entities (e.g., Item 4) does not meet the threshold for extremism.",
      "match": false
    },
    "files": {
      "justification": "No evidence of file-sharing, archives, datasets, or torrents in the messages.",
      "match": false
    },
    "fraud-scams": {
      "justification": "Messages 4, 5, 8, 17, 28, and 29 describe fraudulent schemes: corruption (Arkalov/Bartzakin case), embezzlement (Rostech, Ruspetro), fake loans, and shell company operations. These align with deceptive practices for financial gain.",
      "match": true
    },
    "gaming": {
      "justification": "Message 22 explicitly discusses a World of Warcraft: Shadowlands update (9.1.5), including new features and release date.",
      "match": true
    },
    "hacking": {
      "justification": "No messages reference unauthorized access, intrusion methods, or system compromises.",
      "match": false
    },
    "health": {
      "justification": "Messages 2, 9, 15, 19, and 25 cover COVID-19 updates: injuries from explosions (Item 2), pandemic restrictions (Items 9, 19, 25), and rising severe cases (Item 15).",
      "match": true
    },
    "incident-response": {
      "justification": "No messages discuss cybersecurity incident preparation, triage, containment, or recovery. Health-related responses (e.g., COVID-19) do not fit this taxonomy.",
      "match": false
    },
    "money-laundering-cash-in-out": {
      "justification": "Messages 8, 28, and 29 describe financial schemes involving shell companies, fictitious loans, and offshore structures (e.g., Rostech’s Semen Yakubov, Ruspetro’s transactions), which are indicative of money laundering or cash-out operations.",
      "match": true
    },
    "news": {
      "justification": "The channel predominantly shares current-events reporting: political developments (Items 1, 20), corruption exposés (Items 4–8, 17, 23, 28–29), health updates (Items 2, 9, 15, 19, 25), and economic news (Items 14, 26).",
      "match": true
    },
    "politics": {
      "justification": "Messages 1, 20, 21, and 24 cover political themes: regional governance disputes (Item 1), parliamentary power shifts (Item 20), criticism of Western democracy vs. Russian narratives (Item 21), and historical political figures (Item 24).",
      "match": true
    },
    "pro-entity": {
      "justification": "Messages 24 and 25 express support for specific entities: Lidya Ruslanova’s contributions to WWII victory (Item 24) and Putin’s COVID-19 directives (Item 25). However, the channel’s tone is mixed, with more anti-entity content overall.",
      "match": true
    },
    "social": {
      "justification": "Messages 3 (weather + cultural traditions), 10 (cultural commentary on comics), and 18 (celebrity news about Svetlana Svetlichnaya) touch on social or community-oriented topics, but these are secondary to the channel’s primary focus.",
      "match": true
    },
    "threat-intelligence": {
      "justification": "No messages involve collection/analysis of threat actor data, TTPs, indicators, or cybersecurity intelligence. Fraud/scams (e.g., Items 4, 28) are criminal but not threat-intelligence-specific.",
      "match": false
    }
  }
}
```

raw output:
```
{
  "channel_summary": {
    "description": "The Telegram channel focuses on Russian political, economic, and social news, including corruption scandals, regional governance disputes, COVID-19 updates, cultural commentary, and investigative journalism. It also shares promotional content, advertisements, and occasional off-topic posts (e.g., gaming, weather). Themes include anti-corruption critiques, pro-government narratives, conflict-related discussions, and disinformation risks."
  },
  "keyword_classifications": {
    "advertisements": {
      "justification": "Messages 3, 13, 16, and 27 contain explicit promotional content: weather updates with partner portals (Item 3), discount codes for children's products (Item 13), real estate listings (Item 16), and free subscription promos (Item 27).",
      "match": true
    },
    "anti-entity": {
      "justification": "Messages 4, 5, 6, 8, 17, 20, 23, 28, and 29 criticize specific entities (e.g., law enforcement officers like Colonel Arkalov, Vitaly Borodin’s anti-corruption project, Rostech appointees, Rosseti Ural’s management). These posts express opposition to or expose wrongdoing by individuals/organizations.",
      "match": true
    },
    "conflict-related": {
      "justification": "Message 1 discusses regional political friction (Tatarstan vs. federal center) over a draft law, which touches on governance conflicts but lacks direct armed conflict or military escalation themes. No other messages explicitly cover armed conflict.",
      "match": false
    },
    "cryptocurrencies": {
      "justification": "Message 26 mentions the price surge of Shiba Inu (SHIB) cryptocurrency, explicitly referencing its market performance and ranking.",
      "match": true
    },
    "culture": {
      "justification": "Messages 10 and 24 discuss cultural topics: LGBTQ+ trends in comics (Item 10) and historical cultural figures like Lidya Ruslanova (Item 24).",
      "match": true
    },
    "disinformation": {
      "justification": "No explicit evidence of coordinated false or misleading content intended to deceive. While some posts (e.g., Item 1, 20) may contain biased narratives, they lack clear disinformation intent per the taxonomy.",
      "match": false
    },
    "economy": {
      "justification": "Messages 8, 14, 17, 23, 28, and 29 discuss economic themes: corporate corruption (Rostech, Ruspetro), financial mismanagement, embezzlement, and asset disputes. These directly relate to economic conditions and business practices.",
      "match": true
    },
    "extremist": {
      "justification": "No messages promote, justify, or glorify extremist ideology, political violence, or terrorism. Criticism of entities (e.g., Item 4) does not meet the threshold for extremism.",
      "match": false
    },
    "files": {
      "justification": "No evidence of file-sharing, archives, datasets, or torrents in the messages.",
      "match": false
    },
    "fraud-scams": {
      "justification": "Messages 4, 5, 8, 17, 28, and 29 describe fraudulent schemes: corruption (Arkalov/Bartzakin case), embezzlement (Rostech, Ruspetro), fake loans, and shell company operations. These align with deceptive practices for financial gain.",
      "match": true
    },
    "gaming": {
      "justification": "Message 22 explicitly discusses a World of Warcraft: Shadowlands update (9.1.5), including new features and release date.",
      "match": true
    },
    "hacking": {
      "justification": "No messages reference unauthorized access, intrusion methods, or system compromises.",
      "match": false
    },
    "health": {
      "justification": "Messages 2, 9, 15, 19, and 25 cover COVID-19 updates: injuries from explosions (Item 2), pandemic restrictions (Items 9, 19, 25), and rising severe cases (Item 15).",
      "match": true
    },
    "incident-response": {
      "justification": "No messages discuss cybersecurity incident preparation, triage, containment, or recovery. Health-related responses (e.g., COVID-19) do not fit this taxonomy.",
      "match": false
    },
    "money-laundering-cash-in-out": {
      "justification": "Messages 8, 28, and 29 describe financial schemes involving shell companies, fictitious loans, and offshore structures (e.g., Rostech’s Semen Yakubov, Ruspetro’s transactions), which are indicative of money laundering or cash-out operations.",
      "match": true
    },
    "news": {
      "justification": "The channel predominantly shares current-events reporting: political developments (Items 1, 20), corruption exposés (Items 4–8, 17, 23, 28–29), health updates (Items 2, 9, 15, 19, 25), and economic news (Items 14, 26).",
      "match": true
    },
    "politics": {
      "justification": "Messages 1, 20, 21, and 24 cover political themes: regional governance disputes (Item 1), parliamentary power shifts (Item 20), criticism of Western democracy vs. Russian narratives (Item 21), and historical political figures (Item 24).",
      "match": true
    },
    "pro-entity": {
      "justification": "Messages 24 and 25 express support for specific entities: Lidya Ruslanova’s contributions to WWII victory (Item 24) and Putin’s COVID-19 directives (Item 25). However, the channel’s tone is mixed, with more anti-entity content overall.",
      "match": true
    },
    "social": {
      "justification": "Messages 3 (weather + cultural traditions), 10 (cultural commentary on comics), and 18 (celebrity news about Svetlana Svetlichnaya) touch on social or community-oriented topics, but these are secondary to the channel’s primary focus.",
      "match": true
    },
    "threat-intelligence": {
      "justification": "No messages involve collection/analysis of threat actor data, TTPs, indicators, or cybersecurity intelligence. Fraud/scams (e.g., Items 4, 28) are criminal but not threat-intelligence-specific.",
      "match": false
    }
  }
}
```

# mistral-small3.2:24b-instruct-2506-fp16
elapsed_second_request: 22.38s

```json
{
  "channel_summary": {
    "description": "The Telegram channel focuses on political analysis, corruption investigations, and social commentary in Russia. It frequently discusses regional politics, government policies, economic issues, and high-profile scandals involving public officials and businesses."
  },
  "keyword_classifications": {
    "advertisements": {
      "justification": "Item 13 contains promotional content for an online store offering discounts on children's products.",
      "match": true
    },
    "anti-entity": {
      "justification": "Items 4, 6, 8, 17, and 20 contain criticism of government officials and entities, expressing opposition to their actions or policies.",
      "match": true
    },
    "conflict-related": {
      "justification": "No direct mention of armed conflict, civil unrest, or military escalation. The content is primarily focused on domestic politics and corruption.",
      "match": false
    },
    "cryptocurrencies": {
      "justification": "Item 26 mentions the price surge of Shiba Inu cryptocurrency, indicating market content related to cryptocurrencies.",
      "match": true
    },
    "culture": {
      "justification": "Items 3 and 10 discuss cultural topics such as traditional practices and media commentary on social norms.",
      "match": true
    },
    "disinformation": {
      "justification": "No evidence of false, misleading, or coordinated content intended to deceive audiences.",
      "match": false
    },
    "economy": {
      "justification": "Items 14 and 28 discuss economic activities related to pharmaceutical companies and energy sectors, including financial transactions and market analysis.",
      "match": true
    },
    "extremist": {
      "justification": "No content promoting or glorifying extremist ideology, political violence, or terrorism.",
      "match": false
    },
    "files": {
      "justification": "No mention of documents, archives, images, datasets, or file-sharing posts.",
      "match": false
    },
    "fraud-scams": {
      "justification": "Items 4, 6, 8, 17, and 28 discuss various fraudulent activities and corruption involving public officials and businesses.",
      "match": true
    },
    "gaming": {
      "justification": "Item 22 mentions an update for the game World of Warcraft: Shadowlands, indicating content related to gaming.",
      "match": true
    },
    "hacking": {
      "justification": "No mention of unauthorized access, intrusion methods, or illicit exploitation of technical capabilities.",
      "match": false
    },
    "health": {
      "justification": "Items 2, 9, 15, and 19 discuss health-related topics such as COVID-19 cases, non-working days, and medical treatments.",
      "match": true
    },
    "incident-response": {
      "justification": "No content related to preparation for, triage of, containment of, eradication of, or recovery from cybersecurity incidents.",
      "match": false
    },
    "money-laundering-cash-in-out": {
      "justification": "Items 8, 14, and 29 discuss financial transactions and deals that could be related to money laundering, but no direct evidence of such activities is provided.",
      "match": false
    },
    "news": {
      "justification": "The channel frequently posts news-related content about political developments, economic issues, and social events.",
      "match": true
    },
    "politics": {
      "justification": "Items 1, 20, and 21 discuss political topics such as government policies, regional politics, and political analysis.",
      "match": true
    },
    "pro-entity": {
      "justification": "No content expressing support for a specific country, government, movement, organization, armed group, leader, ideology, or other identifiable entity.",
      "match": false
    },
    "social": {
      "justification": "Items 3 and 10 discuss social norms and cultural practices, indicating general social networking and community conversation.",
      "match": true
    },
    "threat-intelligence": {
      "justification": "No content related to the collection, analysis, enrichment, and sharing of information about threat actors, campaigns, tactics, techniques, procedures, indicators, infrastructure, or targeting.",
      "match": false
    }
  }
}
```

raw output:
```
```json
{
  "channel_summary": {
    "description": "The Telegram channel focuses on political analysis, corruption investigations, and social commentary in Russia. It frequently discusses regional politics, government policies, economic issues, and high-profile scandals involving public officials and businesses."
  },
  "keyword_classifications": {
    "advertisements": {
      "justification": "Item 13 contains promotional content for an online store offering discounts on children's products.",
      "match": true
    },
    "anti-entity": {
      "justification": "Items 4, 6, 8, 17, and 20 contain criticism of government officials and entities, expressing opposition to their actions or policies.",
      "match": true
    },
    "conflict-related": {
      "justification": "No direct mention of armed conflict, civil unrest, or military escalation. The content is primarily focused on domestic politics and corruption.",
      "match": false
    },
    "cryptocurrencies": {
      "justification": "Item 26 mentions the price surge of Shiba Inu cryptocurrency, indicating market content related to cryptocurrencies.",
      "match": true
    },
    "culture": {
      "justification": "Items 3 and 10 discuss cultural topics such as traditional practices and media commentary on social norms.",
      "match": true
    },
    "disinformation": {
      "justification": "No evidence of false, misleading, or coordinated content intended to deceive audiences.",
      "match": false
    },
    "economy": {
      "justification": "Items 14 and 28 discuss economic activities related to pharmaceutical companies and energy sectors, including financial transactions and market analysis.",
      "match": true
    },
    "extremist": {
      "justification": "No content promoting or glorifying extremist ideology, political violence, or terrorism.",
      "match": false
    },
    "files": {
      "justification": "No mention of documents, archives, images, datasets, or file-sharing posts.",
      "match": false
    },
    "fraud-scams": {
      "justification": "Items 4, 6, 8, 17, and 28 discuss various fraudulent activities and corruption involving public officials and businesses.",
      "match": true
    },
    "gaming": {
      "justification": "Item 22 mentions an update for the game World of Warcraft: Shadowlands, indicating content related to gaming.",
      "match": true
    },
    "hacking": {
      "justification": "No mention of unauthorized access, intrusion methods, or illicit exploitation of technical capabilities.",
      "match": false
    },
    "health": {
      "justification": "Items 2, 9, 15, and 19 discuss health-related topics such as COVID-19 cases, non-working days, and medical treatments.",
      "match": true
    },
    "incident-response": {
      "justification": "No content related to preparation for, triage of, containment of, eradication of, or recovery from cybersecurity incidents.",
      "match": false
    },
    "money-laundering-cash-in-out": {
      "justification": "Items 8, 14, and 29 discuss financial transactions and deals that could be related to money laundering, but no direct evidence of such activities is provided.",
      "match": false
    },
    "news": {
      "justification": "The channel frequently posts news-related content about political developments, economic issues, and social events.",
      "match": true
    },
    "politics": {
      "justification": "Items 1, 20, and 21 discuss political topics such as government policies, regional politics, and political analysis.",
      "match": true
    },
    "pro-entity": {
      "justification": "No content expressing support for a specific country, government, movement, organization, armed group, leader, ideology, or other identifiable entity.",
      "match": false
    },
    "social": {
      "justification": "Items 3 and 10 discuss social norms and cultural practices, indicating general social networking and community conversation.",
      "match": true
    },
    "threat-intelligence": {
      "justification": "No content related to the collection, analysis, enrichment, and sharing of information about threat actors, campaigns, tactics, techniques, procedures, indicators, infrastructure, or targeting.",
      "match": false
    }
  }
}
```
```

# nemotron-3-super:latest
elapsed_second_request: 39.28s

```json
{
  "channel_summary": {
    "description": "The channel mixes motivational content with news on politics, health, regional governance, cultural traditions, promotional offers, gaming updates, and cryptocurrency market movements."
  },
  "keyword_classifications": {
    "advertisements": {
      "justification": "Item 13 lists discount promotions from Дочки & Сыночки and Item 27 shares Apple Music promo codes, both are promotional solicitations.",
      "match": true
    },
    "anti-entity": {
      "justification": "Item 1 describes regional opposition to federal law proposals, framing them as a challenge to the central authority, indicating hostility toward the federal government.",
      "match": true
    },
    "conflict-related": {
      "justification": "No messages describe armed conflict, insurgency, or violence; only political dissent is mentioned.",
      "match": false
    },
    "cryptocurrencies": {
      "justification": "Item 26 reports Shiba Inu price reaching a historical high, providing market information on a cryptocurrency.",
      "match": true
    },
    "culture": {
      "justification": "Item 3 details Orthodox holiday traditions and banya customs; Item 10 discusses rainbow‑colored comic characters, both cultural topics.",
      "match": true
    },
    "disinformation": {
      "justification": "No clear evidence that the channel spreads false or misleading content with intent to deceive; statements appear as opinions or news without verification of falsity.",
      "match": false
    },
    "economy": {
      "justification": "While crypto prices are mentioned, there is no macroeconomic analysis (inflation, trade, labor markets) that fits the economy definition.",
      "match": false
    },
    "extremist": {
      "justification": "No content promotes extremist ideology, political violence, or terrorism.",
      "match": false
    },
    "files": {
      "justification": "The channel shares text and links but does not distribute documents, archives, or file‑sharing posts as defined.",
      "match": false
    },
    "fraud-scams": {
      "justification": "Allegations of corruption are reported, but the channel itself does not promote deceptive schemes for financial gain.",
      "match": false
    },
    "gaming": {
      "justification": "Item 22 announces a World of Warcraft patch update, directly concerning gaming content.",
      "match": true
    },
    "hacking": {
      "justification": "No discussion of unauthorized intrusion, exploits, or hacking techniques is present.",
      "match": false
    },
    "health": {
      "justification": "Item 2 notes an explosion injury; Item 15 and Item 26 report rising severe COVID‑19 cases, covering public health topics.",
      "match": true
    },
    "incident-response": {
      "justification": "No material covers preparation, triage, containment, or recovery from cybersecurity incidents.",
      "match": false
    },
    "money-laundering-cash-in-out": {
      "justification": "There is no description of services for moving or concealing illicit proceeds.",
      "match": false
    },
    "news": {
      "justification": "Multiple items report recent events: explosion in Naberezhnye Chelny (Item 2), COVID‑19 updates (Items 15, 26), weather forecast (Item 3), and legislative developments (Item 1).",
      "match": true
    },
    "politics": {
      "justification": "Item 1 discusses federal law proposals and regional pushback; Item 20 describes parliamentary power shifts; Item 5 cites Putin’s COVID‑19 directives.",
      "match": true
    },
    "pro-entity": {
      "justification": "No explicit support for a specific government, movement, or entity is expressed; the tone is critical or neutral rather than endorsing.",
      "match": false
    },
    "social": {
      "justification": "Items 3 (weather, holiday customs), 10 (comic‑book recoloring meme), and 27 (promo codes) reflect casual community conversation and lifestyle sharing.",
      "match": true
    },
    "threat-intelligence": {
      "justification": "The channel does not collect, analyze, or share information about threat actors, tactics, or indicators.",
      "match": false
    }
  }
}
```

raw output:
```
{
  "channel_summary": {
    "description": "The channel mixes motivational content with news on politics, health, regional governance, cultural traditions, promotional offers, gaming updates, and cryptocurrency market movements."
  },
  "keyword_classifications": {
    "advertisements": {
      "justification": "Item 13 lists discount promotions from Дочки & Сыночки and Item 27 shares Apple Music promo codes, both are promotional solicitations.",
      "match": true
    },
    "anti-entity": {
      "justification": "Item 1 describes regional opposition to federal law proposals, framing them as a challenge to the central authority, indicating hostility toward the federal government.",
      "match": true
    },
    "conflict-related": {
      "justification": "No messages describe armed conflict, insurgency, or violence; only political dissent is mentioned.",
      "match": false
    },
    "cryptocurrencies": {
      "justification": "Item 26 reports Shiba Inu price reaching a historical high, providing market information on a cryptocurrency.",
      "match": true
    },
    "culture": {
      "justification": "Item 3 details Orthodox holiday traditions and banya customs; Item 10 discusses rainbow‑colored comic characters, both cultural topics.",
      "match": true
    },
    "disinformation": {
      "justification": "No clear evidence that the channel spreads false or misleading content with intent to deceive; statements appear as opinions or news without verification of falsity.",
      "match": false
    },
    "economy": {
      "justification": "While crypto prices are mentioned, there is no macroeconomic analysis (inflation, trade, labor markets) that fits the economy definition.",
      "match": false
    },
    "extremist": {
      "justification": "No content promotes extremist ideology, political violence, or terrorism.",
      "match": false
    },
    "files": {
      "justification": "The channel shares text and links but does not distribute documents, archives, or file‑sharing posts as defined.",
      "match": false
    },
    "fraud-scams": {
      "justification": "Allegations of corruption are reported, but the channel itself does not promote deceptive schemes for financial gain.",
      "match": false
    },
    "gaming": {
      "justification": "Item 22 announces a World of Warcraft patch update, directly concerning gaming content.",
      "match": true
    },
    "hacking": {
      "justification": "No discussion of unauthorized intrusion, exploits, or hacking techniques is present.",
      "match": false
    },
    "health": {
      "justification": "Item 2 notes an explosion injury; Item 15 and Item 26 report rising severe COVID‑19 cases, covering public health topics.",
      "match": true
    },
    "incident-response": {
      "justification": "No material covers preparation, triage, containment, or recovery from cybersecurity incidents.",
      "match": false
    },
    "money-laundering-cash-in-out": {
      "justification": "There is no description of services for moving or concealing illicit proceeds.",
      "match": false
    },
    "news": {
      "justification": "Multiple items report recent events: explosion in Naberezhnye Chelny (Item 2), COVID‑19 updates (Items 15, 26), weather forecast (Item 3), and legislative developments (Item 1).",
      "match": true
    },
    "politics": {
      "justification": "Item 1 discusses federal law proposals and regional pushback; Item 20 describes parliamentary power shifts; Item 5 cites Putin’s COVID‑19 directives.",
      "match": true
    },
    "pro-entity": {
      "justification": "No explicit support for a specific government, movement, or entity is expressed; the tone is critical or neutral rather than endorsing.",
      "match": false
    },
    "social": {
      "justification": "Items 3 (weather, holiday customs), 10 (comic‑book recoloring meme), and 27 (promo codes) reflect casual community conversation and lifestyle sharing.",
      "match": true
    },
    "threat-intelligence": {
      "justification": "The channel does not collect, analyze, or share information about threat actors, tactics, or indicators.",
      "match": false
    }
  }
}
```

# qwen3.5:122b
elapsed_second_request: 54.83s

```json
{
  "channel_summary": {
    "description": "A Russian-language Telegram channel aggregating diverse content including political commentary on Russian governance and corruption scandals, public health updates regarding COVID-19 measures, lifestyle news, gaming updates, and promotional offers such as discount codes and cryptocurrency market data."
  },
  "keyword_classifications": {
    "advertisements": {
      "justification": "Multiple posts contain explicit promotions and commercial solicitations. Item 3 promotes a partner portal with over two million products. Item 13 details specific discount codes (e.g., DR25) for an online toy store. Item 16 lists rental property contact information. Item 27 offers Apple Music promo codes.",
      "match": true
    },
    "anti-entity": {
      "justification": "Content expresses opposition to specific government structures and officials. Item 1 describes regions (Tatarstan, Tyumen) challenging federal center legislation ('ultimatum of Kazan'). Items 4-8 and 14 criticize high-ranking officials for corruption and lifestyle excesses, framing them as antagonistic to public interest.",
      "match": true
    },
    "conflict-related": {
      "justification": "While Item 1 mentions political friction ('fronda', 'ultimatum') between regions and the federal center, there is no evidence of armed conflict, civil unrest, or military escalation. The content remains within the realm of legislative and administrative disagreement.",
      "match": false
    },
    "cryptocurrencies": {
      "justification": "Item 26 explicitly discusses market content regarding cryptocurrencies, specifically noting that the mem-cryptocurrency Shiba Inu updated its historical maximum price and ranking by capitalization.",
      "match": true
    },
    "culture": {
      "justification": "Several posts discuss cultural identity and traditions. Item 3 details Orthodox church holidays, bathhouse customs, and weather folklore. Item 10 comments on cultural trends in comics regarding LGBTQ+ representation. Item 24 references historical cultural figures (Lidia Ruslanova).",
      "match": true
    },
    "disinformation": {
      "justification": "The channel reposts allegations and news snippets without clear evidence of coordinated deception or proven falsehoods intended to distort public understanding. Claims about corruption are presented as investigative reporting rather than confirmed disinformation.",
      "match": false
    },
    "economy": {
      "justification": "Content covers macroeconomic and corporate financial conditions. Items 28, 29, and 30 detail bankruptcy proceedings, debts (129 million rubles), asset stripping schemes in energy companies (Rosseti, Ruspetro), and labor contract disputes involving foreign nationals.",
      "match": true
    },
    "extremist": {
      "justification": "No content promotes political violence, terrorism, or extremist ideology. Political criticism is present but remains within the bounds of civic discourse and corruption exposure without calls for violent action.",
      "match": false
    },
    "files": {
      "justification": "There are no posts offering documents, archives, datasets, torrents, or file-sharing links. All external references point to other Telegram channels or websites.",
      "match": false
    },
    "fraud-scams": {
      "justification": "Multiple messages describe deceptive schemes intended to obtain money or assets. Item 4 details a fraudster ('Istrinsky Kidala-Reshala') who deprived a widow of property via document forgery. Items 28 and 29 describe corporate fraud involving fictitious loans and inflated salaries in bankrupt companies.",
      "match": true
    },
    "gaming": {
      "justification": "Item 22 explicitly announces an update (9.1.5) for the video game World of Warcraft: Shadowlands, detailing gameplay changes like covenant swapping and dungeon access.",
      "match": true
    },
    "hacking": {
      "justification": "No content discusses unauthorized access, intrusion methods, exploits, or system takeovers. Technical discussions are limited to software updates (e.g., game patches).",
      "match": false
    },
    "health": {
      "justification": "Significant coverage of public health issues. Items 9, 15, 19, and 25 report on COVID-19 restrictions, vaccination mandates, hospital capacity, and government orders regarding remote work for vulnerable groups.",
      "match": true
    },
    "incident-response": {
      "justification": "While Item 2 mentions emergency services (MChS) responding to a gas explosion, this refers to physical disaster response. There is no content related to cybersecurity incident preparation, triage, or recovery.",
      "match": false
    },
    "money-laundering-cash-in-out": {
      "justification": "Items 28 and 29 describe methods for concealing and moving illicit proceeds through financial systems. Specifically, funds were withdrawn via fictitious loans to affiliated commercial structures and inflated salary payments to foreign nationals during bankruptcy proceedings.",
      "match": true
    },
    "news": {
      "justification": "The channel functions primarily as a news aggregator. Items 1, 2, 9, 18, 19, 20, 21, and 25 provide current-events reporting on legislation, accidents, political appointments, and government orders.",
      "match": true
    },
    "politics": {
      "justification": "Heavy focus on political actors and governance. Item 1 discusses Duma legislation and regional power dynamics. Item 20 analyzes the State Duma committee reshuffle involving Volodin and AP (Administration of the President). Items 4-8, 14, 17, 23 discuss official corruption.",
      "match": true
    },
    "pro-entity": {
      "justification": "The content is predominantly critical of government officials and structures rather than expressing support for a specific country or organization. No propaganda material supporting the state entity was observed.",
      "match": false
    },
    "social": {
      "justification": "While Item 16 contains personal rental information, the channel operates as a broadcast feed rather than a social networking space for friend groups or community conversation. Interaction is limited to reposting external links.",
      "match": false
    },
    "threat-intelligence": {
      "justification": "There is no collection or analysis of threat actors, campaigns, tactics, techniques, procedures (TTPs), or indicators of compromise related to cybersecurity threats.",
      "match": false
    }
  }
}
```

raw output:
```
{
  "channel_summary": {
    "description": "A Russian-language Telegram channel aggregating diverse content including political commentary on Russian governance and corruption scandals, public health updates regarding COVID-19 measures, lifestyle news, gaming updates, and promotional offers such as discount codes and cryptocurrency market data."
  },
  "keyword_classifications": {
    "advertisements": {
      "justification": "Multiple posts contain explicit promotions and commercial solicitations. Item 3 promotes a partner portal with over two million products. Item 13 details specific discount codes (e.g., DR25) for an online toy store. Item 16 lists rental property contact information. Item 27 offers Apple Music promo codes.",
      "match": true
    },
    "anti-entity": {
      "justification": "Content expresses opposition to specific government structures and officials. Item 1 describes regions (Tatarstan, Tyumen) challenging federal center legislation ('ultimatum of Kazan'). Items 4-8 and 14 criticize high-ranking officials for corruption and lifestyle excesses, framing them as antagonistic to public interest.",
      "match": true
    },
    "conflict-related": {
      "justification": "While Item 1 mentions political friction ('fronda', 'ultimatum') between regions and the federal center, there is no evidence of armed conflict, civil unrest, or military escalation. The content remains within the realm of legislative and administrative disagreement.",
      "match": false
    },
    "cryptocurrencies": {
      "justification": "Item 26 explicitly discusses market content regarding cryptocurrencies, specifically noting that the mem-cryptocurrency Shiba Inu updated its historical maximum price and ranking by capitalization.",
      "match": true
    },
    "culture": {
      "justification": "Several posts discuss cultural identity and traditions. Item 3 details Orthodox church holidays, bathhouse customs, and weather folklore. Item 10 comments on cultural trends in comics regarding LGBTQ+ representation. Item 24 references historical cultural figures (Lidia Ruslanova).",
      "match": true
    },
    "disinformation": {
      "justification": "The channel reposts allegations and news snippets without clear evidence of coordinated deception or proven falsehoods intended to distort public understanding. Claims about corruption are presented as investigative reporting rather than confirmed disinformation.",
      "match": false
    },
    "economy": {
      "justification": "Content covers macroeconomic and corporate financial conditions. Items 28, 29, and 30 detail bankruptcy proceedings, debts (129 million rubles), asset stripping schemes in energy companies (Rosseti, Ruspetro), and labor contract disputes involving foreign nationals.",
      "match": true
    },
    "extremist": {
      "justification": "No content promotes political violence, terrorism, or extremist ideology. Political criticism is present but remains within the bounds of civic discourse and corruption exposure without calls for violent action.",
      "match": false
    },
    "files": {
      "justification": "There are no posts offering documents, archives, datasets, torrents, or file-sharing links. All external references point to other Telegram channels or websites.",
      "match": false
    },
    "fraud-scams": {
      "justification": "Multiple messages describe deceptive schemes intended to obtain money or assets. Item 4 details a fraudster ('Istrinsky Kidala-Reshala') who deprived a widow of property via document forgery. Items 28 and 29 describe corporate fraud involving fictitious loans and inflated salaries in bankrupt companies.",
      "match": true
    },
    "gaming": {
      "justification": "Item 22 explicitly announces an update (9.1.5) for the video game World of Warcraft: Shadowlands, detailing gameplay changes like covenant swapping and dungeon access.",
      "match": true
    },
    "hacking": {
      "justification": "No content discusses unauthorized access, intrusion methods, exploits, or system takeovers. Technical discussions are limited to software updates (e.g., game patches).",
      "match": false
    },
    "health": {
      "justification": "Significant coverage of public health issues. Items 9, 15, 19, and 25 report on COVID-19 restrictions, vaccination mandates, hospital capacity, and government orders regarding remote work for vulnerable groups.",
      "match": true
    },
    "incident-response": {
      "justification": "While Item 2 mentions emergency services (MChS) responding to a gas explosion, this refers to physical disaster response. There is no content related to cybersecurity incident preparation, triage, or recovery.",
      "match": false
    },
    "money-laundering-cash-in-out": {
      "justification": "Items 28 and 29 describe methods for concealing and moving illicit proceeds through financial systems. Specifically, funds were withdrawn via fictitious loans to affiliated commercial structures and inflated salary payments to foreign nationals during bankruptcy proceedings.",
      "match": true
    },
    "news": {
      "justification": "The channel functions primarily as a news aggregator. Items 1, 2, 9, 18, 19, 20, 21, and 25 provide current-events reporting on legislation, accidents, political appointments, and government orders.",
      "match": true
    },
    "politics": {
      "justification": "Heavy focus on political actors and governance. Item 1 discusses Duma legislation and regional power dynamics. Item 20 analyzes the State Duma committee reshuffle involving Volodin and AP (Administration of the President). Items 4-8, 14, 17, 23 discuss official corruption.",
      "match": true
    },
    "pro-entity": {
      "justification": "The content is predominantly critical of government officials and structures rather than expressing support for a specific country or organization. No propaganda material supporting the state entity was observed.",
      "match": false
    },
    "social": {
      "justification": "While Item 16 contains personal rental information, the channel operates as a broadcast feed rather than a social networking space for friend groups or community conversation. Interaction is limited to reposting external links.",
      "match": false
    },
    "threat-intelligence": {
      "justification": "There is no collection or analysis of threat actors, campaigns, tactics, techniques, procedures (TTPs), or indicators of compromise related to cybersecurity threats.",
      "match": false
    }
  }
}
```

# qwen3.6:35b
elapsed_second_request: 29.73s

```json
{
  "channel_summary": {
    "description": "A Russian-language Telegram channel that aggregates and shares news, political commentary, corporate corruption reports, health updates, entertainment, gaming announcements, cryptocurrency market data, and promotional offers, primarily focused on domestic Russian affairs and current events."
  },
  "keyword_classifications": {
    "advertisements": {
      "justification": "Messages 13, 16, and 27 explicitly promote commercial products and services, including discount codes for a children's store, real estate listings with pricing and contact numbers, and free subscription offers for Apple Music.",
      "match": true
    },
    "anti-entity": {
      "justification": "The channel critiques specific Russian officials and corporate executives for corruption but does not express hostility toward or opposition to a specific country, government, movement, or identifiable entity as defined.",
      "match": false
    },
    "conflict-related": {
      "justification": "Message 24 references a historical WWII event involving a Soviet singer, but no current armed conflict, civil unrest, military escalation, or wartime narratives are discussed.",
      "match": false
    },
    "cryptocurrencies": {
      "justification": "Message 26 explicitly reports on the Shiba Inu (SHIB) meme-cryptocurrency hitting a historical price maximum and discusses its market capitalization ranking among digital assets.",
      "match": true
    },
    "culture": {
      "justification": "Messages 10, 18, and 24 discuss cultural topics including LGBTQ+ representation in Western comics, the disappearance of a famous Russian actress, and the historical legacy of Soviet singer Lidiya Ruslanova.",
      "match": true
    },
    "disinformation": {
      "justification": "The channel aggregates news and commentary from various sources but contains no evidence of coordinated deception, manipulated media, or content explicitly designed to distort public understanding.",
      "match": false
    },
    "economy": {
      "justification": "Messages 14, 28, 29, and 30 detail corporate bankruptcies, state pharmaceutical contracts, real estate pricing, financial fraud schemes, and labor market policies related to vaccination leave.",
      "match": true
    },
    "extremist": {
      "justification": "No content promotes, justifies, recruits for, or glorifies extremist ideology, political violence, terrorism, or anti-democratic violence.",
      "match": false
    },
    "files": {
      "justification": "Messages contain text links to other channels and websites but do not share documents, archives, datasets, torrents, or file storage exchanges.",
      "match": false
    },
    "fraud-scams": {
      "justification": "Messages 4, 6, 8, 17, 28, and 29 describe alleged deceptive schemes involving officials and corporate executives, including fake loans, inflated salaries, embezzlement, and bankruptcy fraud to obtain financial gain.",
      "match": true
    },
    "gaming": {
      "justification": "Message 22 provides specific details about an upcoming update for the video game World of Warcraft: Shadowlands, including gameplay mechanics and release dates.",
      "match": true
    },
    "hacking": {
      "justification": "No messages discuss unauthorized access, intrusion methods, system compromises, or illicit exploitation of technical capabilities.",
      "match": false
    },
    "health": {
      "justification": "Messages 2, 9, 15, 19, and 25 report on COVID-19 infection waves, hospital patient data, government vaccination policies, remote work mandates for high-risk groups, and public health restrictions.",
      "match": true
    },
    "incident-response": {
      "justification": "The channel does not discuss cybersecurity incident preparation, triage, containment, eradication, recovery, or coordinated response activities.",
      "match": false
    },
    "money-laundering-cash-in-out": {
      "justification": "While messages describe corporate embezzlement and offshore structures, they do not explicitly detail services or methods for concealing proceeds, converting illicit funds, or cashing out through financial systems.",
      "match": false
    },
    "news": {
      "justification": "The channel consistently aggregates and reports on current events across politics, health, business, entertainment, and technology, functioning as a general news feed.",
      "match": true
    },
    "politics": {
      "justification": "Multiple messages focus on Russian legislative processes, regional-federal power struggles, Kremlin internal dynamics, Duma committee restructuring, and presidential decrees on governance.",
      "match": true
    },
    "pro-entity": {
      "justification": "The channel critiques specific officials and policies but does not express explicit support for a specific country, government, movement, organization, or identifiable entity.",
      "match": false
    },
    "social": {
      "justification": "The content is structured as news aggregation and commentary rather than general social networking, personal updates, friend group chats, or community conversation.",
      "match": false
    },
    "threat-intelligence": {
      "justification": "No messages contain collection, analysis, or sharing of information regarding threat actors, campaigns, TTPs, indicators, infrastructure, or targeting methodologies.",
      "match": false
    }
  }
}
```

raw output:
```
{
  "channel_summary": {
    "description": "A Russian-language Telegram channel that aggregates and shares news, political commentary, corporate corruption reports, health updates, entertainment, gaming announcements, cryptocurrency market data, and promotional offers, primarily focused on domestic Russian affairs and current events."
  },
  "keyword_classifications": {
    "advertisements": {
      "justification": "Messages 13, 16, and 27 explicitly promote commercial products and services, including discount codes for a children's store, real estate listings with pricing and contact numbers, and free subscription offers for Apple Music.",
      "match": true
    },
    "anti-entity": {
      "justification": "The channel critiques specific Russian officials and corporate executives for corruption but does not express hostility toward or opposition to a specific country, government, movement, or identifiable entity as defined.",
      "match": false
    },
    "conflict-related": {
      "justification": "Message 24 references a historical WWII event involving a Soviet singer, but no current armed conflict, civil unrest, military escalation, or wartime narratives are discussed.",
      "match": false
    },
    "cryptocurrencies": {
      "justification": "Message 26 explicitly reports on the Shiba Inu (SHIB) meme-cryptocurrency hitting a historical price maximum and discusses its market capitalization ranking among digital assets.",
      "match": true
    },
    "culture": {
      "justification": "Messages 10, 18, and 24 discuss cultural topics including LGBTQ+ representation in Western comics, the disappearance of a famous Russian actress, and the historical legacy of Soviet singer Lidiya Ruslanova.",
      "match": true
    },
    "disinformation": {
      "justification": "The channel aggregates news and commentary from various sources but contains no evidence of coordinated deception, manipulated media, or content explicitly designed to distort public understanding.",
      "match": false
    },
    "economy": {
      "justification": "Messages 14, 28, 29, and 30 detail corporate bankruptcies, state pharmaceutical contracts, real estate pricing, financial fraud schemes, and labor market policies related to vaccination leave.",
      "match": true
    },
    "extremist": {
      "justification": "No content promotes, justifies, recruits for, or glorifies extremist ideology, political violence, terrorism, or anti-democratic violence.",
      "match": false
    },
    "files": {
      "justification": "Messages contain text links to other channels and websites but do not share documents, archives, datasets, torrents, or file storage exchanges.",
      "match": false
    },
    "fraud-scams": {
      "justification": "Messages 4, 6, 8, 17, 28, and 29 describe alleged deceptive schemes involving officials and corporate executives, including fake loans, inflated salaries, embezzlement, and bankruptcy fraud to obtain financial gain.",
      "match": true
    },
    "gaming": {
      "justification": "Message 22 provides specific details about an upcoming update for the video game World of Warcraft: Shadowlands, including gameplay mechanics and release dates.",
      "match": true
    },
    "hacking": {
      "justification": "No messages discuss unauthorized access, intrusion methods, system compromises, or illicit exploitation of technical capabilities.",
      "match": false
    },
    "health": {
      "justification": "Messages 2, 9, 15, 19, and 25 report on COVID-19 infection waves, hospital patient data, government vaccination policies, remote work mandates for high-risk groups, and public health restrictions.",
      "match": true
    },
    "incident-response": {
      "justification": "The channel does not discuss cybersecurity incident preparation, triage, containment, eradication, recovery, or coordinated response activities.",
      "match": false
    },
    "money-laundering-cash-in-out": {
      "justification": "While messages describe corporate embezzlement and offshore structures, they do not explicitly detail services or methods for concealing proceeds, converting illicit funds, or cashing out through financial systems.",
      "match": false
    },
    "news": {
      "justification": "The channel consistently aggregates and reports on current events across politics, health, business, entertainment, and technology, functioning as a general news feed.",
      "match": true
    },
    "politics": {
      "justification": "Multiple messages focus on Russian legislative processes, regional-federal power struggles, Kremlin internal dynamics, Duma committee restructuring, and presidential decrees on governance.",
      "match": true
    },
    "pro-entity": {
      "justification": "The channel critiques specific officials and policies but does not express explicit support for a specific country, government, movement, organization, or identifiable entity.",
      "match": false
    },
    "social": {
      "justification": "The content is structured as news aggregation and commentary rather than general social networking, personal updates, friend group chats, or community conversation.",
      "match": false
    },
    "threat-intelligence": {
      "justification": "No messages contain collection, analysis, or sharing of information regarding threat actors, campaigns, TTPs, indicators, infrastructure, or targeting methodologies.",
      "match": false
    }
  }
}
```
