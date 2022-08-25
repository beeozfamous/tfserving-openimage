import random
LEVEL_1_LABELS = ['Accordion', 'Adhesive tape', 'Airplane', 'Alarm clock', 'Alpaca', 'Ambulance', 'Ant', 'Antelope',
                  'Apple', 'Artichoke', 'Asparagus', 'Backpack', 'Bagel', 'Balloon', 'Banana', 'Barge', 'Barrel',
                  'Baseball bat', 'Baseball glove', 'Bat', 'Bathroom cabinet', 'Bathtub', 'Beaker', 'Bee', 'Beehive',
                  'Beer', 'Bell pepper', 'Belt', 'Bench', 'Bicycle', 'Bicycle helmet', 'Bicycle wheel', 'Bidet',
                  'Billboard', 'Billiard table', 'Binoculars', 'Blender', 'Blue jay', 'Book', 'Bookcase', 'Boot',
                  'Bottle', 'Bow and arrow', 'Bowl', 'Box', 'Boy', 'Brassiere', 'Bread', 'Briefcase', 'Broccoli',
                  'Bronze sculpture', 'Brown bear', 'Bull', 'Burrito', 'Bus', 'Bust', 'Butterfly', 'Cabbage',
                  'Cabinetry', 'Cake', 'Cake stand', 'Camel', 'Camera', 'Canary', 'Candle', 'Candy', 'Cannon',
                  'Canoe', 'Carrot', 'Cart', 'Castle', 'Cat', 'Caterpillar', 'Cattle', 'Ceiling fan', 'Cello',
                  'Centipede', 'Chair', 'Cheetah', 'Chest of drawers', 'Chicken', 'Chopsticks', 'Christmas tree',
                  'Coat', 'Cocktail', 'Coconut', 'Coffee', 'Coffee cup', 'Coffee table', 'Coffeemaker', 'Coin',
                  'Common fig', 'Computer keyboard', 'Computer monitor', 'Computer mouse', 'Convenience store',
                  'Cookie', 'Corded phone', 'Countertop', 'Cowboy hat', 'Crab', 'Cricket ball', 'Crocodile',
                  'Croissant', 'Crown', 'Crutch', 'Cucumber', 'Cupboard', 'Curtain', 'Cutting board', 'Dagger',
                  'Deer', 'Desk', 'Dice', 'Digital clock', 'Dinosaur', 'Dog', 'Dog bed', 'Doll', 'Dolphin',
                  'Door', 'Door handle', 'Doughnut', 'Dragonfly', 'Drawer', 'Dress', 'Drinking straw', 'Drum',
                  'Duck', 'Dumbbell', 'Eagle', 'Earrings', 'Egg', 'Elephant', 'Envelope', 'Falcon', 'Fedora',
                  'Filing cabinet', 'Fire hydrant', 'Fireplace', 'Flag', 'Flashlight', 'Flowerpot', 'Flute',
                  'Food processor', 'Football', 'Football helmet', 'Fork', 'Fountain', 'Fox', 'French fries',
                  'Frog', 'Frying pan', 'Gas stove', 'Giraffe', 'Girl', 'Glasses', 'Goat', 'Goggles', 'Goldfish',
                  'Golf ball', 'Golf cart', 'Gondola', 'Goose', 'Grape', 'Grapefruit', 'Guacamole', 'Guitar',
                  'Hamburger', 'Hamster', 'Handbag', 'Handgun', 'Harbor seal', 'Harp', 'Harpsichord', 'Headphones',
                  'Helicopter', 'High heels', 'Honeycomb', 'Horn', 'Horse', 'Hot dog', 'House', 'Houseplant',
                  'Human arm', 'Human beard', 'Human ear', 'Human eye', 'Human face', 'Human foot', 'Human hair',
                  'Human hand', 'Human head', 'Human leg', 'Human mouth', 'Human nose', 'Ice cream', 'Infant bed',
                  'Jacket', 'Jaguar', 'Jeans', 'Jellyfish', 'Jet ski', 'Jug', 'Juice', 'Kangaroo', 'Kettle',
                  'Kitchen & dining room table', 'Kitchen knife', 'Kite', 'Knife', 'Ladder', 'Ladybug', 'Lamp',
                  'Lantern', 'Laptop', 'Lavender', 'Lemon', 'Leopard', 'Lifejacket', 'Light bulb', 'Light switch',
                  'Lighthouse', 'Lily', 'Limousine', 'Lion', 'Lizard', 'Lobster', 'Loveseat', 'Lynx', 'Man',
                  'Mango', 'Maple', 'Measuring cup', 'Mechanical fan', 'Microphone', 'Microwave oven', 'Miniskirt',
                  'Mirror', 'Missile', 'Mixer', 'Mobile phone', 'Monkey', 'Motorcycle', 'Mouse', 'Muffin', 'Mug',
                  'Mule', 'Mushroom', 'Musical keyboard', 'Nail', 'Necklace', 'Nightstand', 'Oboe', 'Office building',
                  'Orange', 'Organ', 'Ostrich', 'Otter', 'Oven', 'Owl', 'Oyster', 'Paddle', 'Palm tree', 'Pancake',
                  'Paper towel', 'Parachute', 'Parrot', 'Pasta', 'Peach', 'Pear', 'Pen', 'Penguin', 'Piano',
                  'Picnic basket', 'Picture frame', 'Pig', 'Pillow', 'Pineapple', 'Pitcher', 'Pizza', 'Plastic bag',
                  'Plate', 'Platter', 'Polar bear', 'Pomegranate', 'Popcorn', 'Porch', 'Porcupine', 'Poster',
                  'Potato', 'Power plugs and sockets', 'Pressure cooker', 'Pretzel', 'Printer', 'Pumpkin',
                  'Punching bag', 'Rabbit', 'Raccoon', 'Radish', 'Raven', 'Refrigerator', 'Rhinoceros', 'Rifle',
                  'Ring binder', 'Rocket', 'Roller skates', 'Rose', 'Rugby ball', 'Ruler', 'Salad',
                  'Salt and pepper shakers', 'Sandal', 'Saucer', 'Saxophone', 'Scarf', 'Scissors', 'Scoreboard',
                  'Screwdriver', 'Sea lion', 'Sea turtle', 'Seahorse', 'Seat belt', 'Segway', 'Serving tray',
                  'Sewing machine', 'Shark', 'Sheep', 'Shelf', 'Shirt', 'Shorts', 'Shotgun', 'Shower', 'Shrimp',
                  'Sink', 'Skateboard', 'Ski', 'Skull', 'Skyscraper', 'Slow cooker', 'Snail', 'Snake', 'Snowboard',
                  'Snowman', 'Snowmobile', 'Snowplow', 'Sock', 'Sofa bed', 'Sombrero', 'Sparrow', 'Spatula',
                  'Spider', 'Spoon', 'Sports uniform', 'Squirrel', 'Stairs', 'Starfish', 'Stationary bicycle',
                  'Stool', 'Stop sign', 'Strawberry', 'Street light', 'Stretcher', 'Studio couch',
                  'Submarine sandwich', 'Suit', 'Suitcase', 'Sun hat', 'Sunflower', 'Sunglasses', 'Surfboard',
                  'Sushi', 'Swan', 'Swim cap', 'Swimming pool', 'Swimwear', 'Sword', 'Table tennis racket',
                  'Tablet computer', 'Taco', 'Tank', 'Tap', 'Tart', 'Taxi', 'Tea', 'Teapot', 'Teddy bear',
                  'Television', 'Tennis ball', 'Tennis racket', 'Tent', 'Tiara', 'Tick', 'Tie', 'Tiger', 'Tin can',
                  'Tire', 'Toaster', 'Toilet', 'Toilet paper', 'Tomato', 'Torch', 'Tortoise', 'Towel', 'Tower',
                  'Traffic light', 'Train', 'Training bench', 'Treadmill', 'Tripod', 'Trombone', 'Truck',
                  'Trumpet', 'Turkey', 'Umbrella', 'Van', 'Vase', 'Vehicle registration plate', 'Violin',
                  'Volleyball', 'Waffle', 'Wall clock', 'Washing machine', 'Waste container', 'Watch',
                  'Watermelon', 'Whale', 'Wheel', 'Wheelchair', 'Whiteboard', 'Willow', 'Window',
                  'Window blind', 'Wine', 'Wine glass', 'Winter melon', 'Wok', 'Woman', 'Wood-burning stove',
                  'Woodpecker', 'Wrench', 'Zebra', 'Zucchini']


