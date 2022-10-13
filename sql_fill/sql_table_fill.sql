INSERT INTO food_supplies (food_type, price)
VALUES  ('meat', 15),
        ('fish', 11),
	    ('vegetation',10);


INSERT INTO breeds (breed_name, food_eaten_daily, regime_type, era, biome_needed, price)
VALUES  ('Triceratops','40','vegetation','late cretaceous','jungle',10000),
        ('Tyrannosaure','200','meat','Late Triassic','jungle',40000),
        ('Diplodocus','180','vegetation','Late Triassic','jungle',25000),
        ('Steakosaure','30','vegetation','Jurassic','jungle',7000),
        ('Compsognathus','5','meat','Tithonian','jungle',300),
        ('Mosasaurus','5','fish','late cretaceous','jungle',300),
        ('Nyasasaurus','15','fish','Middle Triassic', 'jungle', 20000),
        ('Allausore','15','meat','Middle Triassic', 'jungle', 20000),
        ('Thyreophora','15','meat','Jurassic', 'jungle', 20000);





INSERT INTO enclosures (id_enclosure, biome, maintenance_cost )
VALUES  (0,'jungle', 95000),
        (1,'forest', 17000),
        (2,'forest', 6),
        (3,'lowland', 72000),
        (4,'forest', 25000),
        (5,'aquatic', 400);






INSERT INTO teams(id_team , team_type, vehicle_type )
VALUES      (0,'Intervention','helicopter'),
           (1,'Intervention','car'),
           (2,'Intervention','car'),
           (3,'Medical','helicopter'),
           (4,'Medical','car'),
           (5,'Medical','car'),
           (6,'restock','car'),
           (7,'restock','car'),
           (8,'restock','car'),
           (9,'Cleaning','car'),
           (10,'Cleaning','car'),
           (11,'Cleaning','car');


INSERT INTO employees(id_employee_member, id_team, family_name, surname, phone_number, social_security_member, emergency_contact )
VALUES      (0,0 ,'Dupon', 'Héloïse', '0738293819', '0313834719381','0738293819'),
            (1,0 ,'Dupont', 'Léo', '0738293819', '0313834719381','0738293819'),
            (2,0 ,'Dupond', 'Célian', '0738293819', '031383471938', '0738293819' ),

            (3,1 ,'Dupons', 'Mariette', '0738233819', '0313834719381', '0738293819'),
            (4,1 ,'Duponts', 'Bernadette', '0738293819', '031383471938', '0738293819' ),
             (5,1 ,'Duponds', 'Isidor', '0738293819', '031383471938', '0738293819' ),

            (6,2 ,'Duppon', 'René', '0738293819', '031383471938', '0738293819' ),
            (7,2 ,'Dupport', 'Claudette', '0738293819', '031383471938', '0738293819' ),
            (8,2 ,'Duppond', 'Lisette', '0738293819', '031383471938', '0738293819' ),

            (9,3 ,'Duppons', 'Patrick', '0738293819', '031383471938', '0738293819' ),
            (10,3 ,'Dupponts', 'Patricia', '0738293819', '031383471938', '0738293819' ),
            (11,3 ,'Dupponds', 'Frank', '0738293819', '031383471938', '0738293819' ),

            (12,4 ,'Duipon', 'Edgard', '0738293819', '031383471938', '0738293819' ),
            (13,4 ,'Duipont', 'Lilianne', '0738293819', '031383471938', '0738293819' ),
            (14,4 ,'Dupond', 'Josselin', '0738293819', '031383471938', '0738293819' ),

            (15,5 ,'Duphond', 'Jean-François-Ferdinant le 3', '0738293819', '031383471938', '0738293819' ),
            (16,5 ,'Duphont', 'Marie-Huguette-Henriette la 2', '0738293819', '031383471938', '0738293819' ),
            (17,5 ,'Duhphon', 'Viviane-Justine-Viviane', '0738293819', '0313834719381', '0738293819' ),

            (18,6 ,'Duplomb', 'Harnold', '0738293819', '031383471938', '0738293819' ),
            (19,6 ,'DuSansPlomb95', 'Gasparde', '0738293819', '031383471938', '0738293819' ),

            (20,7 ,'Dupondpond', 'Hernest', '0738293819', '031383471938', '0738293819' ),
            (21,7 ,'Dupontpont', 'Marceline', '0738293819', '031383471938', '0738293819' ),

            (22,8 ,'Pondu', 'Martine', '0738293819', '031383471938', '0738293819' ),
            (23,8 ,'tonpu', 'Gaston et Octave et Oscar et Gustave', '0738293819', '031383471938', '0738293819' ),

            (24,9 ,'DeLaPasserelle', 'Jean-François-Antoine', '0738293819', '031383471938', '0738293819' ),
            (25,9 ,'d-d-d-d-duuu-dudu-du-p-p-p-p-ond', 'Didier', '0738293819', '031383471938', '0738293819' ),

            (26,10 ,'Dupong', 'Marcel', '0738293819', '031383471938', '0738293819' ),
            (27,10 ,'Duping', 'Ernestine', '0738293819', '031383471938', '0738293819' ),

            (28,11 ,'tiponche', 'Yvon', '0738293819', '031383471938', '0738293819' ),
            (29,11 ,'DuPompe', 'Yvonne', '0738293819', '031383471938', '0738293819' );


INSERT INTO teams_organisations (id_enclosure, id_team )
VALUES  (0,1),
        (1,2),
        (2,0),
        (3,2),
        (4,0),
        (5,2),
        (0,3),
        (1,4),
        (2,5),
        (3,4),
        (4,3),
        (5,5),
        (0,6),
        (1,6),
        (2,7),
        (3,7),
        (4,8),
        (5,8),
        (0,9),
        (1,9),
        (2,10),
        (3,10),
        (4,11),
        (5,11);



INSERT INTO dinosaurs(dinosaur_name, breed_name, id_enclosure, creation_date, gender, height, weight, id_employees)
VALUES  ('Héloïse','Compsognathus',2,'2002-01-06','female',1,3,2),
        ('Léo','Allausore',1,'2003-12-04','male',4,5183,1),
        ('Célian','Tyrannosaure',0,'2002-10-24','male',5,8238,2),
        ('Anthony','Diplodocus',3,'1979-07-1','female',29,15203,1),
        ('Thiery','Nyasasaurus',3,'1850-02-01','male',3,50,2),
        ('Kevin','Thyreophora',3,'2002-10-08','female',8,40283,1),
        ('Christopher','Steakosaure',3,'2001-12-12','male',9,3271,1),
        ('Lucas','Thyreophora',4,'2003-05-23','female',7,60193,1),
        ('David','Steakosaure',4,'2001-03-30','male',7,3928,0),
        ('Maxime','Diplodocus',4,'2004-10-03','female',3,13291,0),
        ('Kevine','Thyreophora',4,'2003-09-08','male',9,80201,2),
        ('Jérance','Thyreophora',3,'2007-10-13','female',10,85392,0),
        ('Mathilde','Compsognathus',2,'2006-11-28','female',1,2,0),
        ('Julien','Nyasasaurus',4,'2004-08-19','female',2,30,2),
        ('Philémon','Thyreophora',3,'2005-12-10','male',4,620294,1),
        ('Mohamed','Steakosaure',4,'2005-10-04','female',8,3912,1),
        ('Gaëtan', 'Mosasaurus', 5, '2008-10-21', 'female',17, 30281,2);