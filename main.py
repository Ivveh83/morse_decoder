from write import Write
from play import Play
from record_sound import Record
from  analyze import Analyze
import time

choice = input('Do you wish to play, record or analyze a morse signal?'
               ' Write "play", "record" or "analyze" for your choice:\n').lower()

if choice == 'play':
    text = input('Write something: ')

    writing_text = Write()
    text_to_morse = writing_text.write(text)
    print(f"Morse Code: {text_to_morse}")

    play_text = Play()
    play_text.play(text)
elif choice == 'record':
    record_time = int(input('How many seconds do you wish to record? Write in numbers:\n'))
    recorded_sound = Record()
    print('Starting to record in 3...')
    time.sleep(1)
    print('2...')
    time.sleep(1)
    print('1...')
    time.sleep(1)
    recorded_sound.record(record_time)
    recorded_sound.create_spectrogram()
elif choice == 'analyze':
    analyze = Analyze()
    binary_morse_spectrogram = analyze.read_spectrogram()
    morse_sequence = analyze.analyze_spectrogram(binary_morse_spectrogram)
    code = analyze.read_morse_sequence(morse_sequence)
    grouped_morse_code = analyze.create_morse(code)
    morse_to_text = analyze.decode_morse(grouped_morse_code)

    print(f"Morse code translates as: {morse_to_text.capitalize()}")



