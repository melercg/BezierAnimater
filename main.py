import numpy as np
import dash
from dash import dcc, html
from dash.dependencies import  Output, Input, State
import plotly.graph_objs as go



app = dash.Dash(__name__)

control_points = [
    {"x": 0.2, "y": 0.8},
    {"x": 0.4, "y": 0.6},
    {"x": 0.6, "y": 0.4},
    {"x": 0.8, "y": 0.2},
]


def calc_bezier_points(c_points , sample_point):
    x_point = ((1-sample_point) ** 3 )* c_points[0]["x"] + \
                3 * ((1-sample_point) ** 2) * sample_point * c_points[1]["x"] + \
                    3 * ((1-sample_point) * (sample_point**2))*c_points[2]["x"] + \
                        (sample_point ** 3) * c_points[3]["x"]

    y_point = ((1 - sample_point) ** 3) * c_points[0]["y"] + \
              3 * ((1 - sample_point) ** 2) * sample_point * c_points[1]["y"] + \
              3 * ((1 - sample_point) * (sample_point ** 2)) * c_points[2]["y"] + \
              (sample_point ** 3) * c_points[3]["y"]


    return (x_point,y_point)

def bezier_curve(control_points, samples):
    sample_points = np.linspace(0,1,samples)
    curve = []
    for point in sample_points:
        x,y = calc_bezier_points(control_points,point)
        curve.append((x,y))


    return zip(*curve)





app.layout = html.Div([


    html.H1("Bezier Animater", style={"textAlign":"center","font-family":"Arial","background-color":"#2d2d2d","padding":"30px","color":"white"}),

    html.H4(children="Melisa Erocağı | 2020123113 ", style={"textAlign":"center","font-family":"Arial"})
    ,




    dcc.Graph(id="bezier-graph"),

    html.Div([html.Button("Play Circle", id="circle-ply-btn", n_clicks=0,
                          style={"margin": "15px", "font-size": "18px", "border": "2px solid #ca2517",
                                 "background-color": "transparent", "border-radius": "8px"}),
              html.Button("Stop Circle", id="circle-stp-btn", n_clicks=0,
                          style={"margin": "15px", "font-size": "18px", "border": "2px solid #ca2517",
                                 "background-color": "transparent", "border-radius": "8px"}),
              html.Button("Reset Circle", id="circle-rst-btn", n_clicks=0,
                          style={"margin": "15px", "font-size": "18px", "border": "2px solid #ca2517",
                                 "background-color": "transparent", "border-radius": "8px"}),
              ], style={"display": "flex", "justifyContent": "center", "alignItems": "center"}),




    html.Div([
            html.Div([
                html.H4(f"Control Point {i + 1}"),
                html.Label("X:"),
                dcc.Slider(
                    id=f"point-{i}-x",
                    min=0, max=1, step=0.01, value=point["x"],
                    marks={0: "0", 0.5: "0.5", 1: "1"}
                ),
                html.Label("Y:"),
                dcc.Slider(
                    id=f"point-{i}-y",
                    min=0, max=1, step=0.01, value=point["y"],
                    marks={0: "0", 0.5: "0.5", 1: "1"}
                ),
            ], style={"marginBottom": "20px"}) for i, point in enumerate(control_points)
        ], style={"width": "100%","display": "flex",
                                                    "justifyContent": "center",
                                                    "alignItems": "center",
                                                    "gap":"40px",
                                                    "margin": "10px"}),


        html.Div([


                html.Div([
                    html.Label("Wind Speed"),
                    dcc.Slider(id="wind-speed", min=0, max=10, step=0.1, value=0)
                ], style={"margin": "auto"}),

                html.Div([
                    html.Label("Wind Direction"),
                    dcc.Dropdown(
                        id="wind-direction",
                        options=[
                            {"label": "North", "value": "north"},
                            {"label": "South", "value": "south"},
                            {"label": "East", "value": "east"},
                            {"label": "West", "value": "west"}
                        ],
                        value="north"
                    )
                ], style={"margin": "20px"}),

                html.Div([
                    html.Label("Gravity Force"),
                    dcc.Slider(id="gravity-force", min=0, max=10, step=0.1, value=0)
                ], style={"margin": "20px"}),


            ]),
        dcc.Interval(id="animation-interval", interval=50, n_intervals=0,disabled=True),
        dcc.Store(id="circle-position", data=0),
        dcc.Store(id="animation-active", data=False),


        ],





    style={"width":"70%", "height":"100%","margin":"auto"})






