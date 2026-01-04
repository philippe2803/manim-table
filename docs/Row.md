# Row Class

The `Row` class represents a horizontal group of cells within a `Table`.

## Overview

Generally, you do not need to instantiate `Row` directly; it is managed by the `Table` class. However, you may interact with `Row` objects returned by table methods.

## Constructor

### `__init__`

```python
Row(
    values: List[str],
    cell_widths: Union[float, List[float]] = 1.5,
    cell_height: float = 0.5,
    font_size: int = 20,
    is_header: bool = False,
    show_border: bool = True,
    index: int = 0,
    **kwargs
)
```

**Arguments:**
- `values`: Text content for each cell in the row.
- `cell_widths`: Single float or list of floats for column widths.
- `cell_height`: Height of cells.
- `font_size`: Font size of text.
- `is_header`: Render as header (bold).
- `show_border`: Visible borders.
- `index`: The row's index in the table.

## Methods

- `get_cell(index)`: Get the `Cell` at the specified column index.
- `__getitem__(index)`: Alias for `get_cell`.
- `__len__()`: Returns number of cells in the row.
- `create_cells()`: Internal method to initialize cells (called in `__init__`).

## Example

```python
# Accessing a cell within a row
row = table.get_row(1)
first_cell = row[0]
first_cell.set_font_color(RED)
```
