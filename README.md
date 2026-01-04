# manim-table

A simple library to create and animate tables in ManimGL.

## Installation

You can install the library via pip:

```bash
pip install manim-table
```

## Usage

Here is how you create a basic table.

```python
from manimlib import Scene, Write
from manim_table import Table

class TableExample(Scene):
    def construct(self):
        data = [
            ["Name", "Age", "City"],
            ["Alice", "25", "New York"],
            ["Bob", "30", "Paris"],
        ]
        
        # Create the table
        table = Table(data)
        
        # Animate it
        self.play(Write(table))
```

### Modifying the Table

You can add or remove rows and columns with animations.

```python
# Add a new row
new_row, animations = table.add_row(["Charlie", "35", "London"])
self.play(*animations)

# Delete a row (index starts at 1 for data rows)
deleted_row, shift_anims, resize_anims = table.delete_row(1)

self.play(FadeOut(deleted_row))
self.play(*shift_anims)
if resize_anims:
    self.play(*resize_anims)
```

### Styling

You can easily change colors and styles.

```python
from manimlib import BLUE, RED

# Style the header
table.set_header_background_color(BLUE)

# Style specific cells (row, column)
# Row 0 is header, Row 1 is first data row
table.get_cell(1, 1).set_font_color(RED)
```
