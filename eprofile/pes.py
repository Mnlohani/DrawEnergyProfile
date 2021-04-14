import matplotlib.pyplot as plt

obj_list = []
obj_multi_list = []


def draw_line(ax, line_obj):
    '''
    draw horizontal line for a stationary level object
    :param ax: figure axis
    :param line_obj: stationary level object
    :return: None
    '''
    ax.hlines(line_obj.energy, line_obj.left, line_obj.right, lw=line_obj.linewidth, color=line_obj.linecolor)
    ax.text(line_obj.left + line_obj.dim / 2., line_obj.energy - line_obj.v_offset, line_obj.label,
            fontsize=line_obj.txt_font,
            color=line_obj.txtcolor, horizontalalignment='center', verticalalignment='top')
    ax.text(line_obj.left + line_obj.dim / 2., line_obj.energy + line_obj.v_offset, str(line_obj.energy),
            fontsize=line_obj.txt_font,
            color=line_obj.txtcolor, horizontalalignment='center', verticalalignment='bottom')

    pass


def draw_lines(ax):
    '''
    draws horizontal lines for all stationary level objects
    :param ax: figure axis
    :return: None
    '''
    for eachline in obj_list:
        draw_line(ax, eachline)


def draw_multilines(ax):
    '''draw horizontal line for a stationary level object
    but differs from draw_line()
    draw_line() plots all horizontal lines for reaction profile
    assuming one line of reaction
    draw_multilines() draws other stationary levels showing another energy profile
    pls refer example (shown as red)
    :param ax: figure axis
    :return: None
    '''
    for eachline in obj_multi_list:
        draw_line(ax, eachline)


def connect_stationary_lines(ax, line_1, line_2, linecolor='black', linestyle='dashed'):
    '''
    connects stationary levels
    :param ax: figure axis
    :param line_1: left level
    :param line_2: right level to be connected
    :param linecolor: color of connecting line
    :param linestyle: style of connecting line
    :return:
    '''
    ax.plot([line_1.right, line_2.left], [line_1.energy, line_2.energy], color=linecolor, linestyle=linestyle,
            dashes=(15, 10), linewidth=0.4)
    pass


def set_figure(length=15, width=6, y_label="$\Delta$E / kcal mol$^{-1}$", dpi=300, y_label_fontsize=20):
    '''
    sets energy diagram properties
    :param length, width : diagram length , width
    :param y_label:
    :param dpi: dpi of output diagram
    :param y_label_fontsize: y_label fontsize
    :return: figure, axis
    '''
    fig, ax = plt.subplots(figsize=(length, width), dpi=dpi)
    ax.set_ylabel(y_label, fontsize=y_label_fontsize)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('left')
    ax.set_xticklabels([])
    ax.tick_params(axis='y', which='major', labelsize=14)
    return fig, ax


class PES:
    '''
    for global properties of stationary levels used i n diagrams
    '''
    def __init__(self, x_start=1.35, dim=0.5, v_offset=1.0, line_space=0.5):
        '''

        :param x_start: left indent of first stationary level
        :param dim: length of stationary level
        :param v_offset: spacing between level and corresponding label
        :param line_space: spacing between two statinary levels
        '''
        self.x_start = x_start
        self.dim = dim
        self.v_offset = v_offset
        self.line_space = line_space


class Stationary_line(PES):
    '''class for stationary level'''

    def __init__(self, line_index, energy=None, label=None, linewidth=2,
                 txt_font=12, linecolor='black', txtcolor='black'):
        '''
        :param line_index: stationary level index
        :param energy: energy of stationary level
        :param label: label for stationary level
        :param linewidth: stationary level width in diagram
        :param txt_font: font size
        :param linecolor: color of level
        :param txtcolor: color for label
        '''
        super().__init__()
        self.line_index = line_index
        self.energy = energy
        self.linewidth = linewidth
        self.label = label
        self.txt_font = txt_font
        self.linecolor = linecolor
        self.txtcolor = txtcolor
        if self.line_index == 0:
            self.left = self.x_start
        else:
            self.left = self.x_start + self.line_index * self.dim + self.line_index * self.line_space
        self.right = self.left + self.dim
        obj_list.append(self)


class Multi_level(PES):
    ''' class for drawing multiple level (refer example shown with red)'''
    def __init__(self, line_index, energy, left_line_object, left_line_offset, label=None, dim=0.6, linewidth=2,
                 txt_font=12, linecolor='black', txtcolor='black'):
        '''
        :param left_line_object: left hand side connecting level
        :param left_line_offset: space from left hand side connecting level
        :param dim: length of level
        OTHER PARAMETER DESCRIPTION same as Stationary_line
        '''
        super().__init__()
        self.line_index = line_index
        self.energy = energy
        self.label = label
        self.connect_left_index = left_line_object.line_index
        self.left_line_offset = left_line_offset
        self.dim = dim
        self.energy = energy
        self.linewidth = linewidth
        self.txt_font = txt_font
        self.linecolor = linecolor
        self.txtcolor = txtcolor
        self.left = left_line_object.right + left_line_offset
        self.right = self.left + dim
        obj_multi_list.append(self)

if __name__ == "__main__":
    pass