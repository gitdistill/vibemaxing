---
description: XMLHttpRequest provides HTTP client functionality for making network requests from JavaScript in Max.
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/xmlhttprequest/
title: class XMLHttpRequest
---

# class XMLHttpRequest
XMLHttpRequest provides HTTP client functionality for making network requests from JavaScript in Max.
XMLHttpRequest implements a subset of the web standard XMLHttpRequest API, allowing you to make HTTP requests to fetch data from servers. This implementation is based on the Max `maxurl` object and supports asynchronous requests only.
The readyState property indicates the current state of the request: - 0 (UNSENT): open() has not been called yet - 1 (OPENED): send() has not been called yet - 2 (HEADERS_RECEIVED): send() has been called, and headers and status are available - 3 (LOADING): Downloading; responseText holds partial data - 4 (DONE): The operation is complete
#### Example
```
var req = new XMLHttpRequest();
req.open("GET", "https://api.example.com/data");
req.onreadystatechange = function() {
    if (this.readyState == 4) {
        post("Response: " + this.responseText + "\n");
    }
};
req.send();

```

## Properties
### onabort ((this: [XMLHttpRequest](https://docs.cycling74.com/apiref/js/xmlhttprequest/ "XMLHttpRequest")) => void) | null
Event handler called when the request is aborted.
This behavior is only available in the new v8 javascript engine objects.
### onerror ((this: [XMLHttpRequest](https://docs.cycling74.com/apiref/js/xmlhttprequest/ "XMLHttpRequest"), event: [ProgressEvent](https://docs.cycling74.com/apiref/js/progressevent/ "ProgressEvent")) => void) | null
Event handler called when the request encounters a network error.
This behavior is only available in the new v8 javascript engine objects.
#### Example
```
req.onerror = function(event) {
    post("Network error occurred\n");
};

```

### onload ((this: [XMLHttpRequest](https://docs.cycling74.com/apiref/js/xmlhttprequest/ "XMLHttpRequest")) => void) | null
Event handler called when the request successfully completes.
This behavior is only available in the new v8 javascript engine objects.
#### Example
```
req.onload = function() {
    if (this.status == 200) {
        post("Success: " + this.responseText + "\n");
    } else {
        post("Error: " + this.status + "\n");
    }
};

```

### onloadend ((this: [XMLHttpRequest](https://docs.cycling74.com/apiref/js/xmlhttprequest/ "XMLHttpRequest")) => void) | null
Event handler called when the request finishes, regardless of success or failure.
This behavior is only available in the new v8 javascript engine objects.
### onloadstart ((this: [XMLHttpRequest](https://docs.cycling74.com/apiref/js/xmlhttprequest/ "XMLHttpRequest")) => void) | null
Event handler called when the request starts loading data.
This behavior is only available in the new v8 javascript engine objects.
### onprogress ((this: [XMLHttpRequest](https://docs.cycling74.com/apiref/js/xmlhttprequest/ "XMLHttpRequest"), event: [ProgressEvent](https://docs.cycling74.com/apiref/js/progressevent/ "ProgressEvent")) => void) | null
Event handler called periodically as data is received.
This behavior is only available in the new v8 javascript engine objects.
#### Example
```
req.onprogress = function(event) {
    post("Progress: " + event.loaded + " / " + event.total + "\n");
};

```

### onreadystatechange ((this: [XMLHttpRequest](https://docs.cycling74.com/apiref/js/xmlhttprequest/ "XMLHttpRequest")) => void) | null
Event handler called whenever the readyState property changes.
#### Example
```
req.onreadystatechange = function() {
    post("readyState: " + this.readyState + "\n");
};

```

