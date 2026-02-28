---
description: Passing messages over a network
group: Max Tutorials
kind: tutorial
section: Learn
sourceUrl: https://docs.cycling74.com/learn/articles/communicationschapter03/
title: UDP Networking
---

Download Series Content and Patchers
# Communications Tutorial 3: UDP Networking
## Introduction
This tutorial provides information on using a network for transferring Max messages. We examine the [udpsend](https://docs.cycling74.com/reference/udpsend/ "udpsend") and [udpreceive](https://docs.cycling74.com/reference/udpreceive/ "udpreceive") objects, which provide sending and receiving of messages through the UDP networking protocol.
There are many reasons to implement computer networking in Max patchers. Often, in large projects, the work needing to be done exceeds what a single machine can handle. In those cases, it can be useful to use an existing network to harvest CPU cycles from unused machines, or to send synchronization messages between machines running subsections of the whole performance patch. In addition, network protocols can be useful for sharing information among computers that are run by multiple performers, even in separate locations. The [udpsend](https://docs.cycling74.com/reference/udpsend/ "udpsend") and [udpreceive](https://docs.cycling74.com/reference/udpreceive/ "udpreceive") messages wrap the standard UDP networking protocol into a pair of Max objects, providing an easy way to transmit messages between two computers on a network.
## General UDP Overview
The UDP protocol is a lightweight and flexible communications protocol used for Internet application-to-application exchanges. It doesn’t require a connection to be maintained between two machines; rather, the receiving application watches a specific _port_ for data packets (called _datagrams_) and treats them as incoming messages. The transmitting program is required to specify the destination _address_ and port of the receiver.
UDP isn’t the most robust protocol: it does not guarantee that packets will arrive in any order, nor does it provide any means of error or packet loss notification. However, it is a high-speed protocol, often used for networked audio and video content, and happens to be easy to coerce into working with Max messages.
## Sending messages of all types
Take a look at our tutorial. At the left is a [udpsend](https://docs.cycling74.com/reference/udpsend/ "udpsend") object with several different Max message types connected. This is the “transmitting” side of the network connection: the [udpsend](https://docs.cycling74.com/reference/udpsend/ "udpsend") object takes Max messages, turns them into UDP datagrams, and sends them to the destination specified by the machine's TCP/IP address and port (the arguments to the object). The [patcher](https://docs.cycling74.com/reference/patcher/ "patcher") named “network_receiver” is, as its name suggests, the receiving end of this patch. If you open the subpatcher, you will see a [udpreceive](https://docs.cycling74.com/reference/udpreceive/ "udpreceive") object watching port `7000` (you don’t have to specify a network address – the object assumes you are watching the port on “this computer”).
When you click or change any of the messages connected to the [udpsend](https://docs.cycling74.com/reference/udpsend/ "udpsend") object, you will see that they appear in the subpatcher. Both simple and complex messages can be sent through the [udpsend](https://docs.cycling74.com/reference/udpsend/ "udpsend") object; the [multislider](https://docs.cycling74.com/reference/multislider/ "multislider") sends a 12-entry list ([prepend](https://docs.cycling74.com/reference/prepend/ "prepend") ed with the word `multislider`, so we can [route](https://docs.cycling74.com/reference/route/ "route") that at the receiving end), but even the simplest message can be packaged and sent over the network.
We should quickly discuss the network address used in this example. Since we want to test this _locally_ on our own machine, we need to use a network address that consistently represents the host machine. That address is the so-called IP loopback address: `127.0.0.1`. Whenever that network address is used, it means “route this internally, rather than through an external network”. If you wanted to test this patch on a pair of networked machines, the [udpsend](https://docs.cycling74.com/reference/udpsend/ "udpsend") object would have to be changed to use the TCP/IP address of the receiving machine.
## A basic chat program
The second segment of our tutorial patch is an example of a simple chat program. Again, there is a subpatcher that is used to show the communications in action, although you could make some simple changes to have it work between two machines – you would only need to change the network address from “localhost” (the symbolic name for `127.0.0.1`) to the appropriate addresses of the connected computers. This part of the patch sends text (entered in a [textedit](https://docs.cycling74.com/reference/textedit/ "textedit") object) on port `7003`, and receives messages on port `7002`.
Unlike our first example, this shows bidirectional communication in action. When sending information between two computers, each will need a [udpsend](https://docs.cycling74.com/reference/udpsend/ "udpsend") and [udpreceive](https://docs.cycling74.com/reference/udpreceive/ "udpreceive") object, with [udpsend](https://docs.cycling74.com/reference/udpsend/ "udpsend") pointing to the other system’s network address. Additionally, by convention, bidirectional communications occur through two adjacent ports: `7002` and `7003`, in this case. If you open the `chat_buddy`[patcher](https://docs.cycling74.com/reference/patcher/ "patcher"), you will see that it, too, communicates using localhost, but the port order is reversed. Text is sent on port `7002` and received on port `7003`. You can now type text into one of the chat patches (in the white [textedit](https://docs.cycling74.com/reference/textedit/ "textedit") object), when you hit the return key, it will appear in the grey area of the other patch.
## Summary
Max message handling over the network uses the [udpsend](https://docs.cycling74.com/reference/udpsend/ "udpsend") and [udpreceive](https://docs.cycling74.com/reference/udpreceive/ "udpreceive") object, taking advantage of the simple and lightweight UDP protocol to flexibly pass any message or list type. Within a single system, the localhost network address can be used, but the same mechanism will allow you to send messages across the network to any other reachable machine.
## See Also
  * [udpsend - Send Max messages over a network using UDP](https://docs.cycling74.com/reference/udpsend/)
  * [udpreceive - Receive Max messages over a network using UDP](https://docs.cycling74.com/reference/udpreceive/)
  * [textedit - User-entered text in a patcher](https://docs.cycling74.com/reference/textedit/)



Kind
    Tutorial 

Category
    Communication 

Author
    Cycling '74
* * *
The content of this article and any downloadable files are available under the following [license](https://docs.cycling74.com/learn/license/).
