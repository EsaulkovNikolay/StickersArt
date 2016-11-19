CREATE TABLE "Client" (
	"Client_ID" serial NOT NULL,
	"First_Name" VARCHAR(25) NOT NULL,
	"Last_Name" VARCHAR(25) NOT NULL,
	"Email" VARCHAR(50) NOT NULL,
	"Contact_Phone" VARCHAR(50),
	"Address" VARCHAR(50),
	CONSTRAINT Client_pk PRIMARY KEY ("Client_ID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Cheques" (
	"Cheque_ID" serial NOT NULL,
	"Client_ID" serial NOT NULL,
	"Book_ID" integer NOT NULL,
	"Date" integer NOT NULL,
	"Quantity" integer NOT NULL,
	CONSTRAINT Cheques_pk PRIMARY KEY ("Cheque_ID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Stickers" (
	"Sticker_ID" serial NOT NULL,
	"Picture" VARCHAR(255) NOT NULL UNIQUE,
	CONSTRAINT Stickers_pk PRIMARY KEY ("Sticker_ID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Stickerbooks" (
	"Book_ID" serial(255) NOT NULL,
	"Material" serial(30) NOT NULL,
	CONSTRAINT Stickerbooks_pk PRIMARY KEY ("Book_ID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Materials" (
	"Material_ID" integer NOT NULL,
	"Name" VARCHAR(255) NOT NULL,
	CONSTRAINT Materials_pk PRIMARY KEY ("Material_ID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Stickers_In_Stickerbooks" (
	"Book_ID" integer NOT NULL,
	"Sticker_ID" integer NOT NULL
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Prices" (
	"Book_ID" integer NOT NULL,
	"Price" integer NOT NULL
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Passwords" (
	"Client_ID" integer NOT NULL,
	"Password" VARCHAR(255) NOT NULL
) WITH (
  OIDS=FALSE
);




ALTER TABLE "Cheques" ADD CONSTRAINT "Cheques_fk0" FOREIGN KEY ("Client_ID") REFERENCES "Client"("Client_ID");
ALTER TABLE "Cheques" ADD CONSTRAINT "Cheques_fk1" FOREIGN KEY ("Book_ID") REFERENCES "Stickerbooks"("Book_ID");


ALTER TABLE "Stickerbooks" ADD CONSTRAINT "Stickerbooks_fk0" FOREIGN KEY ("Material") REFERENCES "Materials"("Material_ID");


ALTER TABLE "Stickers_In_Stickerbooks" ADD CONSTRAINT "Stickers_In_Stickerbooks_fk0" FOREIGN KEY ("Book_ID") REFERENCES "Stickerbooks"("Book_ID");
ALTER TABLE "Stickers_In_Stickerbooks" ADD CONSTRAINT "Stickers_In_Stickerbooks_fk1" FOREIGN KEY ("Sticker_ID") REFERENCES "Stickers"("Sticker_ID");

ALTER TABLE "Prices" ADD CONSTRAINT "Prices_fk0" FOREIGN KEY ("Book_ID") REFERENCES "Stickerbooks"("Book_ID");

ALTER TABLE "Passwords" ADD CONSTRAINT "Passwords_fk0" FOREIGN KEY ("Client_ID") REFERENCES "Client"("Client_ID");