LEVEL_2_LABELS = ['Toy', 'Home appliance', 'Plumbing fixture', 'Office supplies', 'Tableware', 'Kitchen appliance',
                  'Couch', 'Bed', 'Table', 'Clock', 'Sculpture', 'Traffic sign', 'Building', 'Person', 'Dessert',
                  'Fruit', 'Shellfish', 'Squash', 'Sandwich', 'Tree', 'Flower', 'Car', 'Boat', 'Aircraft', 'Hat',
                  'Skirt', 'Glove', 'Trousers', 'Footwear', 'Luggage and bags', 'Helmet', 'Bird',
                  'Marine invertebrates', 'Beetle', 'Moths and butterflies', 'Bear', 'Marine mammal', 'Turtle',
                  'Fish', 'Personal care', 'Musical instrument', 'Ball', 'Racket', 'Weapon', 'Telephone',
                  'Drink']

LEVEL_3_LABELS = ['Seafood', 'Watercraft', 'Insect', 'Carnivore']

# Some classes upper to make more than one class for single net
LEVEL_4_LABELS = ['Vegetable', 'Land vehicle', 'Reptile', 'Invertebrate']

# Some classes upper to make more than one class for single net
LEVEL_5_LABELS = ['Furniture', 'Vehicle', 'Animal']

