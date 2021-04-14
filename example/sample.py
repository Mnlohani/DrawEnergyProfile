from eprofile.pes import PES, set_figure, Stationary_line, draw_lines, connect_stationary_lines, Multi_level, draw_multilines

# set PES Diagram dimension
# set_figure(length=15, width=6, y_label=None,dpi=300, y_label_fontsize=15)

fig, ax = set_figure(15, 6, '$\Delta$E / kcal mol$^{-1}$')

# make object of PES to set common property of stationary lines
# tweek the parameters to get a desired output with respect to
# figure size.
# PES(x_start=1.35, dim=0.5, v_offset=1.0, line_space=0.5)

sample_pes = PES()

# Approach: first make single line of stationary levels then add multilevel lines
# stationary line creation
# Stationary_line(line_index, energy, label, linewidth=2,
#            txt_font=12, linecolor='black', txtcolor='black')

l1 = Stationary_line(0, 0.0, 'R1 + R2')
l2 = Stationary_line(1, 10.0, 'TS 1')
l3 = Stationary_line(2, 8.0, 'product')

draw_lines(ax)

connect_stationary_lines(ax, l1, l2)
connect_stationary_lines(ax, l2, l3)

# draw multi level
# Multi_level(line_index, energy, left_line_object, left_line_offset, label=None, dim=0.6, linewidth=2,
#                 txt_font=12, linecolor='black', txtcolor='black')
m1 = Multi_level(3, 15.0, l2, 0.1, 'INT 1', dim=0.1, linecolor='red', txtcolor='red')
m2 = Multi_level(4, 13.0, m1, 0.1, 'TS 2', dim=0.1, linecolor='red', txtcolor='red')

draw_multilines(ax)

connect_stationary_lines(ax, l2, m1, linecolor='red')
connect_stationary_lines(ax, m1, m2, linecolor='red')
connect_stationary_lines(ax, m2, l3, linecolor='red')

# save figure with extension
fig.savefig('ep_sample.png')
