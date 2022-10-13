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





INSERT INTO enclosures (biome, maintenance_cost )
VALUES  ('jungle', 95000),
        ('forest', 17000),
        ('forest', 6),
        ('lowland', 72000),
        ('forest', 25000),
        ('aquatic', 400);






INSERT INTO teams(team_type, vehicle_type)
VALUES      ('Intervention','helicopter'),
           ('Intervention','car'),
           ('Intervention','car'),
           ('Medical','helicopter'),
           ('Medical','car'),
           ('Medical','car'),
           ('restock','car'),
           ('restock','car'),
           ('restock','car'),
           ('Cleaning','car'),
           ('Cleaning','car'),
           ('Cleaning','car');


INSERT INTO employees(id_team, family_name, surname, phone_number, social_security_member, emergency_contact )
VALUES      (12 ,'Dupon', 'Héloïse', '0738293819', '0313834719381','0738293819'),
            (12 ,'Dupont', 'Léo', '0738293819', '0313834719381','0738293819'),
            (12 ,'Dupond', 'Célian', '0738293819', '031383471938', '0738293819' ),

            (1 ,'Dupons', 'Mariette', '0738233819', '0313834719381', '0738293819'),
            (1 ,'Duponts', 'Bernadette', '0738293819', '031383471938', '0738293819' ),
             (1 ,'Duponds', 'Isidor', '0738293819', '031383471938', '0738293819' ),

            (2 ,'Duppon', 'René', '0738293819', '031383471938', '0738293819' ),
            (2 ,'Dupport', 'Claudette', '0738293819', '031383471938', '0738293819' ),
            (2 ,'Duppond', 'Lisette', '0738293819', '031383471938', '0738293819' ),

            (3 ,'Duppons', 'Patrick', '0738293819', '031383471938', '0738293819' ),
            (3 ,'Dupponts', 'Patricia', '0738293819', '031383471938', '0738293819' ),
            (3 ,'Dupponds', 'Frank', '0738293819', '031383471938', '0738293819' ),

            (4 ,'Duipon', 'Edgard', '0738293819', '031383471938', '0738293819' ),
            (4 ,'Duipont', 'Lilianne', '0738293819', '031383471938', '0738293819' ),
            (4 ,'Dupond', 'Josselin', '0738293819', '031383471938', '0738293819' ),

            (5 ,'Duphond', 'Jean-François-Ferdinant le 3', '0738293819', '031383471938', '0738293819' ),
            (5 ,'Duphont', 'Marie-Huguette-Henriette la 2', '0738293819', '031383471938', '0738293819' ),
            (5 ,'Duhphon', 'Viviane-Justine-Viviane', '0738293819', '0313834719381', '0738293819' ),

            (6 ,'Duplomb', 'Harnold', '0738293819', '031383471938', '0738293819' ),
            (6 ,'DuSansPlomb95', 'Gasparde', '0738293819', '031383471938', '0738293819' ),

            (7 ,'Dupondpond', 'Hernest', '0738293819', '031383471938', '0738293819' ),
            (7 ,'Dupontpont', 'Marceline', '0738293819', '031383471938', '0738293819' ),

            (8 ,'Pondu', 'Martine', '0738293819', '031383471938', '0738293819' ),
            (8 ,'tonpu', 'Gaston et Octave et Oscar et Gustave', '0738293819', '031383471938', '0738293819' ),

            (9 ,'DeLaPasserelle', 'Jean-François-Antoine', '0738293819', '031383471938', '0738293819' ),
            (9 ,'d-d-d-d-duuu-dudu-du-p-p-p-p-ond', 'Didier', '0738293819', '031383471938', '0738293819' ),

            (10 ,'Dupong', 'Marcel', '0738293819', '031383471938', '0738293819' ),
            (10 ,'Duping', 'Ernestine', '0738293819', '031383471938', '0738293819' ),

            (11 ,'tiponche', 'Yvon', '0738293819', '031383471938', '0738293819' ),
            (11 ,'DuPompe', 'Yvonne', '0738293819', '031383471938', '0738293819' );


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
        ('Célian','Tyrannosaure',6,'2002-10-24','male',5,8238,2),
        ('Anthony','Diplodocus',3,'1979-07-1','female',29,15203,1),
        ('Thiery','Nyasasaurus',3,'1850-02-01','male',3,50,2),
        ('Kevin','Thyreophora',3,'2002-10-08','female',8,40283,1),
        ('Christopher','Steakosaure',3,'2001-12-12','male',9,3271,1),
        ('Lucas','Thyreophora',4,'2003-05-23','female',7,60193,1),
        ('David','Steakosaure',4,'2001-03-30','male',7,3928,3),
        ('Maxime','Diplodocus',4,'2004-10-03','female',3,13291,3),
        ('Kevine','Thyreophora',4,'2003-09-08','male',9,80201,2),
        ('Jérance','Thyreophora',3,'2007-10-13','female',10,85392,3),
        ('Mathilde','Compsognathus',2,'2006-11-28','female',1,2,3),
        ('Julien','Nyasasaurus',4,'2004-08-19','female',2,30,2),
        ('Philémon','Thyreophora',3,'2005-12-10','male',4,620294,1),
        ('Mohamed','Steakosaure',4,'2005-10-04','female',8,3912,1),
        ('Gaëtan', 'Mosasaurus', 5, '2008-10-21', 'female',17, 30281,2);