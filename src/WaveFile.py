#http://qiita.com/mzmttks/items/7a7c8c4b42007e13812a
import wave
from pydub import AudioSegment
class WaveFile:
    @staticmethod
    def Write(data, bit=16, fs=8000, channels=1, filename='output.wav'):    
        wf = wave.open(filename, "w")
#        wf.setnchannels(channels)
#        wf.setsampwidth(bit / 8)
#        wf.setframerate(fs)
        wf.setparams((
            channels,                 # channel
            int(bit / 8),             # byte width
            fs,                       # sampling rate
            len(data),                # number of frames
            "NONE", "not compressed"  # no compression
        ))
        wf.writeframes(data)
        wf.close()

def create_dirs(basepath):
    #$ mkdir -p  res/scales/wav/
    basepath = pathlib.PurePath('../res/scales')
#    basepath = pathlib.PurePath('../res/scales/wav')
    pathlib.Path(basepath).mkdir(parents=True, exist_ok=True)
    pathlib.Path(basepath.joinpath('wav')).mkdir(parents=True, exist_ok=True)
    pathlib.Path(basepath.joinpath('ogg')).mkdir(parents=True, exist_ok=True)
    pathlib.Path(basepath.joinpath('mp3')).mkdir(parents=True, exist_ok=True)
    pathlib.Path(basepath.joinpath('flac')).mkdir(parents=True, exist_ok=True)
    # resolve().mkdir(...) とすると作成されない
#    basepath = pathlib.PurePath('../res/scales/wav/')
#    pathlib.Path(basepath).resolve().mkdir(parents=True, exist_ok=True)
#    pathlib.Path(basepath.joinpath('dummpy.txt')).resolve().mkdir(parents=True, exist_ok=True)

def convert(filename):
    basepath = pathlib.PurePath('../res/scales')
    extensions = ['mp3', 'ogg', 'flac']
    for ext in extensions:
        f = AudioSegment.from_file(str(pathlib.Path(basepath.joinpath('wav', filename + '.' + 'wav')).resolve()))
    #    f = AudioSegment.from_file("res/CMajor.wav")
        basepath.joinpath(ext, filename + '.' + ext)
#        kwargs = {'format': ext}
        kwargs = {'format': ext, 'bitrate': '32k'}
#        if 'mp3' == ext: kwargs['bitrate'] = '32k'
#        f.export(str(pathlib.Path(basepath.joinpath(ext, filename + '.' + ext)).resolve(), **kwargs))
        f.export(str(pathlib.Path(basepath.joinpath(ext, filename + '.' + ext)).resolve()), **kwargs)
#        f.export("res/CMajor.mp3", format="mp3", bitrate='32k')
#        f.export("res/CMajor.ogg", format="ogg")
#        f.export("res/CMajor.flac", format="flac")

    

if __name__ == "__main__":
    import pathlib
    import Sampler
    import BaseWaveMaker
    import MusicTheory.EqualTemperament
    import MusicTheory.Scale
    import MusicTheory.tempo
    
    basepath = pathlib.PurePath('../res/scales/wav/')
    create_dirs(basepath)
    
    wm = BaseWaveMaker.BaseWaveMaker()
    sampler = Sampler.Sampler()
    scale = MusicTheory.Scale.Scale()
    timebase = MusicTheory.tempo.TimeBase()
    timebase.BPM = 120
    timebase.Metre=(4,4)
    nv = MusicTheory.tempo.NoteValue(timebase)
    for key in ['C']:
#    for key in ['C','C+','D','D+','E','F','F+','G','G+','A','A+','B']:
        print(key, 'メジャー・スケール')
        scale.Major(key=key)
        waves = []
        for f0 in scale.Frequencies:
            waves.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=f0, sec=nv.Get(4))))
#            p.Play(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=f0, sec=0.25)))
#            p.Play(sampler.Sampling(wm.Triangle(a=1, fs=8000, f0=f0, sec=0.25)))
        name = key.replace('+', 's') + 'Major'
        WaveFile.Write(b''.join(waves), filename=str(pathlib.Path(basepath.joinpath(name + '.wav')).resolve()))
        convert(name)
        
        print(key, 'マイナー・スケール')
        scale.Minor(key=key)
        waves = []
        for f0 in scale.Frequencies:
            waves.append(sampler.Sampling(wm.Sin(a=1, fs=8000, f0=f0, sec=nv.Get(4))))
#        WaveFile.Write(b''.join(waves), filename=key.replace('+', 's') + 'Minor' + '.wav')
        name = key.replace('+', 's') + 'Minor'
        WaveFile.Write(b''.join(waves), filename=str(pathlib.Path(basepath.joinpath(name + '.wav')).resolve()))
        convert(name)

