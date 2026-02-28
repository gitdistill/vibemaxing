---
description: This class represents a Drum Rack pad in Live.
group: lom
kind: api-page
section: API Reference
sourceUrl: https://docs.cycling74.com/apiref/lom/drumpad/
title: DrumPad
---

# DrumPad
This class represents a Drum Rack pad in Live.
## Canonical Path
```
live_set tracks N devices M drum_pads L

```

## Children
### chains [Chain](https://docs.cycling74.com/apiref/lom/chain/ "Chain") read-onlyobserve
## Properties
### mute bool observe
1 = muted
### name symbol read-onlyobserve
### note int read-only
### solo bool observe
1 = soloed (Solo switch on)   
Does not automatically turn Solo off in other chains.
## Functions
### delete_all_chains
