USE [master];
GO

DROP DATABASE IF EXISTS Stocks
GO

CREATE DATABASE Stocks;
GO

USE Stocks;
GO

DROP TABLE IF EXISTS tbl_StocksStreaming;
GO

CREATE TABLE tbl_StocksStreaming
(
    [datetime] DATETIME
        DEFAULT GETDATE() NOT NULL,
    stock_ticker NVARCHAR(10)
        DEFAULT 'N/A' NOT NULL,
    [stock_name] NVARCHAR(40),
    currency NVARCHAR(5),
    stock_price NUMERIC(18, 2),
);
GO

ALTER TABLE tbl_StocksStreaming
ADD CONSTRAINT pk_composite
    PRIMARY KEY
    (
        [datetime],
        stock_ticker
    )
GO
