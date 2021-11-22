#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Ber
# Generated: Fri Feb  5 23:45:24 2021
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
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import epy_block_0_0
import epy_block_0_1
import epy_block_0_2
import epy_block_0_3
import epy_block_0_4
import epy_block_0_5
import epy_block_0_6
import pmt
import sip
import sys
from gnuradio import qtgui


class BER(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Ber")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Ber")
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

        self.settings = Qt.QSettings("GNU Radio", "BER")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_1.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	10, #size
        	samp_rate, #samp_rate
        	"BER", #name
        	7 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(0, 0.1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['Node 1 to Node 2', 'Node 1 to Node 3', 'Node 1 to Node 4', 'Node 2 to Node 3', 'Node 2 to Node 4',
                  'Node 3 to Node 4', 'Node 2 to Node 3 to Node 4', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "yellow", "Dark Blue",
                  "cyan", "magenta", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [2, 7, 4, 1, 9,
                   2, 0, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(7):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.epy_block_0_6 = epy_block_0_6.blk()
        self.epy_block_0_5 = epy_block_0_5.blk()
        self.epy_block_0_4 = epy_block_0_4.blk()
        self.epy_block_0_3 = epy_block_0_3.blk()
        self.epy_block_0_2 = epy_block_0_2.blk()
        self.epy_block_0_1 = epy_block_0_1.blk()
        self.epy_block_0_0 = epy_block_0_0.blk()
        self.blocks_throttle_0_6 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_5 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_4 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_3 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_2 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_1 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_sub_xx_0_6 = blocks.sub_ff(1)
        self.blocks_sub_xx_0_5 = blocks.sub_ff(1)
        self.blocks_sub_xx_0_4 = blocks.sub_ff(1)
        self.blocks_sub_xx_0_3 = blocks.sub_ff(1)
        self.blocks_sub_xx_0_2 = blocks.sub_ff(1)
        self.blocks_sub_xx_0_1 = blocks.sub_ff(1)
        self.blocks_sub_xx_0_0 = blocks.sub_ff(1)
        self.blocks_float_to_uchar_0_6 = blocks.float_to_uchar()
        self.blocks_float_to_uchar_0_5 = blocks.float_to_uchar()
        self.blocks_float_to_uchar_0_4 = blocks.float_to_uchar()
        self.blocks_float_to_uchar_0_3 = blocks.float_to_uchar()
        self.blocks_float_to_uchar_0_2 = blocks.float_to_uchar()
        self.blocks_float_to_uchar_0_1 = blocks.float_to_uchar()
        self.blocks_float_to_uchar_0_0 = blocks.float_to_uchar()
        self.blocks_file_source_2_7 = blocks.file_source(gr.sizeof_char*1, 'D:\\DCL\\finalproject\\input.jpg', False)
        self.blocks_file_source_2_7.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_2_6 = blocks.file_source(gr.sizeof_float*1, 'D:\\DCL\\finalproject\\reciever432.jpg', False)
        self.blocks_file_source_2_6.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_2_5 = blocks.file_source(gr.sizeof_float*1, 'D:\\DCL\\finalproject\\reciever42.jpg', False)
        self.blocks_file_source_2_5.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_2_4 = blocks.file_source(gr.sizeof_float*1, 'D:\\DCL\\finalproject\\reciever43.jpg', False)
        self.blocks_file_source_2_4.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_2_3 = blocks.file_source(gr.sizeof_float*1, 'D:\\DCL\\finalproject\\reciever3.jpg', False)
        self.blocks_file_source_2_3.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_2_2_0 = blocks.file_source(gr.sizeof_char*1, 'D:\\DCL\\finalproject\\reciever4.jpg', False)
        self.blocks_file_source_2_2_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_2_2 = blocks.file_source(gr.sizeof_float*1, 'D:\\DCL\\finalproject\\reciever4.jpg', False)
        self.blocks_file_source_2_2.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_2_1 = blocks.file_source(gr.sizeof_float*1, 'D:\\DCL\\finalproject\\reciever32.jpg', False)
        self.blocks_file_source_2_1.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_2_0 = blocks.file_source(gr.sizeof_float*1, 'D:\\DCL\\finalproject\\reciever2.jpg', False)
        self.blocks_file_source_2_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_2 = blocks.file_source(gr.sizeof_float*1, 'D:\\DCL\\finalproject\\input.jpg', False)
        self.blocks_file_source_2.set_begin_tag(pmt.PMT_NIL)
        self.blks2_error_rate_0 = grc_blks2.error_rate(
        	type='BER',
        	win_size=1000,
        	bits_per_symbol=2,
        )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blks2_error_rate_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_file_source_2, 0), (self.blocks_sub_xx_0_0, 0))
        self.connect((self.blocks_file_source_2, 0), (self.blocks_sub_xx_0_1, 0))
        self.connect((self.blocks_file_source_2, 0), (self.blocks_sub_xx_0_2, 0))
        self.connect((self.blocks_file_source_2, 0), (self.blocks_sub_xx_0_3, 0))
        self.connect((self.blocks_file_source_2, 0), (self.blocks_sub_xx_0_4, 0))
        self.connect((self.blocks_file_source_2, 0), (self.blocks_sub_xx_0_5, 0))
        self.connect((self.blocks_file_source_2, 0), (self.blocks_sub_xx_0_6, 0))
        self.connect((self.blocks_file_source_2_0, 0), (self.blocks_sub_xx_0_0, 1))
        self.connect((self.blocks_file_source_2_1, 0), (self.blocks_sub_xx_0_3, 1))
        self.connect((self.blocks_file_source_2_2, 0), (self.blocks_sub_xx_0_2, 1))
        self.connect((self.blocks_file_source_2_2_0, 0), (self.blks2_error_rate_0, 1))
        self.connect((self.blocks_file_source_2_3, 0), (self.blocks_sub_xx_0_1, 1))
        self.connect((self.blocks_file_source_2_4, 0), (self.blocks_sub_xx_0_5, 1))
        self.connect((self.blocks_file_source_2_5, 0), (self.blocks_sub_xx_0_4, 1))
        self.connect((self.blocks_file_source_2_6, 0), (self.blocks_sub_xx_0_6, 1))
        self.connect((self.blocks_file_source_2_7, 0), (self.blks2_error_rate_0, 0))
        self.connect((self.blocks_float_to_uchar_0_0, 0), (self.epy_block_0_0, 0))
        self.connect((self.blocks_float_to_uchar_0_1, 0), (self.epy_block_0_1, 0))
        self.connect((self.blocks_float_to_uchar_0_2, 0), (self.epy_block_0_2, 0))
        self.connect((self.blocks_float_to_uchar_0_3, 0), (self.epy_block_0_3, 0))
        self.connect((self.blocks_float_to_uchar_0_4, 0), (self.epy_block_0_4, 0))
        self.connect((self.blocks_float_to_uchar_0_5, 0), (self.epy_block_0_5, 0))
        self.connect((self.blocks_float_to_uchar_0_6, 0), (self.epy_block_0_6, 0))
        self.connect((self.blocks_sub_xx_0_0, 0), (self.blocks_float_to_uchar_0_0, 0))
        self.connect((self.blocks_sub_xx_0_1, 0), (self.blocks_float_to_uchar_0_1, 0))
        self.connect((self.blocks_sub_xx_0_2, 0), (self.blocks_float_to_uchar_0_2, 0))
        self.connect((self.blocks_sub_xx_0_3, 0), (self.blocks_float_to_uchar_0_3, 0))
        self.connect((self.blocks_sub_xx_0_4, 0), (self.blocks_float_to_uchar_0_4, 0))
        self.connect((self.blocks_sub_xx_0_5, 0), (self.blocks_float_to_uchar_0_5, 0))
        self.connect((self.blocks_sub_xx_0_6, 0), (self.blocks_float_to_uchar_0_6, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.qtgui_time_sink_x_0, 4))
        self.connect((self.blocks_throttle_0_1, 0), (self.qtgui_time_sink_x_0, 3))
        self.connect((self.blocks_throttle_0_2, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.blocks_throttle_0_3, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_throttle_0_4, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_throttle_0_5, 0), (self.qtgui_time_sink_x_0, 6))
        self.connect((self.blocks_throttle_0_6, 0), (self.qtgui_time_sink_x_0, 5))
        self.connect((self.epy_block_0_0, 0), (self.blocks_throttle_0_4, 0))
        self.connect((self.epy_block_0_1, 0), (self.blocks_throttle_0_3, 0))
        self.connect((self.epy_block_0_2, 0), (self.blocks_throttle_0_2, 0))
        self.connect((self.epy_block_0_3, 0), (self.blocks_throttle_0_1, 0))
        self.connect((self.epy_block_0_4, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.epy_block_0_5, 0), (self.blocks_throttle_0_6, 0))
        self.connect((self.epy_block_0_6, 0), (self.blocks_throttle_0_5, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "BER")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0_6.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_5.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_4.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_3.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_2.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)


def main(top_block_cls=BER, options=None):

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
