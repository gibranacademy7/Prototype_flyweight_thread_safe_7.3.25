"""
+--------------------+
|   EmojiImage      |
|--------------------|
| - file_name: str  |
|--------------------|
| + __init__()      |
+--------------------+

       ▲
       │
       │  (Shared instances via factory)
       │
+--------------------+      +----------------------+
| EmojiImageFactory |      |       Emoji         |
|--------------------|      |----------------------|
| - _images: dict   |      | - name: str         |
|--------------------|      | - size: int         |
| + get_image()     |◄──────| - image: EmojiImage |
| + total_images()  |      |----------------------|
+--------------------+      | + __init__()        |
                            +----------------------+


Explanation:
EmojiImage: Represents an emoji image with a file_name.
EmojiImageFactory: Implements the Flyweight pattern, ensuring each EmojiImage is stored only once.
Emoji: Represents an emoji that contains a reference to an EmojiImage, rather than storing a duplicate.

"""

