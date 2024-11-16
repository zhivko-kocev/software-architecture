import { sequelize } from "../config/db-config.js";
import { DataTypes } from "sequelize";

const StockTransaction = sequelize.define(
  "StockTransaction",
  {
    id: {
      type: DataTypes.INTEGER,
      primaryKey: true,
      autoIncrement: true,
    },
    code: {
      type: DataTypes.STRING,
      allowNull: true,
    },
    date: {
      type: DataTypes.DATE,
      allowNull: true,
    },
    last_transaction: {
      type: DataTypes.STRING,
      allowNull: true,
    },
    max_transaction: {
      type: DataTypes.STRING,
      allowNull: true,
    },
    min_transaction: {
      type: DataTypes.STRING,
      allowNull: true,
    },
    avg_transaction: {
      type: DataTypes.STRING,
      allowNull: true,
    },
    cash_flow_per: {
      type: DataTypes.STRING,
      allowNull: true,
    },
    quantity: {
      type: DataTypes.STRING,
      allowNull: true,
    },
    cash_flow: {
      type: DataTypes.STRING,
      allowNull: true,
    },
  },
  {
    tableName: "StockTransaction",
    timestamps: false,
  }
);

export default StockTransaction;
