# Kickdrum Script for Clone Hero

This is a script that turns an guitar pedal plugged through an audio interface into a kick pedal for rhythm games like Clone Hero.

## Story behind the project
One day I bought Rockband drums but unfortunately they didn't come with the pedal. I also couldn't find any loose pedals on the internet. <br/>
It got me thinking about other options. I looked around my room and saw a guitar pedal that lets me switch my amp from lead to clean and vice versa.<br/>
I curiosly plugged it to my interface as an audio input to see what will i hear on my headphones. When i plugged it in there was total silence,<br/>
but when i pressed it there was a quiet bzzzzt. It was really kind of binary and perfectly synced up with the press.<br/>
I proceeded to embark on a journey to turn that bzzzt in my head into a keyboard input.

## How it works
This scripts isn't exactly advanced nor is it suitable for every specs. It just registers my audio interface, then on every tick it calculates the<br/>
average volume of the registered sounds. Then it just checks whether the volume passed a certain threshold and if it does, then it gives back a keyboard<br/>
input of the number 7. Additionaly it waits for the release of the pedal (by checking if the volume is still high), so when you hold the pedal <br/>
it doesn't give you 7 continously, but just once until you release it.

## How to use
As i said, the script isn't suitable for every situation. It's expected to be finely tuned accordingly.<br/>
First you make the setup (you plug an audio interface to your pc, then a pedal as an audio input).<br/>
Also open the script and make sure you have the needed python libraries.<br/>
Then you launch the script and wait for 2 seconds.<br/>
After that you will probably have to change the compared values in if statements for them to register the presses.<br/>
It shouldn't be that hard as the script also continously prints the volume captured from the interface.<br/>

##
**Well have fun!** I hope it works for youuu!
