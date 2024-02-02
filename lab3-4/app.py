from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    shape = request.form.get('shape')
    precision = request.form.get('precision')

    if shape == 'cube':
        length_str = request.form.get('length')
        if length_str and length_str.strip():
            length = float(length_str)
            volume = calculate_cube_volume(length, precision)
        else:
            volume = None
    elif shape == 'sphere':
        radius_str = request.form.get('radius')
        if radius_str and radius_str.strip():
            radius = float(radius_str)
            volume = calculate_sphere_volume(radius, precision)
        else:
            volume = None
    else:
        volume = None

    return render_template('result.html', shape=shape, volume=volume, precision=precision)

def calculate_cube_volume(length, precision):
    volume = length**3
    return "{:.{}f}".format(volume, precision)

def calculate_sphere_volume(radius, precision):
    import math
    volume = (4/3) * math.pi * radius**3
    return "{:.{}f}".format(volume, precision)

if __name__ == '__main__':
    app.run(debug=True)
