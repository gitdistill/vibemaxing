---
description: The argument provided to aMaxobjListenercallback function.
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/maxobjlistenerdata/
title: class MaxobjListenerData
---

# class MaxobjListenerData
The argument provided to a [MaxobjListener](https://docs.cycling74.com/apiref/js/maxobjlistener/ "MaxobjListener") callback function.
## Properties
### attrname string | undefined read-only
If the [MaxobjListener](https://docs.cycling74.com/apiref/js/maxobjlistener/ "MaxobjListener") is observing an attribute, the attributes name, otherwise undefined
### listener [MaxobjListener](https://docs.cycling74.com/apiref/js/maxobjlistener/ "MaxobjListener") read-only
The [MaxobjListener](https://docs.cycling74.com/apiref/js/maxobjlistener/ "MaxobjListener") which called the function
### maxobject [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") read-only
The [Maxobj](https://docs.cycling74.com/apiref/js/maxobj/ "Maxobj") being observed
### value number | number[] | string read-only
The current value of the observed object or attribute
