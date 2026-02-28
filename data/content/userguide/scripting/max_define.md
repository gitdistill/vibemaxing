---
description: Use the define message to Max to create macros that create top-level objects out of specific object configurations
group: Scripting
kind: guide
section: User Guide
sourceUrl: https://docs.cycling74.com/userguide/max_define/
title: The define Message
---

# The define Message
The **define** message to the `max` object (see [Controlling Max with Messages](https://docs.cycling74.com/userguide/controlling_max_with_messages/)) lets you declare an object that loads a file of code for one of Max's powerful supported language-based objects: JavaScript ([v8](https://docs.cycling74.com/reference/v8/ "v8")), Gen, and [jit.gl.slab](https://docs.cycling74.com/reference/jit.gl.slab "jit.gl.slab").
Once defined the object can have its own help file and reference page and will appear in object box autocompletion.
The define message was used to create the **jit.fx** series of shader-based effects using a combination of [v8](https://docs.cycling74.com/reference/v8/ "v8") and [jit.gl.slab](https://docs.cycling74.com/reference/jit.gl.slab "jit.gl.slab").
## Using define
### Text Substitution
For this example we are including the leading semicolon needed if you are entering a message to max in a message box. Later when you create a text file with your defines in it, you will omit the leading semicolon.
Suppose you have a JavaScript file called mycode.js. Here's how you can use the define message so that merely typing mycode will create a [v8](https://docs.cycling74.com/reference/v8/ "v8") object with `mycode.js` as an argument.
`; max define mycode v8 mycode.js`
The word after `define` is the name of the object you'll type into an object box, in this case `mycode`. Everything after that will become the actual contents of the object box, but it's not substituted for the text you type in; instead it's hidden in the background.
### Arguments
Any arguments you type after the defined object name will be appended after the specified subtitution text. For example, if you typed `mycode 1 2 3` the resulting object box (which remains a secret) contains `v8 mycode.js 1 2 3`.
### Typed-in Attribute Handling
It's also possible to specify preset values for typed-in attributes. To continue with our JavaScript example, imagine that mycode.js declares two attributes:
```

declareattribute("attr1");
declareattribute("attr2");
declareattribute("attr3");


```

You can set the initial values for any of these attributes as part of your define.
`; max define mycode v8 mycode.js @attr1 25 @attr2 freedie`
If the user of your define also adds arguments to their use of the define, those are substituted after the arguments in the define (in this case, `mycode.js`) but _before_ the typed-in attribute values. With the above define, `mycode 1 2 3` would produce `v8 mycode.js 1 2 3 @attr1 25 @attr2 freddie`
Finally, if the user of your define includes typed-in attributes, those are placed at the very end. And, if they supply values for attributes already in the define, the user's attribute values are used instead of the ones in the define. As an example, if the user enters `mycode 1 2 3 @attr3 1000` the resulting object will be created with `v8 mycode.js 1 2 3 @attr1 25 @attr2 freddie @attr3 1000`. And if the user enters `mycode 1 2 3 @attr1 50 @attr3 1000` the result will be `v8 mycode.js 1 2 3 @attr1 50 @attr2 freddie @attr3 1000`.
For Gen, typed-in attributes set the initial values of Gen **param** objects.
### Inspector Behavior
In order to put the focus on the settings the user can change, Gen, [v8](https://docs.cycling74.com/reference/v8/ "v8"), and [jit.gl.slab](https://docs.cycling74.com/reference/jit.gl.slab "jit.gl.slab") hide certain attributes in the inspector when you are using a define. For example, you typically can't read in a different file.
## Recovering the Original
To recover the original object and arguments used to create an object using define, use the Object Action Menu and Transform > **Convert Define to Arguments**.
![](https://docs.cycling74.com/images/8907c84e5a2b6f6aa965bb52136767ba_417.webp)
As an example, after using Convert Define to Arguments, the [jit.fx.threshold](https://docs.cycling74.com/reference/jit.fx.threshold "jit.fx.threshold") object becomes a [jit.gl.slab](https://docs.cycling74.com/reference/jit.gl.slab "jit.gl.slab") hosting the shader file `jit.fx.threshold.jxs`.
![](https://docs.cycling74.com/images/4f6ed9a75cea2ec030f5a17c00498928_271.webp)
## Storing Your define in a Package
Currently, the best way to create permanent access to a define is to use packages. Here is the recommended folder structure for a package that uses this feature:
```
package_folder/
├── init/
│   └── text file with max define messages
└── code/
    ├── JavaScript files
    ├── Shader files
    └── Gen files

```

The text file that will be stored in the init folder should end in `.txt`. Omit the leading semicolon required by the message box but include a trailing semicolon at the end of your message.
```

max define mycode v8 mycode.js @attr1 25 @attr2 freedie;
max define yourcode v8 yourcode.js;


```

After your package is assembled, copy it into the Max Packages folder. To test, relaunch Max, wait for the database to rebuild (as indicated in the left toolbar) and try typing your define into an object box. It should be displayed in autocompletion after typing the first two or three characters.
