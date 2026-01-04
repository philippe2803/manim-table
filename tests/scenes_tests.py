"""
Example scenes demonstrating the manim_table database animation extension.

Run with:
    cd /Users/philippe.oger/PersoProjects/manimal
    manimgl tests/scenes_tests.py TableDemo -o
"""

from manimlib import Scene, Write, FadeOut, FadeIn, FlashAround, AnimationGroup, ORIGIN, LEFT, RIGHT, UP, DOWN, UL, ReplacementTransform, VGroup, RED, GREEN, BLUE, YELLOW, WHITE, GREY

# Import from the manim_table package
from manim_table import Table


class TableDemo(Scene):
    """
    Demonstrates basic table creation, row operations, and column selection.
    """
    
    def construct(self):
        # Create a table from data (first row is header)
        table = Table([
            ["first_name", "last_name", "age"],
            ["John", "Doe", "34"],
            ["Jane", "Doe", "32"],
            ["Emily", "Doe", "8"],
        ])
        table.move_to(ORIGIN)
        
        # Animate table appearing
        self.play(Write(table, run_time=2))
        self.wait(1)
        
        # Move table to the left
        self.play(table.animate.shift(LEFT * 3))
        self.wait(0.5)
        
        # Move table to the right
        self.play(table.animate.shift(RIGHT * 6))
        self.wait(0.5)
        
        # Move back to center
        self.play(table.animate.move_to(ORIGIN))
        self.wait(0.5)
        
        # Flash around the whole table
        self.play(FlashAround(table, buff=0.1))
        self.wait(0.5)
        
        # Flash around a specific cell (row 1, column 2 = "26")
        self.play(FlashAround(table.get_cell(1, 2), buff=0.1))
        self.wait(0.5)
        
        # Flash around a column by name
        self.play(FlashAround(table.get_column_by_name("age"), buff=0.1))
        self.wait(0.5)
        
        # Add a new row with animation
        new_row, animations = table.add_row(["Alice", "Smith", "30"])
        self.play(AnimationGroup(*animations, lag_ratio=0.2))
        self.wait(1)
        
        # Delete row 1 (John) with animation - this will trigger column resize
        deleted_row, shift_anims, resize_anims = table.delete_row(1)
        self.play(FadeOut(deleted_row))
        self.play(AnimationGroup(*shift_anims, lag_ratio=0.1))
        if resize_anims:
            self.play(AnimationGroup(*resize_anims, lag_ratio=0.05))
        self.wait(1)
        
        # Change a cell value with animation (Jane's age: 32 -> 33)
        cell = table.get_cell(1, 2)  # First data row (was Jane), age column
        old_text = cell.text.copy()
        cell.set_value("33")
        self.play(ReplacementTransform(old_text, cell.text))
        self.wait(1)
        
        # Move table after cell update to verify it still works
        self.play(table.animate.shift(LEFT * 2))
        self.wait(0.3)
        self.play(table.animate.shift(RIGHT * 4))
        self.wait(0.3)
        self.play(table.animate.move_to(ORIGIN))
        self.wait(1)
        
        # Move table to top-left corner and scale down
        self.play(
            table.animate.scale(0.5).to_corner(UL, buff=0.5)
        )
        self.wait(0.5)
        
        # Create 3 copies of the table and position them below
        table_copies = []
        for i in range(3):
            table_copy = table.copy()
            table_copy.next_to(
                table if i == 0 else table_copies[i - 1], 
                DOWN, 
                buff=0.3
            )
            table_copies.append(table_copy)
        
        # Animate the copies appearing one by one
        for table_copy in table_copies:
            self.play(FadeIn(table_copy), run_time=0.5)
        
        self.wait(2)


class TableWithExplicitHeader(Scene):
    """
    Shows alternative table creation with explicit header.
    """
    
    def construct(self):
        table = Table(
            header=["id", "product", "price"],
            rows=[
                ["1", "Apple", "$1.50"],
                ["2", "Banana", "$0.75"],
                ["3", "Orange", "$2.00"],
            ],
            cell_width=2.0,
            cell_height=0.6,
            font_size=24,
        )
        table.move_to(ORIGIN)
        
        self.play(Write(table))
        self.wait(2)


class BorderlessTable(Scene):
    """
    Demonstrates a table without borders.
    """
    
    def construct(self):
        table = Table(
            data=[
                ["Name", "Score"],
                ["Alice", "95"],
                ["Bob", "87"],
                ["Charlie", "92"],
            ],
            show_border=False,
            font_size=28,
        )
        table.move_to(ORIGIN)
        
        self.play(Write(table))
        self.wait(2)


