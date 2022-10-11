# back-end

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

Send all food supply

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


## PUT


```/employees/{id_employees} donnée body json```

Replace all employee’s data

POST 

```/enclosures/ et données dans le body json```

   Create new enclosure

```/dinosaurs/{data}```

   Create new dinosaur

```/breeds/{data}```

   Create new dinosaur breed

```/food_supplies/{data}```

   Create new food type (?)

```/teams/{data}```

   Create new team

```/employees/{data}```

   Create new employee

## PATCH 

```/enclosures/{id}donnée body json```
    
Edit an enclosure


```/dinosaurs/{id} donnée body json```

Edit an dinosaur


```/breeds{id} donnée body json```

Edit a breed


```/food_supplies/{id} donnée body json```

edit a food supply


```/teams/{id} donnée body json```

Edit a team


```/employees/{id} donnée body json```

Edit an employee
