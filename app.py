from flask import Flask, render_template
from data import SourceData

app = Flask(__name__)

source = SourceData()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/s0_l1_input')
def s0_l1_input():
    d0,d1,d2,d3,d4 = source.seg_0_lstm_1_w_i
    return render_template('s0_l1_input.html', d0=d0,d1=d1,d2=d2,d3=d3,d4=d4)

@app.route('/s1_l1_input')
def s1_l1_input():
    d0,d1,d2,d3,d4 = source.seg_1_lstm_1_w_i
    return render_template('s1_l1_input.html', d0=d0,d1=d1,d2=d2,d3=d3,d4=d4)

@app.route('/s2_l1_input')
def s2_l1_input():
    d0,d1,d2,d3,d4 = source.seg_2_lstm_1_w_i
    return render_template('s2_l1_input.html', d0=d0,d1=d1,d2=d2,d3=d3,d4=d4)

@app.route('/s3_l1_input')
def s3_l1_input():
    d0,d1,d2,d3,d4 = source.seg_3_lstm_1_w_i
    return render_template('s3_l1_input.html', d0=d0,d1=d1,d2=d2,d3=d3,d4=d4)

@app.route('/s4_l1_input')
def s4_l1_input():
    d0,d1,d2,d3,d4 = source.seg_4_lstm_1_w_i
    return render_template('s4_l1_input.html', d0=d0,d1=d1,d2=d2,d3=d3,d4=d4)


# @app.route('/bar')
# def bar():
#     data = source.bar
#     return render_template('bar.html', title=data.title, data=data.values, legend=data.legend, xAxis=data.xAxis,
#                            unit=data.unit)


# @app.route('/bar_y')
# def bar_y():
#     data = source.bar_y
#     return render_template('bar_y.html', title=data.title, data=data.values, legend=data.legend, xAxis=data.xAxis,
#                            unit=data.unit)


# @app.route('/bar_polar')
# def bar_polar():
#     data = source.bar_polar
#     return render_template('bar_polar.html', title=data.title, data=data.values, legend=data.legend, xAxis=data.xAxis,
#                            unit=data.unit)


# @app.route('/bar_waterfall')
# def bar_waterfall():
#     data = source.bar_waterfall
#     return render_template('bar_waterfall.html', title=data.title, data=data.values, legend=data.legend,
#                            xAxis=data.xAxis, special=data.special,
#                            unit=data.unit)


# @app.route('/pie')
# def pie():
#     data = source.pie
#     return render_template('pie.html', title=data.title, data=data.values, legend=data.legend, unit=data.unit)


# @app.route('/pie_doughnut')
# def pie_doughnut():
#     data = source.pie_doughnut
#     return render_template('pie_doughnut.html', title=data.title, data=data.values, legend=data.legend, unit=data.unit)


# @app.route('/china')
# def china():
#     data = source.china
#     return render_template('china.html', title=data.title, data=data.values, unit=data.unit)


# @app.route('/wordcloud')
# def wordcloud():
#     data = source.wordcloud
#     return render_template('wordcloud.html', title=data.title, data=data.values, unit=data.unit)


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
