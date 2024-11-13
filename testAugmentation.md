# test 1
tutte le augmentation che implicano cambi di colore dell'immagine 

| nome | score |
|------|-------|
| channelShuffle | 88.87%   |
| RandomCutout | 95.73%   |
| RandomHue |  12.5%   |
| JitteredResize  | 94.45%    |
| RandomSaturation | 14.03%     |
| RandomSharpness | 12.5%  |

# test 2 

|index|Augmentation Combination|Accuracy|
|---|---|---|
|0|empty model|95\.76|
|1|channelShuffle|90\.13|
|2|RandomCutout|92\.97|
|3|JitteredResize|93\.67|
|4|RandomShear|92\.97|
|5|channelShuffle\_RandomCutout|91\.87|
|6|channelShuffle\_JitteredResize|91\.74|
|7|channelShuffle\_RandomShear|94\.66|
|8|RandomCutout\_JitteredResize|91\.28|
|9|RandomCutout\_RandomShear|92\.84|
|10|JitteredResize\_RandomShear|90\.37|
|11|channelShuffle\_RandomCutout\_JitteredResize|91\.36|
|12|channelShuffle\_RandomCutout\_RandomShear|13\.04|
|13|channelShuffle\_JitteredResize\_RandomShear|91\.77|
|14|channelShuffle\_RandomShear\_RandomCutout|93\.83|
|15|RandomCutout\_JitteredResize\_RandomShear|92\.11|
|16|channelShuffle\_RandomCutout\_JitteredResize\_RandomShear|93\.56|
