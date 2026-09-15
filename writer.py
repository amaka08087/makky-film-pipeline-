import json

class FilmWriter:
    def __init__(self, brand_name, concept, duration_minutes=10, aspect_ratio="16:9", content_type="Narration & Singing"):
        self.brand_name = brand_name
        self.concept = concept
        self.duration_minutes = max(1, min(duration_minutes, 10))  # Scales up to 10 mins
        self.aspect_ratio = aspect_ratio  # Supports "16:9" or "9:16"
        self.content_type = content_type  # Supports "Narration", "Singing", or "Narration & Singing"

    def generate_storyboard(self):
        """Generates an extended 5-Act multi-format script structure."""
        print(f"Creating a {self.duration_minutes}-min {self.content_type} film in {self.aspect_ratio}...")
        
        script_structure = {
            "brand": self.brand_name,
            "core_concept": self.concept,
            "target_duration": f"{self.duration_minutes} Minutes",
            "aspect_ratio": self.aspect_ratio,
            "content_mode": self.content_type,
            "acts": [
                {
                    "act": "Act 1: The Setup & Atmospheric Hook",
                    "time_marker": "0:00 - 2:00",
                    "visual_prompt": f"({self.aspect_ratio}) Cinematic establishing shot, deep emotional atmosphere, soft dramatic lighting.",
                    "audio_script": f"[{self.content_type}] Opening spoken narration or haunting acoustic motif setting the scene."
                },
                {
                    "act": "Act 2: Rising Tension & Core Conflict",
                    "time_marker": "2:00 - 4:00",
                    "visual_prompt": f"({self.aspect_ratio}) Dynamic movement, contrasting shadows, expressive character framing.",
                    "audio_script": f"[{self.content_type}] Deepening voiceover narrative or building verse exploring the core conflict."
                },
                {
                    "act": "Act 3: The Turning Point / Flashback",
                    "time_marker": "4:00 - 6:00",
                    "visual_prompt": f"({self.aspect_ratio}) Dramatic shift in color grading, intense close-up, turning point realization.",
                    "audio_script": f"[{self.content_type}] Transitional monologue or emotional bridge before the peak."
                },
                {
                    "act": "Act 4: The Master Climax",
                    "time_marker": "6:00 - 8:30",
                    "visual_prompt": f"({self.aspect_ratio}) Sweeping cinematic camera angles, peak visual intensity and performance.",
                    "audio_script": f"[{self.content_type}] Soaring chorus performance or powerful climax narration."
                },
                {
                    "act": "Act 5: Resolution & Resonant Outro",
                    "time_marker": "8:30 - 10:00",
                    "visual_prompt": f"({self.aspect_ratio}) Warm fading light, peaceful closing shot, elegant fade to black.",
                    "audio_script": f"[{self.content_type}] Final lingering words or fading acoustic note leaving a lasting impact."
                }
            ]
        }
        return json.dumps(script_structure, indent=4)

if __name__ == "__main__":
    # Example: 10-minute 16:9 narrative & singing epic
    writer = FilmWriter("MakkySigStories", "The Ultimate 10-Min Epic", duration_minutes=10, aspect_ratio="16:9", content_type="Narration & Singing")
    print(writer.generate_storyboard())
