# Are you asleep?

Due to my personal design I often fall asleep while watching movies late at night. That's why I've chosen to make an app that will ask me if I'm asleep and based on response will or will not shutdown the system.

## GUI - tkinter library

When the clock hit 11PM or any hour up to 6AM there will be a window with ```Yes/No``` options and content just like 'Are you asleep?' It won't be anything special just basic alert that tkinter provides

## Logic behind it

Local time of PC will be main variable. As previously said each hour such pop-up will show and give user 10 minutes to respond. Unless PC will be shutted down. When user chose "YES" pop-up will disapear and reapear the next hour.