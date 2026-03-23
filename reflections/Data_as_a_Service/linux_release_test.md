# Title

#### 20th March 2026

### What?

Recently, Aaron and his team (which I had left earlier) managed to reach their MVP for The Shadows of Vahlvadell project.

On 16th of March 2026, I built the project for Linux. I then packaged it and sent it over to Aaron for him to post on his website.

Last friday (20th March 2026), I mentioned what I had done during our weekly ASD meetings, and Michael Walkey proposed to test the Linux build for us.

I was more than happy to say yes to his proposal, and following is how that went:

### So what?

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

The game tried falling back on OpenGL (which is a more rudamentary API with fewer bells and whistles), however OpenGL was deprecated in this version of UnrealEngine, and so the game exited with an error.

I 







'So What?' allows you to extract the meaning of 'What?'. Moreover, you should question what knowledge you and others had in the situation, and what knowledge or theories that could help you make sense of the situation.

### Now what?

'Now what?' allows you to create an action plan for the future based on the previous questions.
