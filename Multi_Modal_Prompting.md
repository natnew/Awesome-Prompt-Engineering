---
layout: default
title: Multi-Modal Prompting
description: Techniques for image, video, and cross-modal AI systems.
nav_order: 5
---

[Home](https://natnew.github.io/Awesome-Prompt-Engineering/)

## Multi-Modal Prompting

Multi-modal prompting encompasses techniques for working with AI models that process and generate images, video, audio, and combinations of media types. As AI systems become increasingly capable across modalities, understanding how to craft effective prompts for visual and multi-modal tasks is essential.

This guide covers prompting strategies for image generation, image understanding, video creation, and cross-modal applications.

---

### Text-to-Image Fundamentals

Text-to-image models translate natural language descriptions into visual outputs. The quality of your prompt directly determines the quality of the generated image.

#### The Progressive Detail Approach

Start simple and add detail iteratively to understand how each element affects the output.

**Level 1 - Basic Concept:**
> A lighthouse on a cliff

**Level 2 - Add Setting and Mood:**
> A lighthouse on a rocky cliff at sunset, dramatic clouds in the sky, waves crashing below

**Level 3 - Specify Style and Details:**
> A lighthouse on a rocky cliff at golden hour sunset, dramatic orange and purple clouds, powerful waves crashing against the rocks below, cinematic composition, photorealistic style, volumetric lighting

**Level 4 - Technical Refinement:**
> A solitary white lighthouse perched on dramatic rocky cliffs during golden hour, the setting sun casting long shadows and painting the clouds in vibrant oranges and deep purples, powerful Atlantic waves crashing against weathered rocks creating white spray, shot with a 35mm lens, photorealistic rendering, volumetric god rays, 8K resolution, National Geographic photography style

---

### Prompt Structure for Image Generation

A well-structured image prompt typically includes:

```
[Subject] + [Setting/Environment] + [Style/Medium] + [Lighting] + [Composition] + [Technical Parameters]
```

#### Component Breakdown

| Component | Examples |
|-----------|----------|
| **Subject** | A woman, a dragon, a coffee cup, an abstract pattern |
| **Setting** | In a forest, on Mars, in a cozy café, floating in space |
| **Style/Medium** | Oil painting, 3D render, watercolor, photorealistic, anime |
| **Lighting** | Golden hour, neon lights, soft diffused, dramatic chiaroscuro |
| **Composition** | Close-up portrait, wide establishing shot, bird's eye view |
| **Technical** | 8K, highly detailed, sharp focus, depth of field |

#### Example Compositions

**Portrait:**
> Close-up portrait of an elderly fisherman with weathered skin and kind eyes, wearing a cable-knit sweater, soft natural window lighting, shallow depth of field, shot on medium format film, intimate and dignified mood

**Landscape:**
> Sweeping vista of terraced rice paddies in Vietnam at sunrise, morning mist rising from the valleys, a farmer in a conical hat walking along a path, lush green tones, travel photography style, golden hour lighting

**Product:**
> Minimalist product photography of a ceramic coffee mug on a marble surface, steam rising from fresh coffee, soft morning light from the left, clean white background, commercial advertising style, sharp focus

**Abstract:**
> Abstract fluid art composition in deep ocean blues and metallic gold, organic flowing shapes suggesting underwater currents, high contrast, luminescent quality, suitable for large canvas print

---

### Negative Prompts

Negative prompts specify what you don't want in the image, helping avoid common issues and unwanted elements.

#### Common Negative Prompt Elements
```
Negative prompt: blurry, low quality, distorted, deformed, ugly, duplicate, 
watermark, text, signature, out of frame, cropped, low resolution, artifacts, 
noise, oversaturated, underexposed
```

#### Use Case-Specific Negatives

**For Portraits:**
```
Negative: deformed face, extra limbs, mutated hands, poorly drawn hands, 
poorly drawn face, long neck, bad anatomy, bad proportions, cross-eyed
```

**For Architecture:**
```
Negative: impossible geometry, floating elements, inconsistent perspective, 
warped lines, physically impossible structure
```

**For Product Photography:**
```
Negative: cluttered background, harsh shadows, overexposed highlights, 
visible imperfections, distracting elements, uneven lighting
```

---

### Model-Specific Syntax

Different platforms have unique syntax for controlling generation parameters.

#### Midjourney Parameters
```
/imagine prompt: A cyberpunk street market in Tokyo --ar 16:9 --v 6 --style raw --q 2

Parameters:
--ar 16:9       Aspect ratio (width:height)
--v 6           Model version
--style raw     Less stylized, more literal interpretation
--q 2           Quality level (higher = more detail, slower)
--s 250         Stylization amount (0-1000)
--c 25          Chaos/variation (0-100)
--no trees      Exclude specific elements
--seed 12345    Reproducible results
```

#### DALL-E 3 Best Practices
```
DALL-E 3 works best with natural language descriptions rather than keyword lists.

Less effective: "cat, orange, sitting, window, sunlight, photorealistic, 8K"

More effective: "A fluffy orange tabby cat sitting contentedly on a windowsill, 
bathed in warm afternoon sunlight streaming through the glass. The cat's fur 
glows golden in the light. Photorealistic style with fine detail."
```

#### Stable Diffusion Weighting
```
Syntax: (element:weight) where 1.0 is default

Example: A (beautiful sunset:1.3) over the ocean, with (dramatic clouds:1.2) 
and a (small sailboat:0.8) in the distance

Higher weights (>1.0) = more emphasis
Lower weights (<1.0) = less emphasis
Double parentheses = stronger effect: ((very important element))
```

---

### Image-to-Text Prompting

Vision-language models can analyze, describe, and reason about images. Effective prompting improves accuracy and relevance of the analysis.

#### Basic Image Analysis
```
Analyze this image and provide:
1. A detailed description of what you see
2. The apparent setting and context
3. Notable objects and their spatial relationships
4. The mood or atmosphere conveyed
5. Any text visible in the image
```

#### Structured Image Extraction
```
Extract information from this receipt image:

<output_format>
{
  "store_name": "",
  "date": "",
  "items": [
    {"name": "", "quantity": 0, "price": 0.00}
  ],
  "subtotal": 0.00,
  "tax": 0.00,
  "total": 0.00,
  "payment_method": ""
}
</output_format>

If any field is unclear or not visible, use null.
```

#### Comparative Image Analysis
```
Compare these two images and identify:
1. Similarities in composition, color, or subject matter
2. Key differences between them
3. Which image is more effective for [specific purpose] and why
4. Technical quality comparison (lighting, focus, exposure)
```

#### Visual Reasoning
```
Look at this image of a room and answer:
1. What time of day does this appear to be? What visual cues indicate this?
2. What season might it be? Why?
3. What can you infer about the person who lives here?
4. What is happening or has recently happened in this scene?
```

---

### Image Editing Prompts

Modern models support various image editing operations through natural language instructions.

#### Inpainting (Editing Regions)
```
Edit the selected region of this image:
- Replace the cloudy sky with a vibrant sunset
- Keep the foreground buildings exactly as they are
- Ensure the lighting on the buildings is consistent with sunset lighting
- Blend the edges naturally
```

#### Style Transfer
```
Transform this photograph into the style of [artist/movement]:
- Maintain the original composition and subject matter
- Apply the characteristic brushwork/technique of [style]
- Keep colors within the typical palette of [style]
- Preserve recognizable features of the original subject
```

#### Outpainting (Extending Images)
```
Extend this image to the [left/right/top/bottom]:
- Continue the natural environment seamlessly
- Maintain consistent lighting and perspective
- Add contextually appropriate elements
- Ensure the extension feels like a natural part of the original scene
```

---

### Video Generation Prompts

Text-to-video models require additional considerations for temporal consistency and motion.

#### Video Prompt Structure
```
[Scene description] + [Motion/Action] + [Camera movement] + [Duration/Pacing] + [Style]
```

#### Example Video Prompts

**Establishing Shot:**
> A slow cinematic drone shot ascending over a misty forest at dawn, revealing 
> a mountain range in the distance as the camera rises above the treeline, 
> 10-second duration, smooth movement, nature documentary style

**Character Action:**
> A chef in a professional kitchen carefully plates a gourmet dish, 
> hands moving with precision, close-up on the hands transitioning to 
> medium shot revealing the focused expression, warm kitchen lighting, 
> 8 seconds, slight camera drift

**Abstract/Motion Graphics:**
> Flowing liquid metal morphing between geometric shapes, reflecting 
> rainbow iridescent colors, seamless looping animation, 6 seconds, 
> smooth continuous transformation, dark background

#### Video-Specific Considerations
```
Motion guidance:
- Specify speed: "slow-motion," "real-time," "time-lapse"
- Describe transitions: "dissolve to," "cut to," "smooth transition"
- Camera movement: "static," "pan left," "zoom in," "tracking shot"
- Subject motion: "walking toward camera," "rotating slowly," "bouncing"

Temporal consistency:
- Maintain character appearance throughout
- Keep lighting consistent across frames
- Specify if environment should change or remain static
```

---

### Multi-Modal Chains

Combining image and text capabilities in sequence for complex workflows.

#### Image → Analysis → Generation
```
Step 1: Analyze this photograph of a room interior
Step 2: Identify the design style, color palette, and key furniture
Step 3: Generate a prompt for a similar room with [specified modifications]
Step 4: Generate the new image
```

#### Text → Image → Critique → Refine
```
Step 1: Generate image from initial prompt
Step 2: Analyze the generated image for issues
Step 3: Create improved prompt addressing issues
Step 4: Regenerate with refined prompt
Step 5: Compare and select best result
```

#### Document → Visual Summary
```
Step 1: Read and analyze this research paper
Step 2: Identify 4-5 key concepts that would benefit from visualization
Step 3: Create image prompts for each concept
Step 4: Generate illustrations
Step 5: Assemble into visual summary/infographic layout
```

---

### Prompt Templates by Use Case

#### Product Photography
```
Professional product photography of [product], centered on [surface material] 
surface, [lighting type] lighting from [direction], [background description], 
commercial advertising style, sharp focus on product, [mood/feeling], 
suitable for [platform: e-commerce/print/social media]
```

#### Portrait/Character
```
[Shot type: close-up/medium/full body] portrait of [subject description], 
[age/expression/pose], wearing [clothing/accessories], [setting/background], 
[lighting type and direction], [art style or photography style], 
[mood/atmosphere], [additional technical details]
```

#### Environment/Landscape
```
[View type: panoramic/establishing/intimate] of [location type], 
[time of day] with [weather/atmospheric conditions], [key elements in 
foreground/midground/background], [color palette], [style: photorealistic/
painterly/stylized], evoking [mood/feeling], [compositional notes]
```

#### Concept Art
```
Concept art of [subject] for [context: game/film/book], [design style], 
[key visual elements and details], [color scheme], [reference influences], 
[functional/narrative purpose], professional quality, suitable for 
production reference
```

---

### Quality Control Checklist

Before finalizing your prompt:

- [ ] **Subject clarity** — Is the main subject unambiguous?
- [ ] **Style defined** — Have you specified artistic style or medium?
- [ ] **Lighting described** — Is lighting direction and quality clear?
- [ ] **Composition noted** — Camera angle, framing, depth of field?
- [ ] **Mood established** — Emotional tone and atmosphere?
- [ ] **Negative prompts** — Unwanted elements explicitly excluded?
- [ ] **Technical specs** — Resolution, aspect ratio, quality level?
- [ ] **Platform syntax** — Using correct parameters for your tool?

---

### Quick Reference: Image Generation Models

| Model | Strengths | Best For |
|-------|-----------|----------|
| **DALL-E 3** | Natural language understanding, safety | General purpose, beginners |
| **Midjourney v6** | Artistic quality, aesthetics | Art, design, creative work |
| **Stable Diffusion 3** | Control, customization, open-source | Technical users, fine-tuning |
| **Ideogram** | Text rendering, typography | Logos, graphics with text |
| **Flux** | Photorealism, speed | Realistic images, iteration |

---

### Notes

Feedback and suggestions are welcome!

Multi-modal AI is evolving rapidly. These techniques provide a foundation, but experimentation with specific models is essential for mastering their unique capabilities.

**Explore further:**
- [Midjourney Documentation](https://docs.midjourney.com)
- [DALL-E Guide](https://platform.openai.com/docs/guides/images)
- [Stable Diffusion Resources](https://stability.ai)
- [Runway ML](https://runwayml.com) (Video generation)