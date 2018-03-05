from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
     line: add a line to the edge matrix -
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix -
	 scale: create a scale matrix,
	    then multiply the transform matrix by the scale matrix -
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix,
	    then multiply the transform matrix by the translation matrix -
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    # File I/O
    f = open(fname,'r')
    scriptfile = f.read()

    commands = scriptfile.split('\n')
    for i in range(len(commands)):
        if commands[i] == 'line':
            nextline = commands[i + 1]
            args = nextline.split(" ")
            x0 = int(args[0])
            y0 = int(args[1])
            z0 = int(args[2])
            x1 = int(args[3])
            y1 = int(args[4])
            z1 = int(args[5])
            add_edge(points, x0, y0, z0, x1, y1, z1)
        elif commands[i] == 'ident':
            ident(transform)
        elif commands[i] == 'scale':
            nextline = commands[i + 1]
            args = nextline.split(" ")
            sx = int(args[0])
            sy = int(args[1])
            sz = int(args[2])
            smatrix = make_scale(sx, sy, sz)
       	    matrix_mult( smatrix, transform )
        elif commands[i] == 'move':
            nextline = commands[i + 1]
            args = nextline.split(" ")
            tx = int(args[0])
            ty = int(args[1])
            tz = int(args[2])
            tmatrix = make_translate(tx, ty, tz)
       	    matrix_mult( tmatrix, transform )
        elif commands[i] == 'rotate':
            nextline = commands[i + 1]
            args = nextline.split(" ")
            axis = args[0]
            theta = int(args[1])
            if axis == 'x':
                rmatrix = make_rotX(theta)
            elif axis == 'y':
                rmatrix = make_rotY(theta)
            elif axis == 'z':
                rmatrix = make_rotZ(theta)
       	    matrix_mult( rmatrix, transform )
        elif commands[i] == 'apply':
            matrix_mult(transform, points)
        elif commands[i] == 'display':
            for r in range(len(points)):
				for c in range(4):
					points[r][c] = int(points[r][c])
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
        elif commands[i] == 'save':
            nextline = commands[i + 1]
            args = nextline.split(" ")
            filename = args[0]
            draw_lines(points, screen, color)
            save_extension(screen, filename)
        elif commands[i] == 'quit':
            break
    f.close()
