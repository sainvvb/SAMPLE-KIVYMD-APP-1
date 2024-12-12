import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar


class BMSApp(App):
    def build(self):
        # Main layout is BoxLayout to hold title and two sections of grid
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Title at the top of the screen (centered)
        title = Label(text='5S1P-BMS', size_hint=(1, 0.1), font_size=40, bold=True)
        main_layout.add_widget(title)

        # Create additional sections for current, voltage, and temperature
        self.current_label = Label(text='Voltage (V):', font_size=20, bold=True)
        self.current_value = TextInput(
            text=str(round(random.uniform(11.5, 14.5), 2)),
            multiline=False,
            readonly=True,  # Make the TextInput read-only (no user input)
            font_size=30,
            halign='center',
            font_name='Roboto-Bold',
        )

        self.voltage_label = Label(text='Current (A):', font_size=20, bold=True)
        self.voltage_value = TextInput(
            text=str(round(random.uniform(0.0, 10.0), 2)),
            multiline=False,
            readonly=True,  # Make the TextInput read-only (no user input)
            font_size=30,
            halign='center',
            font_name='Roboto-Bold',
        )

        self.temperature_label = Label(text='Temperature (°C):', font_size=20, bold=True)
        self.temperature_value = TextInput(
            text=str(round(random.uniform(20.0, 40.0), 2)),
            multiline=False,
            readonly=True,  # Make the TextInput read-only (no user input)
            font_size=30,
            halign='center',
            font_name='Roboto-Bold',
        )

        # Add these new labels and TextInputs to the main layout
        current_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=20)
        current_layout.add_widget(self.current_label)
        current_layout.add_widget(self.current_value)
        main_layout.add_widget(current_layout)

        voltage_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=20)
        voltage_layout.add_widget(self.voltage_label)
        voltage_layout.add_widget(self.voltage_value)
        main_layout.add_widget(voltage_layout)

        temperature_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=20)
        temperature_layout.add_widget(self.temperature_label)
        temperature_layout.add_widget(self.temperature_value)
        main_layout.add_widget(temperature_layout)

        # SOC Label and TextInput
        self.soc_label = Label(text='State of Charge (SOC):', font_size=20, bold=True)
        self.soc_value = TextInput(
            text=str(round(random.uniform(0.0, 100.0), 2)) + '%',  # Initial SOC value
            multiline=False,
            readonly=True,  # Make the TextInput read-only (no user input)
            font_size=30,
            halign='center',
            font_name='Roboto-Bold',
        )
        soc_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=20)
        soc_layout.add_widget(self.soc_label)
        soc_layout.add_widget(self.soc_value)
        main_layout.add_widget(soc_layout)

        # SOC Progress Bar (representing the charge level)
        self.soc_progress_bar = ProgressBar(
            value=random.uniform(0, 100),  # Initial SOC value
            max=100,
            size_hint=(1, 0.05),
            height=40,
        )
        main_layout.add_widget(self.soc_progress_bar)

        # Create the two sections (7 cells on each side)
        # Use a horizontal layout to position the two grid sections
        grid_layout = BoxLayout(size_hint=(1, 0.8))

        # Create the left section with 7 numerical displays
        self.left_grid = GridLayout(cols=1, spacing=10, size_hint=(0.5, 1))  # Increased spacing between cells
        self.left_text_inputs = []
        for i in range(1, 9):  # Starting serial number from 1 for 7 cells
            # Generate random float values between 3.567 and 3.694
            random_value = round(random.uniform(3.567, 3.694), 3)

            # Create a horizontal BoxLayout for serial number and text input side by side
            cell_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=60, spacing=20)

            # Create a label for the serial number
            serial_label = Label(text=f"Cell {i}", font_size=25, size_hint=(0.2, 1), bold=True)
            cell_layout.add_widget(serial_label)

            # For each cell, create a TextInput for numerical value (read-only)
            text_input = TextInput(
                text=str(random_value),
                multiline=False,
                readonly=True,  # Make the TextInput read-only (no user input)
                font_size=35,  # Increased font size
                halign='center',  # Center-align the text inside the TextInput
                font_name='Roboto-Bold',  # Use a font that supports bold
            )
            self.left_text_inputs.append(text_input)
            cell_layout.add_widget(text_input)

            # Add the cell layout to the left grid
            self.left_grid.add_widget(cell_layout)

        # Create the right section with 7 numerical displays
        self.right_grid = GridLayout(cols=1, spacing=10, size_hint=(0.5, 1))  # Increased spacing between cells
        self.right_text_inputs = []
        for i in range(9, 17):  # Serial numbers continue from 8 to 14
            # Generate random float values between 3.567 and 3.694
            random_value = round(random.uniform(3.567, 3.694), 3)

            # Create a horizontal BoxLayout for serial number and text input side by side
            cell_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=60, spacing=20)

            # Create a label for the serial number
            serial_label = Label(text=f"Cell {i}", font_size=25, size_hint=(0.2, 1), bold=True)
            cell_layout.add_widget(serial_label)

            # For each cell, create a TextInput for numerical value (read-only)
            text_input = TextInput(
                text=str(random_value),
                multiline=False,
                readonly=True,  # Make the TextInput read-only (no user input)
                font_size=35,  # Increased font size
                halign='center',  # Center-align the text inside the TextInput
                font_name='Roboto-Bold',  # Use a font that supports bold
            )
            self.right_text_inputs.append(text_input)
            cell_layout.add_widget(text_input)

            # Add the cell layout to the right grid
            self.right_grid.add_widget(cell_layout)

        # Add both grids to the main horizontal box layout
        grid_layout.add_widget(self.left_grid)
        grid_layout.add_widget(self.right_grid)

        # Add the grid_layout to the main layout
        main_layout.add_widget(grid_layout)

        # Schedule the update of random values every 1 second
        Clock.schedule_interval(self.update_values, 1)

        return main_layout

    def update_values(self, dt):
        # Update the random values for left grid (even though they are read-only)
        for text_input in self.left_text_inputs:
            new_value = round(random.uniform(3.567, 3.694), 3)
            text_input.text = str(new_value)

        # Update the random values for right grid (even though they are read-only)
        for text_input in self.right_text_inputs:
            new_value = round(random.uniform(3.567, 3.694), 3)
            text_input.text = str(new_value)

        # Update the current value
        self.current_value.text = str(round(random.uniform(0.0, 10.0), 2))

        # Update the voltage value
        self.voltage_value.text = str(round(random.uniform(11.5, 14.5), 2))

        # Update the temperature value
        self.temperature_value.text = str(round(random.uniform(20.0, 40.0), 2))

        # Update the SOC value (both text and progress bar)
        soc_value = round(random.uniform(0.0, 100.0), 2)
        self.soc_value.text = str(soc_value) + '%'
        self.soc_progress_bar.value = soc_value


if __name__ == '__main__':
    BMSApp().run()