class TableColorScene(Scene):
    """
    Demonstrates color customization for tables.
    """
    
    def construct(self):
        # Create a products table
        table = Table([
            ["Product", "Category", "Price", "Stock"],
            ["Apple", "Fruit", "$1.50", "150"],
            ["Banana", "Fruit", "$0.75", "200"],
            ["Carrot", "Vegetable", "$0.50", "100"],
            ["Milk", "Dairy", "$2.00", "50"],
        ])
        table.move_to(ORIGIN)
        
        # Style the header with a blue background
        table.set_header_background_color(BLUE, opacity=0.3)
        table.set_header_font_color(WHITE)
        
        # Color the Price column green
        table.set_column_font_color(2, GREEN)  # Price column
        
        # Color low stock items red
        table.get_cell(4, 3).set_font_color(RED)  # Milk stock = 50
        table.get_cell(4, 3).set_background_color(RED, opacity=0.2)
        
        # Add yellow background to Fruit category rows
        table.get_cell(1, 1).set_background_color(YELLOW, opacity=0.2)  # Apple
        table.get_cell(2, 1).set_background_color(YELLOW, opacity=0.2)  # Banana
        
        # Set border color for the Product column
        table.set_column_border_color(0, GREY)
        
        self.play(Write(table, run_time=2))
        self.wait(2)
        
        # Demonstrate dynamic color change
        self.play(FlashAround(table.get_column(2), buff=0.1))  # Flash Price column
        self.wait(1)
        
        # Move table to top-left corner and scale down
        self.play(
            table.animate.scale(0.4).to_corner(UL, buff=0.3)
        )
        self.wait(0.5)
        
        # Create 4 copies of the table and position them below
        table_copies = []
        for i in range(4):
            table_copy = table.copy()
            table_copy.next_to(
                table if i == 0 else table_copies[i - 1], 
                DOWN, 
                buff=0.2
            )
            table_copies.append(table_copy)
        
        # Animate the copies appearing one by one
        for table_copy in table_copies:
            self.play(FadeIn(table_copy), run_time=0.4)
        
        self.wait(2)


class TableColumnOperationsScene(Scene):
    """
    Demonstrates adding and deleting columns.
    """
    
    def construct(self):
        # Create initial table
        table = Table([
            ["ID", "Name"],
            ["1", "Alice"],
            ["2", "Bob"],
            ["3", "Charlie"],
        ])
        table.move_to(ORIGIN)
        
        self.play(Write(table))
        self.wait(1)
        
        # 1. Add a column at the end
        new_col, shift_anims, appear_anims = table.add_column(
            header="Score",
            values=["85", "92", "78"]
        )
        if shift_anims:
            self.play(AnimationGroup(*shift_anims, lag_ratio=0.1))
        if appear_anims:
            self.play(AnimationGroup(*appear_anims, lag_ratio=0.1))
        self.wait(1)
        
        # 2. Add a column in the middle (index 1)
        new_col, shift_anims, appear_anims = table.add_column(
            header="Role",
            values=["Dev", "Manager", "Tester"],
            index=1
        )
        if shift_anims:
            self.play(AnimationGroup(*shift_anims, lag_ratio=0.1))
        if appear_anims:
            self.play(AnimationGroup(*appear_anims, lag_ratio=0.1))
        self.wait(1)
        
        # 3. Delete a column (ID column, index 0)
        deleted_col, shift_anims = table.delete_column(0)
        self.play(FadeOut(deleted_col))
        if shift_anims:
            self.play(AnimationGroup(*shift_anims, lag_ratio=0.1))
        self.wait(1)
        
        # Integrity check: Move to top-left corner and duplicate
        self.play(
            table.animate.scale(0.4).to_corner(UL, buff=0.3)
        )
        self.wait(0.5)
        
        # Create 4 copies of the table and position them below
        table_copies = []
        for i in range(4):
            table_copy = table.copy()
            table_copy.next_to(
                table if i == 0 else table_copies[i - 1], 
                DOWN, 
                buff=0.2
            )
            table_copies.append(table_copy)
        
        # Animate the copies appearing one by one
        for table_copy in table_copies:
            self.play(FadeIn(table_copy), run_time=0.4)
        
        self.wait(2)
