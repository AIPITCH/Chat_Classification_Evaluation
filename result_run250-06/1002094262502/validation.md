# deepseek-r1:32b
elapsed_second_request: 21.34s

```json
{
  "channel_summary": {
    "description": "A Telegram channel focused on offering proxy services, credential dumps, and various paid digital services such as Netflix, Spotify, and PSN access."
  },
  "keyword_classifications": {
    "credential-dumps-data-leaks": {
      "justification": "Multiple messages mention documents containing email credentials, such as 'Hotmail 6v4_normalized.txt' and others.",
      "match": true
    },
    "credential-theft": {
      "justification": "The channel sells access to private data, including emails and accounts, indicating theft or unauthorized access.",
      "match": true
    },
    "services": {
      "justification": "Offers various services like Netflix accounts, Spotify hits, PSN access, and others for sale with specific pricing.",
      "match": true
    },
    "vpn-proxies-anonymisation": {
      "justification": "The channel offers rotational datacenter proxies via HTTP and SOCKS5 ports.",
      "match": true
    }
  }
}
```

raw output:
```
```json
{
  "channel_summary": {
    "description": "A Telegram channel focused on offering proxy services, credential dumps, and various paid digital services such as Netflix, Spotify, and PSN access."
  },
  "keyword_classifications": {
    "vpn-proxies-anonymisation": {
      "justification": "The channel offers rotational datacenter proxies via HTTP and SOCKS5 ports.",
      "match": true
    },
    "credential-dumps-data-leaks": {
      "justification": "Multiple messages mention documents containing email credentials, such as 'Hotmail 6v4_normalized.txt' and others.",
      "match": true
    },
    "credential-theft": {
      "justification": "The channel sells access to private data, including emails and accounts, indicating theft or unauthorized access.",
      "match": true
    },
    "services": {
      "justification": "Offers various services like Netflix accounts, Spotify hits, PSN access, and others for sale with specific pricing.",
      "match": true
    }
  }
}
```
```

# devstral-2:latest
elapsed_second_request: 74.66s

