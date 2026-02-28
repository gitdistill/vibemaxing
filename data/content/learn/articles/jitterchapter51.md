---
description: Jitter Java
group: Jitter Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/jitterchapter51/
title: Jitter Tutorial 51
---

Download Series Content and Patchers
# Tutorial 51: Jitter Java
This tutorial assumes that the reader is familiar with the process of programming [mxj](https://docs.cycling74.com/reference/mxj/ "mxj") Java classes. The details for how this is done are contained in the _Writing Max Externals in Java_ document.
In this Tutorial we'll outline how [mxj](https://docs.cycling74.com/reference/mxj/ "mxj") classes can operate directly on the cells of an input matrix. We also will see how to create classes in the Java programming language that internally load Jitter objects and define and execute a processing network. Finally, we will learn how to design hardware-accelerated user interface elements by attaching a "listener" to a drawing context and polling a window for mouse events.
The Jitter Java API centers around the **JitterObject** class, which provides a way for [mxj](https://docs.cycling74.com/reference/mxj/ "mxj") classes to instantiate Jitter objects. The following line of code creates a [jit.op](https://docs.cycling74.com/reference/jit.op "jit.op") Jitter object.
```
JitterObject jo = new JitterObject("jit.op");

```

We can send messages to objects in our Java code by using JitterObject's call() or send() methods. For instance, we might set the operator in the above instance of jit.op as follows:
```
jo.send("op", "+");

```

We could alternatively set this attribute using the setAttr() method:
```
jo.setAttr("op","+");

```

The **JitterMatrix** class extends JitterObject – after all, [jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix") is a Jitter Object. Since [jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix") is such a common object it is handy to have convenience methods dedicated to its creation and destruction. For instance, the below line of code creates a new `4` -plane JitterMatrix of type `char` and dimensions `320` by 240.
```
JitterMatrix jm = new JitterMatrix(4, "char", 320, 240);

```

We can also create a JitterMatrix object by specifying the matrix `name` :
```
JitterMatrix jm = new JitterMatrix("Stanley");

```

If a [jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix") object named `Stanley` already exists, this Java peer JitterMatrix object will refer to it. In this case a new [jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix") object is not created.
Conveniences are nice, but the primary reason the JitterMatrix class exists is to provide native methods to access the data in the matrix cells. We'll see an example of this in action when we open the tutorial patch.
## Accessing an Input Matrix
  * Open the tutorial patch `51jJava` in the Jitter Tutorials folder. Double-click on the `matrix info` subpatcher. Click on the [button](https://docs.cycling74.com/reference/button/ "button") object and look at the output in the Max console.

![Information about our matrix printed in the Max console.](https://docs.cycling74.com/images/5b78a1ad3a4056a73a86e8f5c2c7df2b_506.webp) Information about our matrix printed in the Max console.
In this subpatcher, clicking on the [button](https://docs.cycling74.com/reference/button/ "button") object causes the [jit.noise](https://docs.cycling74.com/reference/jit.noise "jit.noise") object to send a `4` plane `64` by `48``float32` matrix into an [mxj](https://docs.cycling74.com/reference/mxj/ "mxj") object with the _j51matrixinfoexample_ class loaded. This Java class sends some basic information about the input matrix out its outlet. Let's examine the code for the class:
```
import com.cycling74.max.*;
import com.cycling74.jitter.*;

public class j51matrixinfoexample extends MaxObject {

   public void jit_matrix(String s)
   {
     JitterMatrix jm = new JitterMatrix(s);

     outlet(0,"name", jm.getName());
     outlet(0,"planecount", jm.getPlanecount());
     outlet(0,"type", jm.getType());
     outlet(0,"dim", jm.getDim());
   }
}

```

The class consists of a single jit_matrix method. Of course since matrices are passed between Jitter objects as named references, we think of a matrix being input as just a simple two element list, and this is how [mxj](https://docs.cycling74.com/reference/mxj/ "mxj") sees it. The argument of the jit_matrix message is of course the matrix `name`, so the first thing our method does is create a new JitterMatrix object with the `name` of the input matrix as the constructor's only argument. The JitterMatrix object that is created will have that named [jit.matrix](https://docs.cycling74.com/reference/jit.matrix "jit.matrix") object as its peer. The next four lines of code simply output the results of some basic queries that can be made using the methods of the JitterMatrix class.
## Operating on a Matrix
  * Close the `matrix info` subpatcher. Open the `striper` subpatcher.


The `striper` subpatcher gives us an example of a class that operates on the data of an input matrix. Note that there are two classes set up to be used, with a[Ggate](https://docs.cycling74.com/reference/gswitch2/) object allowing us to switch between them; we will be comparing two different ways of performing the same operation to see which is more efficient.
  * Click on the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") box to start the [qmetro](https://docs.cycling74.com/reference/qmetro/ "qmetro") object.

![A "striping" effect on a Jitter matrix.](https://docs.cycling74.com/images/eb89a966fb80a0f5e1e5756467e6b380_365.webp) A striping" effect on a Jitter matrix.
These classes "stripe" an input matrix by iterating across each row of the matrix and overwriting the values of some of the cells. Which cells are written to depends on the values of the `on` and `off` attributes: if the `on` attribute has value _v_ and `off` has value _w_ , the algorithm will overwrite _v_ cells, then not write to _w_ cells, and so on as it iterates row-wise through the matrix. 
Here is the code for _j51matrixstriperA_ :
```
import com.cycling74.max.*;
import com.cycling74.jitter.*;

public class j51matrixstriperA extends MaxObject {

   JitterMatrix jm = new JitterMatrix();
   int frgb[] = new int[] {255, 255, 255, 255};
   int on = 2, off = 1;

   j51matrixstriperA()
   {
     declareAttribute("frgb");
     declareAttribute("on");
     declareAttribute("off");
   }

   //note that this method assumes a 2D char matrix!
   public void jit_matrix(String s)
   {
     jm.frommatrix(s);
     int dim[] = jm.getDim();
     int count = 0;
     boolean notoff = true;
     for (int i="0;i<dim[1];i++)"
        for(int j="0;j<dim[0];j++)"
        {
          if (notoff)
             jm.setcell2d(j, i, frgb);
          if ((notoff &&(++count > on))
               ||(!notoff&&(++count > off)))
          {
             count = 0;
             notoff = !notoff;
          }
        }
     outlet(0, "jit_matrix", jm.getName());
   }
}

```

In the jit_matrix method we use the getDim() method to find out the dimensions of our matrix and store them in the int array _dim_ , which we then use as the terminal conditions in the for() loops of our iterative procedure. The setcell2d method allows us to directly set the value of any cell in the matrix. When we are finished processing, we send a `jit_matrix` message out with the name of our JitterMatrix as the argument.
  * Toggle the [Ggate](https://docs.cycling74.com/reference/gswitch2/) object back and forth. Which class is faster?


The only difference between _j51matrixstriperA_ and _j51matrixstriperB_ is the jit_matrix method. Here is _j51matrixstriperB_ 's jit_matrix method:
```
//note that this method assumes a 2D char matrix!
public void jit_matrix(String s)
{
  jm.frommatrix(s);
  int dim[] = jm.getDim();
  int count = 0;
  int planecount = jm.getPlanecount();
  int offset[] = new int[]{0,0};
  boolean notoff = true;
  int row[] = new int[dim[0]*planecount];

  for (int i="0;i<dim[1];i++)"
  {
     offset[1] = i;
     jm.copyVectorToArray(0, offset, row,
                  dim[0]*planecount, 0);
     for(int j="0;j<dim[0];j++)"
     {
       if (notoff)
       {
          for (int k="0;k<planecount;k++)"
            row[j*planecount+k] = frgb[k];
       }
       if ((notoff &&(++count > on))
            ||(!notoff&&(++count > off)))
       {
          count = 0;
          notoff = !notoff;
       }
     }
     jm.copyArrayToVector(0, offset, row,
                  dim[0]*planecount, 0);
  }
  outlet(0, "jit_matrix", jm.getName());
}

```

Rather than set values in the matrix one cell at a time, the jit_matrix method of _j51matrixstriperB_ grabs an entire row from the matrix using JitterMatrix's copyVectorToArray method, overwrites the appropriate values in the row, then writes the row back to the matrix using JitterMatrix's copyArrayToVector method. As you may have noticed, this version of the class is significantly faster than the version that sets cells in the matrix one-by-one. This is an excellent demonstration of the following very important thing to keep in mind: it is very expensive to cross the C/Java boundary. The version of this object that uses setcell must go back and forth across the C/Java boundary once for every cell in the matrix. The latter version goes back and forth just twice per row. If you have tried both versions of the object out, the savings are evident.
The copyVectorToArray and copyArrayToVector methods are overloaded with signatures that cover all the relevant data types. As you can see from a careful examination of the above code, these methods provide and expect the Java arrays with the planar data multiplexed so that all of a cell's data is presented contiguously. There are also copyVectorToArrayPlanar and copyArrayToVectorPlanar methods for moving a single plane's data into Java.
_When using mxj classes to process matrices in Jitter there is no built-in usurp functionality, so it is important to always drive the object network using a **qmetro_ **_object, or some other construction that defers events to prevent backlog._
## Copying Input Data
In the above examples may also have noted the different way that we internally use our JitterMatrix. Whereas in the matrix info example we created a new JitterMatrix every time an input matrix was received, this time we cache one instance of JitterMatrix and copy the input data into it every time using the frommatrix method. Why do we do this?
  * Stop the [qmetro](https://docs.cycling74.com/reference/qmetro/ "qmetro") and close the `striper` subpatch. Open the `why copy?` subpatch. Turn on the [qmetro](https://docs.cycling74.com/reference/qmetro/ "qmetro").

![Why copy?](https://docs.cycling74.com/images/8418ef50150b33ce132a677180485ef2_255.webp) Why copy?
The [trigger](https://docs.cycling74.com/reference/trigger/ "trigger") object in this subpatch sends the output of the [jit.noise](https://docs.cycling74.com/reference/jit.noise "jit.noise") object first into an instance of the [mxj](https://docs.cycling74.com/reference/mxj/ "mxj") class _j51whycopy_ :
```
import com.cycling74.max.*;
import com.cycling74.jitter.*;

public class j51whycopy extends MaxObject {

   JitterMatrix jm = new JitterMatrix();
   boolean copy = false;

   j51whycopy()
   {
     declareAttribute("copy");
   }

   public void jit_matrix(String inname)
   {
     //under normal circumstances
     //we would only create this matrix once
     jm = new JitterMatrix();
     if (copy)
     {
        jm.frommatrix(inname);
     }
     else //!copy
     {
        jm = new JitterMatrix(inname);
     }
     zero(jm);
     outlet(0, "jit_matrix", jm.getName());
   }

   //note that this method assumes the matrix is of type char
   private void zero(JitterMatrix m)
   {
     int z[] = new int[m.getPlanecount()];
     for (int i="0;i<m.getPlanecount();i++)"
        z[i] = 0;
     m.setall(z);
   }
}

```

The `copy` attribute flips the jit_matrix method between two different modes: if `copy` is true, the data from the input matrix is copied into our internal JitterMatrix using the frommatrix method. If `copy` is not true, the JitterMatrix `jm` is created with the input matrix as its peer. In both cases our JitterMatrix is zeroed using the setall method, and then output.
  * Turn the `copy` attribute on and off with the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") box. What happens in the left [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") ?


When the `copy` attribute is off and we create a new JitterMatrix associated with the input name we operate directly on the data of that matrix. Therefore we may be altering the contents of the matrix before other objects have had a chance to see it. In this example patch, when the `copy` attribute is true the left [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") correctly shows the matrix produced by [jit.noise](https://docs.cycling74.com/reference/jit.noise "jit.noise"). When the `copy` attribute is false both [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") objects are black because our [mxj](https://docs.cycling74.com/reference/mxj/ "mxj") class alters the matrix's data directly. Therefore if we are operating on a matrix, we should make sure to copy the input data into an internal cache as we do here with frommatrix.
## Object Composition
In this section we'll examine the use of multiple JitterObjects within a single Java class.
  * Toggle the [qmetro](https://docs.cycling74.com/reference/qmetro/ "qmetro") off and close the subpatcher window. Open the composition subpatcher. Toggle the [qmetro](https://docs.cycling74.com/reference/qmetro/ "qmetro") on. 

![A Jitter processing chain executing within Java.](https://docs.cycling74.com/images/b5fe885234fb92b0131086e7e4ac5d9d_378.webp) A Jitter processing chain executing within Java.
Let's examine the code for the _j51composition_ class:
```
import com.cycling74.max.*;
import com.cycling74.jitter.*;

public class j51composition extends MaxObject {
   JitterMatrix jm = new JitterMatrix();
   JitterMatrix temp = new JitterMatrix();
   JitterObject brcosa;
   JitterObject sobel;
   boolean brcosafirst = false;

   j51composition() {
     declareAttribute("brcosafirst");
     brcosa = new JitterObject("jit.brcosa");
     brcosa.setAttr("brightness", 2.0f);
     sobel = new JitterObject("jit.sobel");
     sobel.setAttr("thresh", 0.5f);
   }

   public void jit_matrix(String mname)
   {
     jm.frommatrix(mname);
     temp.setinfo(jm);
     if (brcosafirst)
     {
        brcosa.matrixcalc(jm, temp);
        sobel.matrixcalc(temp, jm);
     }
     else
     {
        sobel.matrixcalc(jm, temp);
        brcosa.matrixcalc(temp, jm);
     }
     outlet(0, "jit_matrix", jm.getName());
   }

   public void notifyDeleted()
   {
     brcosa.freePeer();
     sobel.freePeer();
   }
}

```

Two JitterObjects are created in the class's constructor: brcosa controls a peer [jit.brcosa](https://docs.cycling74.com/reference/jit.brcosa "jit.brcosa") object, and sobel controls a peer [jit.sobel](https://docs.cycling74.com/reference/jit.sobel "jit.sobel") object. The jit_matrix method copies the data from the input matrix to jm, and then sets the dimensions, `planecount` and `type` of the temp matrix to that of jm with the setinfo method. After this the two JitterObjects can be used to process the data in either order: if the attribute `brcosafirst` is true, the brcosa operates first and then sobel, and of course vice versa is `brcosafirst` is false. We operate on the data in a matrix by calling a JitterObject's matrixcalc method. The two arguments are input and output matrices – it is also possible to use arrays of input and output matrices if the peer Jitter object supports multiple matrix inputs or outputs. This simple example shows how it is possible to define a varying network of Jitter objects within a Java class.
  * Toggle the `brcosafirst` attribute on and off to see the difference in the resulting image.


Finally, note that when the [mxj](https://docs.cycling74.com/reference/mxj/ "mxj") object is deleted and the notifyDeleted method is called, the peer Jitter objects are freed by calling the freePeer() method for every JitterObject we've instantiated. If freePeer() is not called the C object peers will persist until the Java memory manager garbage collects, and this could take a while.
## Listening
  * Toggle the [qmetro](https://docs.cycling74.com/reference/qmetro/ "qmetro") off and close the subpatch. Open the `cubiccurver` subpatch. Turn on the [toggle](https://docs.cycling74.com/reference/toggle/ "toggle") box labeled _verbose_ , move the mouse in the [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") object and observe the results in the Max Console.

![](https://docs.cycling74.com/images/d7586b6910abce74e508740f24405e05_377.webp)
This section assumes you've looked at _Tutorial 47: Using Jitter Object Callbacks in JavaScript_ , which covers object callbacks in Javascript. The Jitter Java API provides the same mechanism for "listening" to events generated by named Jitter objects. In this subpatcher we use this mechanism to track mouse movement within a named [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow"). Let's examine the source code for the _j51pwindowlistener_ class:
```
import com.cycling74.max.*;
import com.cycling74.jitter.*;

public class j51pwindowlistener extends MaxObject
implements JitterNotifiable
{
   JitterListener listener;
   boolean verbose = false;

   j51pwindowlistener()
   {
     declareIO(1,2);
     declareAttribute("verbose");
   }

   public void name(String s)
   {
     listener = new JitterListener(s,this);
   }

   public void notify(JitterEvent e)
   {
     //this gets the name of the listening context
     String subjectname = e.getSubjectName();
     //this gets the type of event...mouse, mouseidle, etc.
     String eventname = e.getEventName();
     //this gets the arguments of the event
     Atom args[] = e.getArgs();
     if (verbose)
     {
        outlet(1,subjectname);
        outlet(1,eventname,args);
     }

     if ((eventname.equals("mouse"))
||(eventname.equals("mouseidle")))
     {
        int xy[] = new int[] {args[0].toInt(),
args[1].toInt()};
        //output the x and y coordinates of the mouse
        outlet(0, xy);
     }
   }
}

```

The first thing to notice is that the class implements an interface called JitterNotifiable. This simple interface ensures that the class has a notify method which will be called when an event is "heard". Notice that the notify method takes a JitterEvent as an argument. The notify method in this class illustrates the methods of these JitterEvents that we'll use to extract the pertinent data: getSubjectName returns the name of the listening context, which is useful if we're listening in more than one place; getEventName returns the name of the event that has been heard; and getArgs returns the arguments that detail the parameters of the event. With the `verbose` attribute enabled, this class's notify method outputs these data out the second outlet and a [print](https://docs.cycling74.com/reference/print/ "print") object sends it to the Max Console. 
The notify method continues by testing the value of _eventname_ for equality with either `mouseidle` (for normal mouse movement) or `mouse` (for movement with the button down). If either of these Strings is a match, the first two arguments, which represent the _x_ and _y_ position of the mouse in the window, are output as a list.
The last thing to note about this class is that before any listening can happen the listener must be created with an existing context. In this case that happens when an instance of the class receives a `name` message. Unlocking the patch will show you how the [jit.pwindow](https://docs.cycling74.com/reference/jit.pwindow "jit.pwindow") object is given a `name` first; the `name` message is then sent to the instance of _j51pwindowlistener_. 
The rest of the patch uses the _jitcubiccurve_ example class to render a cubic curve the follows the mouse around. The control points for the cubic curve are calculated using the _j51fracdistancer_ class, whose code you may want to read through to see if you've understood the material in this lesson:
```
import com.cycling74.max.*;
import com.cycling74.jitter.*;
import java.util.*;

public class j51fracdistancer extends MaxObject{

   JitterMatrix ctlmatrix =
     new JitterMatrix(1, "float32", 8);
   float ctldata[] = new float[8];
   int offset[] = new int[] {0};
   float frac = 0.5f;
   float noise = 0.5f;
   Random r = new Random();

   j51fracdistancer() {
     declareAttribute("frac");
     declareAttribute("noise");
   }

    //new x,y input
   public void list(int args[])
   {
     if (args.length != 2) return;
     float x = (float)args[0];
     float y = (float)args[1];
     for (int i="0;i<4;i++)"
     {
        ctldata[i*2]   += (x-ctldata[i*2])   * frac +
((float)r.nextGaussian()*noise);
        ctldata[i*2+1] += (y-ctldata[i*2+1]) * frac +
((float)r.nextGaussian()*noise);
     }
     ctlmatrix.copyArrayToVector(0,offset, ctldata, 8, 0);
     outlet(0, "jit_matrix", ctlmatrix.getName());
   }

   public void jit_matrix(String mname)
   {
     JitterMatrix jm = new JitterMatrix(mname);
     if (jm.getDim()[0] != 8) return;
     if (jm.getPlanecount() != 1) return;
     if (!jm.getType().equals("float32")) return;

     ctlmatrix.frommatrix(mname);
     ctlmatrix.copyVectorToArray(0, offset, ctldata, 8, 0);
   }
}

```

## Summary
In this tutorial we've introduced the JitterObject, JitterMatrix, and JitterListener classes, and we've seen how to use them to put together [mxj](https://docs.cycling74.com/reference/mxj/ "mxj") classes that operate directly on data, use composition of existing Jitter objects to define graphs of processing, and how to listen to Jitter objects for events in a way that can facilitate the building of user interface components, among other things.
## See Also
  * [jit.matrix - The Jitter Matrix!](https://docs.cycling74.com/reference/jit.matrix)
  * [jit.noise - Generate white noise](https://docs.cycling74.com/reference/jit.noise)
  * [jit.op - Apply binary or unary operators](https://docs.cycling74.com/reference/jit.op)
  * [jit.movie - Play or edit a movie](https://docs.cycling74.com/reference/jit.movie)
  * [mxj - Java in Max](https://docs.cycling74.com/reference/mxj/)



Kind
    Tutorial 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
