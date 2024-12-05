from nicegui import ui

class Demo:
    def __init__(self):
        self.number = 1

demo = Demo()
v = ui.checkbox('visible', value=True)
with ui.column().bind_visibility_from(v, 'value'):
    ui.slider(min=1, max=10).bind_value(demo, 'number')
    ui.toggle({1: 'agua', 2: 'coca-cola', 3: 'pepsi',4:'horchata'}).bind_value(demo, 'number')
    ui.number().bind_value(demo, 'number')

ui.run()
