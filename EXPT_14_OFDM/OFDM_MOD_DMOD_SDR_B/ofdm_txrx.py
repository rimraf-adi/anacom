#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: OFDM Transmitter and Receiver
# Author: AKADEMIKA Lab Solution
# Generated: Fri Sep 23 01:26:22 2022
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
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import scopesink2
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import numpy
import wx


class ofdm_txrx(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="OFDM Transmitter and Receiver")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1000000

        ##################################################
        # Blocks
        ##################################################
        self.notebook_0 = self.notebook_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Input Stream of Bits")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Modulated Signal")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Spectrum of OFDM Signal")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Recovered Stream of Bits")
        self.Add(self.notebook_0)
        self.wxgui_scopesink2_2 = scopesink2.scope_sink_c(
        	self.notebook_0.GetPage(1).GetWin(),
        	title='Modulated Signal',
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
        self.notebook_0.GetPage(1).Add(self.wxgui_scopesink2_2.win)
        self.wxgui_scopesink2_1 = scopesink2.scope_sink_f(
        	self.notebook_0.GetPage(0).GetWin(),
        	title='Input Stream of Bits',
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
        self.notebook_0.GetPage(0).Add(self.wxgui_scopesink2_1.win)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_c(
        	self.notebook_0.GetPage(3).GetWin(),
        	title='Recovered Stream of Bits',
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
        self.notebook_0.GetPage(3).Add(self.wxgui_scopesink2_0.win)
        self.wxgui_fftsink2_1 = fftsink2.fft_sink_c(
        	self.notebook_0.GetPage(2).GetWin(),
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
        	title='Spectrum of OFDM Signal',
        	peak_hold=False,
        )
        self.notebook_0.GetPage(2).Add(self.wxgui_fftsink2_1.win)
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
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
        self.digital_ofdm_mod_0 = grc_blks2.packet_mod_f(digital.ofdm_mod(
        		options=grc_blks2.options(
        			modulation="bpsk",
        			fft_length=512,
        			occupied_tones=200,
        			cp_length=128,
        			pad_for_usrp=True,
        			log=None,
        			verbose=None,
        		),
        	),
        	payload_length=0,
        )
        self.digital_ofdm_demod_0 = grc_blks2.packet_demod_c(digital.ofdm_demod(
        		options=grc_blks2.options(
        			modulation="bpsk",
        			fft_length=512,
        			occupied_tones=200,
        			cp_length=128,
        			snr=20,
        			log=None,
        			verbose=None,
        		),
        		callback=lambda ok, payload: self.digital_ofdm_demod_0.recv_pkt(ok, payload),
        	),
        )
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.analog_random_source_x_0 = blocks.vector_source_s(map(int, numpy.random.randint(0, 2, 10000)), True)
        self.akademika_source_0 = iio.pluto_source('ip:akademika.local', int(400000000), int(2084000), int(20000000), 0x8000, True, True, True, "manual", 0, '', True)
        self.akademika_sink_0 = iio.pluto_sink('ip:akademika.local', int(400000000), int(2084000), int(20000000), 0x8000, False, 10.0, '', True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.akademika_source_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.blocks_short_to_float_0, 0), (self.digital_ofdm_mod_0, 0))
        self.connect((self.blocks_short_to_float_0, 0), (self.wxgui_scopesink2_1, 0))
        self.connect((self.blocks_throttle_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.digital_ofdm_demod_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.digital_ofdm_mod_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.digital_ofdm_mod_0, 0), (self.wxgui_fftsink2_1, 0))
        self.connect((self.digital_ofdm_mod_0, 0), (self.wxgui_scopesink2_2, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.akademika_sink_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.digital_ofdm_demod_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_2.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_1.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)


def main(top_block_cls=ofdm_txrx, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
