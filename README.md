# back-end Dinomania

## GET

``` /enclosures```

Send all existing enclosures

``` /enclosures/{id}```

Send one enclosure

``` /enclosures/{id}/dinosaurs ```

Send all dinosaurs of one enclosure

```/enclosures/{id}/teams```

Send all teams affected to an enclosure

```/enclosures/{id}/teams/employees```

Send all employees of an enclosure

```/teams```

Send all existing teams

```/teams/{id}```

Send one team

```/teams/{id}/employees```

Send all employees of a team

```/teams/{id}/enclosure```

Send all enclosure assigned to a team

```/employees```

Send all employees

```/employees/{id}```

Send one employee

```/food_supplies```

Send all food supplies

```/food_supplies/{id}```

Send on food supply

```/dinosaurs```

Send all dinosaurs alive

```/dinosaurs/{id}```

Send one dinosaur

```/dinosaurs/{id}/breed```

Send the breed of a dinosaur

```/breeds```

Send all breeds

```/breeds/{id}```

Send one breed

```/teams_organisation```

Send all teams_organisation

```/teams_organisation/{id}```

Send one teams_organisation

## PUT
All data are passed in the body

```/employees/{id_employees}```

Replace all employee’s data

## POST
All data are passed in the body

```/enclosures/```

Create new enclosure

```/dinosaurs/```

Create new dinosaur

```/breeds/```

Create new dinosaur breed

```/food_supplies/```

Create new food type

```/teams/```

Create new team

```/employees/```

Create new employee

```/teams_organisation/```

Create one teams_organisation

## PATCH
All data are passed in the body

```/enclosures/{id}```

Edit an enclosure

```/dinosaurs/{id}```

Edit an dinosaur

```/breeds{id}```

Edit a breed

```/food_supplies/{id```

edit a food supply

```/teams/{id}```

Edit a team

```/employees/{id}```

Edit an employee

```/teams_organisation/{id}```

Edit one teams_organisation

## DELETE

```/enclosures/{id}```

Delete new enclosure

```/dinosaurs/{id}```

Delete new dinosaur

```/breeds/{id}```

Delete new dinosaur breed

```/food_supplies/{id}```

Delete new food type

```/teams/{id}```

Delete new team

```/employees/{id}```

Delete new employee

```/teams_organisation/{id}```

Delete one teams_organisation
