# uposatha-inky

Display the details of the upcoming uposatha on a Pimoroni InkyWhat e-Ink display. It uses my new `uposatha` package to get the lunar calendar details and renders them as an image. I use `systemd` to update the display every day at midnight.

You can play around with the code without the hardware. The code detects when the Inky is not available and uses the system image viewer instead.

An example of what is shown on the e-ink display:

### Between Uposathas
![tmph09kv3yi](https://github.com/jhanarato/uposatha-inky/assets/872786/19b7d5bd-edda-4386-918b-fa0be8dac930)

### On Full and New Moon Days

![tmp5j8n1i15](https://github.com/jhanarato/uposatha-inky/assets/872786/71399d4e-552a-427a-9dc7-c0fd0ad87570)


### On Holidays
![tmpf81oy_vp](https://github.com/jhanarato/uposatha-inky/assets/872786/518baa95-2e10-4e59-ad68-fee60684d91b)

### Notes on the Code

I've spent the better part of a year on this. It has been an exercise in exploratory design and test driven development. There are some interesting features including:

- A context manager, `DrawingViewer` to take care of viewing things. It provides an `ImageDraw` that can be drawn on and automatically displayed. It's especially useful for experimenting with PIL as it takes care of setting up the image and then showing it afterward.
- A numeric type `DesignUnits` to handle conversions between various font metrics.
- `components.Glyph` determines the offsets to position a letter taking into account the left side and top side bearings. This was hard. Along the way my code was dramatically slowed down by using the `glyphtools` package, so the required values are precalculated.
