# uposatha-inky

Display the details of the upcoming uposatha on a Pimoroni InkyWhat e-Ink display. It uses my new `uposatha` package to get the lunar calendar details and renders them as an image. I use `systemd` to update the display every day at midnight.

An example of what is shown on the e-ink display:

![tmp4wm8dnim](https://github.com/jhanarato/uposatha-inky/assets/872786/25c5dc7f-16ca-40f2-80ae-52b3a6941f9a)

You can play around with the code without the hardware. The code detects when the Inky is not available and uses the system image viewer instead. I'm still working on alternate views for when today is the uposatha or a holiday.
