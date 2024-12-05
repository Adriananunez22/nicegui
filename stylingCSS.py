from nicegui import ui

ui.icon('thumb_up', color='red').classes('text-7xl')
ui.markdown('This is **Markdown**.')
ui.html('This is <strong>HTML</strong>.')
with ui.row():
    ui.label('adriana').style('color:rgb(189, 148, 155) ; font-weight: bold; font family: Century-Gothic')
    ui.label('Tailwind').classes('arial')
    ui.label('Quasar').classes('q-ml-xl')
ui.link('NiceGUI on GitHub', 'https://github.com/zauberzeug/nicegui')

ui.run()