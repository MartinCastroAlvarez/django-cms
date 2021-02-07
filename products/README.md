# Product Module
This directory contains the definition of Products, CRUD operations and views. 

### Model
- *Name*. Name of the Product.
- *Description*. Description of the Product.
- *Nutritional Values*. Each product can have multiple nutritional values. The product cannot have the same nutritional value multiple times.
- *Status*. Either ACTIVE or INACTIVE.

### Examples

##### Perfect Fries
- *Name*: Perfect Fries
- *Description*: The famous French fries you have heard so much about are the best, the most crispy, the ones with the most flavor, if you try them you will understand the reason for their fame.
- *Status*: ACTIVE.
    - *Nutritional Values*:
    - Weight (g): 159.00
    - Energetic value (Kcal): 389.60
    - Proteins (g): 5.40
    - Carbohydrates (g): 102.10

##### Big Mag
- *Name*: Big Mag
- *Description*: Big Mag will always be our number one. Succulent grilled beef of excellent quality, fresh tomato and lettuce, soft onion and tasty pickles accompanied with mayonnaise and ketchup. Do not forget the soft bread with seeds, which together make a hamburger with a unique flavor and which you would recognize with your eyes closed.
- *Status*: ACTIVE
- *Nutritional Values*:
    - Weight (g): 278.60
    - Energetic value (Kcal): 640.30
    - Proteins (g): 26.70
    - Carbohydrates (g): 51.30
    - Salt (mg) 2321.00

##### Nuka-Cola
- *Name*: Nuka-Cola
- *Description*: The perfect complement to all meals, enjoy the authentic taste of Nuka-Cola.
- *Status*: INACTIVE
- *Nutritional Values*:
    - Weight (g): 500.00
    - Energetic value (Kcal): 210.00
    - Carbohydrates (g): 53.00
    - Sugar (g): 53.00

### Business Logic
- List the products. Inside the list you should display the name of the product, as well as the nutritional values of that product. Allow the user to filter the products. The user should be able to filter the products by their name, as well as their status.
- Create the products.
- Update the products.
- View the details of the products.
- Delete the products.
