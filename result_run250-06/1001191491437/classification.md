# deepseek-r1:32b
elapsed_second_request: 25.28s

investment,money-laundering-cash-in-out,services,trading

raw output:
```
05451c34-d126-51b7-a5c4-669d4f9d3ed2  
d9cc06cf-2e91-5d25-a343-ad23ca79061a  
a8b69ee0-b3e1-5ede-90fe-f16317dc5aca  
31b11b45-f5a8-5cb4-85ea-1594e2a06743
```

# devstral-2:latest
elapsed_second_request: 22.56s

cryptocurrencies,gaming,trading

raw output:
```
d9cc06cf-2e91-5d25-a343-ad23ca79061a
b77a3289-d6c6-5d52-bb4e-8ff2d3d6718f
f106b5ec-d074-5f3f-8770-674e28ce5370
```

# gemma4:12b
elapsed_second_request: 52.48s

advertisements,credential-theft,cybercriminal-services,gaming,investment,products,services,software,trading,vpn-proxies-anonymisation

raw output:
```
c49fdfa3-47c5-596f-a157-d14154315dc8
f106b5ec-d074-5f3f-8770-674e28ce5370
05451c34-d126-51b7-a5c4-669d4f9d3ed2
d9cc06cf-2e91-5d25-a343-ad23ca79061a
3a1d555e-252d-541b-8588-84ecfb31b16c
ed7d6d6e-c30f-557f-9164-ddf8199312bd
d06694d7-ab32-5af0-bfdf-72f99451ed69
cae235c3-d1de-5b7a-b404-a6a9deb8b3e4
db14b663-bbde-52fb-a283-f543810990f5
a8b69ee0-b3e1-5ede-90fe-f16317dc5aca
```

# gemma4:31b
elapsed_second_request: 66.50s

advertisements,credential-theft,cybercriminal-services,fraud-scams,gaming,investment,money-laundering-cash-in-out,software,trading,vpn-proxies-anonymisation

raw output:
```
f106b5ec-d074-5f3f-8770-674e28ce5370
8b63ca37-afb4-5ee4-83fc-4eafd5ee19de
c49fdfa3-47c5-596f-a157-d14154315dc8
31b11b45-f5a8-5cb4-85ea-1594e2a06743
d9cc06cf-2e91-5d25-a343-ad23ca79061a
05451c34-d126-51b7-a5c4-669d4f9d3ed2
cae235c3-d1de-5b7a-b404-a6a9deb8b3e4
db14b663-bbde-52fb-a283-f543810990f5
d06694d7-ab32-5af0-bfdf-72f99451ed69
3a1d555e-252d-541b-8588-84ecfb31b16c
```

# gemma4:e4b
elapsed_second_request: 13.26s

banking,ponzi-financial-gain,services,social

raw output:
```
3281efa6-c734-5dc3-ba93-3c78c1184d37
a8b69ee0-b3e1-5ede-90fe-f16317dc5aca
805f2c9e-20d7-5532-baba-e2cb78fec1fb
2f8a51cb-86cf-5461-b403-8ad32d8503bc
```

# gpt-oss:120b
elapsed_second_request: 11.38s

advertisements,banking,cybercriminal-services,fraud-scams,gaming,investment,money-laundering-cash-in-out,services,trading

raw output:
```
05451c34-d126-51b7-a5c4-669d4f9d3ed2
a8b69ee0-b3e1-5ede-90fe-f16317dc5aca
db14b663-bbde-52fb-a283-f543810990f5
cae235c3-d1de-5b7a-b404-a6a9deb8b3e4
31b11b45-f5a8-5cb4-85ea-1594e2a06743
805f2c9e-20d7-5532-baba-e2cb78fec1fb
d9cc06cf-2e91-5d25-a343-ad23ca79061a
f106b5ec-d074-5f3f-8770-674e28ce5370
8b63ca37-afb4-5ee4-83fc-4eafd5ee19de
```

# granite4.1:30b
elapsed_second_request: 8.39s

carding,credential-dumps-data-leaks,money-laundering-cash-in-out,news

raw output:
```
1c7ba1cc-4ae4-5f42-8fdb-4c71995fc19b
31b11b45-f5a8-5cb4-85ea-1594e2a06743
0f09ad4b-fa8d-5a2c-ad73-c904dbd5e5a1
4614cc52-1711-57b8-a224-889a8bd327fc
```