# Classes with less than 500 samples in train
LEVEL_1_LABELS_LOW_SAMPLES = ['Adhesive tape', 'Alarm clock', 'Ambulance', 'Artichoke', 'Asparagus', 'Bathroom cabinet',
                              'Beaker', 'Belt', 'Bidet', 'Binoculars', 'Blender', 'Blue jay', 'Briefcase', 'Burrito',
                              'Cabbage', 'Cake stand', 'Canary', 'Ceiling fan', 'Centipede', 'Coffeemaker', 'Common fig',
                              'Corded phone', 'Cricket ball', 'Croissant', 'Crutch', 'Cutting board', 'Dagger',
                              'Digital clock', 'Dog bed', 'Drinking straw', 'Dumbbell', 'Envelope', 'Filing cabinet',
                              'Fire hydrant', 'Flashlight', 'Flute', 'Food processor', 'Frying pan', 'Golf ball',
                              'Guacamole', 'Harp', 'Harpsichord', 'Honeycomb', 'Hot dog', 'Infant bed',
                              'Kitchen knife', 'Light switch', 'Limousine', 'Lynx', 'Mango', 'Measuring cup',
                              'Microwave oven', 'Mixer', 'Nail', 'Oboe', 'Organ', 'Paper towel', 'Picnic basket',
                              'Pitcher', 'Popcorn', 'Porcupine', 'Power plugs and sockets', 'Pressure cooker',
                              'Pretzel', 'Printer', 'Punching bag', 'Raccoon', 'Ring binder', 'Rugby ball', 'Ruler',
                              'Salt and pepper shakers', 'Scissors', 'Screwdriver', 'Seahorse', 'Seat belt',
                              'Serving tray', 'Sewing machine', 'Shower', 'Slow cooker', 'Snowmobile', 'Snowplow',
                              'Spatula', 'Stationary bicycle', 'Stop sign', 'Stretcher', 'Submarine sandwich',
                              'Tiara', 'Tick', 'Toaster', 'Toilet paper', 'Torch', 'Towel', 'Training bench',
                              'Treadmill', 'Winter melon', 'Wood-burning stove', 'Wrench']

# All labels
ALL_LABELS = LEVEL_1_LABELS + LEVEL_2_LABELS + LEVEL_3_LABELS + LEVEL_4_LABELS + LEVEL_5_LABELS

COLOR_LIST = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) for i in range(500)]
