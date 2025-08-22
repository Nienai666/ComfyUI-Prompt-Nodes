class BasicFeaturesNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "hairstyle": (['short hair', 'long hair', 'curly hair', 'straight hair'],),
                "face_shape": (['round face', 'oval face', 'square face'],),
                "body_shape": (['slim', 'athletic', 'curvy'],),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "combine_features"

    CATEGORY = "Prompt Nodes"

    def combine_features(self, hairstyle, face_shape, body_shape):
        prompt = f"{hairstyle}, {face_shape}, {body_shape}"
        return (prompt,)

class ClothingNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "clothing": (['dress', 'shirt', 'pants', 'skirt'],),
            },
            "optional": {
                "prompt": ("STRING", {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "combine_clothing"

    CATEGORY = "Prompt Nodes"

    def combine_clothing(self, clothing, prompt=""):
        prompt = f"{prompt}, {clothing}"
        return (prompt,)

class SceneNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "background": (['city', 'forest', 'beach', 'studio'],),
                "camera": (['close-up', 'medium shot', 'long shot'],),
            },
            "optional": {
                "prompt": ("STRING", {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "combine_scene"

    CATEGORY = "Prompt Nodes"

    def combine_scene(self, background, camera, prompt=""):
        prompt = f"{prompt}, {background}, {camera}"
        return (prompt,)

NODE_CLASS_MAPPINGS = {
    "BasicFeaturesNode": BasicFeaturesNode,
    "ClothingNode": ClothingNode,
    "SceneNode": SceneNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BasicFeaturesNode": "Basic Features",
    "ClothingNode": "Clothing",
    "SceneNode": "Scene"
}