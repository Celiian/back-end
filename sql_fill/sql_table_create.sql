#DROP TABLE teams, enclosures, employees, dinosaurs, breeds, food_supplies, teams_organisations;

CREATE TABLE teams (
    id_team INT auto_increment,
    team_type VARCHAR(100),
    vehicle_type VARCHAR(100),
    PRIMARY KEY (id_team)
);


CREATE TABLE enclosures
(
    id_enclosure     INT auto_increment,
    biome            VARCHAR(100),
    maintenance_cost VARCHAR(100),
    PRIMARY KEY (id_enclosure)
);



CREATE TABLE food_supplies
(
    food_type  VARCHAR(100),
    price INT,
    PRIMARY KEY (food_type)
);

CREATE TABLE breeds
(
    breed_name       VARCHAR(100),
    food_eaten_daily INT,
    regime_type      VARCHAR(100),
    era              VARCHAR(100),
    biome_needed     VARCHAR(100),
    price            INT,
    PRIMARY KEY (breed_name),
    FOREIGN KEY (regime_type) REFERENCES food_supplies (food_type)
);



CREATE TABLE employees
(
    id_employee_member        INT auto_increment,
    id_team                INT,
    family_name            VARCHAR(100),
    surname                VARCHAR(100),
    phone_number            VARCHAR(100),
    social_security_number  VARCHAR(100),
    emergency_contact      VARCHAR(100),
    PRIMARY KEY (id_employee_member),
    FOREIGN KEY (id_team) REFERENCES teams (id_team)
);


CREATE TABLE dinosaurs
(
    dinosaur_name VARCHAR(100),
    breed_name    VARCHAR(100),
    id_enclosure  INT,
    creation_date DATE,
    gender        VARCHAR(100),
    height        INT,
    weight         INT,
    id_employees      INT,
    PRIMARY KEY (dinosaur_name),
    FOREIGN KEY (breed_name) REFERENCES breeds (breed_name),
    FOREIGN KEY (id_enclosure) REFERENCES enclosures(id_enclosure),
    FOREIGN KEY (id_employees) REFERENCES employees(id_employee_member)

);


CREATE TABLE teams_organisations(
    id_enclosure INT,
    id_team INT,

    PRIMARY KEY (id_team, id_enclosure),
    FOREIGN KEY (id_team) REFERENCES teams(id_team),
    FOREIGN KEY (id_enclosure) REFERENCES enclosures(id_enclosure)
);