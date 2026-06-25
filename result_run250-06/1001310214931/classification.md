# deepseek-r1:32b
elapsed_second_request: 28.00s

associations,news,pro-entity

raw output:
```
255c1e12-cc19-50c0-920d-e478dad2d90a  
4614cc52-1711-57b8-a224-889a8bd327fc  
48872e43-7dc9-5437-aae3-b24eb3bee09b
```

# devstral-2:latest
elapsed_second_request: 20.21s

anti-entity,extremist,politics

raw output:
```
0ce3bbf3-b2b8-5508-a53e-9a9ad8c6ef42
6c4fe936-5c39-5452-a83c-2f31d34f0743
ac3d1958-666a-5727-82d8-e11f3b05446a
```

# gemma4:12b
elapsed_second_request: 40.14s

anti-entity,conflict-related,disinformation,politics,propaganda,religious-ideological

raw output:
```
0ce3bbf3-5275-5873-b2a0-ac4a7e91078c
ef0e49ba-0dc9-5fae-aebb-191244c7d674
75baf38d-6efb-59fa-8fcf-5b0b3c3aa364
6c4fe936-5c39-5452-a83c-2f31d34f0743
ac3d1958-666a-5727-82d8-e11f3b05446a
64661731-2d6a-5741-b449-b60805c78c61
e38333b4-786c-5ec9-80d9-fa346636a8c8
```

# gemma4:31b
elapsed_second_request: 45.06s

anti-entity,disinformation,extremist,politics,propaganda,social

raw output:
```
ef0e49ba-0dc9-5fae-aebb-191244c7d674
75baf38d-6efb-59fa-8fcf-5b0b3c3aa364
ac3d1958-666a-5727-82d8-e11f3b05446a
0ce3bbf3-b2b8-5508-a53e-9a9ad8c6ef42
6c4fe936-5c39-5452-a83c-2f31d34f0743
2f8a51cb-86cf-5461-b403-8ad32d8503bc
```

# gemma4:e4b
elapsed_second_request: 4.76s

conflict-related,economy,health,infrastructure,investment,nationalist,politics,ponzi-financial-gain,pro-entity,weapons

raw output:
```
05451c34-d126-51b7-a5c4-669d4f9d3ed2
15230a5d-8364-56ae-9d92-7c340e4097ab
255c1e12-cc19-50c0-920d-e478dad2d90a
6c4fe936-5c39-5452-a83c-2f31d34f0743
3281efa6-c734-5dc3-ba93-3c78c1184d37
b11b9378-9b26-5438-965a-45b867679209
e38333b4-786c-5ec9-80d9-fa346636a8c8
da75b78f-2c98-5854-abc4-08194de0ba36
db86f02f-a34c-584a-a948-6c10f10c1b3f
dca1b043-1dbd-5761-8cd8-68b79b03b9a0
```

# gpt-oss:120b
elapsed_second_request: 9.76s

anti-entity,disinformation,extremist,news,politics,propaganda,social

raw output:
```
0ce3bbf3-b2b8-5508-a53e-9a9ad8c6ef42
75baf38d-6efb-59fa-8fcf-5b0b3c3aa364
ef0e49ba-0dc9-5fae-aebb-191244c7d674
6c4fe936-5c39-5452-a83c-2f31d34f0743
ac3d1958-666a-5727-82d8-e11f3b05446a
2f8a51cb-86cf-5461-b403-8ad32d8503bc
4614cc52-1711-57b8-a224-889a8bd327fc
```

# granite4.1:30b
elapsed_second_request: 10.19s

anti-entity,associations,dating,news,politics,pro-entity,propaganda,social

raw output:
```
2f8a51cb-86cf-5461-b403-8ad32d8503bc
6c4fe936-5c39-5452-a83c-2f31d34f0743
75baf38d-6efb-59fa-8fcf-5b0b3c3aa364
255c1e12-cc19-50c0-920d-e478dad2d90a
ac3d1958-666a-5727-82d8-e11f3b05446a
6fb27d25-27e5-5446-8a07-76daab0cc82d
48872e43-7dc9-5437-aae3-b24eb3bee09b
4614cc52-1711-57b8-a224-889a8bd327fc
```

# igorls/gemma4-e4b-classifier:q8_0
elapsed_second_request: 15.33s

anti-entity,disinformation,economy,extremist,politics,propaganda,social

raw output:
```
0ce3bbf3-b2b8-5508-a53e-9a9ad8c6ef42
ef0e49ba-0dc9-5fae-aebb-191244c7d674
6c4fe936-5c39-5452-a83c-2f31d34f0743
ac3d1958-666a-5727-82d8-e11f3b05446a
75baf38d-6efb-59fa-8fcf-5b0b3c3aa364
2f8a51cb-86cf-5461-b403-8ad32d8503bc
b11b9378-9b26-5438-965a-45b867679209
```

# mistral-medium-3.5:latest
elapsed_second_request: 23.37s

anti-entity,disinformation,nationalist,politics,propaganda

raw output:
```
6c4fe936-5c39-5452-a83c-2f31d34f0743
15230a5d-8364-56ae-9d92-7c340e4097ab
ac3d1958-666a-5727-82d8-e11f3b05446a
ef0e49ba-0dc9-5fae-aebb-191244c7d674
75baf38d-6efb-59fa-8fcf-5b0b3c3aa364
```

# mistral-small3.2:24b-instruct-2506-fp16
elapsed_second_request: 7.30s

anti-entity,dating,extremist,politics,propaganda

raw output:
```
Based on the provided chat content, here are the most relevant label UUIDs:

0ce3bbf3-b2b8-5508-a53e-9a9ad8c6ef42
6c4fe936-5c39-5452-a83c-2f31d34f0743
6fb27d25-27e5-5446-8a07-76daab0cc82d
75baf38d-6efb-59fa-8fcf-5b0b3c3aa364
ac3d1958-666a-5727-82d8-e11f3b05446a
```

# nemotron-3-super:latest
elapsed_second_request: 17.17s

anti-entity,disinformation,politics

raw output:
```
ac3d1958-666a-5727-82d8-e11f3b05446a
ef0e49ba-0dc9-5fae-aebb-191244c7d674
6c4fe936-5c39-5452-a83c-2f31d34f0743
```

# qwen3.5:122b
elapsed_second_request: 54.47s

anti-entity,conflict-related,disinformation,extremist,news,propaganda,social

raw output:
```
ef0e49ba-0dc9-5fae-aebb-191244c7d674
6c4fe936-d930-5a54-956d-2f191bf4abae
75baf38d-6efb-59fa-8fcf-5b0b3c3aa364
ac3d1958-666a-5727-82d8-e11f3b05446a
e38333b4-786c-5ec9-80d9-fa346636a8c8
2f8a51cb-86cf-5461-b403-8ad32d8503bc
0ce3bbf3-b2b8-5508-a53e-9a9ad8c6ef42
4614cc52-1711-57b8-a224-889a8bd327fc
```

# qwen3.6:35b
elapsed_second_request: 19.92s

disinformation,politics,propaganda

raw output:
```
ef0e49ba-0dc9-5fae-aebb-191244c7d674
75baf38d-6efb-59fa-8fcf-5b0b3c3aa364
6c4fe936-5c39-5452-a83c-2f31d34f0743
```
