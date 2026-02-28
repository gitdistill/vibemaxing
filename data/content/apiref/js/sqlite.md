---
description: Provides access to the SQLite database system.
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/sqlite/
title: class SQLite
---

# class SQLite
Provides access to the SQLite database system.
A companion object, [SQLResult](https://docs.cycling74.com/apiref/js/sqlresult/ "SQLResult"), is required for most database operations.
## Constructors
```
new SQLite();

```

Constructs a new instance of the `SQLite` class
All future calls to the database will be through this instance of the object.
## Methods
### begintransaction
Start an SQL transaction on the database
This allows you to batch database updates and to roll back sets of changes if they do not all complete. When you are done with batch updates, a call to [SQLite.endtransaction()](https://docs.cycling74.com/apiref/js/sqlite/#endtransaction "SQLite.endtransaction\(\)") should be executed.
```
begintransaction(): void;

```

### close
Close a previously opened SQLite database
```
close(): void;

```

### endtransaction
Complete a transaction and flush all database writes to the file
```
endtransaction(): void;

```

### exec
Perform an SQL command on the database
This command must be in standard SQL language syntax, limited to the operations that SQLite supports.
```
exec(command: string, result: SQLResult): number;

```
Name | Type | Description  
---|---|---  
command | string | SQL command  
result | [SQLResult](https://docs.cycling74.com/apiref/js/sqlresult/ "SQLResult") | SQLResult object to populate with transaction results  
Return Value | number | an error code if unsuccessful or zero if the call results in a completed operation  
#### Example
```
var res = new SQLResult;
var rtn = sqlite.exec(“CREATE TABLE Persons (PersonID INTEGER, LastName TEXT, FirstName TEXT);”, res);

```

### open
Open an SQLite-format file for database operations
```
open(filename: string, on_disk?: number, must_exist?: number): number;

```
Name | Type | Description  
---|---|---  
filename | string | File to access  
_optional_ on_disk | number | If the file should be memory-based (0) or disk-based (1)  
_optional_ must_exist | number | If non-zero, requires the file to exist to be opened, otherwise, a file will be created if one does not exist.  
Return Value | number | an error code if unsuccessful or zero if the call results in an opened database