@app.callback(
        Output("bezier-graph","figure"),
                Input("animation-interval", "n_intervals"),
                Input("circle-rst-btn","n_clicks"),


                Input("wind-speed", "value"),
                Input("wind-direction", "value"),
                Input("gravity-force", "value"),

                [Input(f"point-{i}-x", "value") for i in range(4)] +
                [Input(f"point-{i}-y", "value") for i in range(4)] ,

                State("circle-position", "data"),
                State("animation-active", "data") )
def BezierGraphHandler(n_intervals,reset_anim_clicks,wind_speed, wind_direction, gravity_force,*values):
    print(wind_speed)
    points = [{"x": values[i], "y": values[i + 4]} for i in range(4)]
    curve_x_axis, curve_y_axis  = bezier_curve(points,100)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=curve_x_axis, y=curve_y_axis,
        mode="lines", name="Curve",
        line=dict(color="#3d3d3d", width=3)
    ))
    if reset_anim_clicks > 0:
        t = 0
    else:
        t = n_intervals * 0.01 % 1

    x = (1 - t) ** 3 * (points[0]["x"] )+ \
        3 * (1 - t) ** 2 * t * (points[1]["x"] )+ \
        3 * (1 - t) * t ** 2 * (points[2]["x"] )+ \
        t ** 3 * (points[3]["x"] )
    y = (1 - t) ** 3 * ( points[0]["y"] ) + \
        3 * (1 - t) ** 2 * t * ( points[1]["y"] )+ \
        3 * (1 - t) * t ** 2 * ( points[2]["y"] )+ \
        t ** 3 *( points[3]["y"] )

    if wind_direction == "north":
        y -= wind_speed * 0.01
    elif wind_direction == "south":
        y += wind_speed * 0.01
    elif wind_direction == "east":
        x += wind_speed * 0.01
    elif wind_direction == "west":
        x -= wind_speed * 0.01

    y -= gravity_force * 0.01

    fig.add_trace(go.Scatter(
        x=[x], y=[y],
        mode="markers", name="Circle",
        marker=dict(color="green", size=20)
    ))
    fig.add_trace(go.Scatter(
        x=[p["x"] for p in points], y=[p["y"] for p in points],
        mode="markers+lines", name="Control Points",
        marker=dict(color="#ca2517", size=10),
        line=dict(dash="dash", color="red")
    ))



    fig.update_layout(
        xaxis=dict(range=[0, 1], zeroline=False),
        yaxis=dict(range=[0, 1], zeroline=False),

        height=600
    )



    return fig


@app.callback(
    Output("animation-interval", "disabled"),
    Output("circle-position", "data"),
    Output("animation-active", "data"),
    Input("circle-ply-btn", "n_clicks"),
    Input("circle-stp-btn", "n_clicks"),
    Input("circle-rst-btn", "n_clicks"),
    State("circle-position", "data"),
    State("animation-active", "data")
)
def control_animation(play_clicks, pause_clicks, reset_clicks, circle_position, animation_active):
    ctx = dash.callback_context
    if not ctx.triggered:
        return dash.no_update

    trigger = ctx.triggered[0]["prop_id"].split(".")[0]

    if trigger == "circle-ply-btn":
        return False, circle_position, True
    elif trigger == "circle-stp-btn":
        return True, circle_position, False
    elif trigger == "circle-rst-btn":
        return True, 0, False

    return dash.no_update

if __name__ == '__main__':
    app.run(debug=True)
