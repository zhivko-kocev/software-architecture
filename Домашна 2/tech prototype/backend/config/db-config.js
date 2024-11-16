import { Sequelize } from "sequelize";
import dotenv from "dotenv";

dotenv.config();

const sequelize = new Sequelize({
  dialect: "sqlite",
  storage: process.env.STORAGE,
  logging: false,
});

const connect = async () => {
  try {
    await sequelize.authenticate();
    console.log("Database connection has been established successfully!");
    await sequelize.sync();
    console.log("Models synced successfully!");
  } catch (error) {
    console.log(error);
  }
};

export { connect, sequelize };
