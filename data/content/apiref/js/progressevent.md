---
description: ProgressEvent provides information about the progress of a network request.
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/progressevent/
title: class ProgressEvent
---

# class ProgressEvent
ProgressEvent provides information about the progress of a network request.
ProgressEvent objects are passed to progress-related event handlers such as and . They contain information about the amount of data that has been loaded and the total amount expected.
#### Example
```
var req = new XMLHttpRequest();
req.onprogress = function(event) {
    post("loaded: " + event.loaded + " of " + event.total + "\n");
};

```

## Properties
### lengthComputable boolean read-only
Whether the total size of the transfer is known
### loaded number read-only
The number of bytes that have been loaded
### total number read-only
The total number of bytes expected to be loaded
