
CREATE TABLE breed
(
    breed_name       TEXT,
    food_eaten_daily INT,
    regime_type      VARCHAR(100),
    era              INT,
    biome_needed     VARCHAR(100),
    price            INT,
    PRIMARY KEY (breed_name),
    FOREIGN KEY (regime_type) REFERENCES food_supply (food_type)
);



CREATE TABLE dinosaur
(
    dinosaur_name TEXT,
    breed_name    TEXT,
    id_enclosure  INT,
    creation_date DATE,
    gender        TEXT,
    height        INT,
    weigh         INT,
    id_employees      INT,
    PRIMARY KEY (dinosaur_name),
    FOREIGN KEY (breed_name) REFERENCES breed (breed_name),
    FOREIGN KEY (id_enclosure) REFERENCES enclosure(id_enclosure),
    FOREIGN KEY (id_employees) REFERENCES employees(id_employee_member)

);



CREATE TABLE food_supply
(
    food_type  VARCHAR(100),
    price INT,
    PRIMARY KEY (food_type)
);

CREATE TABLE employees
(
    id_employee_member        INT,
    id_team                INT,
    family_name            VARCHAR(100),
    surname                VARCHAR(100),
    phone_number           INT,
    social_security_member INT,
    emergency_contact      VARCHAR(100),
    PRIMARY KEY (id_employee_member),
    FOREIGN KEY (id_team) REFERENCES team (id_team)
);

CREATE TABLE team (
    id_team INT,
    team_type INT,
    vehicle_type TEXT,
    PRIMARY KEY (id_team)
);


CREATE TABLE enclosure
(
    id_enclosure     INT,
    type             VARCHAR(100),
    biome            VARCHAR(100),
    id_team          VARCHAR(100),
    maintenance_cost VARCHAR(100),
    PRIMARY KEY (id_enclosure),
    FOREIGN KEY (id_team) REFERENCES team(id_team)
);



CREATE TABLE team_organisation(
    id_enclosure INT,
    id_team INT,

    PRIMARY KEY (id_team),
    PRIMARY KEY (id_enclosure),
    FOREIGN KEY (id_team) REFERENCES team(id_team),
    FOREIGN KEY (id_enclosure) REFERENCES enclosure(id_enclosure)
);