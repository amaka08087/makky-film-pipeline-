import json

class FilmWriter:
    def __init__(self, brand_name, concept):
        self.brand_name = brand_name
        self.concept = concept

    def generate_storyboard(self):
        """Generates structured scene layouts for production."""
        script_structure = {
            "brand": self.brand_name,
            "core_concept": self.concept,
            "scenes": [
                {
                    "scene_number": 1,
                    "hook_type": "Pattern Interrupt / Villain Arc",
                    "visual_prompt": "Cinematic close-up start frame, dramatic lighting, high contrast, character expression looking directly into camera",
                    "voiceover_lyric": "Are you tired of settling for less when the best is right here?"
                },
                {
                    "scene_number": 2,
                    "hook_type": "Value Proposition",
                    "visual_prompt": "Dynamic product interaction, vibrant colors, clean aesthetic, smooth camera motion",
                    "voiceover_lyric": "Switch it up today and watch everything change!"
                }
            ]
        }
        return json.dumps(script_structure, indent=4)

if __name__ == "__main__":
    writer = FilmWriter("MakkySignature", "Viral Singing Ad Pipeline")
    print(writer.generate_storyboard())
