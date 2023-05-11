import pyudev
import plotly.graph_objs as go
from plotly.subplots import make_subplots

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='firmware')

data = []

while True:
    try:
        device = monitor.poll(timeout=5)
        if device.action == 'add':
            firmware = device.get('FIRMWARE')
            if firmware is not None:
                vendor = device.get('ID_VENDOR')
                model = device.get('ID_MODEL')
                data.append((vendor, model, firmware))
    except KeyboardInterrupt:
        break

fig = make_subplots(rows=len(data), cols=1, subplot_titles=[f'{d[0]} {d[1]}' for d in data])
for i, d in enumerate(data, start=1):
    fig.add_trace(go.Table(
        header=dict(values=['Property', 'Value']),
        cells=dict(values=[['Vendor', 'Model', 'Firmware'], [d[0], d[1], d[2]]])
    ), row=i, col=1)

fig.update_layout(title='BIOS Information')
fig.show()

fig.write_html("bios.html")
