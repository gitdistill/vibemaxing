---
description: A container for results obtained in anSQLite.exec()call.
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/sqlresult/
title: class SQLResult
---

# class SQLResult
A container for results obtained in an [SQLite.exec()](https://docs.cycling74.com/apiref/js/sqlite/#exec "SQLite.exec\(\)") call.
Not every [SQLite.exec()](https://docs.cycling74.com/apiref/js/sqlite/#exec "SQLite.exec\(\)") call will produce results, but any database query (`SELECT` in particular) will generate an [SQLResult](https://docs.cycling74.com/apiref/js/sqlresult/ "SQLResult") object even if the result is empty.
## Constructors
```
new SQLResult();

```

Constructs a new instance of the `SQLResult` class
## Methods
### fieldname
Get the fieldname of a column at a given index
```
fieldname(index: number): string;

```
Name | Type | Description  
---|---|---  
index | number | column index  
Return Value | string | the name of the column  
### numfields
Get the number of fields in the dataset returned in the [SQLResult](https://docs.cycling74.com/apiref/js/sqlresult/ "SQLResult") object
```
numfields(): number;

```
Name | Type | Description  
---|---|---  
Return Value | number | the number of fields  
### numrecords
Get the number of records were returned in the [SQLResult](https://docs.cycling74.com/apiref/js/sqlresult/ "SQLResult") object
```
numrecords(): number;

```
Name | Type | Description  
---|---|---  
Return Value | number | the number of records  
### value
Get the value of a record at a column index and record number
```
value(index: number, record_no: number): number | string;

```
Name | Type | Description  
---|---|---  
index | number | column index  
record_no | number | record number  
Return Value | number | string | the value of the record  
#### Example
```
function print_everything(sqlres) {
    var numrecs = sqlres.numrecords()
    var numflds = sqlres.numfields()

    var field_names = new Array()
    for (var i = 0; i < numflds; i++) {
        field_names[i] = sqlres.fieldname(i)
    }

    for (var i = 0; i < numrecs; i++) {
        for (var j = 0; j < numflds; j++) {
            post(
                "Rec: ",
                i,
                " field ",
                field_names[j],
                " value ",
                sqlres.value(j, i),
                "\n"
            )
        }
    }
}

```

