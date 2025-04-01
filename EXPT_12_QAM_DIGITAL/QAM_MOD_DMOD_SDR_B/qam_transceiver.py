#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: QAM Transmitter and Receiver
# Author: AKADEMIKA Lab Solution
# Generated: Mon Jul 22 11:15:02 2019
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

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import iio
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import numpy
import wx


class qam_transceiver(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="QAM Transmitter and Receiver")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 100000

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_scopesink2_2 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title='Recovered Stream of Bits',
        	sample_rate=samp_rate,
        	v_scale=0.5,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.Add(self.wxgui_scopesink2_2.win)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_c(
        	self.GetWin(),
        	title='QAM Constellation plot',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=True,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=5,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=5,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.digital_qam_mod_0 = digital.qam.qam_mod(
          constellation_points=16,
          mod_code="gray",
          differential=True,
          samples_per_symbol=4,
          excess_bw=0.9,
          verbose=False,
          log=False,
          )
        self.digital_qam_demod_0 = digital.qam.qam_demod(
          constellation_points=16,
          differential=True,
          samples_per_symbol=4,
          excess_bw=0.35,
          freq_bw=6.28/100.0,
          timing_bw=6.28/100.0,
          phase_bw=6.28/100.0,
          mod_code="gray",
          verbose=False,
          log=False,
          )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.analog_random_source_x_0 = blocks.vector_source_s(map(int, numpy.random.randint(0, 2, 20000)), True)
        self.akademika_source_0 = iio.pluto_source('ip:akademika.local', int(400000000), int(2084000), int(20000000), 0x8000, True, True, True, "manual", 64.0, '', True)
        self.akademika_sink_0 = iio.pluto_sink('ip:akademika.local', int(400000000), int(2084000), int(20000000), 0x8000, False, 10.0, '', True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.akademika_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.wxgui_scopesink2_2, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.digital_qam_mod_0, 0))
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.digital_qam_demod_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.digital_qam_mod_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.digital_qam_mod_0, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.akademika_sink_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.digital_qam_demod_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_2.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)


def main(top_block_cls=qam_transceiver, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
