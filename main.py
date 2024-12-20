from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
import random
import os


class BMSApp(App):
    def build(self):
        # Main layout using FloatLayout to handle positioning of image at the bottom right
        main_layout = FloatLayout()

        # Create the BoxLayout for other UI elements
        layout = BoxLayout(orientation='vertical', padding=10, spacing=20)

        # Create the top layout to include the menu button and title
        top_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=100, spacing=20)

        # Menu button that will open the popup
        menu_button = Button(text='Menu', size_hint=(None, None), size=(200, 150), font_size=50,
                             on_press=self.open_menu)
        top_layout.add_widget(menu_button)

        # Title at the top of the screen (centered)
        title = Label(text='5S1P-BMS', size_hint=(1, 0.1), font_size=80, bold=True)
        top_layout.add_widget(title)

        layout.add_widget(top_layout)

        # Add a BoxLayout with a fixed height to add space between the title and voltage section
        layout.add_widget(BoxLayout(size_hint_y=None, height=50))  # Adjust height to control the gap

        # Create additional sections for voltage, current, and temperature
        self.current_label = Label(text='Voltage (V):', font_size=40, bold=True)
        self.current_value = TextInput(
            text=str(round(random.uniform(57, 60), 2)),  # Initial voltage value between 57 and 60
            multiline=False,
            readonly=True,  # Make the TextInput read-only (no user input)
            font_size=70,
            halign='center',
            font_name='Roboto-Bold',
        )

        self.voltage_label = Label(text='Current (A):', font_size=40, bold=True)
        self.voltage_value = TextInput(
            text=str(round(random.uniform(0.0, 10.0), 2)),
            multiline=False,
            readonly=True,  # Make the TextInput read-only (no user input)
            font_size=70,
            halign='center',
            font_name='Roboto-Bold',
        )

        self.temperature_label = Label(text='Temperature (°C):', font_size=40, bold=True)
        self.temperature_value = TextInput(
            text=str(round(random.uniform(20.0, 40.0), 2)),
            multiline=False,
            readonly=True,  # Make the TextInput read-only (no user input)
            font_size=70,
            halign='center',
            font_name='Roboto-Bold',
        )

        # Add these new labels and TextInputs to the layout
        current_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=100, spacing=50)
        current_layout.add_widget(self.current_label)
        current_layout.add_widget(self.current_value)
        layout.add_widget(current_layout)

        voltage_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=100, spacing=50)
        voltage_layout.add_widget(self.voltage_label)
        voltage_layout.add_widget(self.voltage_value)
        layout.add_widget(voltage_layout)

        temperature_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=100, spacing=50)
        temperature_layout.add_widget(self.temperature_label)
        temperature_layout.add_widget(self.temperature_value)
        layout.add_widget(temperature_layout)

        # SOC Label and TextInput
        self.soc_label = Label(text='State of Charge (SOC):', font_size=40, bold=True)
        self.soc_value = TextInput(
            text=str(round(random.uniform(0.0, 100.0), 2)) + '%',  # Initial SOC value
            multiline=False,
            readonly=True,  # Make the TextInput read-only (no user input)
            font_size=70,
            halign='center',
            font_name='Roboto-Bold',
        )
        soc_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=100, spacing=50)
        soc_layout.add_widget(self.soc_label)
        soc_layout.add_widget(self.soc_value)
        layout.add_widget(soc_layout)

        # SOC Progress Bar (representing the charge level)
        self.soc_progress_bar = ProgressBar(
            value=random.uniform(0, 100),  # Initial SOC value
            max=100,
            size_hint=(1, 0.05),
            height=80,  # Increased height for the progress bar
        )
        layout.add_widget(self.soc_progress_bar)

        # Create the two sections (7 cells on each side)
        grid_layout = BoxLayout(size_hint=(1, 0.7), spacing=20)

        # Create the left section with 7 numerical displays
        self.left_grid = GridLayout(cols=1, spacing=20, size_hint=(0.4, 1),
                                    padding=10)  # Further reduced grid width and added padding
        self.left_text_inputs = []
        for i in range(1, 9):  # Starting serial number from 1 for 7 cells
            # Generate random float values between 3.567 and 3.694
            random_value = round(random.uniform(3.567, 3.694), 3)

            # Create a horizontal BoxLayout for serial number and text input side by side
            cell_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=120, spacing=50)

            # Create a label for the serial number
            serial_label = Label(text=f"Cell {i}", font_size=40, size_hint=(0.2, 1), bold=True)
            cell_layout.add_widget(serial_label)

            # For each cell, create a TextInput for numerical value (read-only)
            text_input = TextInput(
                text=str(random_value),
                multiline=False,
                readonly=True,  # Make the TextInput read-only (no user input)
                font_size=70,  # Increased font size for larger grid
                halign='center',  # Center-align the text inside the TextInput
                font_name='Roboto-Bold',  # Use a font that supports bold
            )
            self.left_text_inputs.append(text_input)
            cell_layout.add_widget(text_input)

            # Add the cell layout to the left grid
            self.left_grid.add_widget(cell_layout)

        # Create the right section with 7 numerical displays
        self.right_grid = GridLayout(cols=1, spacing=20, size_hint=(0.4, 1),
                                     padding=10)  # Further reduced grid width and added padding
        self.right_text_inputs = []
        for i in range(9, 17):  # Serial numbers continue from 8 to 14
            # Generate random float values between 3.567 and 3.694
            random_value = round(random.uniform(3.567, 3.694), 3)

            # Create a horizontal BoxLayout for serial number and text input side by side
            cell_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=120, spacing=50)

            # Create a label for the serial number
            serial_label = Label(text=f"Cell {i}", font_size=40, size_hint=(0.2, 1), bold=True)
            cell_layout.add_widget(serial_label)

            # For each cell, create a TextInput for numerical value (read-only)
            text_input = TextInput(
                text=str(random_value),
                multiline=False,
                readonly=True,  # Make the TextInput read-only (no user input)
                font_size=70,  # Increased font size for larger grid
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

        # Add the grid_layout to the layout
        layout.add_widget(grid_layout)

        # Initialize the parameters with some default values
        self.cell_no_value = "1"  # Default Cell Number
        self.nominal_capacity_value = "100"  # Default Nominal Capacity
        self.over_voltage_value = "4.2"  # Default Over Voltage
        self.over_voltage_release_value = "4.1"  # Default Over Voltage Release
        self.under_voltage_value = "3.0"  # Default Under Voltage
        self.under_voltage_release_value = "3.1"  # Default Under Voltage Release
        self.over_temperature_value = "60"  # Default Over Temperature
        self.over_temperature_release_value = "55"  # Default Over Temperature Release
        self.under_temperature_value = "-10"  # Default Under Temperature
        self.under_temperature_release_value = "-5"  # Default Under Temperature Release

        # Label and TextInput for showing the parameters
        self.cell_no_value_display = TextInput(
            text=self.cell_no_value,
            multiline=False,
            readonly=True,  # Make the TextInput read-only (no user input)
            font_size=70,
            halign='center',
            font_name='Roboto-Bold',
        )

        self.nominal_capacity_value_display = TextInput(
            text=self.nominal_capacity_value,
            multiline=False,
            readonly=True,  # Make the TextInput read-only (no user input)
            font_size=70,
            halign='center',
            font_name='Roboto-Bold',
        )

        self.over_voltage_value_display = TextInput(
            text=self.over_voltage_value,
            multiline=False,
            readonly=True,  # Make the TextInput read-only (no user input)
            font_size=70,
            halign='center',
            font_name='Roboto-Bold',
        )

        self.over_voltage_release_value_display = TextInput(
            text=self.over_voltage_release_value,
            multiline=False,
            readonly=True,  # Make the TextInput read-only (no user input)
            font_size=70,
            halign='center',
            font_name='Roboto-Bold',
        )

        self.under_voltage_value_display = TextInput(
            text=self.under_voltage_value,
            multiline=False,
            readonly=True,  # Make the TextInput read-only (no user input)
            font_size=70,
            halign='center',
            font_name='Roboto-Bold',
        )

        self.under_voltage_release_value_display = TextInput(
            text=self.under_voltage_release_value,
            multiline=False,
            readonly=True,  # Make the TextInput read-only (no user input)
            font_size=70,
            halign='center',
            font_name='Roboto-Bold',
        )

        self.over_temperature_value_display = TextInput(
            text=self.over_temperature_value,
            multiline=False,
            readonly=True,  # Make the TextInput read-only (no user input)
            font_size=70,
            halign='center',
            font_name='Roboto-Bold',
        )

        self.over_temperature_release_value_display = TextInput(
            text=self.over_temperature_release_value,
            multiline=False,
            readonly=True,  # Make the TextInput read-only (no user input)
            font_size=70,
            halign='center',
            font_name='Roboto-Bold',
        )

        self.under_temperature_value_display = TextInput(
            text=self.under_temperature_value,
            multiline=False,
            readonly=True,  # Make the TextInput read-only (no user input)
            font_size=70,
            halign='center',
            font_name='Roboto-Bold',
        )

        self.under_temperature_release_value_display = TextInput(
            text=self.under_temperature_release_value,
            multiline=False,
            readonly=True,  # Make the TextInput read-only (no user input)
            font_size=70,
            halign='center',
            font_name='Roboto-Bold',
        )

        # Add the layout to the main layout (FloatLayout)
        main_layout.add_widget(layout)

        # Add an image at the bottom right
        image = Image(source="images/DCS.png", size_hint=(None, None), size=(200, 200),
                      pos_hint={"right": 1, "bottom": 0})
        main_layout.add_widget(image)

        # Schedule the update of random values every 1 second
        Clock.schedule_interval(self.update_values, 1)

        return main_layout

    def update_values(self, dt):
        # Update random values every second
        self.current_value.text = str(round(random.uniform(57, 60), 2))  # Voltage range between 57 and 60
        self.voltage_value.text = str(round(random.uniform(0.0, 10.0), 2))
        self.temperature_value.text = str(round(random.uniform(20.0, 40.0), 2))

        # Update State of Charge (SOC)
        new_soc = round(random.uniform(0.0, 100.0), 2)
        self.soc_value.text = str(new_soc) + '%'
        self.soc_progress_bar.value = new_soc

        # Update cell values every second
        for i, text_input in enumerate(self.left_text_inputs):
            text_input.text = str(round(random.uniform(3.567, 3.694), 3))

        for i, text_input in enumerate(self.right_text_inputs):
            text_input.text = str(round(random.uniform(3.567, 3.694), 3))

    def open_menu(self, instance):
        # Create the menu layout with buttons
        menu_layout = BoxLayout(orientation='vertical', spacing=20, padding=20)

        # Button for opening the Dashboard
        dashboard_button = Button(text="Dashboard", size_hint=(1, 0.5), height=50, on_press=self.show_dashboard)
        menu_layout.add_widget(dashboard_button)

        # Button for setting parameters
        set_parameters_button = Button(text="Set Parameters", size_hint=(1, 0.5), height=50,
                                       on_press=self.show_set_parameters)
        menu_layout.add_widget(set_parameters_button)

        # Close Button to close the menu popup
        close_button = Button(text="Close", size_hint=(1, 0.5), height=50, on_press=self.close_menu)
        menu_layout.add_widget(close_button)

        # Create the popup with the menu layout
        self.popup = Popup(title="Menu", content=menu_layout, size_hint=(None, None), size=(1000, 1500))
        self.popup.open()

    def close_menu(self, instance):
        # Close the menu and set parameters popups
        if hasattr(self, 'popup') and self.popup:
            self.popup.dismiss()
        if hasattr(self, 'parameter_popup') and self.parameter_popup:
            self.parameter_popup.dismiss()

    def show_dashboard(self, instance):
        # Handle dashboard button press (you can implement your dashboard logic here)
        print("Dashboard clicked")

    def show_set_parameters(self, instance):
        # Create the layout for setting parameters
        parameter_layout = BoxLayout(orientation='vertical', spacing=20, padding=20)

        # Create a horizontal layout for each parameter (label + input field)
        def create_param_layout(label_text, input_field):
            param_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10)
            label = Label(text=label_text, font_size=30, size_hint=(0.3, 0.5), bold=True)  # Reduced label width
            param_layout.add_widget(label)
            input_field.size_hint_x = 0.5  # Reduced width for input field (adjust as needed)
            param_layout.add_widget(input_field)
            return param_layout

        # Create the input fields for all parameters including temperature values
        self.cell_no_input = TextInput(
            text=self.cell_no_value,  # Set default value from current value
            multiline=False,
            font_size=30,
            halign='center',
            font_name='Roboto-Bold',
        )

        self.nominal_capacity_input = TextInput(
            text=self.nominal_capacity_value,  # Set default value from current value
            multiline=False,
            font_size=30,
            halign='center',
            font_name='Roboto-Bold',
        )

        self.over_voltage_input = TextInput(
            text=self.over_voltage_value,  # Set default value from current value
            multiline=False,
            font_size=30,
            halign='center',
            font_name='Roboto-Bold',
        )

        self.over_voltage_release_input = TextInput(
            text=self.over_voltage_release_value,  # Set default value from current value
            multiline=False,
            font_size=30,
            halign='center',
            font_name='Roboto-Bold',
        )

        self.under_voltage_input = TextInput(
            text=self.under_voltage_value,  # Set default value from current value
            multiline=False,
            font_size=30,
            halign='center',
            font_name='Roboto-Bold',
        )

        self.under_voltage_release_input = TextInput(
            text=self.under_voltage_release_value,  # Set default value from current value
            multiline=False,
            font_size=30,
            halign='center',
            font_name='Roboto-Bold',
        )

        self.over_temperature_input = TextInput(
            text=self.over_temperature_value,  # Set default value from current value
            multiline=False,
            font_size=30,
            halign='center',
            font_name='Roboto-Bold',
        )

        self.over_temperature_release_input = TextInput(
            text=self.over_temperature_release_value,  # Set default value from current value
            multiline=False,
            font_size=30,
            halign='center',
            font_name='Roboto-Bold',
        )

        self.under_temperature_input = TextInput(
            text=self.under_temperature_value,  # Set default value from current value
            multiline=False,
            font_size=30,
            halign='center',
            font_name='Roboto-Bold',
        )

        self.under_temperature_release_input = TextInput(
            text=self.under_temperature_release_value,  # Set default value from current value
            multiline=False,
            font_size=30,
            halign='center',
            font_name='Roboto-Bold',
        )

        parameter_layout.add_widget(create_param_layout("Cell No:", self.cell_no_input))
        parameter_layout.add_widget(create_param_layout("Nominal Capacity (Ah):", self.nominal_capacity_input))
        parameter_layout.add_widget(create_param_layout("Over Voltage (V):", self.over_voltage_input))
        parameter_layout.add_widget(create_param_layout("Over Voltage Release (V):", self.over_voltage_release_input))
        parameter_layout.add_widget(create_param_layout("Under Voltage (V):", self.under_voltage_input))
        parameter_layout.add_widget(create_param_layout("Under Voltage Release (V):", self.under_voltage_release_input))
        parameter_layout.add_widget(create_param_layout("Over Temperature (°C):", self.over_temperature_input))
        parameter_layout.add_widget(
            create_param_layout("Over Temperature Release (°C):", self.over_temperature_release_input))
        parameter_layout.add_widget(create_param_layout("Under Temperature (°C):", self.under_temperature_input))
        parameter_layout.add_widget(
            create_param_layout("Under Temperature Release (°C):", self.under_temperature_release_input))

        # Add Save and Cancel buttons
        save_button = Button(text="Save", on_press=self.save_parameters, size_hint=(1, 0.2))
        cancel_button = Button(text="Cancel", on_press=self.close_menu, size_hint=(1, 0.2))

        parameter_layout.add_widget(save_button)
        parameter_layout.add_widget(cancel_button)

        # Create the popup for parameters and open it
        self.parameter_popup = Popup(title="Set Parameters", content=parameter_layout, size_hint=(None, None),
                                     size=(1000, 1200))
        self.parameter_popup.open()

    def save_parameters(self, instance):
        # Update the parameter values with the values from the input fields
        self.cell_no_value = self.cell_no_input.text
        self.nominal_capacity_value = self.nominal_capacity_input.text
        self.over_voltage_value = self.over_voltage_input.text
        self.over_voltage_release_value = self.over_voltage_release_input.text
        self.under_voltage_value = self.under_voltage_input.text
        self.under_voltage_release_value = self.under_voltage_release_input.text
        self.over_temperature_value = self.over_temperature_input.text
        self.over_temperature_release_value = self.over_temperature_release_input.text
        self.under_temperature_value = self.under_temperature_input.text
        self.under_temperature_release_value = self.under_temperature_release_input.text

        # Close the parameter popup after saving
        self.parameter_popup.dismiss()


if __name__ == "__main__":
    BMSApp().run()
