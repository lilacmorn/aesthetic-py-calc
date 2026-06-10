import tkinter as tk
from tkinter import font
import math

class AestheticCalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("✦ Aesthetic Calculator ✦")
        self.window.geometry("400x600")
        self.window.resizable(False, False)
        
        # Color scheme (Modern Dark Theme)
        self.colors = {
            'bg': '#0F0F0F',
            'display': '#1A1A1A',
            'button': '#2D2D2D',
            'button_hover': '#3D3D3D',
            'accent': '#FF6B6B',
            'operator': '#4ECDC4',
            'equals': '#FFE66D',
            'clear': '#FF6B6B',
            'text': '#FFFFFF',
            'secondary_text': '#A0A0A0'
        }
        
        self.expression = ""
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        self.setup_ui()
        self.bind_keyboard()
        
    def setup_ui(self):
        # Configure window background
        self.window.configure(bg=self.colors['bg'])
        
        # Custom fonts
        display_font = font.Font(family='Helvetica', size=48, weight='bold')
        button_font = font.Font(family='Helvetica', size=20, weight='bold')
        
        # Display frame
        display_frame = tk.Frame(self.window, bg=self.colors['bg'])
        display_frame.pack(expand=True, fill='both', padx=20, pady=(30, 10))
        
        # Result display
        self.display_label = tk.Label(
            display_frame,
            textvariable=self.result_var,
            font=display_font,
            bg=self.colors['display'],
            fg=self.colors['text'],
            anchor='e',
            padx=20,
            pady=20,
            relief='flat'
        )
        self.display_label.pack(fill='both', expand=True)
        
        # Make display rounded corners using custom style
        self.display_label.configure(highlightthickness=0)
        
        # Buttons frame
        buttons_frame = tk.Frame(self.window, bg=self.colors['bg'])
        buttons_frame.pack(expand=True, fill='both', padx=20, pady=(0, 30))
        
        # Button layout
        buttons = [
            ['C', '±', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]
        
        # Create buttons
        for i, row in enumerate(buttons):
            frame = tk.Frame(buttons_frame, bg=self.colors['bg'])
            frame.pack(expand=True, fill='both', pady=5)
            
            for j, btn_text in enumerate(row):
                if btn_text == '=':
                    # Equals button (span 2 columns)
                    btn = self.create_button(
                        frame, btn_text, button_font,
                        self.colors['equals'], '#333333'
                    )
                    btn.pack(side='left', expand=True, fill='both', padx=2)
                else:
                    btn = self.create_button(
                        frame, btn_text, button_font,
                        self.get_button_color(btn_text), '#333333'
                    )
                    btn.pack(side='left', expand=True, fill='both', padx=2)
                    
                # Add hover effect
                self.add_hover_effect(btn, btn_text)
        
        # Creator credit
        credit_label = tk.Label(
            self.window,
            text="✦ aesthetic calculator ✦",
            font=('Helvetica', 10),
            bg=self.colors['bg'],
            fg=self.colors['secondary_text']
        )
        credit_label.pack(pady=(0, 10))
    
    def create_button(self, parent, text, font, bg_color, fg_color):
        """Create a styled button"""
        btn = tk.Button(
            parent,
            text=text,
            font=font,
            bg=bg_color,
            fg=fg_color,
            relief='flat',
            borderwidth=0,
            cursor='hand2',
            command=lambda: self.button_click(text)
        )
        return btn
    
    def get_button_color(self, text):
        """Return button color based on text"""
        if text in ['÷', '×', '-', '+', '%', '±']:
            return self.colors['operator']
        elif text == 'C':
            return self.colors['clear']
        else:
            return self.colors['button']
    
    def add_hover_effect(self, button, text):
        """Add hover animation to buttons"""
        def on_enter(e):
            button.configure(bg=self.colors['button_hover'])
            
        def on_leave(e):
            button.configure(bg=self.get_button_color(text))
            
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
    
    def button_click(self, value):
        """Handle button clicks"""
        if value == 'C':
            self.clear()
        elif value == '=':
            self.calculate()
        elif value == '±':
            self.negate()
        elif value == '%':
            self.percentage()
        else:
            self.add_to_expression(value)
    
    def add_to_expression(self, value):
        """Add value to expression"""
        # Replace division/multiplication symbols
        if value == '÷':
            value = '/'
        elif value == '×':
            value = '*'
            
        self.expression += str(value)
        self.update_display()
    
    def calculate(self):
        """Evaluate the expression"""
        try:
            # Evaluate expression safely
            result = eval(self.expression)
            
            # Handle float formatting
            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 8)
            
            self.result_var.set(str(result))
            self.expression = str(result)
        except Exception:
            self.result_var.set("Error")
            self.expression = ""
    
    def clear(self):
        """Clear the display"""
        self.expression = ""
        self.result_var.set("0")
    
    def negate(self):
        """Negate the current value"""
        try:
            current = float(self.result_var.get())
            current = -current
            if current.is_integer():
                current = int(current)
            self.result_var.set(str(current))
            self.expression = str(current)
        except:
            pass
    
    def percentage(self):
        """Convert to percentage"""
        try:
            current = float(self.result_var.get())
            current = current / 100
            self.result_var.set(str(current))
            self.expression = str(current)
        except:
            pass
    
    def update_display(self):
        """Update the display with current expression"""
        display_text = self.expression if self.expression else "0"
        # Replace operators for display
        display_text = display_text.replace('*', '×').replace('/', '÷')
        self.result_var.set(display_text)
    
    def bind_keyboard(self):
        """Bind keyboard keys for input"""
        keyboard_map = {
            '0': '0', '1': '1', '2': '2', '3': '3', '4': '4',
            '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
            '.': '.', '+': '+', '-': '-', '*': '*', '/': '/',
            'Return': '=', 'Escape': 'C', 'BackSpace': 'C',
            '%': '%'
        }
        
        for key, value in keyboard_map.items():
            self.window.bind(f'<{key}>', lambda e, v=value: self.button_click(v))
        
        # Handle clear with 'c' key
        self.window.bind('<c>', lambda e: self.button_click('C'))
        self.window.bind('<C>', lambda e: self.button_click('C'))
    
    def run(self):
        """Run the calculator"""
        # Center window on screen
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')
        
        self.window.mainloop()

if __name__ == "__main__":
    calculator = AestheticCalculator()
    calculator.run()