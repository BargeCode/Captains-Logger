# Sector frame


import json
import time
from tkinter import ACTIVE, CENTER, DISABLED, E, \
    HORIZONTAL, N, S, VERTICAL, W, StringVar, ttk


def create_sectors(frame):
    """ The sector part of the main window.
    sector specifics are in the sector.json file. """
    # Open sector json
    filename = 'sector.json'
    with open(filename, 'r', encoding='UTF-8', newline='') as f:
        sectors = json.load(f)

    # Create sector frame
    sector_frame = ttk.Labelframe(frame, text='Sector details')
    sector_frame.grid(
        column=0, columnspan=16,
        row=9, rowspan=len(sectors),
        sticky=(S, W)
        )

    headers_list = [
        'Naam',
        'Kmr', 'Stad', 'Tijd',  # Begin
        'Kmr', 'Stad', 'Tijd',  # End
        'Snelheid',
    ]
    x = 0
    for header in headers_list:
        ttk.Label(
            sector_frame,
            text=header,
        ).grid(row=0, column=x)
        x += 2

    # Horizontal separator
    ttk.Separator(
        sector_frame,
        orient=HORIZONTAL
    ).grid(
        column=0, row=1, columnspan=18, sticky=(W, E)
    )

    # Iterating through all the sectors in the Json file.
    for sector in sectors:
        sector['name'] = Individual_sector(
            sector['#'],
            sector['Name'],
            sector['Start'],
            sector['End'],
            sector['First City'],
            sector['Last City'],
            sector_frame
        )

    x = 0
    # Vertical separators
    for x in range(1, 16, 2):
        ttk.Separator(
            sector_frame,
            orient=VERTICAL
        ).grid(
            column=x, row=1, rowspan=len(sectors)+2, sticky=(N, S)
        )


class Individual_sector():
    def __init__(sec, num, name, start, end, first_city, last_city, frame):
        """Creates a single row in given frame"""
        # Variables
        sec.num = StringVar()
        sec.num.set(num)

        sec.name = StringVar()
        sec.name.set(name)

        sec.start = StringVar()
        sec.start.set(str(start) + " Kmr")

        sec.end = StringVar()
        sec.end.set(str(end) + " Kmr")

        sec.fcity = StringVar()
        sec.fcity.set(first_city)

        sec.lcity = StringVar()
        sec.lcity.set(last_city)

        # calculated or empty var's:
        sec.length = start - end
        sec.start_time = None
        sec.end_time = None
        sec.timelbl_fcity = StringVar()
        sec.timelbl_lcity = StringVar()
        sec.start_button_text = StringVar()
        sec.start_button_text.set('Starten')
        sec.result = StringVar()
        sec.result.set('--------------')

        # List with columns
        label_list = [
            sec.name,
            sec.start,
            sec.fcity,
            sec.timelbl_fcity,
            sec.end,
            sec.lcity,
            sec.timelbl_lcity,
            sec.result
        ]

        # This list is in the same order as the list above for just width value
        width_list = [
            8,   # Name
            8,   # Start Km
            10,  # Start City
            12,  # Start Time
            10,  # End Km
            8,   # End City
            12,  # End Time
            10,   # Result
        ]

        x = 0
        # Iterate trough list with row headers.
        for sec.label, width_value in zip(label_list, width_list):
            sec.label = ttk.Label(
                frame,
                textvariable=sec.label,
                anchor=(CENTER),
                width=width_value
            )
            sec.label.grid(column=x, row=int(sec.num.get())+2)
            x += 2

        # Sector start_button
        sec.start_button = ttk.Button(
            frame,
            textvariable=sec.start_button_text,
            command=sec.sec_button_press,
            width=6
        )
        sec.start_button.grid(column=x, row=int(sec.num.get())+2)

        # Sector reset_button
        sec.reset_button = ttk.Button(
            frame,
            text="X",
            command=sec.sec_button_press,
            state=DISABLED,
            width=1
        )
        sec.reset_button.grid(column=x+1, row=int(sec.num.get())+2)

    def set_time(sec):
        """ Take current time """
        return time.time()

    def sec_button_press(sec):
        """
        Sector start_button press.
        Starts time when not started yet.
        Stops time when already started.
        Calls calculate speed method.
        """
        if sec.start_button_text.get() == 'Starten':
            # Assign for saving the results.
            sec.start_time = sec.set_time()

            # Show time stamp.
            sec.timelbl_fcity.set(time.strftime('%d/%m/%y %H:%M'))

            # Change start_button
            sec.start_button_text.set('Gestart')

            # Show heartbeat assci art.
            sec.result.set('√v^√v^√v^√♥')
            sec.reset_button['state'] = ACTIVE

        elif sec.start_button_text.get() == 'Gestart':
            # Assign for saving the results.
            sec.end_time = sec.set_time()

            # Show time stamp.
            sec.timelbl_lcity.set(time.strftime('%d/%m/%y %H:%M'))

            # Change start_button
            sec.start_button_text.set('Gestopt')
            sec.start_button['state'] = DISABLED

            # Calculate speed.
            sec.calculate_speed()

        elif sec.start_button_text.get() == 'Gestopt':
            # Empty var for overwriting results.
            sec.start_time = None
            sec.end_time = None

            # Empty time stamps
            sec.timelbl_fcity.set("")
            sec.timelbl_lcity.set("")
            sec.result.set('--------------')

            # Change Button
            sec.start_button_text.set('Starten')
            sec.start_button['state'] = ACTIVE
            sec.reset_button['state'] = DISABLED

        else:
            print('something went wrong')

    def calculate_speed(sec):
        """ Calculates speed through dividing timedelta by distance.
        Time_passed is in seconds and after its divided by 3600, it is in \
            hours. """
        sec.time_passed = sec.end_time - sec.start_time
        sec.time_passed = sec.time_passed / 60 / 60
        sec.speed = "{:.2f}".format(sec.length / sec.time_passed)
        sec.result.set(sec.speed + ' Km/h')
