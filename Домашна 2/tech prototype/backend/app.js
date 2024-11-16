import { app } from "./config/app-config.js";
import { connect } from "./config/db-config.js";
import dotenv from "dotenv";

dotenv.config();

const port = process.env.PORT || 3000;

connect().then(() => {
  app.listen(port, () => {
    console.log(`[server]: Server is running at http://localhost:${port}`);
  });
});
