import tkinter as tk
from tkinter import ttk, StringVar
from tkinter import filedialog

window = tk.Tk()

window.title('Add New Customer')
frame_1 = tk.Frame(master=window, borderwidth=2, relief="sunken", height=50)
frame_4 = tk.Frame(master=window, borderwidth=1, width=900, height=200)
frame_5 = tk.Frame(master=window, borderwidth=2, height=50)

# Let's create the menu
menubar = tk.Menu(window)
file_menu = tk.Menu(menubar, tearoff=0)  # this will be our file menu

menubar.add_cascade(label='File', menu=file_menu)


def cp_print_cp():
    print('Clever Programmer!')


def file_saveas(event=None):
    # a+ --> add stuff to the end of the file you are writing to
    f = filedialog.asksaveasfile(mode='a+', defaultextension='.txt')
    s = filedialog.save
    if f is None:
        return

    # lesson_details_to_save = str('\n' + str((subject_entry.get(), hours_entry.get(), amount_entry.get())))
    lessons_to_save = notes_text.get(0.0, tk.END)
    f.write(lessons_to_save)
    f.close()


def submit_lesson(event=None):
    lesson_details_to_save = '{}, {}, {}\n'.format(subject_entry.get(), hours_entry.get(), amount_entry.get())
    notes_text.insert(tk.END, lesson_details_to_save)






file_menu.add_command(label="New Customer", accelerator='Ctrl + N',
                      compound=tk.LEFT, image=None, underline=0)
file_menu.add_command(label="Save",
                      compound=tk.LEFT, image=None, underline=0, command=file_saveas)
file_menu.add_command(label="Save As", accelerator='Ctrl + S',
                      compound=tk.LEFT, image=None, underline=0, command=file_saveas)
file_menu.add_command(label="Print", accelerator='Ctrl + P',
                      compound=tk.LEFT, image=None, underline=0, command=cp_print_cp)

file_menu.add_command(label="Exit", accelerator='',
                      compound=tk.LEFT, image=None, underline=0, command=window.quit)



window.config(menu=menubar)



# Let's make the labels.
new_customer = tk.Label(master=frame_1, text="New Customer")
new_customer_text = tk.Label(master=frame_1, text="Enter customer information and press Save                         "
                                                      "                                              ")

order_label = tk.Label(master=frame_4, text="Order")
number_label = tk.Label(master=frame_4, text="Number")
street_label = tk.Label(master=frame_4, text="Street")
town_label = tk.Label(master=frame_4, text="Town")
name_label = tk.Label(master=frame_4, text="Name")
price_label = tk.Label(master=frame_4, text="Price")
contact_label = tk.Label(master=frame_4, text="Contact")
interval_label = tk.Label(master=frame_4, text="Interval")
notes_label = tk.Label(master=frame_4, text='Notes')
status_label = tk.Label(master=frame_4, text="Status")
round_label = tk.Label(master=frame_4, text="Round Name")
advertising_label = tk.Label(master=frame_4, text="Advertising Method Used")




# Let's make the entry fields + RadioButton + Textfield

order_entry = ttk.Combobox(master=frame_4, state='readonly')
order_entry['values'] = ('FB/txt', 'FB/call', 'F/txt', 'F/call', 'B/txt', 'B/call', 'FB', 'F', 'B')
order_entry.current(0)

number_entry = tk.Entry(master=frame_4)
street_entry = tk.Entry(master=frame_4)
town_entry = tk.Entry(master=frame_4)
name_entry = tk.Entry(master=frame_4)
price_entry = tk.Entry(master=frame_4)
contact_entry = tk.Entry(master=frame_4)

interval_entry = ttk.Combobox(master=frame_4, state='readonly')
interval_entry['values'] = ('30', '60')
interval_entry.current(0)

notes_entry = tk.Text(master=frame_4, width=30, height=2)

status_entry = ttk.Combobox(master=frame_4, state='readonly')
status_entry['values'] = ('Active', 'One Off', 'Inactive')
status_entry.current(0)

round_entry = tk.Entry(master=frame_4)

advertising_entry = ttk.Combobox(master=frame_4, state='readonly')
advertising_entry['values'] = ('Canvassing', 'Word of Mouth', 'Facebook', 'Yell', 'Web Site', 'Google search', 'Approached while working')
advertising_entry.current(0)

save_button = tk.Button(master=frame_1, text="Save", command=file_menu)



# bind save
window.bind('<Control-s>', file_saveas)

# Let's put the labels in a GRID geometry manager!
new_customer.grid(row=0, column=0, sticky='w')
new_customer_text.grid(row=1, column=0, sticky='w')

order_label.grid(row=1, column=0, sticky='w')
number_label.grid(row=2, column=0, sticky='w')
street_label.grid(row=3, column=0, sticky='w')
town_label.grid(row=4, column=0, sticky='w')
name_label.grid(row=5, column=0, sticky='w')
price_label.grid(row=6, column=0, sticky='w')
contact_label.grid(row=7, column=0, sticky='w')
interval_label.grid(row=8, column=0, sticky='w')
notes_label.grid(row=9, column=0, sticky='w')
status_label.grid(row=10, column=0, sticky='w')
round_label.grid(row=11, column=0, sticky='w')
advertising_label.grid(row=12, column=0, sticky='w')

# Let's put the entry fields in a GRID geometry manager!

order_entry.grid(row=1, column=1, sticky='e', pady=5)
number_entry.grid(row=2, column=1, sticky='e', pady=5)
street_entry.grid(row=3, column=1, sticky='e', pady=5)
town_entry.grid(row=4, column=1, sticky='e', pady=5)
name_entry.grid(row=5, column=1, sticky='e', pady=5)
price_entry.grid(row=6, column=1, sticky='e', pady=5)
contact_entry.grid(row=7, column=1, sticky='e', pady=5)
interval_entry.grid(row=8, column=1, sticky='e', pady=5)
notes_entry.grid(row=9, column=1, sticky='e', pady=5)
status_entry.grid(row=10, column=1, sticky='e', pady=5)
round_entry.grid(row=11, column=1, sticky='e', pady=5)
advertising_entry.grid(row=12, column=1, sticky='e', pady=5)

save_button.grid(row=1, column=0, sticky='e', pady=5, padx=5)
# Most importantly, GRID the frame
frame_1.grid(row=0)
frame_4.grid(row=1, column=0, sticky='w')
frame_5.grid(row=2, column=0, sticky='w')


window.mainloop()
