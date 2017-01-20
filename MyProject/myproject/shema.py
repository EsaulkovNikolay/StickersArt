from sqlalchemy import create_engine,Table,Column,MetaData,Integer,String,ForeignKey,Date,Float,Boolean
import os

class Data_Base:
    def __init__(self):
        self.engine = create_engine("sqlite:///some.db")
        self.metaData=MetaData(bind=self.engine)

        self.Client_Table=Table('Client', self.metaData,
                            Column('Client_ID', Integer, primary_key=True,autoincrement=True),
                            Column('First_Name', String),
                            Column('Last_Name', String),
                            Column('Email', String),
                            Column('Contact_Phone', String),
                            Column('Address', String),
                            Column('Password', String,nullable=False)
                            )

        self.Cheque_Table=Table('Cheque',self.metaData,
                            Column('Cheque_ID',Integer,primary_key=True,autoincrement=True),
                            Column('Client_ID',Integer,ForeignKey('Client.Client_ID'),nullable=False),
                            Column('Book_ID',Integer,ForeignKey('Stickerbook.Book_ID'),nullable=False),
                            Column('Date',String),#!!!
                            Column('Quantity',Integer,nullable=False),
                            Column('Complited',Boolean,default=False)
                            )

        self.Sticker_Table=Table('Sticker',self.metaData,
                            Column('Sticker_ID',Integer,primary_key=True,autoincrement=True),
                            Column('Picture',String,unique=True),
                            )

        self.StickerBook_Table=Table('Stickerbook',self.metaData,
                                Column('Book_ID',Integer,primary_key=True,autoincrement=True),
                                Column('Material',Integer,ForeignKey('Material.Material_ID'))
                                )

        self.Material_Table=Table('Material',self.metaData,
                             Column('Material_ID',Integer,primary_key=True,autoincrement=True),
                             Column('Name',String),
                             Column('Price',Integer,nullable=False)
                             )

        self.Stickers_In_StickerBook_Table=Table('Stickers_In_Stickerbook',self.metaData,
                                            Column('Book_ID',Integer,nullable=False),
                                            Column('Sticker_ID',Integer,nullable=False)
                                            )

        self.Price_Table=Table('Price',self.metaData,
                          Column('Book_ID',Integer,ForeignKey('Stickerbook.Book_ID'),nullable=False),
                          Column('Price',Float,nullable=False))



        if not self.engine.dialect.has_table(self.engine, 'имя таблицы'):
            self.metaData.create_all(self.engine)