### ontimeout ((this: [XMLHttpRequest](https://docs.cycling74.com/apiref/js/xmlhttprequest/ "XMLHttpRequest")) => void) | null
Event handler called when the request times out.
This behavior is only available in the new v8 javascript engine objects.
### readyState number read-only
The current state of the request. See for state values.
### responseText string read-only
The response body as a string. Only text responses are currently supported.
### responseType string
The response type. Currently only "text" is supported.
### status number read-only
The HTTP status code of the response (e.g., 200, 404, 500). A value of 0 indicates that the request has not completed or encountered an error.
### statusText string read-only
The HTTP status text of the response (e.g., "OK", "Not Found").
### timeout number
The timeout for the request in milliseconds. Set to 0 for no timeout.
### withCredentials boolean
Whether to include credentials (cookies, authorization headers) in cross-origin requests. Currently not fully implemented.
## Methods
### _getResponseKey
Gets a Max-specific response key from the underlying maxurl object.
This is a Max-specific extension that allows access to maxurl response data not exposed by the standard XMLHttpRequest API. Common keys include: `content_type`, `total_time`, `size_download`, `filename_out`.
```
_getResponseKey(key: string): string;

```
Name | Type | Description  
---|---|---  
key | string | The key name  
Return Value | string | The value associated with the key, or an empty string if not found  
#### Example
```
req.onreadystatechange = function() {
    if (this.readyState == 4) {
        post("Content-Type: " + this._getResponseKey("content_type") + "\n");
        post("Total Time: " + this._getResponseKey("total_time") + "\n");
    }
};

```

### _setRequestKey
Sets a Max-specific request key for the underlying maxurl object.
This is a Max-specific extension that allows access to maxurl features not part of the standard XMLHttpRequest API. For example, you can use this to set the `filename_out` key to save the response directly to a file.
```
_setRequestKey(key: string, value: string): void;

```
Name | Type | Description  
---|---|---  
key | string | The key name  
value | string | The value to set  
#### Example
```
req.open("GET", "https://cycling74.com");
req._setRequestKey("filename_out", "~/Desktop/download.html");
req.send();

```

### abort
Aborts the request if it is still in progress.
After calling abort(), the readyState will be set to UNSENT (0), and the onabort handler will be called if one is set.
```
abort(): void;

```

#### Example
```
req.abort();

```

### getAllResponseHeaders
Gets all response headers as a single string.
```
getAllResponseHeaders(): string;

```
Name | Type | Description  
---|---|---  
Return Value | string | A string containing all response headers, separated by newlines, or an empty string if no headers are available  
#### Example
```
var headers = req.getAllResponseHeaders();
post("Headers:\n" + headers + "\n");

```

### getResponseHeader
Gets the value of a specific response header.
```
getResponseHeader(name: string): string;

```
Name | Type | Description  
---|---|---  
name | string | The name of the header to retrieve  
Return Value | string | The header value, or an empty string if not found  
#### Example
```
var contentType = req.getResponseHeader("Content-Type");
post("Content-Type: " + contentType + "\n");

```

### open
Initializes a request.
```
open(method: string, url: string, async?: boolean, username?: string, password?: string): void;

```
Name | Type | Description  
---|---|---  
method | string | The HTTP method (e.g., "GET", "POST", "PUT", "DELETE")  
url | string | The URL to request  
_optional_ async | boolean | Whether the request should be asynchronous (currently ignored, always async)  
_optional_ username | string | Optional username for HTTP authentication  
_optional_ password | string | Optional password for HTTP authentication  
#### Example
```
req.open("GET", "https://api.example.com/data");
req.open("POST", "https://api.example.com/submit", true);
req.open("GET", "https://api.example.com/data", true, "user", "pass");

```

### overrideMimeType
Overrides the MIME type of the response.
Must be called before .
```
overrideMimeType(mimeType: string): void;

```
Name | Type | Description  
---|---|---  
mimeType | string | The MIME type to use  
#### Example
```
req.open("GET", "https://api.example.com/data");
req.overrideMimeType("text/plain");
req.send();

```

### send
Sends the request.
```
send(body?: string): void;

```
Name | Type | Description  
---|---|---  
_optional_ body | string | Optional request body (for POST, PUT, etc.). If provided as a string, it will be sent as the request body.  
#### Example
```
req.open("POST", "https://api.example.com/submit");
req.setRequestHeader("Content-Type", "application/json");
req.send('{"key": "value"}');

```

### setRequestHeader
Sets a request header.
Must be called after but before .
```
setRequestHeader(name: string, value: string): void;

```
Name | Type | Description  
---|---|---  
name | string | The header name  
value | string | The header value  
#### Example
```
req.open("POST", "https://api.example.com/submit");
req.setRequestHeader("Content-Type", "application/json");
req.setRequestHeader("Authorization", "Bearer token123");
req.send(data);

```

