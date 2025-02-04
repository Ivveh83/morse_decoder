This is a two-way Morse Decoder. 
You can type in a sentence or a word of your choice and have it to played up in Morse Code. 
You can also choose to decode a morse signal and have it translated into pure text.
The first part (text --> morse) was pretty easy to code.


The second part (morse --> text) was more tricky...


It took me a bit of rethinking and plenty of rework...


Firstly, to be able to understand the reasons behind the method I've choose, there needs to be a
few words about Morse Code. Morse Code is simply a combination of long and short beeps and pauses -
short pauses between beeps and characters, longer pauses between words. So all in all there are four
signs that carries significance: short beep (.), long beep (-), short pause (/), long pause (//). And those are the 
ones to decipher.

One way to translate audio into text is to first convert the soundwaves into an image. Once you have
an image, you messaure the lengt of the sounds and pauses in the image to be able to decide if it is
a long or a short pause/beep.

After I had been laborating with different spectrograms, I understood that a melospectrogram is the 
best pick, since it images the dB - the louder the sound the more intense the color on the melospectrogram.
It took a bit of laborating to find the best cap for the dB, so that just enough information was drawn
into the picture, but to leave the distortion out.

To decode the melospectrogram, my first approach was to use Machine Learning, first with Conv2D- and 
later with LSTM-technique. But since I didn't had enough data to train the model, this attempt failed big time. Even
though it would've been cool to use Machine Learning, my second approach - analyze column for column with
pixels - turned out to be way more fruitful. The more columns that are filled with white pixels (sound) in 
a row, the longer the beep. And the opposite - the more columns that are filled with black pixels (pause) in 
a row, the longer the pause. And after that there is only to calculate the columns of sound vs pause, compare them
to each other, and that will give us a morse code.
