---
description: Bind to a Maxdictobject.
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/dict/
title: class Dict
---

# class Dict
Bind to a Max `dict` object.
The Dict object lets you access structured data (a dictionary) associated with a name. If there is a named `dict` object in Max, it will share its contents with the JavaScript [Dict](https://docs.cycling74.com/apiref/js/dict/ "Dict") object of the same name.
## Constructors
```
new Dict(name?: string);

```

Create a named dictionary
If no name is provided as an argument then a unique name will be generated for the dictionary.
Parameter | Type | Description  
---|---|---  
_optional_ name | string | name of the dictionary  
## Properties
### name string
The name of the dictionary
### quiet boolean
Suppresses many errors or warnings if set to true
## Methods
### append
Add values to the associated data
Add values to the end of an array associated with the specified key.
```
append(key: string, ...values: any[]): void;

```
Name | Type | Description  
---|---|---  
key | string | the entry key  
values | any[] |   
### clear
Erase the contents of the dictionary, restoring to a clean state.
```
clear(): void;

```

### clone
Copy the named dictionary into this dictionary
```
clone(name: string): void;

```
Name | Type | Description  
---|---|---  
name | string | name of the dictionary to copy  
#### Example
```
var d1 = new Dict("one");
var d2 = new Dict("two");

d1.clone("two"); // Copies the dictionary named "two" into d1

```

### contains
Return a 0 or 1 indicating the specified key exists (or doesn't) in the dictionary.
```
contains(key: string): number;

```
Name | Type | Description  
---|---|---  
key | string | name of the key to lookup  
Return Value | number |   
### export_json
Write a file in the JSON format.
```
export_json(filename: string): void;

```
Name | Type | Description  
---|---|---  
filename | string | Name of the file to read  
### export_yaml
Write a file in the YAML format.
```
export_yaml(filename: string): void;

```
Name | Type | Description  
---|---|---  
filename | string | Name of the file to read  
### freepeer
Free the native C peer
Frees the dictionary data from the native C peer (created when making a [Dict](https://docs.cycling74.com/apiref/js/dict/ "Dict") object), which is not considered by the JavaScript garbage collector, and may consume lots of memory until the garbage collector decides to run based JS allocated memory. Once called, the [Dict](https://docs.cycling74.com/apiref/js/dict/ "Dict") object is not available for any other use. It's not necessary to call this function, as the memory will be freed eventually, but you can call it whenever you're done with your [Dict](https://docs.cycling74.com/apiref/js/dict/ "Dict") object.
```
freepeer(): void;

```

### get
Return the value associated with a key.
```
get(key: string): any;

```
Name | Type | Description  
---|---|---  
key | string | lookup key  
Return Value | any |   
### getkeys
Return a list of all the keys in a dictionary, or null if the dictionary contains no keys.
```
getkeys(): string[] | null;

```
Name | Type | Description  
---|---|---  
Return Value | string[] | null |   
### getnames
List of all named dictionaries.
Return a list of all the dictionary names that are known to Max.
```
getnames(): string[];

```
Name | Type | Description  
---|---|---  
Return Value | string[] |   
### getsize
Length of the array of values associated with a key.
```
getsize(key: string): number;

```
Name | Type | Description  
---|---|---  
key | string | The key to look up  
Return Value | number |   
### gettype
Type of the value or values associated with a key.
```
gettype(key: string): string;

```
Name | Type | Description  
---|---|---  
key | string | The key to look up  
Return Value | string |   
### import_json
Read a file in the JSON format.
```
import_json(filename: string): void;

```
Name | Type | Description  
---|---|---  
filename | string | Name of the file to read  
### import_yaml
Read a file in the YAML format.
```
import_yaml(filename: string): void;

```
Name | Type | Description  
---|---|---  
filename | string | Name of the file to read  
### parse
Parse a serialized dictionary and replace contents
Replaces the contents of the dictionary by parsing a dictionary serialization. Understands JSON and [Max Dictionary Syntax](https://docs.cycling74.com/userguide/dictionaries/#abbreviated-dictionary-syntax "Max Dictionary Syntax")
```
parse(serialization: string): void;

```
Name | Type | Description  
---|---|---  
serialization | string | serialized dictionary string  
### pull_from_coll
Pull data from a named `coll` object
Adds entries to the dictionary by pulling rows from the given `coll` object. Does not clear existing keys from the dictionary.
```
pull_from_coll(coll_name: string): void;

```
Name | Type | Description  
---|---|---  
coll_name | string | name of the `coll` object in Max  
### push_to_coll
Pull data into a named `coll` object
Push the dictionary's content into a named `coll` object. The keys in the dictionary will become the indices in the `coll`, and the values for those indices the values of the dictionary's keys.
```
push_to_coll(coll_name: string): void;

```
Name | Type | Description  
---|---|---  
coll_name | string | name of the `coll` object in Max  
### readany
Loads the contents of a file.
Replaced the contents of the dictionary, clearing existing keys. Accepts JSON and YAML files.
```
readany(filename: string): void;

```
Name | Type | Description  
---|---|---  
filename | string | name of the file to load  
### remove
Remove a key and its associated value from the dictionary.
```
remove(key: string): void;

```
Name | Type | Description  
---|---|---  
key | string | the key to remove  
### replace
Set the value for a key to a specified value, creating a nested dicts if necessary.
Unlike [Dict.set()](https://docs.cycling74.com/apiref/js/dict/#set "Dict.set\(\)"), this function will create a hierarchical path to a given value if one does not already exist.
```
replace(key: string, ...value: any[]): void;

```
Name | Type | Description  
---|---|---  
key | string | The key or path to a dictionary entry  
value | any[] | The value or values to store at that path  
#### Example
```
var d = new Dict(); // empty dictionary
d.replace("first::second::third", 42);
post(d.get("first").get("second").get("third")); // 42

```

### set
Set the value for a key to a specified value.
Unlike [Dict.replace()](https://docs.cycling74.com/apiref/js/dict/#replace "Dict.replace\(\)"), will not create nested dictionaryies if the nested structure does not already exist.
```
set(key: string, ...value: any[]): void;

```
Name | Type | Description  
---|---|---  
key | string | The key or path to a dictionary entry  
value | any[] | The value or values to store at that path  
### setparse
Set the value for a key using a serialized dictionary
The serialization can be formatted as JSON or as [Max Dictionary Syntax](https://docs.cycling74.com/userguide/dictionaries/#abbreviated-dictionary-syntax "Max Dictionary Syntax")
```
setparse(key: string, serialization: string): void;

```
Name | Type | Description  
---|---|---  
key | string | The key or path to a dictionary entry  
serialization | string | Will be parsed to a dictionary and added to the Dict  
### stringify
Return the content of the dictionary as a JSON string.
```
stringify(): string;

```
Name | Type | Description  
---|---|---  
Return Value | string |   
### writeagain
Open a save dialog to write the dictionary contents to a file.
```
writeagain(): void;

```

