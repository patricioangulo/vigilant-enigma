

suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
def humansize(nbytes):
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])

def file_time(size_file):
    #audio sample rate = 8 kHz
        audio_sample_rate = 8000
        #Channels: Mono (1) Stereo (2)
        channels = 1
        #bit depth = 16 bit
        bit_per_sample = 16
        divisor = audio_sample_rate * channels * (bit_per_sample/8)
        time = size_file/divisor
        return(time)    