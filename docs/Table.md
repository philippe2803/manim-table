# Table Class

The `Table` class is the main component for creating database table visualizations in ManimGL.

## Overview

```python
from manim_table import Table

# simple creation
table = Table([["Header 1", "Header 2"], ["Value 1", "Value 2"]])

# explicit header and rows
table = Table(
    header=["Col 1", "Col 2"], 
    rows=[
        ["Val 1A", "Val 2A"],
        ["Val 1B", "Val 2B"]
    ]
)
```

## Constructor

### `__init__`

Initialize a new Table.

```python
Table(
    data: Optional[List[List[str]]] = None,
    header: Optional[List[str]] = None,
    rows: Optional[List[List[str]]] = None,
    cell_width: float = 1.5,
    cell_height: float = 0.5,
    font_size: int = 20,
    show_border: bool = True,
    auto_fit: bool = True,
    padding: float = 0.3,
    **kwargs
)
```

**Arguments:**
- `data`: List of rows, where the first row is treated as the header. Ignored if `header` is provided.
- `header`: Explicit header row (list of column names).
- `rows`: Data rows (list of lists). Required if `header` is provided.
- `cell_width`: Default width for cells if `auto_fit=False`.
- `cell_height`: Height of each cell.
- `font_size`: Font size for cell text.
- `show_border`: If True, cells have visible borders.
- `auto_fit`: If True (default), column widths automatically fit the content.
- `padding`: Extra padding around text when `auto_fit=True`.
- `**kwargs`: Additional arguments passed to the parent `VGroup`.

## Methods

### Styling

#### `set_column_font_color`

Set the font color for all cells in a specific column.

```python
def set_column_font_color(self, col: int, color, include_header: bool = False)
```

**Example:**
```python
# Set 2nd column text to RED, excluding header
table.set_column_font_color(1, RED)
```

#### `set_column_background_color`

Set the background color for all cells in a column.

```python
def set_column_background_color(self, col: int, color, opacity: float = 0.5, include_header: bool = False)
```

**Example:**
```python
# Highlight 1st column with BLUE background
table.set_column_background_color(0, BLUE, opacity=0.3)
```

#### `set_column_border_color`

Set the border color for all cells in a column.

```python
def set_column_border_color(self, col: int, color, include_header: bool = True)
```

#### `set_header_background_color`

Set the background color for all header cells.

```python
def set_header_background_color(self, color, opacity: float = 0.5)
```

#### `set_header_font_color`

Set the font color for all header cells.

```python
def set_header_font_color(self, color)
```

### Accessors

- `get_cell(row, col)`: Get a specific cell (Row 0 is header).
- `get_row(index)`: Get a row by index (Index 0 is header).
- `get_column(index)`: Get a column as a VGroup.
- `get_column_by_name(name)`: Get a column by its header name.
- `get_header_names()`: Return list of header strings.

### Mutations (Animations)

#### `add_row`

Add a new row to the bottom of the table.

```python
def add_row(self, values: List[str]) -> Tuple[Row, List]
```

**Returns:** `(new_row, animations)`
- `new_row`: The created Row object.
- `animations`: List of `FadeIn` animations.

**Example:**
```python
new_row, anims = table.add_row(["New", "Entry"])
self.play(*anims)
```

#### `delete_row`

Delete a row from the table (animates shifting subsequent rows).

```python
def delete_row(self, index: int) -> Tuple[Row, List, List]
```

**Arguments:**
- `index`: Row index to delete (1-indexed; cannot delete header).

**Returns:** `(deleted_row, shift_animations, resize_animations)`

**Example:**
```python
deleted, shift, resize = table.delete_row(1)
self.play(FadeOut(deleted))
self.play(*shift)
if resize:
    self.play(*resize)
```

#### `add_column`

Add a new column to the table.

```python
def add_column(self, header: str, values: List[str], index: Optional[int] = None) -> Tuple[VGroup, List, List]
```

**Returns:** `(new_column_group, shift_animations, appear_animations)`

**Example:**
```python
col, shifts, appears = table.add_column("New Col", ["v1", "v2"])
self.play(*shifts)
self.play(*appears)
```

#### `delete_column`

Delete a column from the table.

```python
def delete_column(self, index: int) -> Tuple[VGroup, List]
```

**Returns:** `(deleted_column_group, shift_animations)`

**Example:**
```python
deleted, shifts = table.delete_column(1)
self.play(FadeOut(deleted))
self.play(*shifts)
```
