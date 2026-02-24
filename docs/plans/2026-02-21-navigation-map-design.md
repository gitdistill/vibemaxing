# `assets/navigation.json` Schema Design

This document details the planned structure and content for the `assets/navigation.json` file, which will serve as a static, pre-processed map of the Cycling '74 documentation. This map guides the agent's initial discovery and browsing decisions.

The `navigation.json` will contain a top-level `docs_url` and an array of `sections`, each representing a major part of the Cycling '74 documentation (e.g., User Guide, Reference, Tutorials).

```json
{
  "docs_url": "https://docs.cycling74.com",
  "sections": [
    {
      "id": "user_guide",
      "title": "User Guide",
      "base_url": "https://docs.cycling74.com/userguide/",
      "description": "General concepts, usage guidelines, and architectural insights for Max, MSP, and Jitter.",
      "buckets": [
        {
          "id": "audio",
          "title": "Audio",
          "description": "Concepts and techniques for working with audio signals, synthesis, and processing within Max/MSP.",
          "articles": [
            { "title": "Ableton DSP", "url_suffix": "abl", "description": "Placeholder: Learn about Ableton's DSP algorithms in Max." },
            { "title": "Frequency Domain", "url_suffix": "frequency_domain", "description": "Placeholder: Explore audio processing techniques in the frequency domain." },
            { "title": "MC Overview", "url_suffix": "mc", "description": "Placeholder: An introduction to the MC (multi-channel) object system." },
            { "title": "MC and Gen", "url_suffix": "mc/mc_gen", "description": "Placeholder: Understand the integration of MC with the Gen environment." },
            { "title": "MC Wrapper", "url_suffix": "mcwrapper", "description": "Placeholder: Using wrapper objects for multi-channel patching." },
            { "title": "Multi-Channel I/O", "url_suffix": "multichannel", "description": "Placeholder: Managing multiple audio input and output channels." },
            { "title": "Non-Real-Time", "url_suffix": "nrt", "description": "Placeholder: Techniques for offline audio processing and rendering." },
            { "title": "Plugins", "url_suffix": "plugins", "description": "Placeholder: Integrating and developing external audio plugins." },
            { "title": "Polyphony", "url_suffix": "polyphony", "description": "Placeholder: Strategies for handling multiple voices in synthesizers." },
            { "title": "Recording", "url_suffix": "recording", "description": "Placeholder: Methods for recording audio within Max." },
            { "title": "RNBO", "url_suffix": "rnbo", "description": "Placeholder: An introduction to RNBO for exporting Max patches." },
            { "title": "Sample Accurate Messages", "url_suffix": "sampleaccurate", "description": "Placeholder: Achieving precise timing with audio-rate messages." }
          ]
        },
        {
          "id": "colors",
          "title": "Colors",
          "description": "Placeholder: Managing and manipulating colors in Max.",
          "articles": [
            { "title": "Color Palette", "url_suffix": "color_palette", "description": "Placeholder: Working with color palettes." },
            { "title": "Color Themes", "url_suffix": "color_themes", "description": "Placeholder: Customizing Max's visual themes." }
            // ... (other color articles)
          ]
        }
        // ... (other buckets will follow this structure)
      ]
    },
    {
      "id": "reference",
      "title": "Reference",
      "description": "Technical specifications for objects and APIs."
      // Structure to be defined
    },
    {
      "id": "tutorials",
      "title": "Tutorials",
      "base_url": "https://docs.cycling74.com/learn/",
      "description": "Step-by-step guides, walkthroughs, and conceptual explanations across various Max/MSP/Jitter topics.",
      "series": [
        {
          "id": "max-tutorials",
          "title": "Max Tutorials",
          "url_suffix": "series/max-tutorials/",
          "description": "Core Max tutorial series, showing how to create patches, take input from MIDI controllers, manipulate data, and drive dynamic processes.",
          "articles": [] // Placeholder
        },
        {
          "id": "msp-tutorials",
          "title": "MSP Tutorials",
          "url_suffix": "series/msp-tutorials/",
          "description": "Signal processing tutorial series, demonstrating signal processing techniques including sampling, synthesis, effects, and spectral manipulation.",
          "articles": [] // Placeholder
        },
        {
          "id": "jitter-tutorials",
          "title": "Jitter Tutorials",
          "url_suffix": "series/jitter-tutorials/",
          "description": "The classic Jitter tutorial series, exploring matrices of video data, manipulating pixels, and rendering computer graphics scenes.",
          "articles": [] // Placeholder
        },
        {
          "id": "custom-drawing-js",
          "title": "Custom Drawing with JavaScript",
          "url_suffix": "series/js-drawing-tutorials/", 
          "description": "Learn how to use MGraphics and JavaScript to design custom user interfaces.",
          "articles": [] // Placeholder
        },
        {
          "id": "jitter-geometry-tutorials",
          "title": "Jitter Geometry Tutorial",
          "url_suffix": "series/jitter-geometry-tutorials/",
          "description": "Learn the Jitter Geometry objects, used to create half-edge structures for shapes that can be warped and transformed dynamically.",
          "articles": [] // Placeholder
        },
        {
          "id": "polish-your-pixels",
          "title": "Polish Your Pixels",
          "url_suffix": "series/polish-your-pixels/",
          "description": "A guide to superior renders in Jitter. Strategies, tools and techniques from realistic lighting and advanced material setups to subtle post-processing enhancements.",
          "articles": [] // Placeholder
        }
      ]
    }
  ]
}
```