# igorls/gemma4-e4b-classifier:q8_0
elapsed_second_request: 15.38s

carding,fraud-scams,ponzi-financial-gain,services,trading

raw output:
```
1c7ba1cc-4ae4-5f42-8fdb-4c71995fc19b
3281efa6-c734-5dc3-ba93-3c78c1184d37
8b63ca37-afb4-5ee4-83fc-4eafd5ee19de
a8b69ee0-b3e1-5ede-90fe-f16317dc5aca
d9cc06cf-2e91-5d25-a343-ad23ca79061a
```

# mistral-medium-3.5:latest
elapsed_second_request: 39.44s

credential-dumps-data-leaks,gaming,services,trading

raw output:
```
Based on the chat content analysis, I need to identify the most relevant label UUIDs from the allowed list. The channel appears to be a marketplace for various digital goods and services.

Looking at the messages:
- Multiple posts about selling game currencies (MLBB Diamonds, Robux, etc.)
- Posts about selling premium accounts (Spotify, Netflix, etc.)
- Posts about trading signals
- One post about bank logs/wires

The most relevant categories are:
1. **gaming** - for all the game currency and in-game item sales
2. **services** - for the account selling and other service offerings
3. **trading** - for the gold trading signals
4. **credential-dumps-data-leaks** - for the bank logs/wires post

Let me verify these UUIDs exist in the allowed list:
- f106b5ec-d074-5f3f-8770-674e28ce5370: gaming
- a8b69ee0-b3e1-5ede-90fe-f16317dc5aca: services
- d9cc06cf-2e91-5d25-a343-ad23ca79061a: trading
- 0f09ad4b-fa8d-5a2c-ad73-c904dbd5e5a1: credential-dumps-data-leaks

These are the most relevant labels. I should return them one per line.

f106b5ec-d074-5f3f-8770-674e28ce5370
a8b69ee0-b3e1-5ede-90fe-f16317dc5aca
d9cc06cf-2e91-5d25-a343-ad23ca79061a
0f09ad4b-fa8d-5a2c-ad73-c904dbd5e5a1
```

# mistral-small3.2:24b-instruct-2506-fp16
elapsed_second_request: 8.48s

crypto-crime,ddos,fraud-scams,hitman-assassination-services,money-laundering-cash-in-out

raw output:
```
Based on the chat content provided, here are the most relevant label UUIDs from the allowed list:

- 31b11b45-f5a8-5cb4-85ea-1594e2a06743: money-laundering-cash-in-out
- 3f25efba-2b8a-570f-92d1-6e39d8f2edff: ddos
- 4c474636-9e51-5f2d-b7ba-1e2fe6d3100f: crypto-crime
- 8b63ca37-afb4-5ee4-83fc-4eafd5ee19de: fraud-scams
- ecdb0119-317d-59a1-9b4b-433e845ab725: hitman-assassination-services
```

# nemotron-3-super:latest
elapsed_second_request: 60.31s

advertisements,credential-theft,education,gaming,trading

raw output:
```
d9cc06cf-2e91-5d25-a343-ad23ca79061a
f106b5ec-d074-5f3f-8770-674e28ce5370
ed7d6d6e-317d-59a1-9b4b-433e845ab725
db14b663-bbde-52fb-a283-f543810990f5
c49fdfa3-47c5-596f-a157-d14154315dc8
44666037-390d-5ee0-a4e8-426a88837828
```

# qwen3.5:122b
elapsed_second_request: 59.30s

carding,credential-theft,fraud-scams,gaming,investment,products

raw output:
```
1c7ba1cc-4ae4-5f42-8fdb-4c71995fc19b
c49fdfa3-47c5-596f-a157-d14154315dc8
8b63ca37-afb4-5ee4-83fc-4eafd5ee19de
f106b5ec-d074-5f3f-8770-674e28ce5370
ed7d6d6e-c30f-557f-9164-ddf8199312bd
05451c34-d126-51b7-a5c4-669d4f9d3ed2
```

# qwen3.6:35b
elapsed_second_request: 25.15s

advertisements,credential-theft,fraud-scams,investment,products

raw output:
```
ed7d6d6e-c30f-557f-9164-ddf8199312bd
db14b663-bbde-52fb-a283-f543810990f5
c49fdfa3-47c5-596f-a157-d14154315dc8
8b63ca37-afb4-5ee4-83fc-4eafd5ee19de
05451c34-d126-51b7-a5c4-669d4f9d3ed2
```
