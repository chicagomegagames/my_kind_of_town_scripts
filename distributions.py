from collections import OrderedDict
import random

# height and weight numbers derived from (with minor changes)
# https://www2.census.gov/library/publications/2010/compendia/statab/130ed/tables/11s0205.pdf

male_heights = OrderedDict([
    ("5'2",    0.0),
    ("5'3",    3.1),
    ("5'4",    4.4),
    ("5'5",    6.7),
    ("5'6",   13.1),
    ("5'7",   19.6),
    ("5'8",   32.2),
    ("5'9",   45.4),
    ("5'10",  58.1),
    ("5'11",  69.4),
    ("6'",    78.5),
    ("6'1",   89.0),
    ("6'2",   94.0),
    ("6'3",   95.8),
    ("6'4",   97.6),
    ("6'5",   99.4),
    ("6'6",   99.5),
    ("6'7",  100.0),
])

female_heights = OrderedDict([
    ("4'9",    0.0),
    ("4'10",   1.7),
    ("4'11",   3.1),
    ("5'0",    6.0),
    ("5'1",   11.6),
    ("5'2",   19.7),
    ("5'3",   31.1),
    ("5'4",   46.6),
    ("5'5",   61.2),
    ("5'6",   74.0),
    ("5'7",   84.9),
    ("5'8",   91.8),
    ("5'9",   96.1),
    ("5'10",  98.9),
    ("5'11",  99.0),
    ("6'",    99.4),
    ("6'1",   99.9),
    ("6'2",  100.0),
])

male_weights = OrderedDict([
    (120,   0.0),
    (130,   2.1),
    (140,   6.4),
    (150,  11.5),
    (160,  20.4),
    (170,  21.3),
    (180,  40.9),
    (190,  50.6),
    (200,  59.3),
    (210,  70.0),
    (220,  76.1),
    (230,  81.7),
    (240,  85.5),
    (250,  89.6),
    (260,  92.0),
    (270,  93.3),
    (280,  95.1),
    (290,  96.4),
    (300,  96.9),
    (320,  98.2),
    (340,  98.8),
    (360,  99.4),
    (380,  99.7),
    (400, 100.0),
])

female_weights = OrderedDict([
    ( 90,   0.0),
    (100,   1.3),
    (110,   4.7),
    (120,  10.5),
    (130,  18.9),
    (140,  29.8),
    (150,  40.6),
    (160,  51.1),
    (170,  59.8),
    (180,  68.7),
    (190,  73.6),
    (200,  79.4),
    (210,  83.7),
    (220,  89.0),
    (230,  91.3),
    (240,  94.1),
    (250,  95.2),
    (260,  95.8),
    (270,  96.4),
    (280,  97.2),
    (290,  97.5),
    (300,  98.4),
    (320,  99.1),
    (340,  99.5),
    (360,  99.7),
    (380,  99.9),
    (400, 100.0),
])

eye_colors = OrderedDict([
    ("none",    0),
    ("blue",   32),
    ("hazel",  47),
    ("green",  59),
    ("brown",  97),
    ("amber",  98),
    ("gray",  100),
])

def create_sample(data):
    sample = []
    reversed_keys = list(reversed(data.keys()))

    for i in range(0, len(reversed_keys) - 1):
        a = reversed_keys[i]
        b = reversed_keys[i + 1]

        percent = int(data[a] * 10) - int(data[b] * 10)

        for j in range(0, percent):
            sample.append(a)

    return sample

male_height_samples = create_sample(male_heights)
male_weight_samples = create_sample(male_weights)
female_height_samples = create_sample(female_heights)
female_weight_samples = create_sample(female_weights)

eye_colors = create_sample(eye_colors)

mf_sample = [
    {"sex": "male", "height": male_height_samples, "weight": male_weight_samples},
    {"sex": "female", "height": female_height_samples, "weight": female_weight_samples},
]

for i in range(0, 10):
    samples = random.choice(mf_sample)
    height = random.choice(samples["height"])
    weight = random.choice(samples["weight"])
    eye = random.choice(eye_colors)

    print("{} follower: {}\" {}lbs, {} eyes".format(samples["sex"], height, weight, eye))
