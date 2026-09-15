# Studio Configuration for Makky Film Pipeline

# Video Output Settings (Optimized for Vertical Reels & TikTok)
VIDEO_SETTINGS = {
    "resolution": "1080x1920",
    "fps": 30,
    "codec": "libx264",
    "audio_codec": "aac"
}

# AI Generation Defaults
AI_DEFAULTS = {
    "default_aspect_ratio": "9:16",
    "visual_model": "Wan2.1 / LTX-Video",
    "audio_model": "Suno / Custom Audio Engine"
}

def print_studio_config():
    print("=== Makky Film Studio Configuration ===")
    print(f"Target Format : Vertical {VIDEO_SETTINGS['resolution']} @ {VIDEO_SETTINGS['fps']}fps")
    print(f"Primary Models: {AI_DEFAULTS['visual_model']}")
    print("Status: Configuration loaded successfully.\n")

if __name__ == "__main__":
    print_studio_config()
