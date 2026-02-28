---
description: A listener for changes in aJitterObject.
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/jitterlistener/
title: class JitterListener
---

# class JitterListener
A listener for changes in a [JitterObject](https://docs.cycling74.com/apiref/js/jitterobject/ "JitterObject").
#### Example
```
var recv = new JitterObject("jit.net.recv");
var mylistener = new JitterListener(recv.getregisteredname(), callbackfun);

function callbackfun(event) {
    if (event.eventname == "matrix_received") {
        matrixoutput(event.args[0]);
    } else if (event.eventname == "message_received") {
        messageoutput(event.args[0]);
    } else if (event.eventname == "connected_notification") {
        connectedoutput();
    }
}
callbackfun.local = 1;

```

## Constructors
```
new JitterListener(objectName: string, callback: Function);

```

Constructs a new instance of the `JitterListener` class
Parameter | Type | Description  
---|---|---  
objectName | string | name of the object to listen to  
callback | Function | a function called when a change occurs to the listened-to object which takes a [JitterEvent](https://docs.cycling74.com/apiref/js/jitterevent/ "JitterEvent")  
## Properties
### function Function read-only
The callback function to handle the [JitterEvent](https://docs.cycling74.com/apiref/js/jitterevent/ "JitterEvent")
### object [JitterObject](https://docs.cycling74.com/apiref/js/jitterobject/ "JitterObject") read-only
The object being listened to
### subjectname string read-only
Name of the object being listened to
