# deepseek-r1:32b
elapsed_second_request: 28.41s

culture,music,politics,social,threat-intelligence,video-streaming

raw output:
```
6c4fe936-5c39-5452-a83c-2f31d34f0743  
aa5b2b77-ea28-5f5b-a202-ba129092714f  
2f8a51cb-86cf-5461-b403-8ad32d8503bc  
077f03fe-5275-5873-b2a0-ac4a7e91078c  
1dc04154-6956-54c8-8377-4602c2d4cdbc  
e39587b0-1b4c-5279-b085-543d91822ffb
```

# devstral-2:latest
elapsed_second_request: 21.10s

anti-entity,conflict-related,pro-entity,threat-intelligence

raw output:
```
e39587b0-1b4c-5279-b085-543d91822ffb
e38333b4-786c-5ec9-80d9-fa346636a8c8
ac3d1958-666a-5727-82d8-e11f3b05446a
255c1e12-cc19-50c0-920d-e478dad2d90a
```

# gemma4:12b
elapsed_second_request: 42.14s

anti-entity,conflict-related,culture,defense-and-military,music,pro-entity,propaganda,religious-ideological

raw output:
```
e38333b4-786c-5ec9-80d9-fa346636a8c8
75baf38d-6efb-59fa-8fcf-5b0b3c3aa364
64661731-2d6a-5741-b449-b60805c78c61
ac3d1958-666a-5727-82d8-e11f3b05446a
255c1e12-cc19-50c0-920d-e478dad2d90a
535a10f6-9788-55bb-a687-99077d13e427
aa5b2b77-ea28-5f5b-a202-ba129092714f
1dc04154-6956-54c8-8377-4602c2d4cdbc
```

# gemma4:31b
elapsed_second_request: 42.99s

anti-entity,conflict-related,culture,news,politics,pro-entity,propaganda,religious-ideological

raw output:
```
e38333b4-786c-5ec9-80d9-fa346636a8c8
6c4fe936-5c39-5452-a83c-2f31d34f0743
255c1e12-cc19-50c0-920d-e478dad2d90a
ac3d1958-666a-5727-82d8-e11f3b05446a
64661731-2d6a-5741-b449-b60805c78c61
4614cc52-1711-57b8-a224-889a8bd327fc
aa5b2b77-ea28-5f5b-a202-ba129092714f
75baf38d-6efb-59fa-8fcf-5b0b3c3aa364
```

# gemma4:e4b
elapsed_second_request: 11.22s

anti-entity,conflict-related,defense-and-military,pro-entity,propaganda

raw output:
```
75baf38d-6efb-59fa-8fcf-5b0b3c3aa364
e38333b4-786c-5ec9-80d9-fa346636a8c8
ac3d1958-666a-5727-82d8-e11f3b05446a
255c1e12-cc19-50c0-920d-e478dad2d90a
535a10f6-9788-55bb-a687-99077d13e427
```

# gpt-oss:120b
elapsed_second_request: 7.62s

conflict-related,extremist,politics,propaganda,religious-ideological

raw output:
```
0ce3bbf3-b2b8-5508-a53e-9a9ad8c6ef42
75baf38d-6efb-59fa-8fcf-5b0b3c3aa364
e38333b4-786c-5ec9-80d9-fa346636a8c8
6c4fe936-5c39-5452-a83c-2f31d34f0743
64661731-2d6a-5741-b449-b60805c78c61
```

# granite4.1:30b
elapsed_second_request: 11.42s

extremist,pro-entity

raw output:
```
0ce3bbf3-b2b8-5508-a53e-9a9ad8c6ef42
255c1e12-cc19-50c0-920d-e478dad2d90a
anti-entity: Material expressing opposition to, hostility toward, or targeting of a specific country, government, movement, organization, armed group, leader, ideology, or other identifiable entity.
```

# igorls/gemma4-e4b-classifier:q8_0
elapsed_second_request: 15.68s

anti-entity,conflict-related,culture,politics,pro-entity,propaganda,religious-ideological,social

raw output:
```
e38333b4-786c-5ec9-80d9-fa346636a8c8
ac3d1958-666a-5727-82d8-e11f3b05446a
255c1e12-cc19-50c0-920d-e478dad2d90a
75baf38d-6efb-59fa-8fcf-5b0b3c3aa364
64661731-2d6a-5741-b449-b60805c78c61
77f03fe-5275-5873-b2a0-ac4a7e91078c
aa5b2b77-ea28-5f5b-a202-ba129092714f
6c4fe936-5c39-5452-a83c-2f31d34f0743
2f8a51cb-86cf-5461-b403-8ad32d8503bc
```

# mistral-medium-3.5:latest
elapsed_second_request: 25.96s

anti-entity,conflict-related,culture,nationalist,politics,pro-entity,religious-ideological

raw output:
```
e38333b4-786c-5ec9-80d9-fa346636a8c8
6c4fe936-5c39-5452-a83c-2f31d34f0743
ac3d1958-666a-5727-82d8-e11f3b05446a
255c1e12-cc19-50c0-920d-e478dad2d90a
15230a5d-8364-56ae-9d92-7c340e4097ab
64661731-2d6a-5741-b449-b60805c78c61
aa5b2b77-ea28-5f5b-a202-ba129092714f
```

# mistral-small3.2:24b-instruct-2506-fp16
elapsed_second_request: 7.13s

dating,extremist,politics,propaganda,threat-intelligence

raw output:
```
Based on the provided chat content, here are the most relevant label UUIDs:

0ce3bbf3-b2b8-5508-a53e-9a9ad8c6ef42
6c4fe936-5c39-5452-a83c-2f31d34f0743
6fb27d25-27e5-5446-8a07-76daab0cc82d
75baf38d-6efb-59fa-8fcf-5b0b3c3aa364
e39587b0-1b4c-5279-b085-543d91822ffb
```

# nemotron-3-super:latest
elapsed_second_request: 15.15s

extremist,propaganda

raw output:
```
0ce3bbf3-b2b8-5508-a53e-9a9ad8c6ef42
75baf38d-6efb-59fa-8fcf-5b0b3c3aa364
```

# qwen3.5:122b
elapsed_second_request: 66.50s

anti-entity,conflict-related,culture,defense-and-military,extremist,nationalist,politics,pro-entity,propaganda,religious-ideological

raw output:
```
e38333b4-786c-5ec9-80d9-fa346636a8c8
75baf38d-6efb-59fa-8fcf-5b0b3c3aa364
255c1e12-cc19-50c0-920d-e478dad2d90a
ac3d1958-666a-5727-82d8-e11f3b05446a
64661731-2d6a-5741-b449-b60805c78c61
aa5b2b77-ea28-5f5b-a202-ba129092714f
6c4fe936-5c39-5452-a83c-2f31d34f0743
0ce3bbf3-b2b8-5508-a53e-9a9ad8c6ef42
15230a5d-8364-56ae-9d92-7c340e4097ab
535a10f6-9788-55bb-a687-99077d13e427
```

# qwen3.6:35b
elapsed_second_request: 24.15s

anti-entity,conflict-related,news,politics,propaganda,religious-ideological

raw output:
```
e38333b4-786c-5ec9-80d9-fa346636a8c8
75baf38d-6efb-59fa-8fcf-5b0b3c3aa364
ac3d1958-666a-5727-82d8-e11f3b05446a
64661731-2d6a-5741-b449-b60805c78c61
4614cc52-1711-57b8-a224-889a8bd327fc
6c4fe936-5c39-5452-a83c-2f31d34f0743
```
