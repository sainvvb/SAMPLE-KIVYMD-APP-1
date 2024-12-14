from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.slider import Slider
import random


class BMSApp(App):
    def build(self):
        # Main layout is BoxLayout to hold title and two sections of grid
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=20)

        # Create the top layout to include the menu button and title
        top_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=100, spacing=20)

        # Menu Button on the left
        menu_button = Button(
            text="Menu", size_hint=(None, None), size=(100, 50), font_size=30,
            background_color=(0.2, 0.6, 1, 1), bold=True
        )
        menu_button.bind(on_press=self.show_menu)
        top_layout.add_widget(menu_button)

        # Title at the top of the screen (centered)
        title = Label(text='5S1P-BMS', size_hint=(1, 0.1), font_size=80, bold=True)
        top_layout.add_widget(title)

        main_layout.add_widget(top_layout)

        # Add an empty widget to create space between title and voltage
        spacing_widget = BoxLayout(size_hint_y=None, height=50)  # Adjust height for desired space
        main_layout.add_widget(spacing_widget)

        # Create additional sections for current, voltage, and temperature
        self.current_label = Label(text='Voltage (V):', font_size=40, bold=True)
        self.current_value = TextInput(
            text=str(round(random.uniform(11.5, 14.5), 2)),
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

        # Add these new labels and TextInputs to the main layout
        current_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=100, spacing=50)
        current_layout.add_widget(self.current_label)
        current_layout.add_widget(self.current_value)
        main_layout.add_widget(current_layout)

        voltage_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=100, spacing=50)
        voltage_layout.add_widget(self.voltage_label)
        voltage_layout.add_widget(self.voltage_value)
        main_layout.add_widget(voltage_layout)

        temperature_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=100, spacing=50)
        temperature_layout.add_widget(self.temperature_label)
        temperature_layout.add_widget(self.temperature_value)
        main_layout.add_widget(temperature_layout)

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
        main_layout.add_widget(soc_layout)

        # SOC Progress Bar (representing the charge level)
        self.soc_progress_bar = ProgressBar(
            value=random.uniform(0, 100),  # Initial SOC value
            max=100,
            size_hint=(1, 0.05),
            height=80,  # Increased height for the progress bar
        )
        main_layout.add_widget(self.soc_progress_bar)

        # Create the two sections (7 cells on each side)
        # Use a horizontal layout to position the two grid sections
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

        # Add the grid_layout to the main layout
        main_layout.add_widget(grid_layout)

        # Schedule the update of random values every 1 second
        Clock.schedule_interval(self.update_values, 1)

        return main_layout

    def show_menu(self, instance):
        # Create a popup for the menu and store its reference
        menu_content = BoxLayout(orientation='vertical', padding=10)

        # Create a BoxLayout to hold the buttons at the top of the screen
        buttons_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=20)

        # Create menu options
        dashboard_button = Button(text="Dashboard", size_hint_y=None, height=50)
        dashboard_button.bind(on_press=self.show_dashboard)
        buttons_layout.add_widget(dashboard_button)

        set_params_button = Button(text="Set Parameters", size_hint_y=None, height=50)
        set_params_button.bind(on_press=self.show_set_params)
        buttons_layout.add_widget(set_params_button)

        # Create a ScrollView to accommodate more content below the buttons
        scroll_content = BoxLayout(orientation='vertical', size_hint_y=0.5)
        scroll_content.add_widget(Label(text="Additional content or settings can go here"))

        # Add the button layout to the menu content at the top
        menu_content.add_widget(buttons_layout)

        # Add the scrollable content below the buttons
        menu_content.add_widget(scroll_content)

        # Show the popup with the menu options (halved size)
        self.menu_popup = Popup(
            title="Menu",
            content=menu_content,
            size_hint=(None, None),
            size=(6000, 4000)  # Halved size
        )
        self.menu_popup.open()

    def show_set_params(self, instance):
        # Create a new popup for setting parameters with smaller size
        params_content = BoxLayout(orientation='vertical', padding=10, spacing=15)  # Reduced spacing

        # Create a BoxLayout to arrange the title and grid side by side (horizontal orientation)
        top_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)

        # Title for the Set Parameters
        title_label = Label(text="Set Parameters", font_size=20, size_hint=(None, None), width=200, bold=True)
        top_layout.add_widget(title_label)

        # Add the title layout at the top of the popup
        params_content.add_widget(top_layout)

        # Create a GridLayout to hold the parameters' labels and text inputs
        grid_layout = GridLayout(cols=2, spacing=10, size_hint=(1, None), height=400)  # Increased height

        # Create smaller labels and text inputs for each parameter
        cell_no_label = Label(text="Cell No", font_size=20)
        cell_no_value = TextInput(text="1", font_size=20, size_hint_y=None, height=40)

        # Add 'Cell No' as the first row in the grid
        grid_layout.add_widget(cell_no_label)
        grid_layout.add_widget(cell_no_value)

        # Add the rest of the parameters after 'Cell No'
        nominal_capacity_label = Label(text="Nominal Capacity (Ah)", font_size=20)
        nominal_capacity_value = TextInput(text=str(round(random.uniform(50, 100), 2)), font_size=20, size_hint_y=None,
                                           height=40)

        over_voltage_label = Label(text="Over Voltage (V)", font_size=20)
        over_voltage_value = TextInput(text=str(round(random.uniform(13.0, 15.0), 2)), font_size=20, size_hint_y=None,
                                       height=40)

        over_voltage_release_label = Label(text="Over Voltage Release (V)", font_size=20)
        over_voltage_release_value = TextInput(text=str(round(random.uniform(12.5, 14.5), 2)), font_size=20,
                                               size_hint_y=None, height=40)

        under_voltage_label = Label(text="Under Voltage (V)", font_size=20)
        under_voltage_value = TextInput(text=str(round(random.uniform(10.0, 12.0), 2)), font_size=20, size_hint_y=None,
                                        height=40)

        over_temperature_label = Label(text="Over Temperature (°C)", font_size=20)
        over_temperature_value = TextInput(text=str(round(random.uniform(45.0, 60.0), 2)), font_size=20,
                                           size_hint_y=None, height=40)

        over_temperature_release_label = Label(text="Over Temperature Release (°C)", font_size=20)
        over_temperature_release_value = TextInput(text=str(round(random.uniform(35.0, 50.0), 2)), font_size=20,
                                                   size_hint_y=None, height=40)

        over_current_label = Label(text="Over Current (A)", font_size=20)
        over_current_value = TextInput(text=str(round(random.uniform(20.0, 40.0), 2)), font_size=20, size_hint_y=None,
                                       height=40)

        grid_layout.add_widget(nominal_capacity_label)
        grid_layout.add_widget(nominal_capacity_value)
        grid_layout.add_widget(over_voltage_label)
        grid_layout.add_widget(over_voltage_value)
        grid_layout.add_widget(over_voltage_release_label)
        grid_layout.add_widget(over_voltage_release_value)
        grid_layout.add_widget(under_voltage_label)
        grid_layout.add_widget(under_voltage_value)
        grid_layout.add_widget(over_temperature_label)
        grid_layout.add_widget(over_temperature_value)
        grid_layout.add_widget(over_temperature_release_label)
        grid_layout.add_widget(over_temperature_release_value)
        grid_layout.add_widget(over_current_label)
        grid_layout.add_widget(over_current_value)

        # Add the grid layout to the params content
        params_content.add_widget(grid_layout)

        # Show the popup with the parameter setting content (halved size)
        self.params_popup = Popup(
            title="Set Parameters",
            content=params_content,
            size_hint=(None, None),
            size=(6000, 4500)  # Halved size
        )
        self.params_popup.open()

    def update_values(self, dt):
        # Update values every second (for demonstration purposes)
        self.current_value.text = str(round(random.uniform(11.5, 14.5), 2))
        self.voltage_value.text = str(round(random.uniform(0.0, 10.0), 2))
        self.temperature_value.text = str(round(random.uniform(20.0, 40.0), 2))
        self.soc_value.text = str(round(random.uniform(0.0, 100.0), 2)) + '%'
        self.soc_progress_bar.value = random.uniform(0, 100)  # Update the SOC progress bar


if __name__ == '__main__':
    BMSApp().run()
