import sys
import turtle

from os import path

from json.decoder import JSONDecodeError
from yaml import YAMLError

from .figures.simple import Circle, Square, Rectangle
from .figures.polygon import RegularPolygon, Triangle, Pie

from .loaders import JSONLoader, YAMLoader

FIGURE_TYPES = {
    'circle': Circle,
    'square': Square,
    'rectangle': Rectangle,
    'triangle': Triangle,
    'polygon': RegularPolygon,
    'pie': Pie
}

FILE_EXTENSIONS = {
    'json': JSONLoader,
    'yaml': YAMLoader
}


def main():
    if len(sys.argv) < 2:
        print('Usage: {} <input-file>'.format(sys.argv[0]))
        return 1

    try:
        input_data = load_input_data(sys.argv[1])
        figures = create_figures(input_data)
        draw_figures(figures)
    except IOError as ioe:
        print(str(ioe))
        return 2
    except JSONDecodeError as jde:
        print('Failed to parse JSON ' + str(jde))
        return 2
    except YAMLError as ye:
        print('Failed to parse YAML ' + str(ye))
        return 2


def load_input_data(input_filename):
    extension = path.splitext(input_filename)[1][1:]

    if extension in FILE_EXTENSIONS:
        loader_class = FILE_EXTENSIONS[extension](input_filename)
        input_data = loader_class.load_data()
    else:
        raise ValueError('Unsupported format: {}'.format(extension))

    return input_data


def create_figures(input_data):
    figures = []

    for f_info in input_data:
        figure_type = f_info['type']

        if figure_type in FIGURE_TYPES:
            figure_class = FIGURE_TYPES[figure_type]
            figures.append(figure_class(**f_info))
        else:
            raise ValueError('Unsupported figure: {}'.format(figure_type))

    return figures


def draw_figures(figures):
    for figure in figures:
        t = turtle.Turtle()
        t.speed('slow')
        figure.draw_figure(t)

    turtle.exitonclick()
    

if __name__ == "__main__":
    sys.exit(main())
