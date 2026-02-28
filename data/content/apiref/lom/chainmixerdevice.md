---
description: This class represents a chain's mixer device in Live.
group: lom
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/lom/chainmixerdevice/
title: ChainMixerDevice
---

# ChainMixerDevice
This class represents a chain's mixer device in Live.
## Canonical Paths
```
live_set tracks N devices M chains L mixer_device

```
```
live_set tracks N devices M return_chains L mixer_device

```

## Children
### sends list of [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter") read-onlyobserve
[in Audio Effect Racks and Instrument Racks only]   
For Drum Racks, otherwise empty.
### chain_activator [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter") read-only
### panning [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter") read-only
[in Audio Effect Racks and Instrument Racks only]
### volume [DeviceParameter](https://docs.cycling74.com/apiref/lom/deviceparameter/ "DeviceParameter") read-only
[in Audio Effect Racks and Instrument Racks only]
