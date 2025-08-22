## Troubleshooting

### Increasing VRAM on Apple Silicon (M1/M2/M3 Macs)

By default, macOS limits the amount of RAM available to the GPU. You can increase this limit to run larger models.

1.  **Check the current limit (optional):**
    ```bash
    sudo sysctl iogpu.wired_limit_mb
    ```

2.  **Set a new limit (temporary):**
    To temporarily increase the VRAM, run the following command, replacing `<megabytes>` with your desired amount. For example, for a 16GB machine, you might allocate 12000MB.
    ```bash
    sudo sysctl iogpu.wired_limit_mb=12000
    ```
    This change will reset on reboot.

3.  **Set a new limit (persistent):**
    To make the change permanent, create or edit `/etc/sysctl.conf`:
    ```bash
    sudo nano /etc/sysctl.conf
    ```
    Add the following line to the file:
    ```
    iogpu.wired_limit_mb=12000
    ```
    Save the file and reboot. The new limit will be applied automatically.

    **Note:** Do not allocate all your system's memory to the GPU. Leave a reasonable amount for the operating system to function correctly.

## References

- [LM Studio Bug Tracker - MLX Quantization Issue](https://github.com/lmstudio-ai/lmstudio-bug-tracker/issues/839)
- [Adjusting VRAM/RAM split on Apple Silicon (GitHub Discussion)](https://github.com/ggml-org/llama.cpp/discussions/2182)
- [Reddit Discussion on Increasing VRAM Allocation](https://www.reddit.com/r/LocalLLaMA/comments/186phti/m1m2m3_increase_vram_allocation_with_sudo_sysctl/)
