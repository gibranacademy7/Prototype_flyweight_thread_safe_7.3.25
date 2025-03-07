"""
QUESTION 2:

A chat application requires the addition of emojis, where each emoji holds an image in the image field.

Class Definitions:

EmojiImage
file_name: string
Emoji
name: string
size: int
image: EmojiImage
Implement the diagram (note that the Emoji class contains an instance of the EmojiImage class, not an inheritance).

Since images are repeated and duplicated for each emoji, implement the Flyweight pattern to store only one image per emoji type.

After implementation:

Create emojis of at least 3 different types, with at least 2 of each type.
Verify that only 3 unique images exist in the storage.
"""

class EmojiImage:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def __repr__(self):
        return f"{self.file_name}"


class EmojiImageFactory:
    _images = {}

    @classmethod
    def get_image(cls, file_name: str):
        if file_name not in cls._images:
            cls._images[file_name] = EmojiImage(file_name)
        return cls._images[file_name]

    @classmethod
    def total_images(cls):
        return len(cls._images)


class Emoji:
    def __init__(self, name: str, size: int, file_name: str):
        self.name = name
        self.size = size
        self.image = EmojiImageFactory.get_image(file_name)

    def __repr__(self):
        return f"Emoji(name='{self.name}', size={self.size}, image={self.image})"


# Mapping file names to actual emojis
emoji_map = {
    "smile.png": "😊",
    "heart.png": "❤️",
    "thumbs_up.png": "👍"
}

# Creating emojis with repeated images
emoji1 = Emoji("Smile", 32, "smile.png")
emoji2 = Emoji("Smile", 64, "smile.png")
emoji3 = Emoji("Heart", 32, "heart.png")
emoji4 = Emoji("Heart", 64, "heart.png")
emoji5 = Emoji("Thumbs Up", 32, "thumbs_up.png")
emoji6 = Emoji("Thumbs Up", 64, "thumbs_up.png")

# Testing uniqueness of images
print(f"Total unique images stored: {EmojiImageFactory.total_images()}")  # Should print 3

# Displaying emojis with real representations
for emoji in [emoji1, emoji2, emoji3, emoji4, emoji5, emoji6]:
    print(f"Emoji(name='{emoji.name}', size={emoji.size}, image={emoji_map[emoji.image.file_name]})")
