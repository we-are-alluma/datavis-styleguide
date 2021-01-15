import altair as alt


def altair_theme():
    return {
        "width": 600,
        "height": 400,
        "autosize": "pad",
        "config": {
            "padding": 10,
            "geoshape": {"fill": "#D9D9D6", "stroke": "#2B3E4B", "strokeWidth": 0.5},
            "arc": {"fill": "#282828"},
            "area": {"fill": "#282828"},
            "axisBand": {"grid": False},
            "axisBottom": {
                "domain": False,
                "domainColor": "black",
                "domainWidth": 3,
                "grid": True,
                "gridColor": "#C9C9C9",
                "gridWidth": 1,
                "labelFontSize": 12,
                "labelFont": "Helvetica",
                "labelPadding": 8,
                "labelAngle": 0,
                "tickColor": "#282828",
                "tickSize": 10,
                "titleFontSize": 12,
                "titlePadding": 10,
                "titleFont": "Helvetica",
                "title": "",
            },
            "axisLeft": {
                "domainColor": "#282828",
                "domainWidth": 1,
                "gridColor": "#C9C9C9",
                "gridWidth": 1,
                "labelFontSize": 12,
                "labelFont": "Helvetica",
                "labelPadding": 8,
                "tickColor": "#282828",
                "tickSize": 10,
                "tickCount": 10,
                "ticks": True,
                "titleFontSize": 14,
                "titleFontStyle": "italic",
                "titlePadding": 10,
                "titleFont": "Helvetica",
                "titleAngle": 0,
                "titleX": -70,
                "titleY": -18,
                "titleAnchor": "start",
            },
            "axisRight": {
                "domainColor": "#282828",
                "domainWidth": 1,
                "gridColor": "#C9C9C9",
                "gridWidth": 1,
                "labelFontSize": 12,
                "labelFont": "Helvetica",
                "labelPadding": 4,
                "tickColor": "#282828",
                "tickSize": 10,
                "ticks": True,
                "titleFontSize": 12,
                "titlePadding": 10,
                "titleFont": "Helvetica",
            },
            "axisTop": {
                "domain": False,
                "domainColor": "black",
                "domainWidth": 3,
                "grid": True,
                "gridColor": "#C9C9C9",
                "gridWidth": 1,
                "labelFontSize": 12,
                "labelFont": "Helvetica",
                "labelPadding": 4,
                "tickColor": "#282828",
                "tickSize": 10,
                "titleFontSize": 12,
                "titlePadding": 10,
                "titleFont": "Helvetica",
            },
            "background": "#FFFEFE",
            "group": {"fill": "#FFFAFA"},
            "legend": {
                "labelFontSize": 12,
                "labelFont": "Helvetica",
                "labelLimit": 500,
                "padding": 5,
                "symbolSize": 200,
                "symbolType": "square",
                "titleFontSize": 18,
                "titlePadding": 5,
                "titleFont": "Helvetica",
                "titleLimit": 400,
            },
            "line": {"color": "#282828", "stroke": "#282828", "strokeWidth": 3},
            "rule": {"color": "#282828", "stroke": "#282828", "strokeWidth": 3},
            "tick": {"color": "#282828", "stroke": "#282828", "strokeWidth": 1},
            "trail": {
                "color": "#282828",
                "stroke": "#282828",
                "strokeWidth": 0,
                "size": 5,
            },
            "path": {"stroke": "#282828", "strokeWidth": 0.5},
            "point": {"filled": True},
            "rect": {"fill": "#A20C4B", "opacity": 0.3},
            "range": {
                "category": [
                    "#dc0d7a",
                    "#02a3cd",
                    "#e4a100",
                    "#dc0d12",
                    "#0DDC6F",
                    "#074a7e",
                    "#e46800",
                    "#aa3594",
                    "#a20c4b",
                ],
                "diverging": [
                    "#dc0d12",
                    "#e9686b",
                    "#fbe1e1",
                    "#dff4f9",
                    "#81d1e6",
                    "#03a3cd",
                ],
                "heatmap": [
                    "#fff7fd",
                    "#ffdbf7",
                    "#ffb9ec",
                    "#ff91dc",
                    "#ff67c7",
                    "#f83faf",
                    "#ef1d95",
                    "#e4007c",
                ],
            },
            "symbol": {"opacity": 1, "shape": "circle", "size": 40, "strokeWidth": 1},
            "style": {
                "bar": {"binSpacing": 2, "fill": "#282828", "stroke": False},
                "text": {
                    "font": "Helvetica",
                    "fontSize": 12,
                    "align": "right",
                    "fontWeight": 100,
                    "size": 10,
                },
            },
            "title": {
                "anchor": "start",
                "fontSize": 18,
                "fontWeight": 800,
                "font": "Helvetica",
                "offset": 10,
            },
            "view": {"stroke": False, "padding": 15},
            "header": {
                "fontWeight": 400,
                "labelFontSize": 12,
                "labelFont": "Helvetica",
                "titleFontSize": 14,
                "titleFont": "Helvetica",
                "title": " ",
                "titleBaseline": "bottom",
                "titleOffset": -30,
            },
        },
    }


alt.themes.register("custom_theme", altair_theme)
alt.themes.enable("custom_theme")