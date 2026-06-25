# deepseek-r1:32b
elapsed_second_request: 23.00s

associations,news,pro-entity

raw output:
```
The analysis of the Team Trump Telegram channel reveals content primarily focused on political discussions, support for Donald Trump, and community organization. The most relevant labels from the allowed list are:

- politics: The channel discusses political events, government actions, and policies, fitting under this category.
- associations: It encourages joining specific groups and channels, indicating organized collective activity.
- pro-entity: Content expresses support for Donald Trump and his movement, clearly a pro-entity stance.

These labels capture the essence of the channel's content without overstepping into areas not supported by the provided messages.

4614cc52-1711-57b8-a224-889a8bd327fc  
48872e43-7dc9-5437-aae3-b24eb3bee09b  
255c1e12-cc19-50c0-920d-e478dad2d90a
```

# devstral-2:latest
elapsed_second_request: 21.17s

anti-entity,politics,pro-entity

raw output:
```
255c1e12-cc19-50c0-920d-e478dad2d90a
6c4fe936-5c39-5452-a83c-2f31d34f0743
ac3d1958-666a-5727-82d8-e11f3b05446a
```

# gemma4:12b
elapsed_second_request: 62.73s

advertisements,anti-entity,disinformation,fraud-scams,nationalist,phishing,politics,pro-entity,propaganda,religious-ideological

raw output:
```
6c4fe936-5c39-5452-a83c-2f31d34f0743
15230a5d-8364-56ae-9d92-7c340e4097ab
255c1e12-cc19-50c0-920d-e478dad2d90a
75baf38d-6efb-59fa-8fcf-5b0b3c3aa364
ef0e49ba-0dc9-5fae-aebb-191244c7d674
64661731-2d6a-5741-b449-b60805c78c61
ac3d1958-666a-5727-82d8-e11f3b05446a
8b63ca37-afb4-5ee4-83fc-4eafd5ee19de
c0703d1e-af36-5cae-93d1-f996d0d71b04
db14b663-bbde-52fb-a283-f543810990f5
```

# gemma4:31b
elapsed_second_request: 31.57s

anti-entity,disinformation,nationalist,politics,pro-entity,propaganda,social

raw output:
```
6c4fe936-5c39-5452-a83c-2f31d34f0743
255c1e12-cc19-50c0-920d-e478dad2d90a
ac3d1958-666a-5727-82d8-e11f3b05446a
15230a5d-8364-56ae-9d92-7c340e4097ab
ef0e49ba-0dc9-5fae-aebb-191244c7d674
75baf38d-6efb-59fa-8fcf-5b0b3c3aa364
2f8a51cb-86cf-5461-b403-8ad32d8503bc
```

# gemma4:e4b
elapsed_second_request: 32.65s

disinformation,nationalist,politics,pro-entity,propaganda,religious-ideological

raw output:
```
6c4fe936-5c39-5452-a83c-2f31d34f0743
75baf38d-6efb-59fa-8fcf-5b0b3c3aa364
15230a5d-8364-56ae-9d92-7c340e4097ab
255c1e12-cc19-50c0-920d-e478dad2d90a
64661731-2d6a-5741-b449-b60805c78c61
ef0e49ba-0dc9-5fae-aebb-191244c7d674
```

# gpt-oss:120b
elapsed_second_request: 7.28s

disinformation,extremist,nationalist,politics,pro-entity,propaganda

raw output:
```
0ce3bbf3-b2b8-5508-a53e-9a9ad8c6ef42
75baf38d-6efb-59fa-8fcf-5b0b3c3aa364
6c4fe936-5c39-5452-a83c-2f31d34f0743
15230a5d-8364-56ae-9d92-7c340e4097ab
ef0e49ba-0dc9-5fae-aebb-191244c7d674
255c1e12-cc19-50c0-920d-e478dad2d90a
```

# granite4.1:30b
elapsed_second_request: 9.50s

hosting,nationalist,politics,pro-entity,propaganda,religious-ideological,social

raw output:
```
255c1e12-cc19-50c0-920d-e478dad2d90a
15230a5d-8364-56ae-9d92-7c340e4097ab
6c4fe936-5c39-5452-a83c-2f31d34f0743
75baf38d-6efb-59fa-8fcf-5b0b3c3aa364
1a5e8a79-62d5-5870-9dda-4e4109c86f62
64661731-2d6a-5741-b449-b60805c78c61
2f8a51cb-86cf-5461-b403-8ad32d8503bc
```

# igorls/gemma4-e4b-classifier:q8_0
elapsed_second_request: 14.61s

disinformation,nationalist,politics,pro-entity,propaganda,social

raw output:
```
75baf38d-6efb-59fa-8fcf-5b0b3c3aa364
6c4fe936-5c39-5452-a83c-2f31d34f0743
15230a5d-8364-56ae-9d92-7c340e4097ab
ef0e49ba-0dc9-5fae-aebb-191244c7d674
255c1e12-cc19-50c0-920d-e478dad2d90a
2f8a51cb-86cf-5461-b403-8ad32d8503bc
```

# mistral-medium-3.5:latest
elapsed_second_request: 24.30s

nationalist,news,politics,pro-entity,propaganda

raw output:
```
255c1e12-cc19-50c0-920d-e478dad2d90a
6c4fe936-5c39-5452-a83c-2f31d34f0743
15230a5d-8364-56ae-9d92-7c340e4097ab
75baf38d-6efb-59fa-8fcf-5b0b3c3aa364
4614cc52-1711-57b8-a224-889a8bd327fc
```

# mistral-small3.2:24b-instruct-2506-fp16
elapsed_second_request: 8.60s

anti-entity,culture,dating,forensics,politics,pro-entity,threat-intelligence

raw output:
```
6c577620-d930-5a54-956d-2f191bf4abae
255c1e12-cc19-50c0-920d-e478dad2d90a
ac3d1958-666a-5727-82d8-e11f3b05446a
6fb27d25-27e5-5446-8a07-76daab0cc82d
6c4fe936-5c39-5452-a83c-2f31d34f0743
aa5b2b77-ea28-5f5b-a202-ba129092714f
e39587b0-1b4c-5279-b085-543d91822ffb
```

# nemotron-3-super:latest
elapsed_second_request: 16.41s

anti-entity,nationalist,politics,pro-entity

raw output:
```
255c1e12-cc19-50c0-920d-e478dad2d90a
ac3d1958-666a-5727-82d8-e11f3b05446a
6c4fe936-5c39-5452-a83c-2f31d34f0743
15230a5d-8364-56ae-9d92-7c340e4097ab
```

# qwen3.5:122b
elapsed_second_request: 33.89s

disinformation,nationalist,politics,pro-entity,propaganda

raw output:
```
6c4fe936-5c39-5452-a83c-2f31d34f0743
75baf38d-6efb-59fa-8fcf-5b0b3c3aa364
ef0e49ba-0dc9-5fae-aebb-191244c7d674
15230a5d-8364-56ae-9d92-7c340e4097ab
255c1e12-cc19-50c0-920d-e478dad2d90a
```

# qwen3.6:35b
elapsed_second_request: 22.13s

disinformation,nationalist,politics,pro-entity,propaganda

raw output:
```
6c4fe936-5c39-5452-a83c-2f31d34f0743
ef0e49ba-0dc9-5fae-aebb-191244c7d674
75baf38d-6efb-59fa-8fcf-5b0b3c3aa364
15230a5d-8364-56ae-9d92-7c340e4097ab
255c1e12-cc19-50c0-920d-e478dad2d90a
```
