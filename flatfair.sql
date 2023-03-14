CREATE DATABASE flatfair WITH ENCODING 'UTF8';

CREATE TYPE org_level AS ENUM ('client', 'division', 'area', 'branch');

CREATE TABLE OrganisationUnit (
	name 	      TEXT unique,
	id	          INT PRIMARY KEY unique,
    has_fixed_membership    boolean default false,
	fixed_membership_fee    INT default 0,
    level org_level,
    parent        INT REFERENCES OrganisationUnit(id)
);

INSERT INTO OrganisationUnit(name, parent, id, level, has_fixed_membership, fixed_membership_fee) VALUES
('client_a', NULL, 01, 'client', false, 0), 
('division_a', 01, 011, 'division', false, 0), 
('division_b', 01, 012, 'division', TRUE, 35000), 
('area_a', 011, 0111, 'area', TRUE, 45000), 
('area_b', 011, 0112, 'area', FALSE, 0), 
('area_c', 012, 0121, 'area', TRUE, 45000),  
('area_d', 012, 0122, 'area', FALSE, 0), 
('branch_a', 0111, 01111, 'branch', NULL, NULL),  
('branch_b', 0111, 01112, 'branch', false, 0),  
('branch_c', 0111, 01113, 'branch', false, 0),
('branch_d', 0111, 01114, 'branch', NULL, NULL),
('branch_e', 0112, 01121, 'branch', false, 0),
('branch_f', 0112, 01122, 'branch', false, 0),
('branch_g', 0112, 01123, 'branch', false, 0), 
('branch_h', 0112, 01124, 'branch', false, 0), 
('branch_i', 0121, 01211, 'branch', false, 0),
('branch_j', 0121, 01212, 'branch', false, 0), 
('branch_k', 0121, 01213, 'branch', true, 25000),
('branch_l', 0121, 01214, 'branch', false, 0), 
('branch_m', 0122, 01221, 'branch', null, null), 
('branch_n', 0122, 01222, 'branch', false, 0),
('branch_o', 0122, 01223, 'branch', false, 0),
('branch_p', 0122, 01224, 'branch', false, 0);

select * from OrganisationUnit



