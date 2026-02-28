---
description: A function that can be scheduled or repeated.
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/task/
title: class Task
---

# class Task
A function that can be scheduled or repeated.
Although the overall timing accuracy of a [Task](https://docs.cycling74.com/apiref/js/task/ "Task") function is high, the latency between the scheduled time and the actual execution time of a [Task](https://docs.cycling74.com/apiref/js/task/ "Task") function is variable because the function runs in a low-priority thread. Therefore, you should avoid using a [Task](https://docs.cycling74.com/apiref/js/task/ "Task") function in a time-critical operation.
For convenience, a [Task](https://docs.cycling74.com/apiref/js/task/ "Task") object is a property of the function executed in a [Task](https://docs.cycling74.com/apiref/js/task/ "Task"). To access the [Task](https://docs.cycling74.com/apiref/js/task/ "Task") from within its function, use the following syntax:
```
arguments.callee.task

```

#### Example
```
function ticker(a, b, c) {
    post("tick")
}

args = new Array(3)
args[0] = 1
args[1] = 2
args[2] = 3
t = new Task(ticker, this, args)

```

## Constructors
```
new Task(fn: Function, obj?: object, args?: any[]);

```

Constructs a new instance of the `Task` class
Parameter | Type | Description  
---|---|---  
fn | Function | the function to execute  
_optional_ obj | object | the `this` during the execution of the function  
_optional_ args | any[] | the arguments to pass to `fn`  
## Properties
### arguments any[]
The arguments passed to the task's executing function
### function Function
The function executed in the [Task](https://docs.cycling74.com/apiref/js/task/ "Task"). You can change this within the task function itself.
### interval number
The time in milliseconds between repeats of the task function. The default interval is 500 ms.
#### Example
This example will cause the task to run 10% slower each time the function is called.
```
function taskfun() {
    var intv = arguments.callee.task.interval
    arguments.callee.task.interval = intv + intv * 0.1
}

```

### iterations number read-only
The number of times the task function has been called.
Outside of a task function, the value of iteration is always 0. The value resets each time the task is started (using the [Task.repeat()](https://docs.cycling74.com/apiref/js/task/#repeat "Task.repeat\(\)"), [Task.execute()](https://docs.cycling74.com/apiref/js/task/#execute "Task.execute\(\)"), or [Task.schedule()](https://docs.cycling74.com/apiref/js/task/#schedule "Task.schedule\(\)") methods).
### object object
The object assigned to be the `this` in the task function. Most often this will be your `jsthis` object, so you can, for example, access the `outlet()` method. You set up your `jsthis` object to be the `this` by creating a task with the keyword `this` as the first argument.
#### Example
```
arguments.callee.task.object.outlet(1, "bang")
outlet(1, "bang")
this.outlet(1, "bang")

```

### running boolean read-only
Whether the [Task](https://docs.cycling74.com/apiref/js/task/ "Task") is running or not. Within a function executing within a task, this will always be true.
### valid boolean
Whether the [Task](https://docs.cycling74.com/apiref/js/task/ "Task") object has been invalidated and is awaiting garbage collection. An invalid object will no longer respond to the [Task.execute()](https://docs.cycling74.com/apiref/js/task/#execute "Task.execute\(\)") or [Task.schedule()](https://docs.cycling74.com/apiref/js/task/#schedule "Task.schedule\(\)") methods.
## Methods
### cancel
If a task is scheduled or repeating, cancel any future executions. This method can be used within a task function for a self-cancelling [Task](https://docs.cycling74.com/apiref/js/task/ "Task").
```
cancel(): void;

```

#### Example
The following is a task function that will run only once, even if it is started using the [Task.repeat()](https://docs.cycling74.com/apiref/js/task/#repeat "Task.repeat\(\)") function.
```
function once() {
    arguments.callee.task.cancel()
}

```

### execute
Run the task once, right now. Equivalent to calling the task function with its arguments.
```
execute(): void;

```

### freepeer
Invalidate the [Task](https://docs.cycling74.com/apiref/js/task/ "Task") and make it available for garbage collection by the JS engine.
[Task](https://docs.cycling74.com/apiref/js/task/ "Task") objects persist beyond their code scope (otherwise, the object could be garbage collected before its scheduled function is called). The user is responsible for invalidating the [Task](https://docs.cycling74.com/apiref/js/task/ "Task") when it is no longer in use. All [Task](https://docs.cycling74.com/apiref/js/task/ "Task")s (valid or invalid) will be garbage collected and freed when the parent JS object reloads its script or is itself freed.
```
freepeer(): void;

```

#### Example
```
function bang() {
    var tsk = new Task(cb) // Task will not be freed when the bang() function returns
    tsk.schedule(200)
}

function cb() {
    post("right on schedule!\n")
    arguments.callee.task.freepeer() // ensure that the caller can be GC'd
}

```

### repeat
Repeat a task function
```
repeat(n?: number, initialdelay?: number): void;

```
Name | Type | Description  
---|---|---  
_optional_ n | number | Number of repetitions. If none is provided, the task repeats until cancelled.  
_optional_ initialdelay | number | Delay in milliseconds until the first iteration  
#### Example
```
function repeater_function() {
    post(arguments.callee.task.iterations)
}

tsk = new Task(repeater_function, this)
tsk.interval = 1000 // every second
tsk.repeat(3) // do it 3 times

```

### schedule
Run the task once, with a delay.
```
schedule(delay?: number): void;

```
Name | Type | Description  
---|---|---  
_optional_ delay | number | Time in milliseconds before the task function will be executed
