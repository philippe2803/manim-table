# Cell Class

The `Cell` class represents a single unit in the table, containing text and an optional border.

## Overview

Cells are the building blocks of `Row` and `Table` objects. They inherit from `VGroup`.

## Constructor

### `__init__`

```python
Cell(
    value: str,
    width: float = 1.5,
    height: float = 0.5,
    font_size: int = 20,
    is_header: bool = False,
    show_border: bool = True,
    **kwargs
)
```

## Methods

### `set_value`

Change the text content of the cell.

```python
def set_value(self, new_value: str) -> Text
```

**Returns:** The new `Text` mobject.

**Example:**
```python
# Animate text change
cell = table.get_cell(1, 1)
old_text = cell.text.copy()
new_text = cell.set_value("Updated")
self.play(Transform(old_text, new_text))
```

### Styling

- `set_font_color(color)`: Set the text color.
- `set_background_color(color, opacity=0.5)`: Add a colored background rectangle.
- `set_border_color(color)`: Change the border line color.
- `get_value()`: Return the string value of the cell.

### Internal Use

- `get_resized_copy(new_width)`: Returns a new `Cell` instance with updated width (for animations).
- `resize_width(new_width)`: Instantly resizes the cell.
