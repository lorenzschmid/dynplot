import matplotlib.pyplot as plt
from functools import partialmethod


class dplt():
    supported_fcns = ['plot']

    def __init__(self, refresh_rate=0.1):
        # Configure object
        self.refresh_rate = refresh_rate

        # Create figure and axis
        self.fig, self.ax = plt.subplots()

        # Set axis to auto-scale
        self.ax.set_autoscaley_on(True)

        self._initialized = False
        self._crnt_line = 0

    def _update(self, fcn, *args, **kwargs):
         # Create initial lines upon first calls
        if not self._initialized:
            lines = getattr(self.ax, fcn)(*args, **kwargs)

            if not hasattr(self, 'lines') or not self.lines:
                self.lines = lines
            else:
                for line in lines:
                    self.lines.append(line)

        # Reuse existing lines upon following calls
        else:
            # Remove possible line styling indications from *args
            args = list(filter(lambda x: not isinstance(x, str), args))

            # Create set of lines to be updated
            nbr_lines = len(args) // 2

            # Only update parts of the lines
            if nbr_lines < len(self.lines):
                line_ids = list(range(self._crnt_line,
                                      self._crnt_line + nbr_lines))
                line_ids = [i % len(self.lines) for i in line_ids]

                self._crnt_line = (line_ids[-1] + 1) % len(self.lines)

            # Update all lines
            else:
                line_ids = list(range(0, len(self.lines)))
                self._crnt_line = 0

            # Apply changes to set of lines to be updated
            for i, line_id in enumerate(line_ids):
                # Set line values
                self.lines[line_id].set_xdata(args[2*i])
                self.lines[line_id].set_ydata(args[2*i+1])

                # Set line attributes if existing
                for key, value in kwargs.items():
                    getattr(self.lines[line_id], 'set_' + key)(value)

    def __getattr__(self, name):
        if name in self.supported_fcns:

            def wrapper(*args, **kwargs):
                return self._update(name, *args, **kwargs)

            return wrapper

    def show(self, permanent=False, *args, **kwargs):
        self._initialized = True

        # Rescale
        self.ax.relim()
        self.ax.autoscale_view()

        # Draw and flush
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

        if permanent:
            plt.show(*args, **kwargs)
        else:
            plt.pause(self.refresh_rate)
