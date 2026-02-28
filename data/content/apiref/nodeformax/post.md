---
description: Post to the Max console. Setting the last argument to a value of maxAPI.POST_LEVELS allows control of the log level
group: nodeformax
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/nodeformax/post/
title: function post
---

# function post
Post to the Max console. Setting the last argument to a value of maxAPI.POST_LEVELS allows control of the log level
```
export function post(...args: Array<Anything | POST_LEVELS>): Promise<void>;

```
Name | Type | Description  
---|---|---  
args | Array<[Anything](https://docs.cycling74.com/apiref/nodeformax/anything/ "Anything") | [POST_LEVELS](https://docs.cycling74.com/apiref/nodeformax/post_levels/ "POST_LEVELS")> |   
Return Value | Promise<void> | 
