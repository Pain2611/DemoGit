USE master
GO
CREATE DATABASE HSBNThanManTinh
GO
USE HSBNThanManTinh
GO
DROP DATABASE HSBNThanManTinh
GO

CREATE TABLE TaiKhoan
(
	TenDN varchar(50) primary key not null,
	MatKhau varchar(50),
	SDT varchar(20)
)

CREATE TABLE BenhAn
(
	TenDN varchar(50),
	Ngay date,
	Tuoi float,
	bp float,
	sg float,
	al float,
	su float,
	rbc varchar(50),
	pc varchar(50),
	pcc varchar(50),
	ba varchar(50),
	bgr float,
	bu float,
	sc float,
	sod float,
	pot float,
	hemo float,
	pcv int,
	wc int,
	rc float,
	htn varchar(20),
	dm varchar(10),
	cad varchar(10),
	appet varchar(20),
	pe varchar(10),
	ane varchar(10),
	classification varchar(20),
	KetQuaChuanDoan varchar(225),

	constraint fk_tk_ba foreign key(TenDN) references TaiKhoan(TenDN)
)
set dateformat dmy
insert into BenhAn (TenDN, Ngay, Tuoi, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane)
values
(N'Hung', '05/05/2002', 21.0, 80.0, 1.02, 1.0, 0.0, 'normal', 'abnormal', 'present', 'notpresent', 117.0, 56.0, 3.8, 111.0, 2.5, 11.2, 32.0, 6700.0, 3.9, 'yes', 'no', 'no', 'poor', 'yes', 'yes')

insert into TaiKhoan
values
(N'Admin', N'123', N'0123456789'),
(N'Hung', N'123', N'0123456788'),
(N'Phong', N'123', N'0123456787')

select * from BenhAn

