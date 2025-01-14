import asyncio

from toga.fonts import CURSIVE, FANTASY, MONOSPACE, SANS_SERIF, SERIF, SYSTEM
from toga_iOS.libs import NSRunLoop


class BaseProbe:
    def assert_font_family(self, expected):
        assert self.font.family == {
            CURSIVE: "Apple Chancery",
            FANTASY: "Papyrus",
            MONOSPACE: "Courier New",
            SANS_SERIF: "Helvetica",
            SERIF: "Times New Roman",
            SYSTEM: ".AppleSystemUIFont",
        }.get(expected, expected)

    async def redraw(self, message=None, delay=None):
        """Request a redraw of the app, waiting until that redraw has completed."""
        # If we're running slow, wait for a second
        if self.app.run_slow:
            print("Waiting for redraw" if message is None else message)
            delay = 1

        if delay:
            await asyncio.sleep(delay)
        else:
            # Running at "normal" speed, we need to release to the event loop
            # for at least one iteration. `runUntilDate:None` does this.
            NSRunLoop.currentRunLoop.runUntilDate(None)
