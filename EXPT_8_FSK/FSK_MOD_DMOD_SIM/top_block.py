#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: FSK Demodulation
# Author: AKADEMIKA Lab Solution
# Generated: Wed Jul 24 11:16:55 2019
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
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="FSK Demodulation")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1000000
        self.freq1 = freq1 = 50000
        self.freq = freq = 10000
        self.ampli = ampli = 1

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title='Scope Plot',
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
        self.Add(self.wxgui_scopesink2_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
        	self.GetWin(),
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
        	title='FFT Plot',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.mixer_1 = blocks.multiply_vff(1)
        self.mixer_0_0 = blocks.multiply_vff(1)
        self.mixer_0 = blocks.multiply_vff(1)
        self.mixer = blocks.multiply_vff(1)
        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, 3000, 1000, firdes.WIN_HAMMING, 6.76))
        self.invert = blocks.multiply_const_vff((-1, ))
        self.delay = blocks.add_const_vff((1, ))
        self.blocks_threshold_ff_0 = blocks.threshold_ff(0, 0.4, 0)
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_0_2 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, freq, ampli, 0)
        self.analog_sig_source_x_0_1_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, freq1, ampli, 0)
        self.analog_sig_source_x_0_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, freq1, ampli, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_SQR_WAVE, 2000, ampli, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, freq, ampli, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.mixer_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.invert, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.mixer_0, 1))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.mixer, 1))
        self.connect((self.analog_sig_source_x_0_1_0, 0), (self.mixer_1, 1))
        self.connect((self.analog_sig_source_x_0_2, 0), (self.mixer_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.mixer_0_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.mixer_1, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.delay, 0), (self.mixer, 0))
        self.connect((self.invert, 0), (self.delay, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.mixer, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.mixer_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.mixer_0_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.mixer_1, 0), (self.blocks_add_xx_1, 1))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 3000, 1000, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0_2.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_freq1(self):
        return self.freq1

    def set_freq1(self, freq1):
        self.freq1 = freq1
        self.analog_sig_source_x_0_1_0.set_frequency(self.freq1)
        self.analog_sig_source_x_0_1.set_frequency(self.freq1)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.analog_sig_source_x_0_2.set_frequency(self.freq)
        self.analog_sig_source_x_0.set_frequency(self.freq)

    def get_ampli(self):
        return self.ampli

    def set_ampli(self, ampli):
        self.ampli = ampli
        self.analog_sig_source_x_0_2.set_amplitude(self.ampli)
        self.analog_sig_source_x_0_1_0.set_amplitude(self.ampli)
        self.analog_sig_source_x_0_1.set_amplitude(self.ampli)
        self.analog_sig_source_x_0_0.set_amplitude(self.ampli)
        self.analog_sig_source_x_0.set_amplitude(self.ampli)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
