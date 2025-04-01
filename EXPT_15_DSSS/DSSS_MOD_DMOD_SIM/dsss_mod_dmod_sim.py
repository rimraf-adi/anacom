#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: DSSS Modulation Demodulation Simulation
# Author: AKADEMIKA Lab Solution
# Generated: Wed Jul 24 11:28:37 2019
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

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import numpy
import wx


class dsss_mod_dmod_sim(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="DSSS Modulation Demodulation Simulation")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 150000

        ##################################################
        # Blocks
        ##################################################
        self.notebook_0 = self.notebook_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Message Signal")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Generated Sequence")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Recovered Signal")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Spectrum of Recovered Signal")
        self.Add(self.notebook_0)
        self.wxgui_scopesink2_2_0_0 = scopesink2.scope_sink_f(
        	self.notebook_0.GetPage(0).GetWin(),
        	title='Message Signal',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.notebook_0.GetPage(0).GridAdd(self.wxgui_scopesink2_2_0_0.win, 2, 0, 1, 1)
        self.wxgui_scopesink2_2_0 = scopesink2.scope_sink_f(
        	self.notebook_0.GetPage(1).GetWin(),
        	title='Generated Sequence',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.notebook_0.GetPage(1).GridAdd(self.wxgui_scopesink2_2_0.win, 2, 0, 1, 1)
        self.wxgui_scopesink2_2 = scopesink2.scope_sink_f(
        	self.notebook_0.GetPage(2).GetWin(),
        	title='Recovered Signal',
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
        self.notebook_0.GetPage(2).GridAdd(self.wxgui_scopesink2_2.win, 2, 0, 1, 1)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
        	self.notebook_0.GetPage(3).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='Spectrum of Recovered Signal',
        	peak_hold=False,
        )
        self.notebook_0.GetPage(3).GridAdd(self.wxgui_fftsink2_0.win, 2, 0, 1, 1)
        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	2, samp_rate, 3000, 1000, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_1 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 2000, 1, 0)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 2, 100000)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.wxgui_scopesink2_2_0_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.blocks_char_to_float_0, 0), (self.wxgui_scopesink2_2_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_throttle_1, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_throttle_1, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.low_pass_filter_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.wxgui_scopesink2_2, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_2_0_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_2_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_2.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(2, self.samp_rate, 3000, 1000, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)


def main(top_block_cls=dsss_mod_dmod_sim, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
