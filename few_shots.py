few_shots = [
    {
        'Question': 'Give me all the front of store products',
        'SQLQuery': "SELECT * FROM zara_sales_data WHERE `Product Position` = 'Front of Store'",
        'SQLResult': 'Result of the SQL query',
        'Answer': "[('127644', 'Front of Store', 'No', 'Clothing', 'Yes', 1498, 'Zara', 'https://www.zara.com/us/en/topstitch-sneakers-p12240320.html', '311287075-120-39', 'TOPSTITCH SNEAKERS', 'Sneakers. Pieces and topstitching at upper. Lacing with six pairs of eyelets. Contrasting slightly chunky soles.', 45.9, 'USD', '2/19/2024 9:00', 'shoes', 'MAN'), ('144848', 'Front of Store', 'No', 'Clothing', 'No', 2193, 'Zara', 'https://www.zara.com/us/en/chunky-sole-canvas-lace-up-boots-p12005320.html', '311287149-800-39', 'CHUNKY SOLE CANVAS LACE-UP BOOTS', 'High shaft boots. Lacing with eight pairs of eyelets. Back pull tab for ease. Rounded shape. Chunky lug soles.', 89.9, 'USD', '2/19/2024 9:00', 'shoes', 'MAN')]"
    },
    {
        'Question': "list all of the productId's and names of product which are not promoted and not seasonal",
        'SQLQuery': "SELECT `Product ID`, name FROM zara_sales_data WHERE Promotion = 'No' AND Seasonal = 'No'",
        'SQLResult': 'Result of the SQL query',
        'Answer': '185102, BASIC PUFFER JACKET'
    },
    {
        'Question': "List all of the productId's and names of the products where volume and price is more than 2000 and 120 simultaneously",
        'SQLQuery': 'SELECT `Product ID` , name FROM zara_sales_data WHERE `Sales Volume` > 2000 AND price > 120',
        'SQLResult': 'Result of the SQL query',
        'Answer': "[('180176', 'SLIM FIT SUIT JACKET'), ('192936', 'DOUBLE FACED JACKET'), ('182157', 'SUIT JACKET IN 100% LINEN')]"
    },
    {
        'Question': 'List all of the names of the jackets',
        'SQLQuery': "SELECT name FROM zara_sales_data WHERE terms = 'jackets'",
        'SQLResult': 'Result of the SQL query',
        'Answer': 'BASIC PUFFER JACKET, TUXEDO JACKET, SLIM FIT SUIT JACKET, STRETCH SUIT JACKET, DOUBLE FACED JACKET, CONTRASTING COLLAR JACKET, FAUX LEATHER PUFFER JACKET, SUIT JACKET IN 100% LINEN, 100% WOOL SUIT JACKET, 100% FEATHER FILL PUFFER JACKET, HERRINGBONE TEXTURED JACKET, OVERSIZED CROPPED JACKET LIMITED EDITION, LEATHER BIKER JACKET, CROPPED LEATHER JACKET, FAUX LEATHER BOXY FIT JACKET, FAUX LEATHER JACKET, FAUX SUEDE BOMBER JACKET, DENIM BOMBER JACKET, BOUCLÉ TEXTURED JACKET, SUIT JACKET IN 100% LINEN, JACQUARD DENIM JACKET, PADDED DENIM JACKET, LEATHER JACKET, LIGHTWEIGHT BOMBER JACKET, SUIT JACKET, FAUX LEATHER BOMBER JACKET, PATCH BOMBER JACKET, STRETCH POCKET OVERSHIRT, RIB COLLAR JACKET, FAUX LEATHER OVERSIZED JACKET LIMITED EDITION, CONTRASTING PATCHES BOMBER JACKET, PATCH BOMBER JACKET, CROPPED BOMBER JACKET LIMITED EDITION, FAUX LEATHER PUFFER JACKET, FAUX LEATHER BOMBER JACKET, BOMBER JACKET, FAUX SUEDE JACKET, FAUX SUEDE BOMBER JACKET, SUEDE JACKET, CONTRASTING COLLAR JACKET, TEXTURED JACKET, CROPPED TEXTURED JACKET, POCKET PUFFER JACKET, TECHNICAL JACKET WITH POCKETS, FAUX LEATHER JACKET, FAUX SUEDE JACKET, RIPPED DENIM JACKET, TEXTURED POCKET JACKET, FAUX SUEDE PATCH JACKET, PUFFER JACKET WITH POUCH POCKET, BOMBER JACKET, TEXTURED WEAVE OVERSHIRT, STRAIGHT SUIT JACKET, HOODED QUILTED JACKET, LIGHTWEIGHT PUFFER JACKET, COTTON BLEND BOMBER JACKET, POCKET JACKET, OVERSIZED BOMBER JACKET, EMBROIDERED PATCH JACKET, ACID WASH DENIM JACKET, VINTAGE EFFECT LEATHER BOMBER JACKET, TEXTURED DENIM JACKET LIMITED EDITION, WOOL BLEND JACKET, COTTON - LINEN BLEND JACKET, FLEECE BOMBER JACKET, ZIPPERED JACKET, COTTON JACKET, WOOL BLEND TEXTURED JACKET, CONTRAST JACQUARD JACKET, CROPPED OVERSHIRT, CONTRASTING PATCHES HOODED JACKET, UTILITY POCKET JACKET, , LIGHTWEIGHT BOMBER JACKET, WOOL BLEND JACKET, TECHNICAL PADDED JACKET, MIXED COLLAR WAXED JACKET, CONTRASTING PATCHES BOMBER JACKET, PADDED BOMBER JACKET, TECHNICAL PADDED JACKET, POCKET DENIM JACKET, BOXY FIT DENIM JACKET, FAUX SHEARLING PLAID JACKET, EMBROIDERED FOREST JACKET, POCKET OVERSHIRT, BOUCLE TEXTURED VEST, COLOR BLOCK PUFFER JACKET, LONGLINE QUILTED JACKET, WOOL BLEND SUIT JACKET, HOODED KNIT CARDIGAN, HOODED TECHNICAL JACKET, HOUNDSTOOTH SUIT JACKET, BOMBER JACKET, HOODED TECHNICAL JACKET, HOODED TECHNICAL JACKET, WASHED EFFECT BOMBER JACKET, WASHED TECHNICAL JACKET, 100% FEATHER FILL PUFFER JACKET, PADDED BOMBER JACKET, POCKET JACKET, SLIM FIT SUIT JACKET, MIXED COLLAR JACKET, HOODED DENIM JACKET, WAXED EFFECT PLAID JACKET, WOOL BLEND FELT TEXTURE JACKET, PRINTED DENIM OVERSHIRT, STRUCTURED TWILL OVERSHIRT, COTTON OVERSHIRT, REVERSIBLE PLAID OVERSHIRT, PLAID OVERSHIRT, POCKET OVERSHIRT, 100% LINEN OVERSHIRT, PLAID OVERSHIRT, POCKET DENIM OVERSHIRT, FAUX SUEDE OVERSHIRT, PLAID OVERSHIRT, TEXTURED POCKET OVERSHIRT, POCKET OVERSHIRT, OVERSHIRT, PLAID OVERSHIRT, POCKET OVERSHIRT, ZIPPERED WOOL BLEND OVERSHIRT, GEOMETRIC JACQUARD OVERSHIRT, PAINT PRINT OVERSHIRT, PADDED CORDUROY OVERSHIRT, PLAID TIE DYE OVERSHIRT, OVERSHIRT'},
    {
        'Question': 'Find out total volume of the jackets',
        'SQLQuery': "SELECT SUM(`Sales Volume`) FROM `zara_sales_data` WHERE terms='jackets'",
        'SQLResult': 'Result of the SQL query',
        'Answer': '259468'},
    {
        'Question': 'Find out total revenue of the jackets ',
        'SQLQuery': "SELECT SUM(`Sales Volume`*price) FROM zara_sales_data WHERE terms = 'jackets'",
        'SQLResult': 'Result of the SQL query',
        'Answer': '26581815.87'},
    {
        'Question': 'Find out total revenue of the seasoned mens products ',
        'SQLQuery': "SELECT SUM(`sales volume` * price) FROM zara_sales_data WHERE section = 'MAN' AND seasonal = 'Yes'",
        'SQLResult': 'Result of the SQL query',
        'Answer': '17661874.21'},
    {
        'Question': 'Find out total non promoted Womens products prositioned At end cap',
        'SQLQuery': "SELECT count(*) FROM zara_sales_data WHERE section = 'WOMAN' AND `Product Position` = 'End-cap' AND Promotion = 'No'",
        'SQLResult': 'Result of the SQL query',
        'Answer': '6'},
    {
        'Question': "Find out total promoted seasonal Woman's products prositioned At Aisle",
        'SQLQuery': "SELECT count(*) FROM zara_sales_data WHERE `Product Position` = 'Aisle' AND section = 'WOMAN' AND `Seasonal` = 'Yes' AND `Promotion` = 'Yes'",
        'SQLResult': 'Result of the SQL query',
        'Answer': '5'}
]
