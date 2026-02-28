---
description: Pointer event object passed to onpointer* event handlers
group: js
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/js/pointerevent/
title: interface PointerEvent
---

# interface PointerEvent
Pointer event object passed to onpointer* event handlers
This behavior is only available in the new v8 javascript engine objects.
These events adhere as close as possible to the standard PointerEvent structure: [https://developer.mozilla.org/en-US/docs/Web/API/Pointer\\_events](https://developer.mozilla.org/en-US/docs/Web/API/Pointer%5C_events)
Multi-touch and tablet events are currently only supported on Windows.
Max includes extensions to the standard for convenience: - commandKey: command key on Mac, ctrl key on Win - contextModifier: right click or control click on Mac, with right click on Win - capsLock: caps lock state - tipInverted: Pen tip inverted--i.e. eraser pointed at tablet (coming in future)
Currently unsupported properties: - width: contact area width - height: contact area height - tangentialPressure: tangential pressure
* * *
## Properties
### buttons number
Bitmask of buttons currently pressed: - 1: left button (also touch contact, or pen contact) - 2: right button - 4: middle button (also pen barrel) - 8: x1 button (aka "back") - 16: x2 button (aka "forward") - 32: eraser
### capsLock number
Caps lock state
### clientX number
X coordinate of the pointer in client space
### clientY number
Y coordinate of the pointer in client space
### commandKey number
Command key on Mac, ctrl key on Win
### contextModifier number
Right click or control click on Mac, with right click on Win
### eventType string
The type of event (e.g., "pointerenter", "pointerleave", "pointermove", "pointerup", "pointerdown")
### pointerId number
A unique identifier for the pointer event
### pointerType "mouse" | "touch" | "pen"
The type of pointer device ("mouse", "touch", or "pen")
### pressure number
Normalized pressure of the pointer (0.0 to 1.0)
### tiltX number
Planar tilt angle in degrees (-90 to 90)
### tiltY number
Planar tilt angle in degrees (-90 to 90)
### tipInverted number
Pen tip inverted--i.e. eraser pointed at tablet (coming in future)
### twist number
Rotation angle of the pointer in degrees (0-359)
