from sqlalchemy import create_engine,Table,Column,MetaData,Integer,String,ForeignKey,Date,Float
import os

if os.path.exists("some.db"):
    os.remove("some.db")

engine = create_engine("sqlite:///some.db")
metaData=MetaData()

Client_Table=Table('Client', metaData,
                    Column('Client_ID', Integer, primary_key=True),
                    Column('First_Name', String),
                    Column('Last_Name', String),
                    Column('Email', String),
                    Column('Contact_Phone', String),
                    Column('Address', String),
                    Column('Password', String,nullable=False)
                    )

Cheque_Table=Table('Cheque',metaData,
                    Column('Cheque_ID',Integer,primary_key=True),
                    Column('Client_ID',Integer,ForeignKey('Client.Client_ID'),nullable=False),
                    Column('Book_ID',Integer,ForeignKey('Stickerbooks.Book_ID'),nullable=False),
                    Column('Date',Date,nullable=False),
                    Column('Quantity',Integer,nullable=False)
                    )

Sticker_Table=Table('Sticker',metaData,
                    Column('Sticker_ID',Integer,primary_key=True),
                    Column('Picture',String,unique=True),
                    )

StickerBook_Table=Table('Stickerbook',metaData,
                        Column('Book_ID',Integer,primary_key=True),
                        Column('Material',Integer,ForeignKey('Material.Material_ID'))
                        )

Material_Table=Table('Material',metaData,
                     Column('Material_ID',Integer,primary_key=True),
                     Column('Name',String)
                     )


Stickers_In_StickerBook_Table=Table('Stickers_In_Stickerbook',metaData,
                                    Column('Book_ID',Integer,nullable=False),
                                    Column('Sticker_ID',Integer,nullable=False)
                                    )

Price_Table=Table('Price',metaData,
                  Column('Book_ID',Integer,ForeignKey('Stickerbook.Book_ID'),nullable=False),
                  Column('Price',Float,nullable=False))