```json
{
  "channel_summary": {
    "description": "The Telegram channel 'CRACK HU' primarily focuses on sharing and selling stolen credentials, including email lists, payment card details, and premium account access for various streaming services. It also advertises cybercriminal services such as Netflix account configurations, SMTP access, and proxy services."
  },
  "keyword_classifications": {
    "adult-content": {
      "justification": "No evidence of adult-oriented material or discussions in the messages.",
      "match": false
    },
    "advertisements": {
      "justification": "The channel contains multiple promotional posts for selling credentials, accounts, and services, including Netflix configurations and SMTP access.",
      "match": true
    },
    "anti-entity": {
      "justification": "One message contains anti-Israel sentiment, but it is isolated and not a recurring theme.",
      "match": false
    },
    "botnets": {
      "justification": "No evidence of botnet-related discussions or services in the messages.",
      "match": false
    },
    "carding": {
      "justification": "Multiple messages contain payment card details and discussions about card validation, indicating carding activity.",
      "match": true
    },
    "cloud": {
      "justification": "Mentions of 'private cloud' and 'cloud' in the context of credential dumps, but not a primary focus.",
      "match": false
    },
    "credential-dumps-data-leaks": {
      "justification": "Numerous messages contain attachments and discussions about leaked credentials, including email lists and payment card details.",
      "match": true
    },
    "credential-theft": {
      "justification": "The channel is centered around the sale and distribution of stolen credentials, including emails and premium account access.",
      "match": true
    },
    "cybercriminal-services": {
      "justification": "The channel offers various cybercriminal services, such as Netflix account configurations, SMTP access, and proxy services.",
      "match": true
    },
    "disinformation": {
      "justification": "No evidence of coordinated disinformation campaigns or misleading content in the messages.",
      "match": false
    },
    "economy": {
      "justification": "No discussions about macroeconomic conditions, labor markets, or economic indicators.",
      "match": false
    },
    "extremist": {
      "justification": "No evidence of extremist ideology, political violence, or terrorism promotion in the messages.",
      "match": false
    },
    "files": {
      "justification": "Multiple messages contain attachments and discussions about sharing files, including credential dumps and configurations.",
      "match": true
    },
    "fraud-scams": {
      "justification": "The channel is involved in selling stolen credentials and premium account access, which are indicative of fraudulent activities.",
      "match": true
    },
    "gaming": {
      "justification": "No discussions about video games, esports, or gaming culture.",
      "match": false
    },
    "hacking": {
      "justification": "The channel discusses unauthorized access to accounts and the sale of stolen credentials, indicating hacking-related activities.",
      "match": true
    },
    "hardware": {
      "justification": "No discussions about physical computing devices, components, or hardware-related topics.",
      "match": false
    },
    "health": {
      "justification": "No discussions about public health, medicine, or healthcare systems.",
      "match": false
    },
    "hosting": {
      "justification": "No discussions about web hosting, server hosting, or infrastructure services.",
      "match": false
    },
    "music": {
      "justification": "No discussions about music files, albums, or music-related content.",
      "match": false
    },
    "phishing": {
      "justification": "No direct evidence of phishing attempts or discussions about phishing kits in the messages.",
      "match": false
    },
    "politics": {
      "justification": "No discussions about political parties, campaigns, elections, or governance.",
      "match": false
    },
    "products": {
      "justification": "The channel sells digital products such as premium account access and configurations, but not tangible goods.",
      "match": false
    },
    "services": {
      "justification": "The channel offers various services, including Netflix account configurations, SMTP access, and proxy services.",
      "match": true
    },
    "social": {
      "justification": "No evidence of general social networking, chat, or community conversations unrelated to cybercriminal activities.",
      "match": false
    },
    "software": {
      "justification": "No discussions about applications, installers, scripts, or software downloads.",
      "match": false
    },
    "spam-phishing-services": {
      "justification": "No evidence of bulk messaging, spam delivery, or managed phishing campaign services in the messages.",
      "match": false
    },
    "telecommunications": {
      "justification": "No discussions about mobile networks, fixed-line networks, or telecommunications infrastructure.",
      "match": false
    },
    "video-streaming": {
      "justification": "The channel discusses and sells access to premium streaming accounts, including Netflix and Disney+.",
      "match": true
    },
    "vpn-proxies-anonymisation": {
      "justification": "The channel mentions rotational datacenter proxies and proxy services, indicating discussions about anonymization tools.",
      "match": true
    },
    "vulnerabilities-exploits": {
      "justification": "No discussions about software vulnerabilities, exploit research, or proof-of-concept exploits.",
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
    "description": "The Telegram channel 'CRACK HU' primarily focuses on sharing and selling stolen credentials, including email lists, payment card details, and premium account access for various streaming services. It also advertises cybercriminal services such as Netflix account configurations, SMTP access, and proxy services."
  },
  "keyword_classifications": {
    "adult-content": {
      "justification": "No evidence of adult-oriented material or discussions in the messages.",
      "match": false
    },
    "advertisements": {
      "justification": "The channel contains multiple promotional posts for selling credentials, accounts, and services, including Netflix configurations and SMTP access.",
      "match": true
    },
    "anti-entity": {
      "justification": "One message contains anti-Israel sentiment, but it is isolated and not a recurring theme.",
      "match": false
    },
    "botnets": {
      "justification": "No evidence of botnet-related discussions or services in the messages.",
      "match": false
    },
    "carding": {
      "justification": "Multiple messages contain payment card details and discussions about card validation, indicating carding activity.",
      "match": true
    },
    "cloud": {
      "justification": "Mentions of 'private cloud' and 'cloud' in the context of credential dumps, but not a primary focus.",
      "match": false
    },
    "credential-dumps-data-leaks": {
      "justification": "Numerous messages contain attachments and discussions about leaked credentials, including email lists and payment card details.",
      "match": true
    },
    "credential-theft": {
      "justification": "The channel is centered around the sale and distribution of stolen credentials, including emails and premium account access.",
      "match": true
    },
    "cybercriminal-services": {
      "justification": "The channel offers various cybercriminal services, such as Netflix account configurations, SMTP access, and proxy services.",
      "match": true
    },
    "disinformation": {
      "justification": "No evidence of coordinated disinformation campaigns or misleading content in the messages.",
      "match": false
    },
    "economy": {
      "justification": "No discussions about macroeconomic conditions, labor markets, or economic indicators.",
      "match": false
    },
    "extremist": {
      "justification": "No evidence of extremist ideology, political violence, or terrorism promotion in the messages.",
      "match": false
    },
    "files": {
      "justification": "Multiple messages contain attachments and discussions about sharing files, including credential dumps and configurations.",
      "match": true
    },
    "fraud-scams": {
      "justification": "The channel is involved in selling stolen credentials and premium account access, which are indicative of fraudulent activities.",
      "match": true
    },
    "gaming": {
      "justification": "No discussions about video games, esports, or gaming culture.",
      "match": false
    },
    "hacking": {
      "justification": "The channel discusses unauthorized access to accounts and the sale of stolen credentials, indicating hacking-related activities.",
      "match": true
    },
    "hardware": {
      "justification": "No discussions about physical computing devices, components, or hardware-related topics.",
      "match": false
    },
    "health": {
      "justification": "No discussions about public health, medicine, or healthcare systems.",
      "match": false
    },
    "hosting": {
      "justification": "No discussions about web hosting, server hosting, or infrastructure services.",
      "match": false
    },
    "music": {
      "justification": "No discussions about music files, albums, or music-related content.",
      "match": false
    },
    "phishing": {
      "justification": "No direct evidence of phishing attempts or discussions about phishing kits in the messages.",
      "match": false
    },
    "politics": {
      "justification": "No discussions about political parties, campaigns, elections, or governance.",
      "match": false
    },
    "products": {
      "justification": "The channel sells digital products such as premium account access and configurations, but not tangible goods.",
      "match": false
    },
    "services": {
      "justification": "The channel offers various services, including Netflix account configurations, SMTP access, and proxy services.",
      "match": true
    },
    "social": {
      "justification": "No evidence of general social networking, chat, or community conversations unrelated to cybercriminal activities.",
      "match": false
    },
    "software": {
      "justification": "No discussions about applications, installers, scripts, or software downloads.",
      "match": false
    },
    "spam-phishing-services": {
      "justification": "No evidence of bulk messaging, spam delivery, or managed phishing campaign services in the messages.",
      "match": false
    },
    "telecommunications": {
      "justification": "No discussions about mobile networks, fixed-line networks, or telecommunications infrastructure.",
      "match": false
    },
    "video-streaming": {
      "justification": "The channel discusses and sells access to premium streaming accounts, including Netflix and Disney+.",
      "match": true
    },
    "vpn-proxies-anonymisation": {
      "justification": "The channel mentions rotational datacenter proxies and proxy services, indicating discussions about anonymization tools.",
      "match": true
    },
    "vulnerabilities-exploits": {
      "justification": "No discussions about software vulnerabilities, exploit research, or proof-of-concept exploits.",
      "match": false
    }
  }
}
```
```

# gemma4:12b
elapsed_second_request: 41.92s

```json
{
  "channel_summary": {
    "description": "The channel serves as a marketplace for cybercriminal activities, including the sale of stolen credentials (email/password lists), credit card dumps, premium accounts for streaming services (Netflix, Disney+, Shahid), and automated configuration files for tools like SilverBullet."
  },
  "keyword_classifications": {
    "adult-content": {
      "justification": "No evidence of sexually explicit or adult-oriented material was found in the messages.",
      "match": false
    },
    "advertisements": {
      "justification": "The channel contains numerous promotional posts for 'private data', premium accounts, and configuration files with specific pricing details.",
      "match": true
    },
    "anti-entity": {
      "justification": "Item 73 contains a hostile slur directed at the state of Israel.",
      "match": true
    },
    "botnets": {
      "justification": "While automated tools are mentioned, there is no specific evidence of botnet infrastructure or command-and-control operations.",
      "match": false
    },
    "carding": {
      "justification": "Item 57 explicitly mentions a '1M cc dump' and several items (32-34) list detailed credit card information including brand, type, and bank.",
      "match": true
    },
    "cloud": {
      "justification": "While Item 10 mentions a 'private cloud', it refers to the source of stolen data rather than the provision of cloud infrastructure services.",
      "match": false
    },
    "credential-dumps-data-leaks": {
      "justification": "Multiple messages (Items 10-20, 57, 60-71) contain large lists of stolen email/password combinations and credit card dumps.",
      "match": true
    },
    "credential-theft": {
      "justification": "The distribution of 'Good Emails' and 'cc dump' files indicates the theft and sharing of authentication credentials.",
      "match": true
    },
    "cybercriminal-services": {
      "justification": "The channel offers various criminal services including account selling, configuration file sales, and access to stolen data.",
      "match": true
    },
    "disinformation": {
      "justification": "No evidence of coordinated disinformation or misleading content intended to influence public opinion was found.",
      "match": false
    },
    "economy": {
      "justification": "There is no discussion regarding macroeconomic conditions, trade, or economic indicators.",
      "match": false
    },
    "extremist": {
      "justification": "While anti-entity sentiment exists, there is no evidence of promoting extremist ideology or terrorism.",
      "match": false
    },
    "files": {
      "justification": "Numerous text files (.txt) and configuration files (.svb) are shared throughout the channel.",
      "match": true
    },
    "fraud-scams": {
      "justification": "The sale of 'cracked' accounts and fraudulent premium access constitutes a scam/fraud operation.",
      "match": true
    },
    "gaming": {
      "justification": "Item 104 offers the sale of PSN (PlayStation Network) accounts.",
      "match": true
    },
    "hacking": {
      "justification": "The use of 'configs' for automated tools like SilverBullet and the distribution of stolen credentials indicate hacking activities.",
      "match": true
    },
    "hardware": {
      "justification": "No discussion regarding physical computing devices or hardware components was found.",
      "match": false
    },
    "health": {
      "justification": "No content related to public health, medicine, or healthcare was found.",
      "match": false
    },
    "hosting": {
      "justification": "While 'smtp' is mentioned, it is in the context of account sales rather than hosting infrastructure services.",
      "match": false
    },
    "music": {
      "justification": "Item 35 offers the sale of Spotify premium accounts.",
      "match": true
    },
    "phishing": {
      "justification": "While stolen data is present, there are no specific phishing kits or lures being actively deployed in these messages.",
      "match": false
    },
    "politics": {
      "justification": "Item 73 contains a political statement/insult directed at a nation's government.",
      "match": true
    },
    "products": {
      "justification": "The channel lists various digital products for sale, including account access and configuration files.",
      "match": true
    },
    "services": {
      "justification": "The channel offers services such as providing premium accounts and technical configurations to users.",
      "match": true
    },
    "social": {
      "justification": "No general social networking or community-focused content was found beyond the commercial transactions.",
      "match": false
    },
    "software": {
      "justification": "The distribution of .svb files represents configuration for automated software tools.",
      "match": true
    },
    "spam-phishing-services": {
      "justification": "The provision of 'configs' for automation tools like SilverBullet is used to facilitate spam and automated account operations.",
      "match": true
    },
    "telecommunications": {
      "justification": "No content related to mobile networks or telecommunication infrastructure was found.",
      "match": false
    },
    "video-streaming": {
      "justification": "Multiple items (47, 76, 88, 92, 99) offer accounts for streaming services like Netflix and Disney+.",
      "match": true
    },
    "vpn-proxies-anonymisation": {
      "justification": "Items 1 and 2 provide lists of Datacenter Proxies and SOCKS5 proxies.",
      "match": true
    },
    "vulnerabilities-exploits": {
      "justification": "No specific software vulnerabilities or proof-of-concept exploits were discussed.",
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
    "description": "The channel serves as a marketplace for cybercriminal activities, including the sale of stolen credentials (email/password lists), credit card dumps, premium accounts for streaming services (Netflix, Disney+, Shahid), and automated configuration files for tools like SilverBullet."
  },
  "keyword_classifications": {
    "adult-content": {
      "justification": "No evidence of sexually explicit or adult-oriented material was found in the messages.",
      "match": false
    },
    "advertisements": {
      "justification": "The channel contains numerous promotional posts for 'private data', premium accounts, and configuration files with specific pricing details.",
      "match": true
    },
    "anti-entity": {
      "justification": "Item 73 contains a hostile slur directed at the state of Israel.",
      "match": true
    },
    "botnets": {
      "justification": "While automated tools are mentioned, there is no specific evidence of botnet infrastructure or command-and-control operations.",
      "match": false
    },
    "carding": {
      "justification": "Item 57 explicitly mentions a '1M cc dump' and several items (32-34) list detailed credit card information including brand, type, and bank.",
      "match": true
    },
    "cloud": {
      "justification": "While Item 10 mentions a 'private cloud', it refers to the source of stolen data rather than the provision of cloud infrastructure services.",
      "match": false
    },
    "credential-dumps-data-leaks": {
      "justification": "Multiple messages (Items 10-20, 57, 60-71) contain large lists of stolen email/password combinations and credit card dumps.",
      "match": true
    },
    "credential-theft": {
      "justification": "The distribution of 'Good Emails' and 'cc dump' files indicates the theft and sharing of authentication credentials.",
      "match": true
    },
    "cybercriminal-services": {
      "justification": "The channel offers various criminal services including account selling, configuration file sales, and access to stolen data.",
      "match": true
    },
    "disinformation": {
      "justification": "No evidence of coordinated disinformation or misleading content intended to influence public opinion was found.",
      "match": false
    },
    "economy": {
      "justification": "There is no discussion regarding macroeconomic conditions, trade, or economic indicators.",
      "match": false
    },
    "extremist": {
      "justification": "While anti-entity sentiment exists, there is no evidence of promoting extremist ideology or terrorism.",
      "match": false
    },
    "files": {
      "justification": "Numerous text files (.txt) and configuration files (.svb) are shared throughout the channel.",
      "match": true
    },
    "fraud-scams": {
      "justification": "The sale of 'cracked' accounts and fraudulent premium access constitutes a scam/fraud operation.",
      "match": true
    },
    "gaming": {
      "justification": "Item 104 offers the sale of PSN (PlayStation Network) accounts.",
      "match": true
    },
    "hacking": {
      "justification": "The use of 'configs' for automated tools like SilverBullet and the distribution of stolen credentials indicate hacking activities.",
      "match": true
    },
    "hardware": {
      "justification": "No discussion regarding physical computing devices or hardware components was found.",
      "match": false
    },
    "health": {
      "justification": "No content related to public health, medicine, or healthcare was found.",
      "match": false
    },
    "hosting": {
      "justification": "While 'smtp' is mentioned, it is in the context of account sales rather than hosting infrastructure services.",
      "match": false
    },
    "music": {
      "justification": "Item 35 offers the sale of Spotify premium accounts.",
      "match": true
    },
    "phishing": {
      "justification": "While stolen data is present, there are no specific phishing kits or lures being actively deployed in these messages.",
      "match": false
    },
    "politics": {
      "justification": "Item 73 contains a political statement/insult directed at a nation's government.",
      "match": true
    },
    "products": {
      "justification": "The channel lists various digital products for sale, including account access and configuration files.",
      "match": true
    },
    "services": {
      "justification": "The channel offers services such as providing premium accounts and technical configurations to users.",
      "match": true
    },
    "social": {
      "justification": "No general social networking or community-focused content was found beyond the commercial transactions.",
      "match": false
    },
    "software": {
      "justification": "The distribution of .svb files represents configuration for automated software tools.",
      "match": true
    },
    "spam-phishing-services": {
      "justification": "The provision of 'configs' for automation tools like SilverBullet is used to facilitate spam and automated account operations.",
      "match": true
    },
    "telecommunications": {
      "justification": "No content related to mobile networks or telecommunication infrastructure was found.",
      "match": false
    },
    "video-streaming": {
      "justification": "Multiple items (47, 76, 88, 92, 99) offer accounts for streaming services like Netflix and Disney+.",
      "match": true
    },
    "vpn-proxies-anonymisation": {
      "justification": "Items 1 and 2 provide lists of Datacenter Proxies and SOCKS5 proxies.",
      "match": true
    },
    "vulnerabilities-exploits": {
      "justification": "No specific software vulnerabilities or proof-of-concept exploits were discussed.",
      "match": false
    }
  }
}
```
```

# gemma4:31b
elapsed_second_request: 77.98s

```json
{
  "channel_summary": {
    "description": "The channel 'CRACK HU' operates as a cybercriminal marketplace. It primarily distributes stolen credential dumps (combos), sells access to private data groups, trades cracked accounts for streaming services (Netflix, Disney+, Spotify) and gaming (PSN), shares SilverBullet (.svb) configurations for account cracking, and sells infrastructure tools such as rotating proxies and SMTP inboxes."
  },
  "keyword_classifications": {
    "adult-content": {
      "justification": "No sexually explicit or adult-oriented material was found in the messages.",
      "match": false
    },
    "advertisements": {
      "justification": "The channel contains numerous promotional posts selling accounts, private group access, and technical services with pricing details (e.g., Items 17, 26, 47).",
      "match": true
    },
    "anti-entity": {
      "justification": "Item 73 contains hostile language and insults directed at Israel.",
      "match": true
    },
    "botnets": {
      "justification": "While 'bots' are mentioned in the context of SilverBullet configurations (Items 84, 91), there is no evidence of botnet C2 operations or compromised device networks.",
      "match": false
    },
    "carding": {
      "justification": "The channel shares specific credit card data including card numbers, expiry dates, and CVVs (Items 32-34) and distributes a '1M cc dump' file (Item 57).",
      "match": true
    },
    "cloud": {
      "justification": "Mention of 'private cloud' in Item 10 is vague and refers to the source of a credential combo rather than cloud computing services or architecture.",
      "match": false
    },
    "credential-dumps-data-leaks": {
      "justification": "The channel extensively shares text files containing stolen email and password combinations (Items 2-9, 12-16, 18-30) and lists of accounts with subscription details (Items 37, 40, 41, 59-71).",
      "match": true
    },
    "credential-theft": {
      "justification": "The sale of 'full mail access' (Item 17) and the distribution of stolen account logs indicate the result of credential theft.",
      "match": true
    },
    "cybercriminal-services": {
      "justification": "The author offers criminal services including selling access to private data groups (Items 17, 26), SMTP inboxes for spamming (Items 52, 53), and RDPS (Item 95).",
      "match": true
    },
    "disinformation": {
      "justification": "No evidence of coordinated false narratives or deceptive content intended to influence public opinion.",
      "match": false
    },
    "economy": {
      "justification": "No discussion of macroeconomic indicators, labor markets, or trade trends.",
      "match": false
    },
    "extremist": {
      "justification": "While Item 73 is hostile, it consists of insults rather than the promotion of extremist ideology, terrorism, or political violence as defined.",
      "match": false
    },
    "files": {
      "justification": "The channel frequently shares attached files including .txt credential lists and .svb configuration files (Items 2-9, 84, 91).",
      "match": true
    },
    "fraud-scams": {
      "justification": "The sale of 'cracked' or stolen accounts for services like Netflix and Spotify (Items 35, 47, 88) constitutes fraudulent activity.",
      "match": true
    },
    "gaming": {
      "justification": "Item 104 explicitly offers the sale of PSN (PlayStation Network) accounts.",
      "match": true
    },
    "hacking": {
      "justification": "The channel distributes SilverBullet (.svb) configurations for automated account cracking (Items 84, 91, 96, 102) and discusses tools for cracking Amazon SES (Item 58).",
      "match": true
    },
    "hardware": {
      "justification": "No mention of physical computing devices or hardware components.",
      "match": false
    },
    "health": {
      "justification": "No health-related content or medical information present.",
      "match": false
    },
    "hosting": {
      "justification": "The channel mentions the availability of RDPS (Remote Desktop Protocol Servers) in Items 95 and 103, which relates to server infrastructure hosting.",
      "match": true
    },
    "music": {
      "justification": "Item 35 involves the sale of Spotify premium accounts.",
      "match": true
    },
    "phishing": {
      "justification": "While tools for phishing (SMTP) are sold, there is no direct evidence of active phishing lures or deceptive websites in the provided text.",
      "match": false
    },
    "politics": {
      "justification": "Item 73 contains political hostility directed at a specific state (Israel).",
      "match": true
    },
    "products": {
      "justification": "The channel lists various digital products for sale, including streaming accounts and gaming accounts (Items 35, 47, 89, 104).",
      "match": true
    },
    "services": {
      "justification": "The author offers services such as account creation ('Created not cracked' in Item 36) and access to private data groups (Item 17).",
      "match": true
    },
    "social": {
      "justification": "Item 39 explicitly invites users to join a channel chat for discussion.",
      "match": true
    },
    "software": {
      "justification": "The channel distributes .svb configuration files, which are scripts used with the SilverBullet software (Items 84, 91, 96).",
      "match": true
    },
    "spam-phishing-services": {
      "justification": "The author advertises the sale of SMTP inboxes (Items 52, 53, 97), which are primary tools used for bulk spam and phishing campaigns.",
      "match": true
    },
    "telecommunications": {
      "justification": "No discussion of mobile networks or telecommunications policy; mentions of 'mobile operator' in account logs refer to payment methods, not infrastructure.",
      "match": false
    },
    "video-streaming": {
      "justification": "A significant portion of the content focuses on selling and dumping accounts for streaming platforms including Netflix, Disney+, Canal+, and Starz Play (Items 21, 47, 89, 98).",
      "match": true
    },
    "vpn-proxies-anonymisation": {
      "justification": "Item 1 provides links to lists of rotating datacenter proxies, and Items 95/103 mention RDPS.",
      "match": true
    },
    "vulnerabilities-exploits": {
      "justification": "The channel shares cracking configurations, but these target authentication via credential stuffing rather than exploiting specific software vulnerabilities or providing PoCs.",
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
    "description": "The channel 'CRACK HU' operates as a cybercriminal marketplace. It primarily distributes stolen credential dumps (combos), sells access to private data groups, trades cracked accounts for streaming services (Netflix, Disney+, Spotify) and gaming (PSN), shares SilverBullet (.svb) configurations for account cracking, and sells infrastructure tools such as rotating proxies and SMTP inboxes."
  },
  "keyword_classifications": {
    "adult-content": {
      "justification": "No sexually explicit or adult-oriented material was found in the messages.",
      "match": false
    },
    "advertisements": {
      "justification": "The channel contains numerous promotional posts selling accounts, private group access, and technical services with pricing details (e.g., Items 17, 26, 47).",
      "match": true
    },
    "anti-entity": {
      "justification": "Item 73 contains hostile language and insults directed at Israel.",
      "match": true
    },
    "botnets": {
      "justification": "While 'bots' are mentioned in the context of SilverBullet configurations (Items 84, 91), there is no evidence of botnet C2 operations or compromised device networks.",
      "match": false
    },
    "carding": {
      "justification": "The channel shares specific credit card data including card numbers, expiry dates, and CVVs (Items 32-34) and distributes a '1M cc dump' file (Item 57).",
      "match": true
    },
    "cloud": {
      "justification": "Mention of 'private cloud' in Item 10 is vague and refers to the source of a credential combo rather than cloud computing services or architecture.",
      "match": false
    },
    "credential-dumps-data-leaks": {
      "justification": "The channel extensively shares text files containing stolen email and password combinations (Items 2-9, 12-16, 18-30) and lists of accounts with subscription details (Items 37, 40, 41, 59-71).",
      "match": true
    },
    "credential-theft": {
      "justification": "The sale of 'full mail access' (Item 17) and the distribution of stolen account logs indicate the result of credential theft.",
      "match": true
    },
    "cybercriminal-services": {
      "justification": "The author offers criminal services including selling access to private data groups (Items 17, 26), SMTP inboxes for spamming (Items 52, 53), and RDPS (Item 95).",
      "match": true
    },
    "disinformation": {
      "justification": "No evidence of coordinated false narratives or deceptive content intended to influence public opinion.",
      "match": false
    },
    "economy": {
      "justification": "No discussion of macroeconomic indicators, labor markets, or trade trends.",
      "match": false
    },
    "extremist": {
      "justification": "While Item 73 is hostile, it consists of insults rather than the promotion of extremist ideology, terrorism, or political violence as defined.",
      "match": false
    },
    "files": {
      "justification": "The channel frequently shares attached files including .txt credential lists and .svb configuration files (Items 2-9, 84, 91).",
      "match": true
    },
    "fraud-scams": {
      "justification": "The sale of 'cracked' or stolen accounts for services like Netflix and Spotify (Items 35, 47, 88) constitutes fraudulent activity.",
      "match": true
    },
    "gaming": {
      "justification": "Item 104 explicitly offers the sale of PSN (PlayStation Network) accounts.",
      "match": true
    },
    "hacking": {
      "justification": "The channel distributes SilverBullet (.svb) configurations for automated account cracking (Items 84, 91, 96, 102) and discusses tools for cracking Amazon SES (Item 58).",
      "match": true
    },
    "hardware": {
      "justification": "No mention of physical computing devices or hardware components.",
      "match": false
    },
    "health": {
      "justification": "No health-related content or medical information present.",
      "match": false
    },
    "hosting": {
      "justification": "The channel mentions the availability of RDPS (Remote Desktop Protocol Servers) in Items 95 and 103, which relates to server infrastructure hosting.",
      "match": true
    },
    "music": {
      "justification": "Item 35 involves the sale of Spotify premium accounts.",
      "match": true
    },
    "phishing": {
      "justification": "While tools for phishing (SMTP) are sold, there is no direct evidence of active phishing lures or deceptive websites in the provided text.",
      "match": false
    },
    "politics": {
      "justification": "Item 73 contains political hostility directed at a specific state (Israel).",
      "match": true
    },
    "products": {
      "justification": "The channel lists various digital products for sale, including streaming accounts and gaming accounts (Items 35, 47, 89, 104).",
      "match": true
    },
    "services": {
      "justification": "The author offers services such as account creation ('Created not cracked' in Item 36) and access to private data groups (Item 17).",
      "match": true
    },
    "social": {
      "justification": "Item 39 explicitly invites users to join a channel chat for discussion.",
      "match": true
    },
    "software": {
      "justification": "The channel distributes .svb configuration files, which are scripts used with the SilverBullet software (Items 84, 91, 96).",
      "match": true
    },
    "spam-phishing-services": {
      "justification": "The author advertises the sale of SMTP inboxes (Items 52, 53, 97), which are primary tools used for bulk spam and phishing campaigns.",
      "match": true
    },
    "telecommunications": {
      "justification": "No discussion of mobile networks or telecommunications policy; mentions of 'mobile operator' in account logs refer to payment methods, not infrastructure.",
      "match": false
    },
    "video-streaming": {
      "justification": "A significant portion of the content focuses on selling and dumping accounts for streaming platforms including Netflix, Disney+, Canal+, and Starz Play (Items 21, 47, 89, 98).",
      "match": true
    },
    "vpn-proxies-anonymisation": {
      "justification": "Item 1 provides links to lists of rotating datacenter proxies, and Items 95/103 mention RDPS.",
      "match": true
    },
    "vulnerabilities-exploits": {
      "justification": "The channel shares cracking configurations, but these target authentication via credential stuffing rather than exploiting specific software vulnerabilities or providing PoCs.",
      "match": false
    }
  }
}
```
```

# gemma4:e4b
elapsed_second_request: 24.30s

```json
{
  "channel_summary": {
    "description": "The channel functions as a dark web marketplace for illicit digital goods and services. Content revolves around the sale of stolen data, including massive dumps of emails and credentials, credit card information (CC dumps), premium streaming accounts (Netflix, Disney+), proxies, and specialized hacking configurations/tools."
  },
  "keyword_classifications": {
    "adult-content": {
      "justification": "No sexually explicit or adult-oriented material was observed in the messages.",
      "match": false
    },
    "advertisements": {
      "justification": "Nearly every message is a commercial solicitation, advertising goods (accounts, proxies) and services for sale with stated prices ('Price = 3$', 'For Sell').",
      "match": true
    },
    "anti-entity": {
      "justification": "Message Item 73 contains Arabic text that translates to hostile language targeting a specific entity/group (Israel).",
      "match": true
    },
    "botnets": {
      "justification": "The messages discuss and sell configurations containing 'Bot' counts (e.g., Item 84, 91), indicating involvement with automated bot activity.",
      "match": true
    },
    "carding": {
      "justification": "Messages Item 32, 33, and 34 explicitly display and sell credit card information (CC dumps) including Brand, Type, and Country.",
      "match": true
    },
    "cloud": {
      "justification": "The term 'private cloud' is mentioned once (Item 10), but the overall focus remains on data theft and account sales rather than general cloud infrastructure services.",
      "match": false
    },
    "credential-dumps-data-leaks": {
      "justification": "Multiple messages advertise and attach large files containing lists of leaked emails, usernames, and credentials (e.g., 'Good Emails_Hotmail.txt', '1M cc dump.txt').",
      "match": true
    },
    "credential-theft": {
      "justification": "The primary commodity sold is stolen access and authentication material, such as email accounts and streaming service credentials (e.g., Netflix With Your Emails).",
      "match": true
    },
    "cybercriminal-services": {
      "justification": "The channel sells multiple criminal services including proxies, account configurations, and data dumps for illicit use.",
      "match": true
    },
    "disinformation": {
      "justification": "No evidence of false or misleading content intended to influence public understanding on a broad topic was observed; the deception is purely transactional/criminal.",
      "match": false
    },
    "economy": {
      "justification": "The messages do not contain macro-economic indicators, labor market analysis, or general business climate discussions.",
      "match": false
    },
    "extremist": {
      "justification": "While Item 73 contains hostile political speech, it is too specific and does not constitute content promoting a broader extremist ideology or violence as defined.",
      "match": false
    },
    "files": {
      "justification": "The channel repeatedly shares and sells large data files attached to messages (e.g., .txt, .svb documents).",
      "match": true
    },
    "fraud-scams": {
      "justification": "The entire content of the channel constitutes a fraudulent marketplace for stolen goods and services.",
      "match": true
    },
    "gaming": {
      "justification": "No discussion or sale of video games, esports, or gaming assets was observed.",
      "match": false
    },
    "hacking": {
      "justification": "The channel advertises and sells tools and configurations for unauthorized access and exploitation (e.g., 'Config netflix vm +sub for sell').",
      "match": true
    },
    "hardware": {
      "justification": "No discussion or sale of physical computing devices, components, or peripherals was observed.",
      "match": false
    },
    "health": {
      "justification": "There is no content related to medicine, public health, or wellness.",
      "match": false
    },
    "hosting": {
      "justification": "The focus is on selling data and accounts, not general web hosting infrastructure services (like domain registration or server colocation).",
      "match": false
    },
    "music": {
      "justification": "No content related to music files, artists, or streaming was observed.",
      "match": false
    },
    "phishing": {
      "justification": "While the sale of email lists facilitates phishing, the messages themselves are selling the *tools* and *data*, not executing a specific deceptive lure or kit deployment process.",
      "match": false
    },
    "politics": {
      "justification": "Any mention of countries is limited to data origin (e.g., 'Country: UNITED STATES 🇺🇸') and does not constitute general political discussion or policy debate.",
      "match": false
    },
    "products": {
      "justification": "The items sold are primarily digital access, credentials, and configurations; the classification 'services' is more accurate than 'products'.",
      "match": false
    },
    "services": {
      "justification": "The channel operates by selling various services, including proxy access, account subscriptions, and configuration setups.",
      "match": true
    },
    "social": {
      "justification": "The messages are purely transactional and criminal in nature; they do not contain general social networking or community conversation.",
      "match": false
    },
    "software": {
      "justification": "Users sell configuration files and tools (e.g., '.svb' files) which function as software utilities for automation/scraping.",
      "match": true
    },
    "spam-phishing-services": {
      "justification": "The sale of proxies, email lists, and configurations is directly related to bulk messaging and managed spam campaigns.",
      "match": true
    },
    "telecommunications": {
      "justification": "Messages include the sale of phone numbers and communication access details (e.g., Item 37, 108).",
      "match": true
    },
    "video-streaming": {
      "justification": "The content is about selling *access* to streaming platforms (Netflix, Disney+), not the distribution of video files or live streams.",
      "match": false
    },
    "vpn-proxies-anonymisation": {
      "justification": "Proxies are explicitly advertised and sold multiple times ('Rotational Datacenter Proxies', 'Proxy: HQ❗️').",
      "match": true
    },
    "vulnerabilities-exploits": {
      "justification": "The channel sells the *result* of exploitation (access/configs), but does not discuss the technical vulnerability or proof-of-concept exploit methodology itself.",
      "match": false
    }
  }
}
```

raw output:
```
{
  "channel_summary": {
    "description": "The channel functions as a dark web marketplace for illicit digital goods and services. Content revolves around the sale of stolen data, including massive dumps of emails and credentials, credit card information (CC dumps), premium streaming accounts (Netflix, Disney+), proxies, and specialized hacking configurations/tools."
  },
  "keyword_classifications": {
    "adult-content": {
      "justification": "No sexually explicit or adult-oriented material was observed in the messages.",
      "match": false
    },
    "advertisements": {
      "justification": "Nearly every message is a commercial solicitation, advertising goods (accounts, proxies) and services for sale with stated prices ('Price = 3$', 'For Sell').",
      "match": true
    },
    "anti-entity": {
      "justification": "Message Item 73 contains Arabic text that translates to hostile language targeting a specific entity/group (Israel).",
      "match": true
    },
    "botnets": {
      "justification": "The messages discuss and sell configurations containing 'Bot' counts (e.g., Item 84, 91), indicating involvement with automated bot activity.",
      "match": true
    },
    "carding": {
      "justification": "Messages Item 32, 33, and 34 explicitly display and sell credit card information (CC dumps) including Brand, Type, and Country.",
      "match": true
    },
    "cloud": {
      "justification": "The term 'private cloud' is mentioned once (Item 10), but the overall focus remains on data theft and account sales rather than general cloud infrastructure services.",
      "match": false
    },
    "credential-dumps-data-leaks": {
      "justification": "Multiple messages advertise and attach large files containing lists of leaked emails, usernames, and credentials (e.g., 'Good Emails_Hotmail.txt', '1M cc dump.txt').",
      "match": true
    },
    "credential-theft": {
      "justification": "The primary commodity sold is stolen access and authentication material, such as email accounts and streaming service credentials (e.g., Netflix With Your Emails).",
      "match": true
    },
    "cybercriminal-services": {
      "justification": "The channel sells multiple criminal services including proxies, account configurations, and data dumps for illicit use.",
      "match": true
    },
    "disinformation": {
      "justification": "No evidence of false or misleading content intended to influence public understanding on a broad topic was observed; the deception is purely transactional/criminal.",
      "match": false
    },
    "economy": {
      "justification": "The messages do not contain macro-economic indicators, labor market analysis, or general business climate discussions.",
      "match": false
    },
    "extremist": {
      "justification": "While Item 73 contains hostile political speech, it is too specific and does not constitute content promoting a broader extremist ideology or violence as defined.",
      "match": false
    },
    "files": {
      "justification": "The channel repeatedly shares and sells large data files attached to messages (e.g., .txt, .svb documents).",
      "match": true
    },
    "fraud-scams": {
      "justification": "The entire content of the channel constitutes a fraudulent marketplace for stolen goods and services.",
      "match": true
    },
    "gaming": {
      "justification": "No discussion or sale of video games, esports, or gaming assets was observed.",
      "match": false
    },
    "hacking": {
      "justification": "The channel advertises and sells tools and configurations for unauthorized access and exploitation (e.g., 'Config netflix vm +sub for sell').",
      "match": true
    },
    "hardware": {
      "justification": "No discussion or sale of physical computing devices, components, or peripherals was observed.",
      "match": false
    },
    "health": {
      "justification": "There is no content related to medicine, public health, or wellness.",
      "match": false
    },
    "hosting": {
      "justification": "The focus is on selling data and accounts, not general web hosting infrastructure services (like domain registration or server colocation).",
      "match": false
    },
    "music": {
      "justification": "No content related to music files, artists, or streaming was observed.",
      "match": false
    },
    "phishing": {
      "justification": "While the sale of email lists facilitates phishing, the messages themselves are selling the *tools* and *data*, not executing a specific deceptive lure or kit deployment process.",
      "match": false
    },
    "politics": {
      "justification": "Any mention of countries is limited to data origin (e.g., 'Country: UNITED STATES 🇺🇸') and does not constitute general political discussion or policy debate.",
      "match": false
    },
    "products": {
      "justification": "The items sold are primarily digital access, credentials, and configurations; the classification 'services' is more accurate than 'products'.",
      "match": false
    },
    "services": {
      "justification": "The channel operates by selling various services, including proxy access, account subscriptions, and configuration setups.",
      "match": true
    },
    "social": {
      "justification": "The messages are purely transactional and criminal in nature; they do not contain general social networking or community conversation.",
      "match": false
    },
    "software": {
      "justification": "Users sell configuration files and tools (e.g., '.svb' files) which function as software utilities for automation/scraping.",
      "match": true
    },
    "spam-phishing-services": {
      "justification": "The sale of proxies, email lists, and configurations is directly related to bulk messaging and managed spam campaigns.",
      "match": true
    },
    "telecommunications": {
      "justification": "Messages include the sale of phone numbers and communication access details (e.g., Item 37, 108).",
      "match": true
    },
    "video-streaming": {
      "justification": "The content is about selling *access* to streaming platforms (Netflix, Disney+), not the distribution of video files or live streams.",
      "match": false
    },
    "vpn-proxies-anonymisation": {
      "justification": "Proxies are explicitly advertised and sold multiple times ('Rotational Datacenter Proxies', 'Proxy: HQ❗️').",
      "match": true
    },
    "vulnerabilities-exploits": {
      "justification": "The channel sells the *result* of exploitation (access/configs), but does not discuss the technical vulnerability or proof-of-concept exploit methodology itself.",
      "match": false
    }
  }
}
```

# gpt-oss:120b
elapsed_second_request: 15.55s

```json
{
  "channel_summary": {
    "description": "The Telegram channel distributes stolen credentials, account access (Netflix, Disney+, PSN, etc.), credit card dumps, rotating proxy lists, and configuration files for automated tools. It repeatedly advertises sales, pricing, and contact information, targeting cybercriminal customers."
  },
  "keyword_classifications": {
    "adult-content": {
      "justification": "No sexually explicit material or adult service advertising is present in the messages.",
      "match": false
    },
    "advertisements": {
      "justification": "Multiple posts contain promotional text, pricing, and calls to purchase services (e.g., Netflix accounts, proxies, credit cards).",
      "match": true
    },
    "anti-entity": {
      "justification": "Repeated Arabic phrase \"ينعل كسم إسرائيل\" expresses hostility toward Israel.",
      "match": true
    },
    "botnets": {
      "justification": "Messages mention bot counts in configs but do not explicitly offer botnet rental or C2 infrastructure.",
      "match": false
    },
    "carding": {
      "justification": "Posts include raw credit card numbers, expiration dates, CVV and related details (items 32‑34).",
      "match": true
    },
    "cloud": {
      "justification": "References to \"new customer on our cloud\" and \"Combo from private cloud\" indicate cloud‑based services.",
      "match": true
    },
    "credential-dumps-data-leaks": {
      "justification": "Numerous attached text files contain large email/password combos and other leaked credential lists.",
      "match": true
    },
    "credential-theft": {
      "justification": "The channel distributes stolen login credentials for various services (e.g., Netflix, Disney+, Hotmail).",
      "match": true
    },
    "cybercriminal-services": {
      "justification": "Offers for selling compromised accounts, proxy lists, and configuration files constitute criminal‑oriented services.",
      "match": true
    },
    "disinformation": {
      "justification": "No false or manipulative political narratives are observed.",
      "match": false
    },
    "economy": {
      "justification": "The content does not discuss macroeconomic indicators or market analysis.",
      "match": false
    },
    "extremist": {
      "justification": "While anti‑Israel statements appear, there is no promotion of extremist ideology or violent action.",
      "match": false
    },
    "files": {
      "justification": "Many messages include attached files (e.g., credential dumps, config scripts).",
      "match": true
    },
    "fraud-scams": {
      "justification": "Selling stolen account access and credit card data constitutes fraudulent schemes.",
      "match": true
    },
    "gaming": {
      "justification": "Posts advertise PlayStation Network (PSN) accounts and mention gaming‑related services.",
      "match": true
    },
    "hacking": {
      "justification": "References to cracking tools, configs for automated attacks, and credential harvesting indicate hacking activity.",
      "match": true
    },
    "hardware": {
      "justification": "No discussion of physical computing devices or components is present.",
      "match": false
    },
    "health": {
      "justification": "Health‑related topics are absent.",
      "match": false
    },
    "hosting": {
      "justification": "The channel does not explicitly offer web or server hosting services.",
      "match": false
    },
    "music": {
      "justification": "No music content or discussion is found.",
      "match": false
    },
    "phishing": {
      "justification": "There are no phishing kits, lure URLs, or spoofed brand campaigns advertised.",
      "match": false
    },
    "politics": {
      "justification": "Aside from an anti‑Israel remark, there is no broader political discussion or policy content.",
      "match": false
    },
    "products": {
      "justification": "The channel lists digital products such as Netflix accounts, proxy lists, and credit card data for sale.",
      "match": true
    },
    "services": {
      "justification": "Offers include access provisioning, configuration creation, and account selling services.",
      "match": true
    },
    "social": {
      "justification": "Content is focused on illicit commerce rather than casual social interaction.",
      "match": false
    },
    "software": {
      "justification": "Configuration files (.svb) and scripts for automated tools are shared, constituting software distribution.",
      "match": true
    },
    "spam-phishing-services": {
      "justification": "No dedicated spam or phishing campaign services are advertised.",
      "match": false
    },
    "telecommunications": {
      "justification": "The channel does not discuss telecom networks, carriers, or related policy.",
      "match": false
    },
    "video-streaming": {
      "justification": "Sales of Netflix and Disney+ account access relate to video‑streaming services.",
      "match": true
    },
    "vpn-proxies-anonymisation": {
      "justification": "Rotating datacenter proxies, residential proxies, and proxy lists are repeatedly offered.",
      "match": true
    },
    "vulnerabilities-exploits": {
      "justification": "No vulnerability research or exploit code is shared.",
      "match": false
    }
  }
}
```

raw output:
```
{
  "channel_summary": {
    "description": "The Telegram channel distributes stolen credentials, account access (Netflix, Disney+, PSN, etc.), credit card dumps, rotating proxy lists, and configuration files for automated tools. It repeatedly advertises sales, pricing, and contact information, targeting cybercriminal customers."
  },
  "keyword_classifications": {
    "adult-content": {
      "justification": "No sexually explicit material or adult service advertising is present in the messages.",
      "match": false
    },
    "advertisements": {
      "justification": "Multiple posts contain promotional text, pricing, and calls to purchase services (e.g., Netflix accounts, proxies, credit cards).",
      "match": true
    },
    "anti-entity": {
      "justification": "Repeated Arabic phrase \"ينعل كسم إسرائيل\" expresses hostility toward Israel.",
      "match": true
    },
    "botnets": {
      "justification": "Messages mention bot counts in configs but do not explicitly offer botnet rental or C2 infrastructure.",
      "match": false
    },
    "carding": {
      "justification": "Posts include raw credit card numbers, expiration dates, CVV and related details (items 32‑34).",
      "match": true
    },
    "cloud": {
      "justification": "References to \"new customer on our cloud\" and \"Combo from private cloud\" indicate cloud‑based services.",
      "match": true
    },
    "credential-dumps-data-leaks": {
      "justification": "Numerous attached text files contain large email/password combos and other leaked credential lists.",
      "match": true
    },
    "credential-theft": {
      "justification": "The channel distributes stolen login credentials for various services (e.g., Netflix, Disney+, Hotmail).",
      "match": true
    },
    "cybercriminal-services": {
      "justification": "Offers for selling compromised accounts, proxy lists, and configuration files constitute criminal‑oriented services.",
      "match": true
    },
    "disinformation": {
      "justification": "No false or manipulative political narratives are observed.",
      "match": false
    },
    "economy": {
      "justification": "The content does not discuss macroeconomic indicators or market analysis.",
      "match": false
    },
    "extremist": {
      "justification": "While anti‑Israel statements appear, there is no promotion of extremist ideology or violent action.",
      "match": false
    },
    "files": {
      "justification": "Many messages include attached files (e.g., credential dumps, config scripts).",
      "match": true
    },
    "fraud-scams": {
      "justification": "Selling stolen account access and credit card data constitutes fraudulent schemes.",
      "match": true
    },
    "gaming": {
      "justification": "Posts advertise PlayStation Network (PSN) accounts and mention gaming‑related services.",
      "match": true
    },
    "hacking": {
      "justification": "References to cracking tools, configs for automated attacks, and credential harvesting indicate hacking activity.",
      "match": true
    },
    "hardware": {
      "justification": "No discussion of physical computing devices or components is present.",
      "match": false
    },
    "health": {
      "justification": "Health‑related topics are absent.",
      "match": false
    },
    "hosting": {
      "justification": "The channel does not explicitly offer web or server hosting services.",
      "match": false
    },
    "music": {
      "justification": "No music content or discussion is found.",
      "match": false
    },
    "phishing": {
      "justification": "There are no phishing kits, lure URLs, or spoofed brand campaigns advertised.",
      "match": false
    },
    "politics": {
      "justification": "Aside from an anti‑Israel remark, there is no broader political discussion or policy content.",
      "match": false
    },
    "products": {
      "justification": "The channel lists digital products such as Netflix accounts, proxy lists, and credit card data for sale.",
      "match": true
    },
    "services": {
      "justification": "Offers include access provisioning, configuration creation, and account selling services.",
      "match": true
    },
    "social": {
      "justification": "Content is focused on illicit commerce rather than casual social interaction.",
      "match": false
    },
    "software": {
      "justification": "Configuration files (.svb) and scripts for automated tools are shared, constituting software distribution.",
      "match": true
    },
    "spam-phishing-services": {
      "justification": "No dedicated spam or phishing campaign services are advertised.",
      "match": false
    },
    "telecommunications": {
      "justification": "The channel does not discuss telecom networks, carriers, or related policy.",
      "match": false
    },
    "video-streaming": {
      "justification": "Sales of Netflix and Disney+ account access relate to video‑streaming services.",
      "match": true
    },
    "vpn-proxies-anonymisation": {
      "justification": "Rotating datacenter proxies, residential proxies, and proxy lists are repeatedly offered.",
      "match": true
    },
    "vulnerabilities-exploits": {
      "justification": "No vulnerability research or exploit code is shared.",
      "match": false
    }
  }
}
```

# granite4.1:30b
elapsed_second_request: 30.90s

```json
{
  "channel_summary": {
    "description": "The Telegram channel CRACK HU primarily focuses on selling illicit credentials, proxy services, and access to streaming accounts (Netflix, Spotify, Disney+, etc.). It frequently advertises email/password combos, credential dumps, rotating datacenter proxies, VPN/proxy anonymization tools, carding information (stolen credit cards), phishing kits, and various cybercriminal services for account takeover and fraud. Recurring themes include daily updates of new files, bulk sales of credentials, pricing lists for access, and requests for additional config templates or captcha-solving solutions."
  },
  "keyword_classifications": {
    "adult-content": {
      "justification": "No messages contain sexually explicit material, adult entertainment discussion, or age‑restricted content.",
      "match": false
    },
    "advertisements": {
      "justification": "Numerous posts explicitly promote and price services (proxies, credential dumps, streaming account access), matching the definition of promotional/advertisement content.",
      "match": true
    },
    "anti-entity": {
      "justification": "Only a few isolated messages contain anti‑Israeli text; this does not indicate a systematic focus on opposing any entity.",
      "match": false
    },
    "botnets": {
      "justification": "No references to networks of compromised devices, C2 operations, or botnet rentals are present.",
      "match": false
    },
    "carding": {
      "justification": "Multiple messages list full credit‑card details (number, expiry, CVV) with validation status, clearly indicating card theft and sale activity.",
      "match": true
    },
    "cloud": {
      "justification": "A couple of posts mention \"Combo from private cloud\" and a private cloud service, but there is no broader discussion of cloud providers or services.",
      "match": false
    },
    "credential-dumps-data-leaks": {
      "justification": "Many messages attach files named like \"1M cc dump.txt\", \"Good Emails_Hotmail.txt\", and similar lists, indicating traded credential dumps.",
      "match": true
    },
    "credential-theft": {
      "justification": "Repeated sharing of email/password combos, Hotmail/Gmail credentials, and account access details demonstrates credential theft activity.",
      "match": true
    },
    "cybercriminal-services": {
      "justification": "The channel offers rotating proxies, captcha‑solving configs, SMTP services, Netflix/Spotify account bundles, and config templates – all commercial cybercrime services.",
      "match": true
    },
    "disinformation": {
      "justification": "No evidence of false or misleading narratives aimed at deception is observed.",
      "match": false
    },
    "economy": {
      "justification": "Pricing lists and sales discussions exist but do not analyze macro‑economic conditions or policy impacts.",
      "match": false
    },
    "extremist": {
      "justification": "Only isolated anti‑Israeli statements appear; there is no promotion of extremist ideology, violence, or recruitment.",
      "match": false
    },
    "files": {
      "justification": "Numerous \"Document Attached:\" entries indicate routine file sharing (credential lists, config files), satisfying the definition.",
      "match": true
    },
    "fraud-scams": {
      "justification": "Sales of stolen credentials, streaming account access, and credit‑card data are classic fraudulent schemes.",
      "match": true
    },
    "gaming": {
      "justification": "No mentions of video games, cheats, or gaming communities are present.",
      "match": false
    },
    "hacking": {
      "justification": "While unauthorized access is implied by credential sales, there are no explicit hacking techniques or intrusion claims discussed.",
      "match": false
    },
    "hardware": {
      "justification": "No discussions of physical computing devices, components, or hardware repair appear.",
      "match": false
    },
    "health": {
      "justification": "Health‑related content is absent.",
      "match": false
    },
    "hosting": {
      "justification": "No web/app hosting, server colocation, or DNS services are advertised.",
      "match": false
    },
    "music": {
      "justification": "Although Spotify accounts are sold, there is no music‑file sharing or production content.",
      "match": false
    },
    "phishing": {
      "justification": "Several posts request captcha‑solver keys and provide phishing kit configurations (e.g., \"#Config  { Busuu [SOLVER] }\"), indicating phishing service offerings.",
      "match": true
    },
    "politics": {
      "justification": "Only brief anti‑Israeli remarks exist; no broader political debate or policy analysis is evident.",
      "match": false
    },
    "products": {
      "justification": "The channel repeatedly lists and prices tangible/digital products (proxies, credential bundles, streaming account access), matching the definition.",
      "match": true
    },
    "services": {
      "justification": "Numerous offers for paid services (proxy rental, config templates, captcha solving, SMTP inbox sales) confirm this classification.",
      "match": true
    },
    "social": {
      "justification": "While there are generic chat prompts, the channel's primary function is commercial illicit trade rather than general social networking.",
      "match": false
    },
    "software": {
      "justification": "Config files (`.svb` extensions) and phishing kits are shared as software artifacts, satisfying the keyword.",
      "match": true
    },
    "spam-phishing-services": {
      "justification": "Requests for captcha‑solver keys and provision of phishing kit configurations indicate managed spam/phishing service offerings.",
      "match": true
    },
    "telecommunications": {
      "justification": "Some credential lists mention telecom operators (e.g., Etisalat, Vodafone) but there is no discussion of network infrastructure or carrier services.",
      "match": false
    },
    "video-streaming": {
      "justification": "Multiple posts explicitly advertise Netflix, Spotify, Disney+, and Starz Play account bundles for sale, directly matching this keyword.",
      "match": true
    },
    "vpn-proxies-anonymisation": {
      "justification": "The first message advertises rotating datacenter HTTP and SOCKS5 proxies; later messages request SMTP services and captcha solvers used for anonymization, confirming the classification.",
      "match": true
    },
    "vulnerabilities-exploits": {
      "justification": "No discussion of software/hardware vulnerabilities, proof‑of‑concept exploits, or patch information is present.",
      "match": false
    }
  }
}
```

raw output:
```
{
  "channel_summary": {
    "description": "The Telegram channel CRACK HU primarily focuses on selling illicit credentials, proxy services, and access to streaming accounts (Netflix, Spotify, Disney+, etc.). It frequently advertises email/password combos, credential dumps, rotating datacenter proxies, VPN/proxy anonymization tools, carding information (stolen credit cards), phishing kits, and various cybercriminal services for account takeover and fraud. Recurring themes include daily updates of new files, bulk sales of credentials, pricing lists for access, and requests for additional config templates or captcha-solving solutions."
  },
  "keyword_classifications": {
    "adult-content": { 
      "justification": "No messages contain sexually explicit material, adult entertainment discussion, or age‑restricted content.",
      "match": false
    },
    "advertisements": { 
      "justification": "Numerous posts explicitly promote and price services (proxies, credential dumps, streaming account access), matching the definition of promotional/advertisement content.",
      "match": true
    },
    "anti-entity": { 
      "justification": "Only a few isolated messages contain anti‑Israeli text; this does not indicate a systematic focus on opposing any entity.",
      "match": false
    },
    "botnets": { 
      "justification": "No references to networks of compromised devices, C2 operations, or botnet rentals are present.",
      "match": false
    },
    "carding": { 
      "justification": "Multiple messages list full credit‑card details (number, expiry, CVV) with validation status, clearly indicating card theft and sale activity.",
      "match": true
    },
    "cloud": { 
      "justification": "A couple of posts mention \"Combo from private cloud\" and a private cloud service, but there is no broader discussion of cloud providers or services.",
      "match": false
    },
    "credential-dumps-data-leaks": { 
      "justification": "Many messages attach files named like \"1M cc dump.txt\", \"Good Emails_Hotmail.txt\", and similar lists, indicating traded credential dumps.",
      "match": true
    },
    "credential-theft": { 
      "justification": "Repeated sharing of email/password combos, Hotmail/Gmail credentials, and account access details demonstrates credential theft activity.",
      "match": true
    },
    "cybercriminal-services": { 
      "justification": "The channel offers rotating proxies, captcha‑solving configs, SMTP services, Netflix/Spotify account bundles, and config templates – all commercial cybercrime services.",
      "match": true
    },
    "disinformation": { 
      "justification": "No evidence of false or misleading narratives aimed at deception is observed.",
      "match": false
    },
    "economy": { 
      "justification": "Pricing lists and sales discussions exist but do not analyze macro‑economic conditions or policy impacts.",
      "match": false
    },
    "extremist": { 
      "justification": "Only isolated anti‑Israeli statements appear; there is no promotion of extremist ideology, violence, or recruitment.",
      "match": false
    },
    "files": { 
      "justification": "Numerous \"Document Attached:\" entries indicate routine file sharing (credential lists, config files), satisfying the definition.",
      "match": true
    },
    "fraud-scams": { 
      "justification": "Sales of stolen credentials, streaming account access, and credit‑card data are classic fraudulent schemes.",
      "match": true
    },
    "gaming": { 
      "justification": "No mentions of video games, cheats, or gaming communities are present.",
      "match": false
    },
    "hacking": { 
      "justification": "While unauthorized access is implied by credential sales, there are no explicit hacking techniques or intrusion claims discussed.",
      "match": false
    },
    "hardware": { 
      "justification": "No discussions of physical computing devices, components, or hardware repair appear.",
      "match": false
    },
    "health": { 
      "justification": "Health‑related content is absent.",
      "match": false
    },
    "hosting": { 
      "justification": "No web/app hosting, server colocation, or DNS services are advertised.",
      "match": false
    },
    "music": { 
      "justification": "Although Spotify accounts are sold, there is no music‑file sharing or production content.",
      "match": false
    },
    "phishing": { 
      "justification": "Several posts request captcha‑solver keys and provide phishing kit configurations (e.g., \"#Config  { Busuu [SOLVER] }\"), indicating phishing service offerings.",
      "match": true
    },
    "politics": { 
      "justification": "Only brief anti‑Israeli remarks exist; no broader political debate or policy analysis is evident.",
      "match": false
    },
    "products": { 
      "justification": "The channel repeatedly lists and prices tangible/digital products (proxies, credential bundles, streaming account access), matching the definition.",
      "match": true
    },
    "services": { 
      "justification": "Numerous offers for paid services (proxy rental, config templates, captcha solving, SMTP inbox sales) confirm this classification.",
      "match": true
    },
    "social": { 
      "justification": "While there are generic chat prompts, the channel's primary function is commercial illicit trade rather than general social networking.",
      "match": false
    },
    "software": { 
      "justification": "Config files (`.svb` extensions) and phishing kits are shared as software artifacts, satisfying the keyword.",
      "match": true
    },
    "spam-phishing-services": { 
      "justification": "Requests for captcha‑solver keys and provision of phishing kit configurations indicate managed spam/phishing service offerings.",
      "match": true
    },
    "telecommunications": { 
      "justification": "Some credential lists mention telecom operators (e.g., Etisalat, Vodafone) but there is no discussion of network infrastructure or carrier services.",
      "match": false
    },
    "video-streaming": { 
      "justification": "Multiple posts explicitly advertise Netflix, Spotify, Disney+, and Starz Play account bundles for sale, directly matching this keyword.",
      "match": true
    },
    "vpn-proxies-anonymisation": { 
      "justification": "The first message advertises rotating datacenter HTTP and SOCKS5 proxies; later messages request SMTP services and captcha solvers used for anonymization, confirming the classification.",
      "match": true
    },
    "vulnerabilities-exploits": { 
      "justification": "No discussion of software/hardware vulnerabilities, proof‑of‑concept exploits, or patch information is present.",
      "match": false
    }
  }
}
```

# igorls/gemma4-e4b-classifier:q8_0
elapsed_second_request: 27.56s

```json
{
  "channel_summary": {
    "description": "The channel functions as a dark market marketplace specializing in selling illicit digital goods and services. Recurring themes include cracked subscription accounts (Netflix, Disney+, Spotify), stolen data dumps (email lists, CC information), technical tools like proxies and configuration files (.svb), and various cybercriminal services."
  },
  "keyword_classifications": {
    "adult-content": {
      "justification": "No sexually explicit or adult-oriented material is present in the messages.",
      "match": false
    },
    "advertisements": {
      "justification": "The channel content consists almost entirely of commercial solicitations and sales pitches for digital goods and services, often including pricing information (e.g., 'Price = 3$').",
      "match": true
    },
    "anti-entity": {
      "justification": "Message 73 contains Arabic text expressing hostility towards Israel ('ينعل كسم إسرائيل'), which targets a specific entity.",
      "match": true
    },
    "botnets": {
      "justification": "Configuration files mention 'Bot: 50-100' (Item 84, Item 91), but there is no discussion of operating or renting botnet networks themselves.",
      "match": false
    },
    "carding": {
      "justification": "Messages 32, 33, and 34 display detailed information regarding credit cards (VISA, MASTERCARD) including approval status and CVV matches, indicating card testing or fraudulent use of payment data.",
      "match": true
    },
    "cloud": {
      "justification": "Messages 10 and 11 explicitly mention 'private cloud' and a 'new customer on our cloud,' referring to cloud infrastructure services.",
      "match": true
    },
    "credential-dumps-data-leaks": {
      "justification": "Multiple messages advertise large files containing leaked user data, such as email dumps (e.g., Items 2, 3, 4, 5, 7) and a specific '1M cc dump.txt' (Item 57).",
      "match": true
    },
    "credential-theft": {
      "justification": "The channel sells large lists of harvested email accounts and associated data (e.g., Hotmail dumps), which is a direct result of credential harvesting or theft.",
      "match": true
    },
    "cybercriminal-services": {
      "justification": "The channel offers various paid illicit services, including configuration creation for specific sites (Item 67) and selling access/data.",
      "match": true
    },
    "disinformation": {
      "justification": "There is no observable evidence of coordinated false or misleading content intended to deceive audiences on contested topics.",
      "match": false
    },
    "economy": {
      "justification": "No discussion regarding macroeconomic conditions, inflation, or labor markets is present.",
      "match": false
    },
    "extremist": {
      "justification": "While Message 73 contains hostile content (anti-entity), it does not promote extremist ideology, violence, or terrorism as defined by the taxonomy.",
      "match": false
    },
    "files": {
      "justification": "The channel frequently shares and sells large data files, including dumps, configs, and email lists (e.g., Item 57: '1M cc dump.txt').",
      "match": true
    },
    "fraud-scams": {
      "justification": "While the sale of CC information is fraudulent, the primary activity is a marketplace for illicit goods; specific evidence of deceptive schemes intended to obtain money or sensitive information through social engineering (beyond the sales pitch) is weak.",
      "match": false
    },
    "gaming": {
      "justification": "Message 104 advertises an 'PSN full access account' and mentions purchasing games on it, relating to gaming accounts.",
      "match": true
    },
    "hacking": {
      "justification": "The channel promotes the sale of tools and configurations for unauthorized access (e.g., Item 58: 'crack amzom ses') and cracked account services.",
      "match": true
    },
    "hardware": {
      "justification": "No discussion of physical computing devices, components, or manufacturing is present.",
      "match": false
    },
    "health": {
      "justification": "The messages do not contain any content related to medicine, public health, or wellness.",
      "match": false
    },
    "hosting": {
      "justification": "While 'cloud' is mentioned (Item 10), the context relates more to data storage and service access rather than traditional web/application hosting infrastructure.",
      "match": false
    },
    "music": {
      "justification": "Message 35 advertises premium Spotify access, which is a music streaming service.",
      "match": true
    },
    "phishing": {
      "justification": "The sale of email lists and configuration files for automated capture implies phishing infrastructure, but the messages themselves are sales pitches, not active lures or kits.",
      "match": false
    },
    "politics": {
      "justification": "No content related to political parties, elections, or civic governance is present.",
      "match": false
    },
    "products": {
      "justification": "The channel lists and sells specific digital items such as Starz Play Accounts (Item 89) and PSN accounts (Item 104), which qualify as digital products.",
      "match": true
    },
    "services": {
      "justification": "Many posts offer technical or access services, including configuration creation ('Config Send Otp For Sell,' Item 107) and account provision.",
      "match": true
    },
    "social": {
      "justification": "Message 39 mentions joining a channel chat for discussion, but this is minimal and not the primary theme of the content.",
      "match": false
    },
    "software": {
      "justification": "The sale and distribution of configuration files (.svb) used to automate platform access (e.g., Netflix, Wattpad) constitutes the trade of specialized software/tools.",
      "match": true
    },
    "spam-phishing-services": {
      "justification": "Configuration files are advertised for 'SilverBullet Program' with high CPM and proxy usage (Item 84, Item 91), indicating infrastructure used for bulk messaging or spam campaigns.",
      "match": true
    },
    "telecommunications": {
      "justification": "Subscription plans mention mobile operators (e.g., Etisalat Bundle Month, Item 37), but there is no discussion of general telecom network infrastructure.",
      "match": false
    },
    "video-streaming": {
      "justification": "Multiple posts focus on selling access to streaming platforms like Netflix, Disney+, and Canal+ (Items 21, 88, 98).",
      "match": true
    },
    "vpn-proxies-anonymisation": {
      "justification": "The channel explicitly advertises 'Rotational Datacenter Proxies' (Item 1) and configurations that require proxies ('Proxy: HQ❗️,' Item 98).",
      "match": true
    },
    "vulnerabilities-exploits": {
      "justification": "The use of automated configuration files (.svb) for 'Capture' and specific platform access implies the exploitation of system weaknesses, even if not explicitly named as an exploit.",
      "match": true
    }
  }
}
```

raw output:
```
{
  "channel_summary": {
    "description": "The channel functions as a dark market marketplace specializing in selling illicit digital goods and services. Recurring themes include cracked subscription accounts (Netflix, Disney+, Spotify), stolen data dumps (email lists, CC information), technical tools like proxies and configuration files (.svb), and various cybercriminal services."
  },
  "keyword_classifications": {
    "adult-content": {
      "justification": "No sexually explicit or adult-oriented material is present in the messages.",
      "match": false
    },
    "advertisements": {
      "justification": "The channel content consists almost entirely of commercial solicitations and sales pitches for digital goods and services, often including pricing information (e.g., 'Price = 3$').",
      "match": true
    },
    "anti-entity": {
      "justification": "Message 73 contains Arabic text expressing hostility towards Israel ('ينعل كسم إسرائيل'), which targets a specific entity.",
      "match": true
    },
    "botnets": {
      "justification": "Configuration files mention 'Bot: 50-100' (Item 84, Item 91), but there is no discussion of operating or renting botnet networks themselves.",
      "match": false
    },
    "carding": {
      "justification": "Messages 32, 33, and 34 display detailed information regarding credit cards (VISA, MASTERCARD) including approval status and CVV matches, indicating card testing or fraudulent use of payment data.",
      "match": true
    },
    "cloud": {
      "justification": "Messages 10 and 11 explicitly mention 'private cloud' and a 'new customer on our cloud,' referring to cloud infrastructure services.",
      "match": true
    },
    "credential-dumps-data-leaks": {
      "justification": "Multiple messages advertise large files containing leaked user data, such as email dumps (e.g., Items 2, 3, 4, 5, 7) and a specific '1M cc dump.txt' (Item 57).",
      "match": true
    },
    "credential-theft": {
      "justification": "The channel sells large lists of harvested email accounts and associated data (e.g., Hotmail dumps), which is a direct result of credential harvesting or theft.",
      "match": true
    },
    "cybercriminal-services": {
      "justification": "The channel offers various paid illicit services, including configuration creation for specific sites (Item 67) and selling access/data.",
      "match": true
    },
    "disinformation": {
      "justification": "There is no observable evidence of coordinated false or misleading content intended to deceive audiences on contested topics.",
      "match": false
    },
    "economy": {
      "justification": "No discussion regarding macroeconomic conditions, inflation, or labor markets is present.",
      "match": false
    },
    "extremist": {
      "justification": "While Message 73 contains hostile content (anti-entity), it does not promote extremist ideology, violence, or terrorism as defined by the taxonomy.",
      "match": false
    },
    "files": {
      "justification": "The channel frequently shares and sells large data files, including dumps, configs, and email lists (e.g., Item 57: '1M cc dump.txt').",
      "match": true
    },
    "fraud-scams": {
      "justification": "While the sale of CC information is fraudulent, the primary activity is a marketplace for illicit goods; specific evidence of deceptive schemes intended to obtain money or sensitive information through social engineering (beyond the sales pitch) is weak.",
      "match": false
    },
    "gaming": {
      "justification": "Message 104 advertises an 'PSN full access account' and mentions purchasing games on it, relating to gaming accounts.",
      "match": true
    },
    "hacking": {
      "justification": "The channel promotes the sale of tools and configurations for unauthorized access (e.g., Item 58: 'crack amzom ses') and cracked account services.",
      "match": true
    },
    "hardware": {
      "justification": "No discussion of physical computing devices, components, or manufacturing is present.",
      "match": false
    },
    "health": {
      "justification": "The messages do not contain any content related to medicine, public health, or wellness.",
      "match": false
    },
    "hosting": {
      "justification": "While 'cloud' is mentioned (Item 10), the context relates more to data storage and service access rather than traditional web/application hosting infrastructure.",
      "match": false
    },
    "music": {
      "justification": "Message 35 advertises premium Spotify access, which is a music streaming service.",
      "match": true
    },
    "phishing": {
      "justification": "The sale of email lists and configuration files for automated capture implies phishing infrastructure, but the messages themselves are sales pitches, not active lures or kits.",
      "match": false
    },
    "politics": {
      "justification": "No content related to political parties, elections, or civic governance is present.",
      "match": false
    },
    "products": {
      "justification": "The channel lists and sells specific digital items such as Starz Play Accounts (Item 89) and PSN accounts (Item 104), which qualify as digital products.",
      "match": true
    },
    "services": {
      "justification": "Many posts offer technical or access services, including configuration creation ('Config Send Otp For Sell,' Item 107) and account provision.",
      "match": true
    },
    "social": {
      "justification": "Message 39 mentions joining a channel chat for discussion, but this is minimal and not the primary theme of the content.",
      "match": false
    },
    "software": {
      "justification": "The sale and distribution of configuration files (.svb) used to automate platform access (e.g., Netflix, Wattpad) constitutes the trade of specialized software/tools.",
      "match": true
    },
    "spam-phishing-services": {
      "justification": "Configuration files are advertised for 'SilverBullet Program' with high CPM and proxy usage (Item 84, Item 91), indicating infrastructure used for bulk messaging or spam campaigns.",
      "match": true
    },
    "telecommunications": {
      "justification": "Subscription plans mention mobile operators (e.g., Etisalat Bundle Month, Item 37), but there is no discussion of general telecom network infrastructure.",
      "match": false
    },
    "video-streaming": {
      "justification": "Multiple posts focus on selling access to streaming platforms like Netflix, Disney+, and Canal+ (Items 21, 88, 98).",
      "match": true
    },
    "vpn-proxies-anonymisation": {
      "justification": "The channel explicitly advertises 'Rotational Datacenter Proxies' (Item 1) and configurations that require proxies ('Proxy: HQ❗️,' Item 98).",
      "match": true
    },
    "vulnerabilities-exploits": {
      "justification": "The use of automated configuration files (.svb) for 'Capture' and specific platform access implies the exploitation of system weaknesses, even if not explicitly named as an exploit.",
      "match": true
    }
  }
}
```

# mistral-medium-3.5:latest
elapsed_second_request: 94.65s

```json
{
  "channel_summary": {
    "description": "Telegram channel focused on trading and selling compromised credentials, account access (e.g., Netflix, Spotify, Disney+, PSN), credit card data, SMTP services, and configurations for automated tools. Also includes anti-Israel rhetoric and advertisements for cybercriminal services."
  },
  "keyword_classifications": {
    "adult-content": {
      "justification": "No evidence of sexually explicit material or adult-oriented content in the messages.",
      "match": false
    },
    "advertisements": {
      "justification": "Channel contains repeated promotional posts for selling accounts, configurations, and services (e.g., Netflix access, SMTP, RDP).",
      "match": true
    },
    "anti-entity": {
      "justification": "Message 73 explicitly contains anti-Israel rhetoric ('ينعل كسم إسرائيل').",
      "match": true
    },
    "botnets": {
      "justification": "No direct evidence of botnet operations, malware, or command-and-control discussions. References to 'bots' (e.g., Message 84) relate to automation tools, not botnets.",
      "match": false
    },
    "carding": {
      "justification": "Messages 32-34 and 57 explicitly share credit card details (VISA/MASTERCARD) with validation statuses. Message 10 mentions 'Combo from private cloud' (likely card data).",
      "match": true
    },
    "cloud": {
      "justification": "Messages 10-11 reference a 'private cloud' and 'new customer on our cloud,' indicating cloud-based operations for credential storage/trading.",
      "match": true
    },
    "credential-dumps-data-leaks": {
      "justification": "Multiple messages (2-9, 12-20, 22-30, 57) share or advertise leaked credential files (e.g., 'Good Emails_Hotmail.txt', '1M cc dump.txt').",
      "match": true
    },
    "credential-theft": {
      "justification": "Channel revolves around trading stolen credentials (emails, passwords, account access) and tools for their exploitation (e.g., configs for SilverBullet).",
      "match": true
    },
    "cybercriminal-services": {
      "justification": "Messages offer paid services like account creation (e.g., Netflix, Spotify), SMTP access, RDP sales, and configurations for automated cracking tools (e.g., Messages 21, 47, 88-92, 96-102).",
      "match": true
    },
    "disinformation": {
      "justification": "No evidence of coordinated false or misleading content intended to deceive public audiences.",
      "match": false
    },
    "economy": {
      "justification": "No discussions about macroeconomic conditions, trade, or industry trends. Pricing is limited to cybercriminal transactions.",
      "match": false
    },
    "extremist": {
      "justification": "Message 73 contains anti-Israel rhetoric but lacks explicit promotion of extremist ideology, political violence, or terrorism.",
      "match": false
    },
    "files": {
      "justification": "Numerous messages (2-9, 12-20, 22-30, 57, 84, 91, 96) involve sharing or advertising text files (e.g., credential lists, configs).",
      "match": true
    },
    "fraud-scams": {
      "justification": "Channel facilitates fraud via sale of stolen accounts (Netflix, Spotify), credit card data (Messages 32-34), and tools for unauthorized access.",
      "match": true
    },
    "gaming": {
      "justification": "Message 104 advertises PSN accounts with gaming-related features (PSN Plus, game purchases).",
      "match": true
    },
    "hacking": {
      "justification": "Messages discuss unauthorized access (e.g., account takeovers, configs for cracking tools like SilverBullet in Messages 84, 91, 96, 106).",
      "match": true
    },
    "hardware": {
      "justification": "No discussions about physical computing devices or hardware components.",
      "match": false
    },
    "health": {
      "justification": "No content related to public health, medicine, or healthcare systems.",
      "match": false
    },
    "hosting": {
      "justification": "Message 11 mentions a 'cloud' for customers, but no explicit hosting services (e.g., web/server/DNS) are advertised.",
      "match": false
    },
    "music": {
      "justification": "Messages 35 and 66 advertise Spotify accounts, which are music-streaming related.",
      "match": true
    },
    "phishing": {
      "justification": "No direct evidence of phishing lures, kits, or spoofed identities. Focus is on credential trading, not phishing execution.",
      "match": false
    },
    "politics": {
      "justification": "Message 73 contains political opposition (anti-Israel) but lacks broader political party/campaign/election discussions.",
      "match": false
    },
    "products": {
      "justification": "Channel sells intangible digital products (accounts, configs, credentials) rather than physical or general digital goods.",
      "match": false
    },
    "services": {
      "justification": "Messages offer services like account creation (Netflix, Spotify), SMTP access, RDP sales, and tool configurations (e.g., Messages 21, 47, 88-92).",
      "match": true
    },
    "social": {
      "justification": "No evidence of general social networking, personal updates, or community conversations unrelated to cybercriminal activity.",
      "match": false
    },
    "software": {
      "justification": "Messages 84, 91, 96, 106 share configuration files (e.g., '.svb' for SilverBullet) and discuss software tools for automation/cracking.",
      "match": true
    },
    "spam-phishing-services": {
      "justification": "No evidence of bulk messaging, phishing kit deployment, or managed phishing campaigns. SMTP services (Messages 52-53, 97) could be abused but are not explicitly for spam/phishing.",
      "match": false
    },
    "telecommunications": {
      "justification": "No discussions about mobile networks, ISPs, carriers, or communications infrastructure beyond SMTP email services.",
      "match": false
    },
    "video-streaming": {
      "justification": "Messages 21, 47-48, 76, 88-92, 94, 99-100, 102 advertise Netflix/Disney+/Starz Play accounts for streaming.",
      "match": true
    },
    "vpn-proxies-anonymisation": {
      "justification": "Message 1 explicitly advertises 'Rotational Datacenter Proxies' with HTTP/SOCKS5 ports and external links to proxy lists.",
      "match": true
    },
    "vulnerabilities-exploits": {
      "justification": "No discussions about software/hardware vulnerabilities, exploit development, or mitigation guidance. Configs are for automation, not exploitation of vulnerabilities.",
      "match": false
    }
  }
}
```

raw output:
```
{
  "channel_summary": {
    "description": "Telegram channel focused on trading and selling compromised credentials, account access (e.g., Netflix, Spotify, Disney+, PSN), credit card data, SMTP services, and configurations for automated tools. Also includes anti-Israel rhetoric and advertisements for cybercriminal services."
  },
  "keyword_classifications": {
    "adult-content": {
      "justification": "No evidence of sexually explicit material or adult-oriented content in the messages.",
      "match": false
    },
    "advertisements": {
      "justification": "Channel contains repeated promotional posts for selling accounts, configurations, and services (e.g., Netflix access, SMTP, RDP).",
      "match": true
    },
    "anti-entity": {
      "justification": "Message 73 explicitly contains anti-Israel rhetoric ('ينعل كسم إسرائيل').",
      "match": true
    },
    "botnets": {
      "justification": "No direct evidence of botnet operations, malware, or command-and-control discussions. References to 'bots' (e.g., Message 84) relate to automation tools, not botnets.",
      "match": false
    },
    "carding": {
      "justification": "Messages 32-34 and 57 explicitly share credit card details (VISA/MASTERCARD) with validation statuses. Message 10 mentions 'Combo from private cloud' (likely card data).",
      "match": true
    },
    "cloud": {
      "justification": "Messages 10-11 reference a 'private cloud' and 'new customer on our cloud,' indicating cloud-based operations for credential storage/trading.",
      "match": true
    },
    "credential-dumps-data-leaks": {
      "justification": "Multiple messages (2-9, 12-20, 22-30, 57) share or advertise leaked credential files (e.g., 'Good Emails_Hotmail.txt', '1M cc dump.txt').",
      "match": true
    },
    "credential-theft": {
      "justification": "Channel revolves around trading stolen credentials (emails, passwords, account access) and tools for their exploitation (e.g., configs for SilverBullet).",
      "match": true
    },
    "cybercriminal-services": {
      "justification": "Messages offer paid services like account creation (e.g., Netflix, Spotify), SMTP access, RDP sales, and configurations for automated cracking tools (e.g., Messages 21, 47, 88-92, 96-102).",
      "match": true
    },
    "disinformation": {
      "justification": "No evidence of coordinated false or misleading content intended to deceive public audiences.",
      "match": false
    },
    "economy": {
      "justification": "No discussions about macroeconomic conditions, trade, or industry trends. Pricing is limited to cybercriminal transactions.",
      "match": false
    },
    "extremist": {
      "justification": "Message 73 contains anti-Israel rhetoric but lacks explicit promotion of extremist ideology, political violence, or terrorism.",
      "match": false
    },
    "files": {
      "justification": "Numerous messages (2-9, 12-20, 22-30, 57, 84, 91, 96) involve sharing or advertising text files (e.g., credential lists, configs).",
      "match": true
    },
    "fraud-scams": {
      "justification": "Channel facilitates fraud via sale of stolen accounts (Netflix, Spotify), credit card data (Messages 32-34), and tools for unauthorized access.",
      "match": true
    },
    "gaming": {
      "justification": "Message 104 advertises PSN accounts with gaming-related features (PSN Plus, game purchases).",
      "match": true
    },
    "hacking": {
      "justification": "Messages discuss unauthorized access (e.g., account takeovers, configs for cracking tools like SilverBullet in Messages 84, 91, 96, 106).",
      "match": true
    },
    "hardware": {
      "justification": "No discussions about physical computing devices or hardware components.",
      "match": false
    },
    "health": {
      "justification": "No content related to public health, medicine, or healthcare systems.",
      "match": false
    },
    "hosting": {
      "justification": "Message 11 mentions a 'cloud' for customers, but no explicit hosting services (e.g., web/server/DNS) are advertised.",
      "match": false
    },
    "music": {
      "justification": "Messages 35 and 66 advertise Spotify accounts, which are music-streaming related.",
      "match": true
    },
    "phishing": {
      "justification": "No direct evidence of phishing lures, kits, or spoofed identities. Focus is on credential trading, not phishing execution.",
      "match": false
    },
    "politics": {
      "justification": "Message 73 contains political opposition (anti-Israel) but lacks broader political party/campaign/election discussions.",
      "match": false
    },
    "products": {
      "justification": "Channel sells intangible digital products (accounts, configs, credentials) rather than physical or general digital goods.",
      "match": false
    },
    "services": {
      "justification": "Messages offer services like account creation (Netflix, Spotify), SMTP access, RDP sales, and tool configurations (e.g., Messages 21, 47, 88-92).",
      "match": true
    },
    "social": {
      "justification": "No evidence of general social networking, personal updates, or community conversations unrelated to cybercriminal activity.",
      "match": false
    },
    "software": {
      "justification": "Messages 84, 91, 96, 106 share configuration files (e.g., '.svb' for SilverBullet) and discuss software tools for automation/cracking.",
      "match": true
    },
    "spam-phishing-services": {
      "justification": "No evidence of bulk messaging, phishing kit deployment, or managed phishing campaigns. SMTP services (Messages 52-53, 97) could be abused but are not explicitly for spam/phishing.",
      "match": false
    },
    "telecommunications": {
      "justification": "No discussions about mobile networks, ISPs, carriers, or communications infrastructure beyond SMTP email services.",
      "match": false
    },
    "video-streaming": {
      "justification": "Messages 21, 47-48, 76, 88-92, 94, 99-100, 102 advertise Netflix/Disney+/Starz Play accounts for streaming.",
      "match": true
    },
    "vpn-proxies-anonymisation": {
      "justification": "Message 1 explicitly advertises 'Rotational Datacenter Proxies' with HTTP/SOCKS5 ports and external links to proxy lists.",
      "match": true
    },
    "vulnerabilities-exploits": {
      "justification": "No discussions about software/hardware vulnerabilities, exploit development, or mitigation guidance. Configs are for automation, not exploitation of vulnerabilities.",
      "match": false
    }
  }
}
```

# mistral-small3.2:24b-instruct-2506-fp16
elapsed_second_request: 25.98s

```json
{
  "channel_summary": {
    "description": "The Telegram channel CRACK HU primarily focuses on the sale and distribution of compromised credentials, account access, and related cybercriminal services. The content includes lists of email addresses, payment card details, and subscription accounts for various streaming services like Netflix, Spotify, and Disney+. The channel also offers VPN proxies, SMTP services, and other tools facilitating fraudulent activities."
  },
  "keyword_classifications": {
    "adult-content": {
      "justification": "No evidence of adult content in the messages.",
      "match": false
    },
    "advertisements": {
      "justification": "Multiple posts advertise services and products for sale, including account access, proxies, and SMTP services.",
      "match": true
    },
    "anti-entity": {
      "justification": "No content expressing opposition or hostility toward any specific entity.",
      "match": false
    },
    "botnets": {
      "justification": "No direct mention of botnets or related activities.",
      "match": false
    },
    "carding": {
      "justification": "Several messages contain payment card details and discussions about selling card information.",
      "match": true
    },
    "cloud": {
      "justification": "Mentions of 'private cloud' and cloud-related services in the context of selling account access.",
      "match": true
    },
    "credential-dumps-data-leaks": {
      "justification": "Multiple attachments and messages contain lists of email addresses and credentials, indicating data leaks.",
      "match": true
    },
    "credential-theft": {
      "justification": "Messages discuss the sale of compromised accounts and credentials, indicating credential theft activities.",
      "match": true
    },
    "cybercriminal-services": {
      "justification": "The channel offers services like account access, proxies, and SMTP services, which are used for fraudulent purposes.",
      "match": true
    },
    "disinformation": {
      "justification": "No evidence of disinformation campaigns or misleading content.",
      "match": false
    },
    "economy": {
      "justification": "No discussions related to economic conditions or analysis.",
      "match": false
    },
    "extremist": {
      "justification": "One message contains anti-Israel rhetoric, but it is not a primary theme of the channel.",
      "match": false
    },
    "files": {
      "justification": "Multiple messages include attachments of text files containing credentials and other data.",
      "match": true
    },
    "fraud-scams": {
      "justification": "The channel promotes the sale of compromised accounts and services used for fraudulent activities.",
      "match": true
    },
    "gaming": {
      "justification": "No content related to gaming or esports.",
      "match": false
    },
    "hacking": {
      "justification": "Messages discuss the sale of compromised accounts and services, which involve hacking activities.",
      "match": true
    },
    "hardware": {
      "justification": "No discussions related to hardware or physical devices.",
      "match": false
    },
    "health": {
      "justification": "No content related to health or medical information.",
      "match": false
    },
    "hosting": {
      "justification": "No direct mention of hosting services.",
      "match": false
    },
    "music": {
      "justification": "No content related to music or music files.",
      "match": false
    },
    "phishing": {
      "justification": "No direct evidence of phishing kits or campaigns, but the sale of compromised accounts could be related.",
      "match": false
    },
    "politics": {
      "justification": "No discussions related to political parties, campaigns, or governance.",
      "match": false
    },
    "products": {
      "justification": "Multiple posts advertise products and services for sale.",
      "match": true
    },
    "services": {
      "justification": "The channel offers various services like account access, proxies, and SMTP services.",
      "match": true
    },
    "social": {
      "justification": "No general social networking or community conversation content.",
      "match": false
    },
    "software": {
      "justification": "Messages discuss configurations and tools for accessing accounts, which involve software.",
      "match": true
    },
    "spam-phishing-services": {
      "justification": "No direct mention of spam or phishing services, but the sale of SMTP services could be related.",
      "match": false
    },
    "telecommunications": {
      "justification": "No discussions related to telecommunications infrastructure or policy.",
      "match": false
    },
    "video-streaming": {
      "justification": "Multiple messages discuss the sale of access to streaming services like Netflix and Disney+.",
      "match": true
    },
    "vpn-proxies-anonymisation": {
      "justification": "Messages advertise rotational datacenter proxies and VPN-related services.",
      "match": true
    },
    "vulnerabilities-exploits": {
      "justification": "No discussions related to software vulnerabilities or exploits.",
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
    "description": "The Telegram channel CRACK HU primarily focuses on the sale and distribution of compromised credentials, account access, and related cybercriminal services. The content includes lists of email addresses, payment card details, and subscription accounts for various streaming services like Netflix, Spotify, and Disney+. The channel also offers VPN proxies, SMTP services, and other tools facilitating fraudulent activities."
  },
  "keyword_classifications": {
    "adult-content": {
      "justification": "No evidence of adult content in the messages.",
      "match": false
    },
    "advertisements": {
      "justification": "Multiple posts advertise services and products for sale, including account access, proxies, and SMTP services.",
      "match": true
    },
    "anti-entity": {
      "justification": "No content expressing opposition or hostility toward any specific entity.",
      "match": false
    },
    "botnets": {
      "justification": "No direct mention of botnets or related activities.",
      "match": false
    },
    "carding": {
      "justification": "Several messages contain payment card details and discussions about selling card information.",
      "match": true
    },
    "cloud": {
      "justification": "Mentions of 'private cloud' and cloud-related services in the context of selling account access.",
      "match": true
    },
    "credential-dumps-data-leaks": {
      "justification": "Multiple attachments and messages contain lists of email addresses and credentials, indicating data leaks.",
      "match": true
    },
    "credential-theft": {
      "justification": "Messages discuss the sale of compromised accounts and credentials, indicating credential theft activities.",
      "match": true
    },
    "cybercriminal-services": {
      "justification": "The channel offers services like account access, proxies, and SMTP services, which are used for fraudulent purposes.",
      "match": true
    },
    "disinformation": {
      "justification": "No evidence of disinformation campaigns or misleading content.",
      "match": false
    },
    "economy": {
      "justification": "No discussions related to economic conditions or analysis.",
      "match": false
    },
    "extremist": {
      "justification": "One message contains anti-Israel rhetoric, but it is not a primary theme of the channel.",
      "match": false
    },
    "files": {
      "justification": "Multiple messages include attachments of text files containing credentials and other data.",
      "match": true
    },
    "fraud-scams": {
      "justification": "The channel promotes the sale of compromised accounts and services used for fraudulent activities.",
      "match": true
    },
    "gaming": {
      "justification": "No content related to gaming or esports.",
      "match": false
    },
    "hacking": {
      "justification": "Messages discuss the sale of compromised accounts and services, which involve hacking activities.",
      "match": true
    },
    "hardware": {
      "justification": "No discussions related to hardware or physical devices.",
      "match": false
    },
    "health": {
      "justification": "No content related to health or medical information.",
      "match": false
    },
    "hosting": {
      "justification": "No direct mention of hosting services.",
      "match": false
    },
    "music": {
      "justification": "No content related to music or music files.",
      "match": false
    },
    "phishing": {
      "justification": "No direct evidence of phishing kits or campaigns, but the sale of compromised accounts could be related.",
      "match": false
    },
    "politics": {
      "justification": "No discussions related to political parties, campaigns, or governance.",
      "match": false
    },
    "products": {
      "justification": "Multiple posts advertise products and services for sale.",
      "match": true
    },
    "services": {
      "justification": "The channel offers various services like account access, proxies, and SMTP services.",
      "match": true
    },
    "social": {
      "justification": "No general social networking or community conversation content.",
      "match": false
    },
    "software": {
      "justification": "Messages discuss configurations and tools for accessing accounts, which involve software.",
      "match": true
    },
    "spam-phishing-services": {
      "justification": "No direct mention of spam or phishing services, but the sale of SMTP services could be related.",
      "match": false
    },
    "telecommunications": {
      "justification": "No discussions related to telecommunications infrastructure or policy.",
      "match": false
    },
    "video-streaming": {
      "justification": "Multiple messages discuss the sale of access to streaming services like Netflix and Disney+.",
      "match": true
    },
    "vpn-proxies-anonymisation": {
      "justification": "Messages advertise rotational datacenter proxies and VPN-related services.",
      "match": true
    },
    "vulnerabilities-exploits": {
      "justification": "No discussions related to software vulnerabilities or exploits.",
      "match": false
    }
  }
}
```
```

# nemotron-3-super:latest
elapsed_second_request: 56.94s

```json
{
  "channel_summary": {
    "description": "The channel CRACK HU primarily sells compromised credentials, proxy services, and access to streaming accounts; it shares configs for cracking tools, advertises carding data, and offers various illicit digital products and services."
  },
  "keyword_classifications": {
    "adult-content": {
      "justification": "No sexually explicit or adult-oriented content observed in the messages.",
      "match": false
    },
    "advertisements": {
      "justification": "Multiple posts promote sales with pricing and contact info (e.g., Item 17 offering private data access, Item 21 selling Netflix configs).",
      "match": true
    },
    "anti-entity": {
      "justification": "No content expressing opposition to a specific country, government, or entity observed.",
      "match": false
    },
    "botnets": {
      "justification": "References to rotating datacenter proxies do not demonstrate botnet malware, C2, or rental operations.",
      "match": false
    },
    "carding": {
      "justification": "Messages include credit card numbers with approvals and CVV matches (Items 32-34) and a 1M cc dump file attachment (Item 57).",
      "match": true
    },
    "cloud": {
      "justification": "References to a private cloud and combos from private cloud indicate use of cloud infrastructure for storing/selling data (Item 10, Item 11).",
      "match": true
    },
    "credential-dumps-data-leaks": {
      "justification": "Numerous attachments are email lists and credential files (e.g., Items 2-16, 57) advertised as dumps.",
      "match": true
    },
    "credential-theft": {
      "justification": "The channel sells email/password combos and credit card data, implying theft and sale of credentials (Items 2-16, 32-34, 57).",
      "match": true
    },
    "cybercriminal-services": {
      "justification": "Offers proxy access, Netflix account sales, and config generation constitute illicit services for unauthorized access.",
      "match": true
    },
    "disinformation": {
      "justification": "No false or misleading content intended to deceive audiences on contested topics observed.",
      "match": false
    },
    "economy": {
      "justification": "No discussion of macroeconomic conditions, markets, or economic indicators present.",
      "match": false
    },
    "extremist": {
      "justification": "Insults toward Israel (Items 73) do not constitute extremist ideology promoting violence or terrorism.",
      "match": false
    },
    "files": {
      "justification": "Many messages attach text files containing credentials, configs, and dumps (Items 2-16, 57, 84, 91, 96).",
      "match": true
    },
    "fraud-scams": {
      "justification": "Selling stolen accounts and credit card data represents deceptive schemes to obtain money or services.",
      "match": true
    },
    "gaming": {
      "justification": "No mention of video games, esports, or game-related content observed.",
      "match": false
    },
    "hacking": {
      "justification": "Sharing configs for cracking tools (SilverBullet) and proxies facilitates unauthorized access to systems (Items 84, 91, 96).",
      "match": true
    },
    "hardware": {
      "justification": "No discussion of physical devices, components, or hardware manufacturing present.",
      "match": false
    },
    "health": {
      "justification": "No content related to public health, medicine, or healthcare systems observed.",
      "match": false
    },
    "hosting": {
      "justification": "Rotating datacenter proxies are offered as a proxy hosting service (Item 1).",
      "match": true
    },
    "music": {
      "justification": "Sales of Spotify premium accounts provide access to music streaming services (Item 35, Item 66).",
      "match": true
    },
    "phishing": {
      "justification": "No phishing kits, deceptive emails, or credential theft via spoofed brands observed.",
      "match": false
    },
    "politics": {
      "justification": "No content about political parties, elections, governance, or policy debate present.",
      "match": false
    },
    "products": {
      "justification": "The channel lists digital products for sale such as Netflix accounts, configs, and proxy lists (Items 17, 21, 35).",
      "match": true
    },
    "services": {
      "justification": "Offers include proxy access, account access, and config generation as ongoing services (Items 1, 17, 21).",
      "match": true
    },
    "social": {
      "justification": "While a chat channel is invited (Item 42), the primary focus is illicit trade, not general social networking.",
      "match": false
    },
    "software": {
      "justification": "Config files (.svb) for cracking tools are shared as scripts/utilities for unauthorized access (Items 84, 91, 96).",
      "match": true
    },
    "spam-phishing-services": {
      "justification": "No bulk messaging services, spam delivery, or phishing kit offerings observed.",
      "match": false
    },
    "telecommunications": {
      "justification": "Proxy offers do not constitute mobile/fixed‑line network services or carrier discussions.",
      "match": false
    },
    "video-streaming": {
      "justification": "Sales of Netflix accounts provide access to video streaming platforms (Items 17, 21, 89).",
      "match": true
    },
    "vpn-proxies-anonymisation": {
      "justification": "Rotating datacenter proxies (HTTP/SOCKS5) are advertised as anonymization/proxy services (Item 1).",
      "match": true
    },
    "vulnerabilities-exploits": {
      "justification": "No discussion of software/hardware vulnerabilities, exploit code, or mitigation guidance present.",
      "match": false
    }
  }
}
```

raw output:
```
{
  "channel_summary": {
    "description": "The channel CRACK HU primarily sells compromised credentials, proxy services, and access to streaming accounts; it shares configs for cracking tools, advertises carding data, and offers various illicit digital products and services."
  },
  "keyword_classifications": {
    "adult-content": {
      "justification": "No sexually explicit or adult-oriented content observed in the messages.",
      "match": false
    },
    "advertisements": {
      "justification": "Multiple posts promote sales with pricing and contact info (e.g., Item 17 offering private data access, Item 21 selling Netflix configs).",
      "match": true
    },
    "anti-entity": {
      "justification": "No content expressing opposition to a specific country, government, or entity observed.",
      "match": false
    },
    "botnets": {
      "justification": "References to rotating datacenter proxies do not demonstrate botnet malware, C2, or rental operations.",
      "match": false
    },
    "carding": {
      "justification": "Messages include credit card numbers with approvals and CVV matches (Items 32-34) and a 1M cc dump file attachment (Item 57).",
      "match": true
    },
    "cloud": {
      "justification": "References to a private cloud and combos from private cloud indicate use of cloud infrastructure for storing/selling data (Item 10, Item 11).",
      "match": true
    },
    "credential-dumps-data-leaks": {
      "justification": "Numerous attachments are email lists and credential files (e.g., Items 2-16, 57) advertised as dumps.",
      "match": true
    },
    "credential-theft": {
      "justification": "The channel sells email/password combos and credit card data, implying theft and sale of credentials (Items 2-16, 32-34, 57).",
      "match": true
    },
    "cybercriminal-services": {
      "justification": "Offers proxy access, Netflix account sales, and config generation constitute illicit services for unauthorized access.",
      "match": true
    },
    "disinformation": {
      "justification": "No false or misleading content intended to deceive audiences on contested topics observed.",
      "match": false
    },
    "economy": {
      "justification": "No discussion of macroeconomic conditions, markets, or economic indicators present.",
      "match": false
    },
    "extremist": {
      "justification": "Insults toward Israel (Items 73) do not constitute extremist ideology promoting violence or terrorism.",
      "match": false
    },
    "files": {
      "justification": "Many messages attach text files containing credentials, configs, and dumps (Items 2-16, 57, 84, 91, 96).",
      "match": true
    },
    "fraud-scams": {
      "justification": "Selling stolen accounts and credit card data represents deceptive schemes to obtain money or services.",
      "match": true
    },
    "gaming": {
      "justification": "No mention of video games, esports, or game-related content observed.",
      "match": false
    },
    "hacking": {
      "justification": "Sharing configs for cracking tools (SilverBullet) and proxies facilitates unauthorized access to systems (Items 84, 91, 96).",
      "match": true
    },
    "hardware": {
      "justification": "No discussion of physical devices, components, or hardware manufacturing present.",
      "match": false
    },
    "health": {
      "justification": "No content related to public health, medicine, or healthcare systems observed.",
      "match": false
    },
    "hosting": {
      "justification": "Rotating datacenter proxies are offered as a proxy hosting service (Item 1).",
      "match": true
    },
    "music": {
      "justification": "Sales of Spotify premium accounts provide access to music streaming services (Item 35, Item 66).",
      "match": true
    },
    "phishing": {
      "justification": "No phishing kits, deceptive emails, or credential theft via spoofed brands observed.",
      "match": false
    },
    "politics": {
      "justification": "No content about political parties, elections, governance, or policy debate present.",
      "match": false
    },
    "products": {
      "justification": "The channel lists digital products for sale such as Netflix accounts, configs, and proxy lists (Items 17, 21, 35).",
      "match": true
    },
    "services": {
      "justification": "Offers include proxy access, account access, and config generation as ongoing services (Items 1, 17, 21).",
      "match": true
    },
    "social": {
      "justification": "While a chat channel is invited (Item 42), the primary focus is illicit trade, not general social networking.",
      "match": false
    },
    "software": {
      "justification": "Config files (.svb) for cracking tools are shared as scripts/utilities for unauthorized access (Items 84, 91, 96).",
      "match": true
    },
    "spam-phishing-services": {
      "justification": "No bulk messaging services, spam delivery, or phishing kit offerings observed.",
      "match": false
    },
    "telecommunications": {
      "justification": "Proxy offers do not constitute mobile/fixed‑line network services or carrier discussions.",
      "match": false
    },
    "video-streaming": {
      "justification": "Sales of Netflix accounts provide access to video streaming platforms (Items 17, 21, 89).",
      "match": true
    },
    "vpn-proxies-anonymisation": {
      "justification": "Rotating datacenter proxies (HTTP/SOCKS5) are advertised as anonymization/proxy services (Item 1).",
      "match": true
    },
    "vulnerabilities-exploits": {
      "justification": "No discussion of software/hardware vulnerabilities, exploit code, or mitigation guidance present.",
      "match": false
    }
  }
}
```

# qwen3.5:122b
elapsed_second_request: 88.36s

```json
{
  "channel_summary": {
    "description": "The Telegram channel 'CRACK HU' functions as an illicit marketplace selling stolen credentials, credit card data (carding), subscription account access (Netflix, Spotify, PSN), and hacking tools/configs. It also offers proxy services and invites users to private groups for purchasing access to data dumps."
  },
  "keyword_classifications": {
    "adult-content": {
      "justification": "No sexually explicit or adult-oriented material was found in the messages.",
      "match": false
    },
    "advertisements": {
      "justification": "Multiple posts contain promotional content with pricing and calls to action for purchasing accounts, proxies, and data (e.g., 'For Sell', 'Price = 3$').",
      "match": true
    },
    "anti-entity": {
      "justification": "Item 73 contains repeated Arabic text expressing hostility toward Israel ('ينعل كسم إسرائيل'), targeting a specific country.",
      "match": true
    },
    "botnets": {
      "justification": "While proxies are sold, there is no evidence of networks of compromised devices or command-and-control operations typical of botnets.",
      "match": false
    },
    "carding": {
      "justification": "Messages display credit card numbers with validation status such as 'Charge Full', 'Card approved', and 'CVV Match' (Items 32-34, 57).",
      "match": true
    },
    "cloud": {
      "justification": "References to 'private cloud' and 'new customer on our cloud' indicate the use of cloud infrastructure for illicit data access.",
      "match": true
    },
    "credential-dumps-data-leaks": {
      "justification": "Files named '1M cc dump.txt', 'Hotmail...txt', and lists containing email:password combinations are shared as attachments.",
      "match": true
    },
    "credential-theft": {
      "justification": "Selling access to compromised accounts (Netflix, Spotify) and sharing login credentials implies unauthorized acquisition or theft.",
      "match": true
    },
    "cybercriminal-services": {
      "justification": "The channel offers services such as selling private data group access, proxies, and cracking configurations for a fee.",
      "match": true
    },
    "disinformation": {
      "justification": "No evidence of false or misleading content intended to deceive public understanding was found.",
      "match": false
    },
    "economy": {
      "justification": "The channel focuses on illicit sales rather than macroeconomic conditions, labor markets, or trade analysis.",
      "match": false
    },
    "extremist": {
      "justification": "While hate speech is present (Item 73), it does not explicitly promote political violence or extremist ideology beyond hostility.",
      "match": false
    },
    "files": {
      "justification": "Numerous text file attachments (.txt, .svb) containing data dumps and configurations are shared throughout the channel.",
      "match": true
    },
    "fraud-scams": {
      "justification": "Selling stolen credit cards and unauthorized account access constitutes deceptive schemes for financial gain.",
      "match": true
    },
    "gaming": {
      "justification": "PSN (PlayStation Network) accounts with subscriptions are explicitly offered for sale (Item 104).",
      "match": true
    },
    "hacking": {
      "justification": "Configs provided for cracking subscription sites ('Config by: Root', 'Solver') indicate unauthorized access methods.",
      "match": true
    },
    "hardware": {
      "justification": "No discussion of physical computing devices, components, or manufacturing is present.",
      "match": false
    },
    "health": {
      "justification": "No content related to public health, medicine, or wellness was found.",
      "match": false
    },
    "hosting": {
      "justification": "While proxies are sold, there is no clear evidence of general web or application hosting services for legitimate infrastructure.",
      "match": false
    },
    "music": {
      "justification": "Spotify premium accounts are listed for sale (Item 35), relating to music streaming access.",
      "match": true
    },
    "phishing": {
      "justification": "Configs mention 'Capture' and 'Send Otp', indicating capabilities for credential harvesting or SMS-based attacks.",
      "match": true
    },
    "politics": {
      "justification": "Content focuses on illicit goods rather than civic governance, elections, or policy debate.",
      "match": false
    },
    "products": {
      "justification": "Accounts, credit cards, and configs are treated as tangible/digital items with set prices and warranties.",
      "match": true
    },
    "services": {
      "justification": "Offers include selling access to data groups, proxy services, and config generation for a fee.",
      "match": true
    },
    "social": {
      "justification": "Invitations to join chat groups for discussion are present (e.g., Item 39 'Join to channel chat').",
      "match": true
    },
    "software": {
      "justification": ".svb configuration files and automation scripts used for cracking are distributed as downloadable content.",
      "match": true
    },
    "spam-phishing-services": {
      "justification": "Item 107 explicitly offers 'Config Send Otp For Sell', which is infrastructure often used for spam or phishing campaigns.",
      "match": true
    },
    "telecommunications": {
      "justification": "No discussion of network policy, carrier operations, or communication infrastructure beyond billing data in dumps.",
      "match": false
    },
    "video-streaming": {
      "justification": "Netflix, Canal+, and Starz Play accounts with streaming access are sold (Items 21, 89, 98).",
      "match": true
    },
    "vpn-proxies-anonymisation": {
      "justification": "Item 1 explicitly sells 'Rotational Datacenter Proxies' (HTTP/SOCKS5) for anonymity.",
      "match": true
    },
    "vulnerabilities-exploits": {
      "justification": "Configs exploit subscription billing systems ('Auto Pay Accs', bypassing payment) indicating exploitation of system weaknesses.",
      "match": true
    }
  }
}
```

raw output:
```
{
  "channel_summary": {
    "description": "The Telegram channel 'CRACK HU' functions as an illicit marketplace selling stolen credentials, credit card data (carding), subscription account access (Netflix, Spotify, PSN), and hacking tools/configs. It also offers proxy services and invites users to private groups for purchasing access to data dumps."
  },
  "keyword_classifications": {
    "adult-content": {
      "justification": "No sexually explicit or adult-oriented material was found in the messages.",
      "match": false
    },
    "advertisements": {
      "justification": "Multiple posts contain promotional content with pricing and calls to action for purchasing accounts, proxies, and data (e.g., 'For Sell', 'Price = 3$').",
      "match": true
    },
    "anti-entity": {
      "justification": "Item 73 contains repeated Arabic text expressing hostility toward Israel ('ينعل كسم إسرائيل'), targeting a specific country.",
      "match": true
    },
    "botnets": {
      "justification": "While proxies are sold, there is no evidence of networks of compromised devices or command-and-control operations typical of botnets.",
      "match": false
    },
    "carding": {
      "justification": "Messages display credit card numbers with validation status such as 'Charge Full', 'Card approved', and 'CVV Match' (Items 32-34, 57).",
      "match": true
    },
    "cloud": {
      "justification": "References to 'private cloud' and 'new customer on our cloud' indicate the use of cloud infrastructure for illicit data access.",
      "match": true
    },
    "credential-dumps-data-leaks": {
      "justification": "Files named '1M cc dump.txt', 'Hotmail...txt', and lists containing email:password combinations are shared as attachments.",
      "match": true
    },
    "credential-theft": {
      "justification": "Selling access to compromised accounts (Netflix, Spotify) and sharing login credentials implies unauthorized acquisition or theft.",
      "match": true
    },
    "cybercriminal-services": {
      "justification": "The channel offers services such as selling private data group access, proxies, and cracking configurations for a fee.",
      "match": true
    },
    "disinformation": {
      "justification": "No evidence of false or misleading content intended to deceive public understanding was found.",
      "match": false
    },
    "economy": {
      "justification": "The channel focuses on illicit sales rather than macroeconomic conditions, labor markets, or trade analysis.",
      "match": false
    },
    "extremist": {
      "justification": "While hate speech is present (Item 73), it does not explicitly promote political violence or extremist ideology beyond hostility.",
      "match": false
    },
    "files": {
      "justification": "Numerous text file attachments (.txt, .svb) containing data dumps and configurations are shared throughout the channel.",
      "match": true
    },
    "fraud-scams": {
      "justification": "Selling stolen credit cards and unauthorized account access constitutes deceptive schemes for financial gain.",
      "match": true
    },
    "gaming": {
      "justification": "PSN (PlayStation Network) accounts with subscriptions are explicitly offered for sale (Item 104).",
      "match": true
    },
    "hacking": {
      "justification": "Configs provided for cracking subscription sites ('Config by: Root', 'Solver') indicate unauthorized access methods.",
      "match": true
    },
    "hardware": {
      "justification": "No discussion of physical computing devices, components, or manufacturing is present.",
      "match": false
    },
    "health": {
      "justification": "No content related to public health, medicine, or wellness was found.",
      "match": false
    },
    "hosting": {
      "justification": "While proxies are sold, there is no clear evidence of general web or application hosting services for legitimate infrastructure.",
      "match": false
    },
    "music": {
      "justification": "Spotify premium accounts are listed for sale (Item 35), relating to music streaming access.",
      "match": true
    },
    "phishing": {
      "justification": "Configs mention 'Capture' and 'Send Otp', indicating capabilities for credential harvesting or SMS-based attacks.",
      "match": true
    },
    "politics": {
      "justification": "Content focuses on illicit goods rather than civic governance, elections, or policy debate.",
      "match": false
    },
    "products": {
      "justification": "Accounts, credit cards, and configs are treated as tangible/digital items with set prices and warranties.",
      "match": true
    },
    "services": {
      "justification": "Offers include selling access to data groups, proxy services, and config generation for a fee.",
      "match": true
    },
    "social": {
      "justification": "Invitations to join chat groups for discussion are present (e.g., Item 39 'Join to channel chat').",
      "match": true
    },
    "software": {
      "justification": ".svb configuration files and automation scripts used for cracking are distributed as downloadable content.",
      "match": true
    },
    "spam-phishing-services": {
      "justification": "Item 107 explicitly offers 'Config Send Otp For Sell', which is infrastructure often used for spam or phishing campaigns.",
      "match": true
    },
    "telecommunications": {
      "justification": "No discussion of network policy, carrier operations, or communication infrastructure beyond billing data in dumps.",
      "match": false
    },
    "video-streaming": {
      "justification": "Netflix, Canal+, and Starz Play accounts with streaming access are sold (Items 21, 89, 98).",
      "match": true
    },
    "vpn-proxies-anonymisation": {
      "justification": "Item 1 explicitly sells 'Rotational Datacenter Proxies' (HTTP/SOCKS5) for anonymity.",
      "match": true
    },
    "vulnerabilities-exploits": {
      "justification": "Configs exploit subscription billing systems ('Auto Pay Accs', bypassing payment) indicating exploitation of system weaknesses.",
      "match": true
    }
  }
}
```

# qwen3.6:35b
elapsed_second_request: 38.64s

```json
{
  "channel_summary": {
    "description": "The channel operates as an illicit marketplace for stolen credentials, compromised accounts, automated fraud configurations, and proxy services, frequently sharing data dumps and commercial sales pitches."
  },
  "keyword_classifications": {
    "adult-content": {
      "justification": "No sexually explicit or adult-oriented material is present in the channel messages.",
      "match": false
    },
    "advertisements": {
      "justification": "Multiple posts contain promotional sales pitches, pricing lists, and commercial solicitations for accounts, proxies, and data dumps (e.g., Items 17, 26, 47, 88).",
      "match": true
    },
    "anti-entity": {
      "justification": "Item 73 contains Arabic text expressing derogatory sentiment toward Israel, aligning with opposition to a specific country.",
      "match": true
    },
    "botnets": {
      "justification": "While automation bots are mentioned for account creation configs, there is no evidence of compromised device networks, C2 operations, or botnet infrastructure.",
      "match": false
    },
    "carding": {
      "justification": "Messages explicitly display credit card numbers, expiry dates, CVVs, and bank details with validation results like Charge Full and CVV Match, alongside a file named 1M cc dump.txt (Items 32-34, 57).",
      "match": true
    },
    "cloud": {
      "justification": "References to cloud are used generically to describe data storage or sales infrastructure rather than discussing cloud providers, SaaS, PaaS, or IaaS services.",
      "match": false
    },
    "credential-dumps-data-leaks": {
      "justification": "Numerous attached text files contain bulk email/password combinations and normalized credential lists (e.g., Items 2-9, 12-16, 18-20).",
      "match": true
    },
    "credential-theft": {
      "justification": "The channel actively trades and sells compromised account access, full mail access, and credential dumps for various platforms, indicating theft and abuse of authentication material.",
      "match": true
    },
    "cybercriminal-services": {
      "justification": "The channel operates as a marketplace offering access brokerage, automated fraud configs, SMTP access, and proxy lists for illicit purposes.",
      "match": true
    },
    "disinformation": {
      "justification": "No content is present that attempts to deceive audiences or distort public understanding on contested topics.",
      "match": false
    },
    "economy": {
      "justification": "The channel does not discuss macroeconomic conditions, labor markets, inflation, or industry trends.",
      "match": false
    },
    "extremist": {
      "justification": "While derogatory text toward Israel appears once, it does not promote terrorism, violent accelerationism, or extremist ideology as defined.",
      "match": false
    },
    "files": {
      "justification": "The channel frequently shares attached documents, archives, and text files containing data dumps, configs, and credential lists (e.g., Items 2-9, 57, 84).",
      "match": true
    },
    "fraud-scams": {
      "justification": "Posts facilitate deceptive schemes by selling stolen accounts, automated fraud configurations, CVV-checked cards, and SMTP access for illicit campaigns.",
      "match": true
    },
    "gaming": {
      "justification": "Item 104 explicitly advertises PSN Plus subscription accounts for gaming purposes.",
      "match": true
    },
    "hacking": {
      "justification": "The channel distributes tools, compromised credentials, and methods for unauthorized account access and system compromise.",
      "match": true
    },
    "hardware": {
      "justification": "No discussion of physical computing devices, components, or manufacturing occurs.",
      "match": false
    },
    "health": {
      "justification": "No public health, medical, or wellness content is present.",
      "match": false
    },
    "hosting": {
      "justification": "Proxies and SMTP are sold for fraud infrastructure, not web or application hosting services.",
      "match": false
    },
    "music": {
      "justification": "Items 35 and 66 advertise Spotify premium accounts and configurations for sale.",
      "match": true
    },
    "phishing": {
      "justification": "No phishing kits, deceptive emails, or spoofed identity campaigns are explicitly advertised or discussed.",
      "match": false
    },
    "politics": {
      "justification": "Content focuses on illicit commerce rather than civic governance, elections, or political debate.",
      "match": false
    },
    "products": {
      "justification": "The channel lists tangible and digital products with pricing, availability, and fulfillment details.",
      "match": true
    },
    "services": {
      "justification": "Offers include recurring access subscriptions, automated config services, proxy rentals, and SMTP inbox access sold commercially.",
      "match": true
    },
    "social": {
      "justification": "While a chat link is provided, the channel's primary function is commercial illicit trade, not general social networking or community conversation.",
      "match": false
    },
    "software": {
      "justification": "The channel distributes automation scripts and configuration files for the SilverBullet program used in account fraud.",
      "match": true
    },
    "spam-phishing-services": {
      "justification": "SMTP access is sold, but there is no explicit mention of managed phishing campaigns or bulk mailing list services.",
      "match": false
    },
    "telecommunications": {
      "justification": "Mobile operator payment methods are noted for SVOD accounts, but telecom infrastructure or policy is not discussed.",
      "match": false
    },
    "video-streaming": {
      "justification": "Multiple posts sell access to Netflix, Disney+, and OSN+ streaming service accounts and configurations.",
      "match": true
    },
    "vpn-proxies-anonymisation": {
      "justification": "Item 1 explicitly advertises and provides links for Rotational Datacenter Proxies with HTTP and SOCKS5 ports.",
      "match": true
    },
    "vulnerabilities-exploits": {
      "justification": "Mentions of solvers and configs relate to account automation and fraud rather than software vulnerabilities or proof-of-concept exploits.",
      "match": false
    }
  }
}
```

raw output:
```
{
  "channel_summary": {
    "description": "The channel operates as an illicit marketplace for stolen credentials, compromised accounts, automated fraud configurations, and proxy services, frequently sharing data dumps and commercial sales pitches."
  },
  "keyword_classifications": {
    "adult-content": {
      "justification": "No sexually explicit or adult-oriented material is present in the channel messages.",
      "match": false
    },
    "advertisements": {
      "justification": "Multiple posts contain promotional sales pitches, pricing lists, and commercial solicitations for accounts, proxies, and data dumps (e.g., Items 17, 26, 47, 88).",
      "match": true
    },
    "anti-entity": {
      "justification": "Item 73 contains Arabic text expressing derogatory sentiment toward Israel, aligning with opposition to a specific country.",
      "match": true
    },
    "botnets": {
      "justification": "While automation bots are mentioned for account creation configs, there is no evidence of compromised device networks, C2 operations, or botnet infrastructure.",
      "match": false
    },
    "carding": {
      "justification": "Messages explicitly display credit card numbers, expiry dates, CVVs, and bank details with validation results like Charge Full and CVV Match, alongside a file named 1M cc dump.txt (Items 32-34, 57).",
      "match": true
    },
    "cloud": {
      "justification": "References to cloud are used generically to describe data storage or sales infrastructure rather than discussing cloud providers, SaaS, PaaS, or IaaS services.",
      "match": false
    },
    "credential-dumps-data-leaks": {
      "justification": "Numerous attached text files contain bulk email/password combinations and normalized credential lists (e.g., Items 2-9, 12-16, 18-20).",
      "match": true
    },
    "credential-theft": {
      "justification": "The channel actively trades and sells compromised account access, full mail access, and credential dumps for various platforms, indicating theft and abuse of authentication material.",
      "match": true
    },
    "cybercriminal-services": {
      "justification": "The channel operates as a marketplace offering access brokerage, automated fraud configs, SMTP access, and proxy lists for illicit purposes.",
      "match": true
    },
    "disinformation": {
      "justification": "No content is present that attempts to deceive audiences or distort public understanding on contested topics.",
      "match": false
    },
    "economy": {
      "justification": "The channel does not discuss macroeconomic conditions, labor markets, inflation, or industry trends.",
      "match": false
    },
    "extremist": {
      "justification": "While derogatory text toward Israel appears once, it does not promote terrorism, violent accelerationism, or extremist ideology as defined.",
      "match": false
    },
    "files": {
      "justification": "The channel frequently shares attached documents, archives, and text files containing data dumps, configs, and credential lists (e.g., Items 2-9, 57, 84).",
      "match": true
    },
    "fraud-scams": {
      "justification": "Posts facilitate deceptive schemes by selling stolen accounts, automated fraud configurations, CVV-checked cards, and SMTP access for illicit campaigns.",
      "match": true
    },
    "gaming": {
      "justification": "Item 104 explicitly advertises PSN Plus subscription accounts for gaming purposes.",
      "match": true
    },
    "hacking": {
      "justification": "The channel distributes tools, compromised credentials, and methods for unauthorized account access and system compromise.",
      "match": true
    },
    "hardware": {
      "justification": "No discussion of physical computing devices, components, or manufacturing occurs.",
      "match": false
    },
    "health": {
      "justification": "No public health, medical, or wellness content is present.",
      "match": false
    },
    "hosting": {
      "justification": "Proxies and SMTP are sold for fraud infrastructure, not web or application hosting services.",
      "match": false
    },
    "music": {
      "justification": "Items 35 and 66 advertise Spotify premium accounts and configurations for sale.",
      "match": true
    },
    "phishing": {
      "justification": "No phishing kits, deceptive emails, or spoofed identity campaigns are explicitly advertised or discussed.",
      "match": false
    },
    "politics": {
      "justification": "Content focuses on illicit commerce rather than civic governance, elections, or political debate.",
      "match": false
    },
    "products": {
      "justification": "The channel lists tangible and digital products with pricing, availability, and fulfillment details.",
      "match": true
    },
    "services": {
      "justification": "Offers include recurring access subscriptions, automated config services, proxy rentals, and SMTP inbox access sold commercially.",
      "match": true
    },
    "social": {
      "justification": "While a chat link is provided, the channel's primary function is commercial illicit trade, not general social networking or community conversation.",
      "match": false
    },
    "software": {
      "justification": "The channel distributes automation scripts and configuration files for the SilverBullet program used in account fraud.",
      "match": true
    },
    "spam-phishing-services": {
      "justification": "SMTP access is sold, but there is no explicit mention of managed phishing campaigns or bulk mailing list services.",
      "match": false
    },
    "telecommunications": {
      "justification": "Mobile operator payment methods are noted for SVOD accounts, but telecom infrastructure or policy is not discussed.",
      "match": false
    },
    "video-streaming": {
      "justification": "Multiple posts sell access to Netflix, Disney+, and OSN+ streaming service accounts and configurations.",
      "match": true
    },
    "vpn-proxies-anonymisation": {
      "justification": "Item 1 explicitly advertises and provides links for Rotational Datacenter Proxies with HTTP and SOCKS5 ports.",
      "match": true
    },
    "vulnerabilities-exploits": {
      "justification": "Mentions of solvers and configs relate to account automation and fraud rather than software vulnerabilities or proof-of-concept exploits.",
      "match": false
    }
  }
}
```
