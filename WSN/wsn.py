#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Wsn
# Generated: Fri Feb  5 07:13:22 2021
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import epy_block_0
import epy_block_0_0
import epy_block_0_0_0
import pmt
import sip
import sys
from gnuradio import qtgui


class wsn(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Wsn")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Wsn")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "wsn")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.nfilter = nfilter = 32
        self.MAP = MAP = [0,1,2,3]
        self.A = A = 4
        self.trate = trate = 1024000
        self.sin3d = sin3d = 8
        self.sin2d = sin2d = 4
        self.sin1d = sin1d = 2
        self.samp_rate = samp_rate = 1024000
        self.rrtaps = rrtaps = firdes.root_raised_cosine(nfilter , nfilter , 1/float(sps) , 0.35 , 11 *sps* nfilter)
        self.m = m = 4
        self.k = k = 2
        self.delay = delay = 1.0
        self.d = d = 10
        self.code6 = code6 = '1101100101010111000100011100000100100011000000001011011100001010'
        self.code5 = code5 = '0011101000111010001110101010000101110010110111100100010101000111'
        self.code4 = code4 = '1101010100011011100011000101100001010111110111100101101110011011'
        self.code3 = code3 = '1101100101010111000100011100000100100011000000001011011100001010'
        self.code2 = code2 = '0011101000111010001110101010000101110010110111100100010101000111'
        self.code1 = code1 = '1101010100011011100011000101100001010111110111100101101110011011'
        self.cmaGain = cmaGain = 0.01

        self.c3 = c3 = digital.constellation_calcdist(([-A-A*1j, -A+A*1j, A+A*1j, A-A*1j]), (MAP), 4, 1).base()


        self.c2 = c2 = digital.constellation_calcdist(([-A-A*1j, -A+A*1j, A+A*1j, A-A*1j]), (MAP), 4, 1).base()


        ##################################################
        # Blocks
        ##################################################
        self.qtgui_freq_sink_x_0_2_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Node 3(Data from Transmitter 2) : Modulation", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_2_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_2_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_2_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_2_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_2_0_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_2_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_2_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_2_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_2_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_2_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_2_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_2_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_2_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_2_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_2_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_2_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_2_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_2_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_2_0_0_win)
        self.qtgui_freq_sink_x_0_2_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Node 3(Data from Transmitter 1) : Modulation", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_2_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_2_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_2_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_2_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_2_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_2_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_2_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_2_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_2_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_2_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_2_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_2_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_2_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_2_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_2_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_2_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_2_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_2_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_2_0_win)
        self.qtgui_freq_sink_x_0_2 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Node 2(Data from Transmitter 1) : Modulation", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_2.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_2.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_2.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_2.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_2.enable_grid(True)
        self.qtgui_freq_sink_x_0_2.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_2.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_2.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_2.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_2.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_2.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_2.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_2.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_2.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_2_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_2.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_2_win)
        self.qtgui_freq_sink_x_0_1_0_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Node 4(Data from Transmitter 1) : Costas Loop", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_1_0_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1_0_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_1_0_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1_0_1.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_1_0_1.enable_grid(True)
        self.qtgui_freq_sink_x_0_1_0_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1_0_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1_0_1.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_1_0_1.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_1_0_1.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1_0_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1_0_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1_0_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_0_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_1_0_1_win)
        self.qtgui_freq_sink_x_0_1_0_0_0_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Node 4(Data from Transmitter 3 which is received from Transmitter 2) : Costas Loop", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_1_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1_0_0_0_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_1_0_0_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1_0_0_0_0_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_1_0_0_0_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_1_0_0_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1_0_0_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1_0_0_0_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_1_0_0_0_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_1_0_0_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_1_0_0_0_0_0_win)
        self.qtgui_freq_sink_x_0_1_0_0_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Node 4(Data from Transmitter 3 which is received from Transmitter 1) : Costas Loop", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_1_0_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1_0_0_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_1_0_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1_0_0_0_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_1_0_0_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_1_0_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1_0_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1_0_0_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_1_0_0_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_1_0_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_0_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_1_0_0_0_0_win)
        self.qtgui_freq_sink_x_0_1_0_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Node 4(Data from Transmitter 2) : Costas Loop", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_1_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1_0_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_1_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1_0_0_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_1_0_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_1_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1_0_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_1_0_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_1_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_1_0_0_0_win)
        self.qtgui_freq_sink_x_0_1_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Node 3(Data from Transmitter 2) : Costas Loop", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_1_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_1_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1_0_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_1_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_1_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_1_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_1_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_1_0_0_win)
        self.qtgui_freq_sink_x_0_1_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Node 3(Data from Transmitter 1) : Costas Loop", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_1_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_1_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_1_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_1_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_1_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_1_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_1_0_win)
        self.qtgui_freq_sink_x_0_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Node 2(Data from Transmitter 1) : Costas Loop", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_1.enable_grid(True)
        self.qtgui_freq_sink_x_0_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_1.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_1.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_1_win)
        self.qtgui_freq_sink_x_0_0_1_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Node 4(Data from Transmitter 1) : Polyphase", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_1_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_1_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_1_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_1_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_1_1.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_0_1_1.enable_grid(True)
        self.qtgui_freq_sink_x_0_0_1_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_1_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_1_1.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0_1_1.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0_1_1.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_1_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_1_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_1_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_1_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_1_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_1_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_1_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_1_1_win)
        self.qtgui_freq_sink_x_0_0_1_0_0_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Node 4(Data from Transmitter 3 which is received from Transmitter 2) : Polyphase", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_1_0_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_1_0_0_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_1_0_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_1_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_1_0_0_0_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_0_1_0_0_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0_1_0_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_1_0_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_1_0_0_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0_1_0_0_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0_1_0_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_1_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_1_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_1_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_1_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_1_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_1_0_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_1_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_1_0_0_0_0_win)
        self.qtgui_freq_sink_x_0_0_1_0_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Node 4(Data from Transmitter 3 which is received from Transmitter 1) : Polyphase", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_1_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_1_0_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_1_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_1_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_1_0_0_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_0_1_0_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0_1_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_1_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_1_0_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0_1_0_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0_1_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_1_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_1_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_1_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_1_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_1_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_1_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_1_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_1_0_0_0_win)
        self.qtgui_freq_sink_x_0_0_1_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Node 4(Data from Transmitter 2) : Polyphase", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_1_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_1_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_1_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_1_0_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_0_1_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0_1_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_1_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_1_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0_1_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0_1_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_1_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_1_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_1_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_1_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_1_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_1_0_0_win)
        self.qtgui_freq_sink_x_0_0_1_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Node 3(Data from Transmitter 2) : PolyPhase", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_1_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_1_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_1_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_1_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_0_1_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0_1_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_1_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_1_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0_1_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0_1_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_1_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_1_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_1_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_1_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_1_0_win)
        self.qtgui_freq_sink_x_0_0_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Node 3(Data from Transmitter 1) : PolyPhase", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_1.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_0_1.enable_grid(True)
        self.qtgui_freq_sink_x_0_0_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_1.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0_1.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0_1.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_1_win)
        self.qtgui_freq_sink_x_0_0_0_0_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Node 4(Data from Transmitter 1) : CMA", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_0_0_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_0_0_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_0_0_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0_0_1.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_0_0_0_1.enable_grid(True)
        self.qtgui_freq_sink_x_0_0_0_0_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0_0_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0_0_1.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0_0_0_1.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0_0_0_1.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0_0_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0_0_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0_0_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_0_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_0_1_win)
        self.qtgui_freq_sink_x_0_0_0_0_0_0_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Node 4(Data from Transmitter 3 which is received from Transmitter 2) : CMA", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_0_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_0_0_0_0_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_0_0_0_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0_0_0_0_0_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_0_0_0_0_0_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0_0_0_0_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0_0_0_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0_0_0_0_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0_0_0_0_0_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0_0_0_0_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_0_0_0_0_0_win)
        self.qtgui_freq_sink_x_0_0_0_0_0_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Node 4(Data from Transmitter 3 which is received from Transmitter 1) : CMA", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_0_0_0_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_0_0_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0_0_0_0_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_0_0_0_0_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0_0_0_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0_0_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0_0_0_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0_0_0_0_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0_0_0_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_0_0_0_0_win)
        self.qtgui_freq_sink_x_0_0_0_0_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Node 4(Data from Transmitter 2) : CMA", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_0_0_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_0_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0_0_0_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_0_0_0_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0_0_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0_0_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0_0_0_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0_0_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_0_0_0_win)
        self.qtgui_freq_sink_x_0_0_0_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Node 3(Data from Transmitter 2) : CMA", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_0_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0_0_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_0_0_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0_0_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_0_0_win)
        self.qtgui_freq_sink_x_0_0_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Node 3(Data from Transmitter 1) : CMA", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_0_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_0_win)
        self.qtgui_freq_sink_x_0_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Node 2(Data from Transmitter 1) : CMA", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_win)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Node 2(Data from Transmitter 1) : PolyPhase", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Node 1 : Modulation", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.qtgui_const_sink_x_0_2_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"Node 3(Data from Transmitter 2)", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_2_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_2_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_2_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_2_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_2_0_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0_2_0_0.enable_grid(True)
        self.qtgui_const_sink_x_0_2_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_2_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_2_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_2_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_2_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_2_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_2_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_2_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_2_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_2_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_2_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_2_0_0_win)
        self.qtgui_const_sink_x_0_2_0 = qtgui.const_sink_c(
        	1024, #size
        	"Node 3(Data from Transmitter 1) ", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_2_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_2_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_2_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_2_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_2_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0_2_0.enable_grid(True)
        self.qtgui_const_sink_x_0_2_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_2_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_2_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_2_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_2_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_2_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_2_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_2_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_2_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_2_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_2_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_2_0_win)
        self.qtgui_const_sink_x_0_2 = qtgui.const_sink_c(
        	1024, #size
        	"Node 2(Data from Transmitter 1)", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_2.set_update_time(0.10)
        self.qtgui_const_sink_x_0_2.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_2.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_2.enable_autoscale(True)
        self.qtgui_const_sink_x_0_2.enable_grid(True)
        self.qtgui_const_sink_x_0_2.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_2.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_2.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_2.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_2.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_2.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_2.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_2.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_2_win = sip.wrapinstance(self.qtgui_const_sink_x_0_2.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_2_win)
        self.qtgui_const_sink_x_0_1_0_1 = qtgui.const_sink_c(
        	1024, #size
        	"Node 4(Data from Transmitter 1) : Costas Loop", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_1_0_1.set_update_time(0.10)
        self.qtgui_const_sink_x_0_1_0_1.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_1_0_1.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_1_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_1_0_1.enable_autoscale(True)
        self.qtgui_const_sink_x_0_1_0_1.enable_grid(True)
        self.qtgui_const_sink_x_0_1_0_1.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_1_0_1.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_1_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_1_0_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_1_0_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_1_0_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_1_0_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_1_0_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_1_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_1_0_1_win = sip.wrapinstance(self.qtgui_const_sink_x_0_1_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_1_0_1_win)
        self.qtgui_const_sink_x_0_1_0_0_0_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"Node 4(Data from Transmitter 3 which is received from Transmitter 2) : Costas Loop", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_1_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_1_0_0_0_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_1_0_0_0_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_1_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_1_0_0_0_0_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0_1_0_0_0_0_0.enable_grid(True)
        self.qtgui_const_sink_x_0_1_0_0_0_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_1_0_0_0_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_1_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_1_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_1_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_1_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_1_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_1_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_1_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_1_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_1_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_1_0_0_0_0_0_win)
        self.qtgui_const_sink_x_0_1_0_0_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"Node 4(Data from Transmitter 3 which is received from Transmitter 1) : Costas Loop", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_1_0_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_1_0_0_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_1_0_0_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_1_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_1_0_0_0_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0_1_0_0_0_0.enable_grid(True)
        self.qtgui_const_sink_x_0_1_0_0_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_1_0_0_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_1_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_1_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_1_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_1_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_1_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_1_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_1_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_1_0_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_1_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_1_0_0_0_0_win)
        self.qtgui_const_sink_x_0_1_0_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"Node 4(Data from Transmitter 2) : Costas Loop", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_1_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_1_0_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_1_0_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_1_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_1_0_0_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0_1_0_0_0.enable_grid(True)
        self.qtgui_const_sink_x_0_1_0_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_1_0_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_1_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_1_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_1_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_1_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_1_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_1_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_1_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_1_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_1_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_1_0_0_0_win)
        self.qtgui_const_sink_x_0_1_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"Node 3(Data from Transmitter 2) : Costas Loop", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_1_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_1_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_1_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_1_0_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0_1_0_0.enable_grid(True)
        self.qtgui_const_sink_x_0_1_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_1_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_1_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_1_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_1_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_1_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_1_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_1_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_1_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_1_0_0_win)
        self.qtgui_const_sink_x_0_1_0 = qtgui.const_sink_c(
        	1024, #size
        	"Node 3(Data from Transmitter 1) : Costas Loop", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_1_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_1_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_1_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_1_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0_1_0.enable_grid(True)
        self.qtgui_const_sink_x_0_1_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_1_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_1_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_1_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_1_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_1_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_1_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_1_0_win)
        self.qtgui_const_sink_x_0_1 = qtgui.const_sink_c(
        	1024, #size
        	"Node 2(Data from Transmitter 1) : Costas Loop", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_1.set_update_time(0.10)
        self.qtgui_const_sink_x_0_1.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_1.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_1.enable_autoscale(True)
        self.qtgui_const_sink_x_0_1.enable_grid(True)
        self.qtgui_const_sink_x_0_1.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_1.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_1_win = sip.wrapinstance(self.qtgui_const_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_1_win)
        self.qtgui_const_sink_x_0_0_1_1 = qtgui.const_sink_c(
        	1024, #size
        	"Node 4(Data from Transmitter 1) : Polyphase", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0_1_1.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_1_1.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_1_1.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_1_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_1_1.enable_autoscale(True)
        self.qtgui_const_sink_x_0_0_1_1.enable_grid(True)
        self.qtgui_const_sink_x_0_0_1_1.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_0_1_1.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_1_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_1_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_1_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_1_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_1_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_1_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_1_1.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_1_1_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_1_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_1_1_win)
        self.qtgui_const_sink_x_0_0_1_0_0_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"Node 4(Data from Transmitter 3 which is received from Transmitter 2) : Polyphase", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0_1_0_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_1_0_0_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_1_0_0_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_1_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_1_0_0_0_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0_0_1_0_0_0_0.enable_grid(True)
        self.qtgui_const_sink_x_0_0_1_0_0_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_0_1_0_0_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_1_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_1_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_1_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_1_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_1_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_1_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_1_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_1_0_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_1_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_1_0_0_0_0_win)
        self.qtgui_const_sink_x_0_0_1_0_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"Node 4(Data from Transmitter 3 which is received from Transmitter 1) : Polyphase", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0_1_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_1_0_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_1_0_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_1_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_1_0_0_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0_0_1_0_0_0.enable_grid(True)
        self.qtgui_const_sink_x_0_0_1_0_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_0_1_0_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_1_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_1_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_1_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_1_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_1_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_1_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_1_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_1_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_1_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_1_0_0_0_win)
        self.qtgui_const_sink_x_0_0_1_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"Node 4(Data from Transmitter 2) : Polyphase", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0_1_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_1_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_1_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_1_0_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0_0_1_0_0.enable_grid(True)
        self.qtgui_const_sink_x_0_0_1_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_0_1_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_1_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_1_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_1_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_1_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_1_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_1_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_1_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_1_0_0_win)
        self.qtgui_const_sink_x_0_0_1_0 = qtgui.const_sink_c(
        	1024, #size
        	"Node 3(Data from Transmitter 2) : PolyPhase", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0_1_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_1_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_1_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_1_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0_0_1_0.enable_grid(True)
        self.qtgui_const_sink_x_0_0_1_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_0_1_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_1_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_1_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_1_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_1_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_1_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_1_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_1_0_win)
        self.qtgui_const_sink_x_0_0_1 = qtgui.const_sink_c(
        	1024, #size
        	"Node 3(Data from Transmitter 1) : PolyPhase", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0_1.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_1.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_1.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_1.enable_autoscale(True)
        self.qtgui_const_sink_x_0_0_1.enable_grid(True)
        self.qtgui_const_sink_x_0_0_1.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_0_1.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_1_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_1_win)
        self.qtgui_const_sink_x_0_0_0_0_1 = qtgui.const_sink_c(
        	1024, #size
        	"Node 4(Data from Transmitter 1) : CMA", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0_0_0_1.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_0_0_1.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_0_0_1.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_0_0_1.enable_autoscale(True)
        self.qtgui_const_sink_x_0_0_0_0_1.enable_grid(True)
        self.qtgui_const_sink_x_0_0_0_0_1.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_0_0_0_1.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_0_0_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_0_0_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_0_0_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_0_0_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_0_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_0_0_1_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_0_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_0_0_1_win)
        self.qtgui_const_sink_x_0_0_0_0_0_0_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"Node 4(Data from Transmitter 3 which is received from Transmitter 2) : CMA", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0_0_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_0_0_0_0_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_0_0_0_0_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_0_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_0_0_0_0_0_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0_0_0_0_0_0_0_0.enable_grid(True)
        self.qtgui_const_sink_x_0_0_0_0_0_0_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_0_0_0_0_0_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_0_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_0_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_0_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_0_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_0_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_0_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_0_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_0_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_0_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_0_0_0_0_0_0_win)
        self.qtgui_const_sink_x_0_0_0_0_0_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"Node 4(Data from Transmitter 3 which is received from Transmitter 1) : CMA", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_0_0_0_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_0_0_0_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_0_0_0_0_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0_0_0_0_0_0_0.enable_grid(True)
        self.qtgui_const_sink_x_0_0_0_0_0_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_0_0_0_0_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_0_0_0_0_0_win)
        self.qtgui_const_sink_x_0_0_0_0_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"Node 4(Data from Transmitter 2) : CMA", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_0_0_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_0_0_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_0_0_0_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0_0_0_0_0_0.enable_grid(True)
        self.qtgui_const_sink_x_0_0_0_0_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_0_0_0_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_0_0_0_0_win)
        self.qtgui_const_sink_x_0_0_0_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"Node 3(Data from Transmitter 2) : CMA", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_0_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_0_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_0_0_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0_0_0_0_0.enable_grid(True)
        self.qtgui_const_sink_x_0_0_0_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_0_0_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_0_0_0_win)
        self.qtgui_const_sink_x_0_0_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"Node 3(Data from Transmitter 1) : CMA", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_0_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0_0_0_0.enable_grid(True)
        self.qtgui_const_sink_x_0_0_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_0_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_0_0_win)
        self.qtgui_const_sink_x_0_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"Node 2(Data from Transmitter 1) : CMA", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0_0_0.enable_grid(True)
        self.qtgui_const_sink_x_0_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_0_win)
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"Node 2(Data from Transmitter 1) : PolyPhase", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0_0.enable_grid(True)
        self.qtgui_const_sink_x_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"Node 1", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0.enable_grid(True)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.epy_block_0_0_0 = epy_block_0_0_0.blk(delay=delay)
        self.epy_block_0_0 = epy_block_0_0.blk(delay=delay)
        self.epy_block_0 = epy_block_0.blk(delay=delay)
        self.digital_pfb_clock_sync_xxx_0_0_1 = digital.pfb_clock_sync_ccf(sps, 3.14/50, (rrtaps), nfilter, 16, 1.5, sps)
        self.digital_pfb_clock_sync_xxx_0_0_0_0_0_0 = digital.pfb_clock_sync_ccf(sps, 3.14/50, (rrtaps), nfilter, 16, 1.5, sps)
        self.digital_pfb_clock_sync_xxx_0_0_0_0_0 = digital.pfb_clock_sync_ccf(sps, 3.14/50, (rrtaps), nfilter, 16, 1.5, sps)
        self.digital_pfb_clock_sync_xxx_0_0_0_0 = digital.pfb_clock_sync_ccf(sps, 3.14/50, (rrtaps), nfilter, 16, 1.5, sps)
        self.digital_pfb_clock_sync_xxx_0_0_0 = digital.pfb_clock_sync_ccf(sps, 3.14/50, (rrtaps), nfilter, 16, 1.5, sps)
        self.digital_pfb_clock_sync_xxx_0_0 = digital.pfb_clock_sync_ccf(sps, 3.14/50, (rrtaps), nfilter, 16, 1.5, sps)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, 3.14/50, (rrtaps), nfilter, 16, 1.5, sps)
        self.digital_map_bb_0_0_1 = digital.map_bb((MAP))
        self.digital_map_bb_0_0_0_0_0_0 = digital.map_bb((MAP))
        self.digital_map_bb_0_0_0_0_0 = digital.map_bb((MAP))
        self.digital_map_bb_0_0_0_0 = digital.map_bb((MAP))
        self.digital_map_bb_0_0_0 = digital.map_bb((MAP))
        self.digital_map_bb_0_0 = digital.map_bb((MAP))
        self.digital_map_bb_0 = digital.map_bb((MAP))
        self.digital_diff_decoder_bb_0_0_1 = digital.diff_decoder_bb(m)
        self.digital_diff_decoder_bb_0_0_0_0_0_0 = digital.diff_decoder_bb(m)
        self.digital_diff_decoder_bb_0_0_0_0_0 = digital.diff_decoder_bb(m)
        self.digital_diff_decoder_bb_0_0_0_0 = digital.diff_decoder_bb(m)
        self.digital_diff_decoder_bb_0_0_0 = digital.diff_decoder_bb(m)
        self.digital_diff_decoder_bb_0_0 = digital.diff_decoder_bb(m)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(m)
        self.digital_costas_loop_cc_0_0_1 = digital.costas_loop_cc(3.14/50, 4, False)
        self.digital_costas_loop_cc_0_0_0_0_0_0 = digital.costas_loop_cc(3.14/50, 4, False)
        self.digital_costas_loop_cc_0_0_0_0_0 = digital.costas_loop_cc(3.14/50, 4, False)
        self.digital_costas_loop_cc_0_0_0_0 = digital.costas_loop_cc(3.14/50, 4, False)
        self.digital_costas_loop_cc_0_0_0 = digital.costas_loop_cc(3.14/50, 4, False)
        self.digital_costas_loop_cc_0_0 = digital.costas_loop_cc(3.14/50, 4, False)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(3.14/50, 4, False)
        self.digital_constellation_modulator_0_0_0_0 = digital.generic_mod(
          constellation=c3,
          differential=True,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=0.35,
          verbose=False,
          log=False,
          )
        self.digital_constellation_modulator_0_0_0 = digital.generic_mod(
          constellation=c3,
          differential=True,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=0.35,
          verbose=False,
          log=False,
          )
        self.digital_constellation_modulator_0_0 = digital.generic_mod(
          constellation=c3,
          differential=True,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=0.35,
          verbose=False,
          log=False,
          )
        self.digital_constellation_modulator_0 = digital.generic_mod(
          constellation=c2,
          differential=True,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=0.35,
          verbose=False,
          log=False,
          )
        self.digital_constellation_decoder_cb_0_0_1 = digital.constellation_decoder_cb(c2)
        self.digital_constellation_decoder_cb_0_0_0_0_0_0 = digital.constellation_decoder_cb(c3)
        self.digital_constellation_decoder_cb_0_0_0_0_0 = digital.constellation_decoder_cb(c3)
        self.digital_constellation_decoder_cb_0_0_0_0 = digital.constellation_decoder_cb(c3)
        self.digital_constellation_decoder_cb_0_0_0 = digital.constellation_decoder_cb(c3)
        self.digital_constellation_decoder_cb_0_0 = digital.constellation_decoder_cb(c2)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(c2)
        self.digital_cma_equalizer_cc_0_0_1 = digital.cma_equalizer_cc(15, 1, cmaGain, sps)
        self.digital_cma_equalizer_cc_0_0_0_0_0_0 = digital.cma_equalizer_cc(15, 1, cmaGain, sps)
        self.digital_cma_equalizer_cc_0_0_0_0_0 = digital.cma_equalizer_cc(15, 1, cmaGain, sps)
        self.digital_cma_equalizer_cc_0_0_0_0 = digital.cma_equalizer_cc(15, 1, cmaGain, sps)
        self.digital_cma_equalizer_cc_0_0_0 = digital.cma_equalizer_cc(15, 1, cmaGain, sps)
        self.digital_cma_equalizer_cc_0_0 = digital.cma_equalizer_cc(15, 1, cmaGain, sps)
        self.digital_cma_equalizer_cc_0 = digital.cma_equalizer_cc(15, 1, cmaGain, sps)
        self.channels_fading_model_0_1_0_0_0 = channels.fading_model( sin1d, (10.0+float(d/2)) /samp_rate, False, 4.0, 5 )
        self.channels_fading_model_0_1_0_0 = channels.fading_model( sin1d, (10.0+float(d/2)) /samp_rate, False, 4.0, 5 )
        self.channels_fading_model_0_1_0 = channels.fading_model( sin2d, (10.0+float(d)) /samp_rate, False, 4.0, 3 )
        self.channels_fading_model_0_1 = channels.fading_model( sin1d, (10.0+float(d/2)) /samp_rate, False, 4.0, 5 )
        self.channels_fading_model_0_0_0 = channels.fading_model( sin3d, (10.0+float(3*d/2))/samp_rate, False, 4.0, 5 )
        self.channels_fading_model_0_0 = channels.fading_model( sin2d, (10.0+float(d))/samp_rate, False, 4.0, 5 )
        self.channels_fading_model_0 = channels.fading_model( sin1d, (10.0 + float(d/2))/samp_rate, False, 4.0, 2 )
        self.blocks_throttle_0_0_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_repack_bits_bb_0_0_1 = blocks.repack_bits_bb(2, 8, "", False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_0_0_0_0_0 = blocks.repack_bits_bb(2, 8, "", False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_0_0_0_0 = blocks.repack_bits_bb(2, 8, "", False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_0_0_0 = blocks.repack_bits_bb(2, 8, "", False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_0_0 = blocks.repack_bits_bb(2, 8, "", False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(2, 8, "", False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(2, 8, "", False, gr.GR_MSB_FIRST)
        self.blocks_packed_to_unpacked_xx_0_0_1 = blocks.packed_to_unpacked_bb(1, gr.GR_MSB_FIRST)
        self.blocks_packed_to_unpacked_xx_0_0_0_0_0_0 = blocks.packed_to_unpacked_bb(1, gr.GR_MSB_FIRST)
        self.blocks_packed_to_unpacked_xx_0_0_0_0_0 = blocks.packed_to_unpacked_bb(1, gr.GR_MSB_FIRST)
        self.blocks_packed_to_unpacked_xx_0_0_0_0 = blocks.packed_to_unpacked_bb(1, gr.GR_MSB_FIRST)
        self.blocks_packed_to_unpacked_xx_0_0_0 = blocks.packed_to_unpacked_bb(1, gr.GR_MSB_FIRST)
        self.blocks_packed_to_unpacked_xx_0_0 = blocks.packed_to_unpacked_bb(1, gr.GR_MSB_FIRST)
        self.blocks_packed_to_unpacked_xx_0 = blocks.packed_to_unpacked_bb(1, gr.GR_MSB_FIRST)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, 'D:\\DCL\\finalproject\\input.jpg', False)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0_0_1 = blocks.file_sink(gr.sizeof_char*1, 'D:\\DCL\\finalproject\\reciever4.jpg', False)
        self.blocks_file_sink_0_0_1.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_0_0_0 = blocks.file_sink(gr.sizeof_char*1, 'D:\\DCL\\finalproject\\reciever432.jpg', False)
        self.blocks_file_sink_0_0_0_0_0_0.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_0_0 = blocks.file_sink(gr.sizeof_char*1, 'D:\\DCL\\finalproject\\reciever43.jpg', False)
        self.blocks_file_sink_0_0_0_0_0.set_unbuffered(True)
        self.blocks_file_sink_0_0_0_0 = blocks.file_sink(gr.sizeof_char*1, 'D:\\DCL\\finalproject\\reciever42.jpg', False)
        self.blocks_file_sink_0_0_0_0.set_unbuffered(True)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_char*1, 'D:\\DCL\\finalproject\\reciever32.jpg', False)
        self.blocks_file_sink_0_0_0.set_unbuffered(True)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, 'D:\\DCL\\finalproject\\reciever3.jpg', False)
        self.blocks_file_sink_0_0.set_unbuffered(True)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, 'D:\\DCL\\finalproject\\reciever2.jpg', False)
        self.blocks_file_sink_0.set_unbuffered(True)
        self.blks2_packet_encoder_0_0_0_0 = grc_blks2.packet_mod_b(grc_blks2.packet_encoder(
        		samples_per_symbol=sps,
        		bits_per_symbol=k,
        		preamble=code6,
        		access_code=code5,
        		pad_for_usrp=True,
        	),
        	payload_length=15,
        )
        self.blks2_packet_encoder_0_0_0 = grc_blks2.packet_mod_b(grc_blks2.packet_encoder(
        		samples_per_symbol=sps,
        		bits_per_symbol=k,
        		preamble=code6,
        		access_code=code5,
        		pad_for_usrp=True,
        	),
        	payload_length=15,
        )
        self.blks2_packet_encoder_0_0 = grc_blks2.packet_mod_b(grc_blks2.packet_encoder(
        		samples_per_symbol=sps,
        		bits_per_symbol=k,
        		preamble=code4,
        		access_code=code3,
        		pad_for_usrp=True,
        	),
        	payload_length=15,
        )
        self.blks2_packet_encoder_0 = grc_blks2.packet_mod_b(grc_blks2.packet_encoder(
        		samples_per_symbol=sps,
        		bits_per_symbol=k,
        		preamble=code2,
        		access_code=code1,
        		pad_for_usrp=True,
        	),
        	payload_length=15,
        )
        self.blks2_packet_decoder_0_0_1 = grc_blks2.packet_demod_b(grc_blks2.packet_decoder(
        		access_code=code1,
        		threshold=-1,
        		callback=lambda ok, payload: self.blks2_packet_decoder_0_0_1.recv_pkt(ok, payload),
        	),
        )
        self.blks2_packet_decoder_0_0_0_0_0_0 = grc_blks2.packet_demod_b(grc_blks2.packet_decoder(
        		access_code=code5,
        		threshold=-1,
        		callback=lambda ok, payload: self.blks2_packet_decoder_0_0_0_0_0_0.recv_pkt(ok, payload),
        	),
        )
        self.blks2_packet_decoder_0_0_0_0_0 = grc_blks2.packet_demod_b(grc_blks2.packet_decoder(
        		access_code=code5,
        		threshold=-1,
        		callback=lambda ok, payload: self.blks2_packet_decoder_0_0_0_0_0.recv_pkt(ok, payload),
        	),
        )
        self.blks2_packet_decoder_0_0_0_0 = grc_blks2.packet_demod_b(grc_blks2.packet_decoder(
        		access_code=code3,
        		threshold=-1,
        		callback=lambda ok, payload: self.blks2_packet_decoder_0_0_0_0.recv_pkt(ok, payload),
        	),
        )
        self.blks2_packet_decoder_0_0_0 = grc_blks2.packet_demod_b(grc_blks2.packet_decoder(
        		access_code=code3,
        		threshold=-1,
        		callback=lambda ok, payload: self.blks2_packet_decoder_0_0_0.recv_pkt(ok, payload),
        	),
        )
        self.blks2_packet_decoder_0_0 = grc_blks2.packet_demod_b(grc_blks2.packet_decoder(
        		access_code=code1,
        		threshold=-1,
        		callback=lambda ok, payload: self.blks2_packet_decoder_0_0.recv_pkt(ok, payload),
        	),
        )
        self.blks2_packet_decoder_0 = grc_blks2.packet_demod_b(grc_blks2.packet_decoder(
        		access_code=code1,
        		threshold=-1,
        		callback=lambda ok, payload: self.blks2_packet_decoder_0.recv_pkt(ok, payload),
        	),
        )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blks2_packet_decoder_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blks2_packet_decoder_0, 0), (self.epy_block_0, 0))
        self.connect((self.blks2_packet_decoder_0_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blks2_packet_decoder_0_0, 0), (self.epy_block_0_0, 0))
        self.connect((self.blks2_packet_decoder_0_0_0, 0), (self.blocks_file_sink_0_0_0, 0))
        self.connect((self.blks2_packet_decoder_0_0_0, 0), (self.epy_block_0_0_0, 0))
        self.connect((self.blks2_packet_decoder_0_0_0_0, 0), (self.blocks_file_sink_0_0_0_0, 0))
        self.connect((self.blks2_packet_decoder_0_0_0_0_0, 0), (self.blocks_file_sink_0_0_0_0_0, 0))
        self.connect((self.blks2_packet_decoder_0_0_0_0_0_0, 0), (self.blocks_file_sink_0_0_0_0_0_0, 0))
        self.connect((self.blks2_packet_decoder_0_0_1, 0), (self.blocks_file_sink_0_0_1, 0))
        self.connect((self.blks2_packet_encoder_0, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.blks2_packet_encoder_0_0, 0), (self.digital_constellation_modulator_0_0, 0))
        self.connect((self.blks2_packet_encoder_0_0_0, 0), (self.digital_constellation_modulator_0_0_0, 0))
        self.connect((self.blks2_packet_encoder_0_0_0_0, 0), (self.digital_constellation_modulator_0_0_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blks2_packet_encoder_0, 0))
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.blks2_packet_decoder_0, 0))
        self.connect((self.blocks_packed_to_unpacked_xx_0_0, 0), (self.blks2_packet_decoder_0_0, 0))
        self.connect((self.blocks_packed_to_unpacked_xx_0_0_0, 0), (self.blks2_packet_decoder_0_0_0, 0))
        self.connect((self.blocks_packed_to_unpacked_xx_0_0_0_0, 0), (self.blks2_packet_decoder_0_0_0_0, 0))
        self.connect((self.blocks_packed_to_unpacked_xx_0_0_0_0_0, 0), (self.blks2_packet_decoder_0_0_0_0_0, 0))
        self.connect((self.blocks_packed_to_unpacked_xx_0_0_0_0_0_0, 0), (self.blks2_packet_decoder_0_0_0_0_0_0, 0))
        self.connect((self.blocks_packed_to_unpacked_xx_0_0_1, 0), (self.blks2_packet_decoder_0_0_1, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.blocks_packed_to_unpacked_xx_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.blocks_packed_to_unpacked_xx_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0, 0), (self.blocks_packed_to_unpacked_xx_0_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0_0, 0), (self.blocks_packed_to_unpacked_xx_0_0_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0_0_0, 0), (self.blocks_packed_to_unpacked_xx_0_0_0_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0_0_0_0, 0), (self.blocks_packed_to_unpacked_xx_0_0_0_0_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_1, 0), (self.blocks_packed_to_unpacked_xx_0_0_1, 0))
        self.connect((self.blocks_throttle_0, 0), (self.channels_fading_model_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.channels_fading_model_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.channels_fading_model_0_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.channels_fading_model_0_1, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.channels_fading_model_0_1_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.qtgui_const_sink_x_0_2, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.qtgui_freq_sink_x_0_2, 0))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.channels_fading_model_0_1_0_0, 0))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.qtgui_const_sink_x_0_2_0, 0))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.qtgui_freq_sink_x_0_2_0, 0))
        self.connect((self.blocks_throttle_0_0_0_0, 0), (self.channels_fading_model_0_1_0_0_0, 0))
        self.connect((self.blocks_throttle_0_0_0_0, 0), (self.qtgui_const_sink_x_0_2_0_0, 0))
        self.connect((self.blocks_throttle_0_0_0_0, 0), (self.qtgui_freq_sink_x_0_2_0_0, 0))
        self.connect((self.channels_fading_model_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.channels_fading_model_0_0, 0), (self.digital_pfb_clock_sync_xxx_0_0, 0))
        self.connect((self.channels_fading_model_0_0_0, 0), (self.digital_pfb_clock_sync_xxx_0_0_1, 0))
        self.connect((self.channels_fading_model_0_1, 0), (self.digital_pfb_clock_sync_xxx_0_0_0, 0))
        self.connect((self.channels_fading_model_0_1_0, 0), (self.digital_pfb_clock_sync_xxx_0_0_0_0, 0))
        self.connect((self.channels_fading_model_0_1_0_0, 0), (self.digital_pfb_clock_sync_xxx_0_0_0_0_0, 0))
        self.connect((self.channels_fading_model_0_1_0_0_0, 0), (self.digital_pfb_clock_sync_xxx_0_0_0_0_0_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.qtgui_const_sink_x_0_0_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.qtgui_freq_sink_x_0_0_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0_0, 0), (self.digital_costas_loop_cc_0_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0_0, 0), (self.qtgui_const_sink_x_0_0_0_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0_0, 0), (self.qtgui_freq_sink_x_0_0_0_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0_0_0, 0), (self.digital_costas_loop_cc_0_0_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0_0_0, 0), (self.qtgui_const_sink_x_0_0_0_0_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0_0_0, 0), (self.qtgui_freq_sink_x_0_0_0_0_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0_0_0_0, 0), (self.digital_costas_loop_cc_0_0_0_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0_0_0_0, 0), (self.qtgui_const_sink_x_0_0_0_0_0_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0_0_0_0, 0), (self.qtgui_freq_sink_x_0_0_0_0_0_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0_0_0_0_0, 0), (self.digital_costas_loop_cc_0_0_0_0_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0_0_0_0_0, 0), (self.qtgui_const_sink_x_0_0_0_0_0_0_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0_0_0_0_0, 0), (self.qtgui_freq_sink_x_0_0_0_0_0_0_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0_0_0_0_0_0, 0), (self.digital_costas_loop_cc_0_0_0_0_0_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0_0_0_0_0_0, 0), (self.qtgui_const_sink_x_0_0_0_0_0_0_0_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0_0_0_0_0_0, 0), (self.qtgui_freq_sink_x_0_0_0_0_0_0_0_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0_0_1, 0), (self.digital_costas_loop_cc_0_0_1, 0))
        self.connect((self.digital_cma_equalizer_cc_0_0_1, 0), (self.qtgui_const_sink_x_0_0_0_0_1, 0))
        self.connect((self.digital_cma_equalizer_cc_0_0_1, 0), (self.qtgui_freq_sink_x_0_0_0_0_1, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.digital_map_bb_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0_0, 0), (self.digital_map_bb_0_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0_0_0, 0), (self.digital_map_bb_0_0_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0_0_0_0, 0), (self.digital_map_bb_0_0_0_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0_0_0_0_0, 0), (self.digital_map_bb_0_0_0_0_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0_0_0_0_0_0, 0), (self.digital_map_bb_0_0_0_0_0_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0_0_1, 0), (self.digital_map_bb_0_0_1, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.digital_constellation_modulator_0_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.digital_constellation_modulator_0_0_0, 0), (self.blocks_throttle_0_0_0, 0))
        self.connect((self.digital_constellation_modulator_0_0_0_0, 0), (self.blocks_throttle_0_0_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_const_sink_x_0_1, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_freq_sink_x_0_1, 0))
        self.connect((self.digital_costas_loop_cc_0_0, 0), (self.digital_constellation_decoder_cb_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0, 0), (self.qtgui_const_sink_x_0_1_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0, 0), (self.qtgui_freq_sink_x_0_1_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0_0, 0), (self.digital_constellation_decoder_cb_0_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0_0, 0), (self.qtgui_const_sink_x_0_1_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0_0, 0), (self.qtgui_freq_sink_x_0_1_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0_0_0, 0), (self.digital_constellation_decoder_cb_0_0_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0_0_0, 0), (self.qtgui_const_sink_x_0_1_0_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0_0_0, 0), (self.qtgui_freq_sink_x_0_1_0_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0_0_0_0, 0), (self.digital_constellation_decoder_cb_0_0_0_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0_0_0_0, 0), (self.qtgui_const_sink_x_0_1_0_0_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0_0_0_0, 0), (self.qtgui_freq_sink_x_0_1_0_0_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0_0_0_0_0, 0), (self.digital_constellation_decoder_cb_0_0_0_0_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0_0_0_0_0, 0), (self.qtgui_const_sink_x_0_1_0_0_0_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0_0_0_0_0, 0), (self.qtgui_freq_sink_x_0_1_0_0_0_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0_1, 0), (self.digital_constellation_decoder_cb_0_0_1, 0))
        self.connect((self.digital_costas_loop_cc_0_0_1, 0), (self.qtgui_const_sink_x_0_1_0_1, 0))
        self.connect((self.digital_costas_loop_cc_0_0_1, 0), (self.qtgui_freq_sink_x_0_1_0_1, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.digital_diff_decoder_bb_0_0, 0), (self.blocks_repack_bits_bb_0_0, 0))
        self.connect((self.digital_diff_decoder_bb_0_0_0, 0), (self.blocks_repack_bits_bb_0_0_0, 0))
        self.connect((self.digital_diff_decoder_bb_0_0_0_0, 0), (self.blocks_repack_bits_bb_0_0_0_0, 0))
        self.connect((self.digital_diff_decoder_bb_0_0_0_0_0, 0), (self.blocks_repack_bits_bb_0_0_0_0_0, 0))
        self.connect((self.digital_diff_decoder_bb_0_0_0_0_0_0, 0), (self.blocks_repack_bits_bb_0_0_0_0_0_0, 0))
        self.connect((self.digital_diff_decoder_bb_0_0_1, 0), (self.blocks_repack_bits_bb_0_0_1, 0))
        self.connect((self.digital_map_bb_0, 0), (self.digital_diff_decoder_bb_0, 0))
        self.connect((self.digital_map_bb_0_0, 0), (self.digital_diff_decoder_bb_0_0, 0))
        self.connect((self.digital_map_bb_0_0_0, 0), (self.digital_diff_decoder_bb_0_0_0, 0))
        self.connect((self.digital_map_bb_0_0_0_0, 0), (self.digital_diff_decoder_bb_0_0_0_0, 0))
        self.connect((self.digital_map_bb_0_0_0_0_0, 0), (self.digital_diff_decoder_bb_0_0_0_0_0, 0))
        self.connect((self.digital_map_bb_0_0_0_0_0_0, 0), (self.digital_diff_decoder_bb_0_0_0_0_0_0, 0))
        self.connect((self.digital_map_bb_0_0_1, 0), (self.digital_diff_decoder_bb_0_0_1, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_cma_equalizer_cc_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.qtgui_const_sink_x_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0, 0), (self.digital_cma_equalizer_cc_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0, 0), (self.qtgui_const_sink_x_0_0_1, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0, 0), (self.qtgui_freq_sink_x_0_0_1, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0_0, 0), (self.digital_cma_equalizer_cc_0_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0_0, 0), (self.qtgui_const_sink_x_0_0_1_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0_0, 0), (self.qtgui_freq_sink_x_0_0_1_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0_0_0, 0), (self.digital_cma_equalizer_cc_0_0_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0_0_0, 0), (self.qtgui_const_sink_x_0_0_1_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0_0_0, 0), (self.qtgui_freq_sink_x_0_0_1_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0_0_0_0, 0), (self.digital_cma_equalizer_cc_0_0_0_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0_0_0_0, 0), (self.qtgui_const_sink_x_0_0_1_0_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0_0_0_0, 0), (self.qtgui_freq_sink_x_0_0_1_0_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0_0_0_0_0, 0), (self.digital_cma_equalizer_cc_0_0_0_0_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0_0_0_0_0, 0), (self.qtgui_const_sink_x_0_0_1_0_0_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0_0_0_0_0, 0), (self.qtgui_freq_sink_x_0_0_1_0_0_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0_1, 0), (self.digital_cma_equalizer_cc_0_0_1, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0_1, 0), (self.qtgui_const_sink_x_0_0_1_1, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0_1, 0), (self.qtgui_freq_sink_x_0_0_1_1, 0))
        self.connect((self.epy_block_0, 0), (self.blks2_packet_encoder_0_0, 0))
        self.connect((self.epy_block_0_0, 0), (self.blks2_packet_encoder_0_0_0, 0))
        self.connect((self.epy_block_0_0_0, 0), (self.blks2_packet_encoder_0_0_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "wsn")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrtaps(firdes.root_raised_cosine(self.nfilter , self.nfilter , 1/float(self.sps) , 0.35 , 11 *self.sps* self.nfilter))

    def get_nfilter(self):
        return self.nfilter

    def set_nfilter(self, nfilter):
        self.nfilter = nfilter
        self.set_rrtaps(firdes.root_raised_cosine(self.nfilter , self.nfilter , 1/float(self.sps) , 0.35 , 11 *self.sps* self.nfilter))

    def get_MAP(self):
        return self.MAP

    def set_MAP(self, MAP):
        self.MAP = MAP

    def get_A(self):
        return self.A

    def set_A(self, A):
        self.A = A

    def get_trate(self):
        return self.trate

    def set_trate(self, trate):
        self.trate = trate

    def get_sin3d(self):
        return self.sin3d

    def set_sin3d(self, sin3d):
        self.sin3d = sin3d

    def get_sin2d(self):
        return self.sin2d

    def set_sin2d(self, sin2d):
        self.sin2d = sin2d

    def get_sin1d(self):
        return self.sin1d

    def set_sin1d(self, sin1d):
        self.sin1d = sin1d

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0_2_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_2_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_2.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_1_0_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_1_0_0_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_1_0_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_1_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_1_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_1_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0_1_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0_1_0_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0_1_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0_1_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0_1_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0_0_0_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0_0_0_0_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0_0_0_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0_0_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.channels_fading_model_0_1_0_0_0.set_fDTs((10.0+float(self.d/2)) /self.samp_rate)
        self.channels_fading_model_0_1_0_0.set_fDTs((10.0+float(self.d/2)) /self.samp_rate)
        self.channels_fading_model_0_1_0.set_fDTs((10.0+float(self.d)) /self.samp_rate)
        self.channels_fading_model_0_1.set_fDTs((10.0+float(self.d/2)) /self.samp_rate)
        self.channels_fading_model_0_0_0.set_fDTs((10.0+float(3*self.d/2))/self.samp_rate)
        self.channels_fading_model_0_0.set_fDTs((10.0+float(self.d))/self.samp_rate)
        self.channels_fading_model_0.set_fDTs((10.0 + float(self.d/2))/self.samp_rate)
        self.blocks_throttle_0_0_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_rrtaps(self):
        return self.rrtaps

    def set_rrtaps(self, rrtaps):
        self.rrtaps = rrtaps
        self.digital_pfb_clock_sync_xxx_0_0_1.update_taps((self.rrtaps))
        self.digital_pfb_clock_sync_xxx_0_0_0_0_0_0.update_taps((self.rrtaps))
        self.digital_pfb_clock_sync_xxx_0_0_0_0_0.update_taps((self.rrtaps))
        self.digital_pfb_clock_sync_xxx_0_0_0_0.update_taps((self.rrtaps))
        self.digital_pfb_clock_sync_xxx_0_0_0.update_taps((self.rrtaps))
        self.digital_pfb_clock_sync_xxx_0_0.update_taps((self.rrtaps))
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.rrtaps))

    def get_m(self):
        return self.m

    def set_m(self, m):
        self.m = m

    def get_k(self):
        return self.k

    def set_k(self, k):
        self.k = k

    def get_delay(self):
        return self.delay

    def set_delay(self, delay):
        self.delay = delay
        self.epy_block_0_0_0.delay = self.delay
        self.epy_block_0_0.delay = self.delay
        self.epy_block_0.delay = self.delay

    def get_d(self):
        return self.d

    def set_d(self, d):
        self.d = d
        self.channels_fading_model_0_1_0_0_0.set_fDTs((10.0+float(self.d/2)) /self.samp_rate)
        self.channels_fading_model_0_1_0_0.set_fDTs((10.0+float(self.d/2)) /self.samp_rate)
        self.channels_fading_model_0_1_0.set_fDTs((10.0+float(self.d)) /self.samp_rate)
        self.channels_fading_model_0_1.set_fDTs((10.0+float(self.d/2)) /self.samp_rate)
        self.channels_fading_model_0_0_0.set_fDTs((10.0+float(3*self.d/2))/self.samp_rate)
        self.channels_fading_model_0_0.set_fDTs((10.0+float(self.d))/self.samp_rate)
        self.channels_fading_model_0.set_fDTs((10.0 + float(self.d/2))/self.samp_rate)

    def get_code6(self):
        return self.code6

    def set_code6(self, code6):
        self.code6 = code6

    def get_code5(self):
        return self.code5

    def set_code5(self, code5):
        self.code5 = code5

    def get_code4(self):
        return self.code4

    def set_code4(self, code4):
        self.code4 = code4

    def get_code3(self):
        return self.code3

    def set_code3(self, code3):
        self.code3 = code3

    def get_code2(self):
        return self.code2

    def set_code2(self, code2):
        self.code2 = code2

    def get_code1(self):
        return self.code1

    def set_code1(self, code1):
        self.code1 = code1

    def get_cmaGain(self):
        return self.cmaGain

    def set_cmaGain(self, cmaGain):
        self.cmaGain = cmaGain
        self.digital_cma_equalizer_cc_0_0_1.set_gain(self.cmaGain)
        self.digital_cma_equalizer_cc_0_0_0_0_0_0.set_gain(self.cmaGain)
        self.digital_cma_equalizer_cc_0_0_0_0_0.set_gain(self.cmaGain)
        self.digital_cma_equalizer_cc_0_0_0_0.set_gain(self.cmaGain)
        self.digital_cma_equalizer_cc_0_0_0.set_gain(self.cmaGain)
        self.digital_cma_equalizer_cc_0_0.set_gain(self.cmaGain)
        self.digital_cma_equalizer_cc_0.set_gain(self.cmaGain)

    def get_c3(self):
        return self.c3

    def set_c3(self, c3):
        self.c3 = c3

    def get_c2(self):
        return self.c2

    def set_c2(self, c2):
        self.c2 = c2


def main(top_block_cls=wsn, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
