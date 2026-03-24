# Title

#### 20th March 2026

### What?

Recently, Aaron and his team (which I had left earlier) managed to reach their MVP for The Shadows of Vahlvadell project.

On 16th of March 2026, I built the project for Linux. I then packaged it and sent it over to Aaron for him to post on his website.

Last friday (20th March 2026), I mentioned what I had done during our weekly ASD meetings, and Mike (one of my lecturers) proposed to test the Linux build for us.

Mike wasn't able to run the game. He shared with me his [error logs](../Assets/error_log_mike_walkey.txt) and I investigated them for the exact cause of the issue.

The culprit turned out to be these lines over here:

```
[2026.03.20-15.42.18:353][  0]LogVulkanRHI: Starting Vulkan Profile check for VP_UE_Vulkan_SM6:
[2026.03.20-15.42.18:393][  0]LogVulkanRHI:    - Unsupported extension: VK_EXT_mesh_shader
[2026.03.20-15.42.18:393][  0]LogVulkanRHI:    - Unsupported feature condition: VkPhysicalDeviceMeshShaderFeaturesEXT::meshShader == VK_TRUE
[2026.03.20-15.42.18:393][  0]LogVulkanRHI:    - Unsupported feature condition: VkPhysicalDeviceMeshShaderFeaturesEXT::multiviewMeshShader == VK_TRUE
[2026.03.20-15.42.18:393][  0]LogVulkanRHI:    - Unsupported feature condition: VkPhysicalDeviceMeshShaderFeaturesEXT::taskShader == VK_TRUE
[2026.03.20-15.42.18:393][  0]LogVulkanRHI:    - Unsupported properties condition: 
VkPhysicalDeviceProperties2KHR::properties.limits.maxBoundDescriptorSets >= 9
[2026.03.20-15.42.18:394][  0]LogVulkanRHI: Vulkan Profile check complete.
[2026.03.20-15.42.29:755][  0]Message dialog closed, result: Ok, title: Message, text: Failed to load Vulkan Driver which is required to run the engine.
The engine no longer fallbacks to OpenGL4 which has been deprecated.
```

During initialization of Vulkan (which is Linux's graphics API - analogous to Windows' DirectX), some of the shaders required by the game to run failed to load.

The game tried falling back on OpenGL (which is a more rudamentary cross-platform API with fewer bells and whistles), however OpenGL was deprecated in this version of UnrealEngine, and so the game exited with an error.

To further aid my investigation of why the shaders would fail to load, I requested Mike's specification. He was running a `HP EliteDesk 800 G2 DM 35W` with a `Skylake-S GT2 [HD Graphics 530]` GPU.

The issue is that the GPU is too old and does not support `mesh shaders` as indicated by this line in the error log: `Unsupported feature condition: VkPhysicalDeviceMeshShaderFeaturesEXT::meshShader == VK_TRUE`. This was a fantastic revelation as it revealed that this game has minimum requirements to run.

### So what?

To address those issues, I first made sure to include a couple of custom [Vulkan installation scripts](../assets/drivers/) for a few select Linux distros, namely: Ubuntu, Neon, Linuxmint, Pop, Elementary, Zorin, Tumbleweed, NixOS. I then sought and found the minimum GPU requirements. Those are:

```
Nvidia (Turing architecture): RTX 2060 
AMD (RDNA2 Architecture): Radeon RX 6600
Intel (Xe HPG architecture): Arc A380
```

Upon completion, I submitted my findings over to Aaron, and he reposted the linux version of the game up on his website.



### Now what
