#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: FM_Modulation
# Author: AKADEMIKA Lab Solution
# Description: NBFM Modulation Technique
# Generated: Thu Aug 20 16:07:46 2015
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class fm_mod_sim(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="FM_Modulation")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate1 = samp_rate1 = 500000
        self.samp_rate = samp_rate = 400000
        self.interp_factor = interp_factor = 4
        self.carrier_freq = carrier_freq = 100000
        self.amplitude = amplitude = 1

        ##################################################
        # Blocks
        ##################################################
        _amplitude_sizer = wx.BoxSizer(wx.VERTICAL)
        self._amplitude_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_amplitude_sizer,
        	value=self.amplitude,
        	callback=self.set_amplitude,
        	label='amplitude',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._amplitude_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_amplitude_sizer,
        	value=self.amplitude,
        	callback=self.set_amplitude,
        	minimum=0,
        	maximum=10,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_amplitude_sizer)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate1,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="Specral Representation",
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.blocks_throttle_1 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.analog_sig_source_x_1 = analog.sig_source_c(samp_rate1, analog.GR_COS_WAVE, carrier_freq, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 2000, amplitude, 0)
        self.analog_nbfm_tx_0 = analog.nbfm_tx(
        	audio_rate=32000,
        	quad_rate=32000*interp_factor,
        	tau=75e-6,
        	max_dev=5e3,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_tx_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.analog_nbfm_tx_0, 0))    
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_throttle_1, 0))    
        self.connect((self.blocks_throttle_1, 0), (self.wxgui_fftsink2_0, 0))    


    def get_samp_rate1(self):
        return self.samp_rate1

    def set_samp_rate1(self, samp_rate1):
        self.samp_rate1 = samp_rate1
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate1)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate1)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_1.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_interp_factor(self):
        return self.interp_factor

    def set_interp_factor(self, interp_factor):
        self.interp_factor = interp_factor

    def get_carrier_freq(self):
        return self.carrier_freq

    def set_carrier_freq(self, carrier_freq):
        self.carrier_freq = carrier_freq
        self.analog_sig_source_x_1.set_frequency(self.carrier_freq)

    def get_amplitude(self):
        return self.amplitude

    def set_amplitude(self, amplitude):
        self.amplitude = amplitude
        self._amplitude_slider.set_value(self.amplitude)
        self._amplitude_text_box.set_value(self.amplitude)
        self.analog_sig_source_x_0.set_amplitude(self.amplitude)

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = fm_mod_sim()
    tb.Start(True)
    tb.Wait()
