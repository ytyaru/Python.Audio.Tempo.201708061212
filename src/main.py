#!python3.6
#coding:utf-8
import time
import Player
import Sampler
import BaseWaveMaker
import MusicTheory.EqualTemperament
import MusicTheory.Scale
import MusicTheory.tempo
import WaveFile
if __name__ == "__main__" :
    wm = BaseWaveMaker.BaseWaveMaker()
    sampler = Sampler.Sampler()

    et = MusicTheory.EqualTemperament.EqualTemperament()
    scale = MusicTheory.Scale.Scale()
    timebase = MusicTheory.tempo.TimeBase()
    timebase.BPM = 120
    timebase.Metre=(4,4)
    nv = MusicTheory.tempo.NoteValue(timebase)

    p = Player.Player()
    p.Open()
    print('---------- メジャー・スケール ----------')
    for key in ['C','C+','D','D+','E','F','F+','G','G+','A','A+','B']:
        print(key, 'メジャー・スケール')
        scale.Major(key=key)
#        print(','.join([MusicTheory.Key.Key.ValueToName(k) for k in scale.Scales]))
#        print(','.join([str(f0) for f0 in scale.Frequencies]))
        for f0 in scale.Frequencies:
            p.Play(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=f0, sec=nv.Get(4))))
#            p.Play(sampler.Sampling(wm.Triangle(a=1, fs=8000, f0=f0, sec=0.25)))
        time.sleep(1)
    print('---------- マイナー・スケール ----------')
    for key in ['C','C+','D','D+','E','F','F+','G','G+','A','A+','B']:
        print(key, 'マイナー・スケール')
        scale.Minor(key=key)
#        print(','.join([MusicTheory.Key.Key.ValueToName(k) for k in scale.Scales]))
#        print(','.join([str(f0) for f0 in scale.Frequencies]))
        for f0 in scale.Frequencies:
            p.Play(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=f0, sec=nv.Get(4))))
#            p.Play(sampler.Sampling(wm.Triangle(a=1, fs=8000, f0=f0, sec=0.25)))
        time.sleep(1)
    p.Close()
