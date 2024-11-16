import express from "express";
import cors from "cors";
import { transactionsRouter } from "../routes/transaction-route.js";

const app = express();

app.use(express.json());
app.use(cors());

app.use("/api/transactions", transactionsRouter);

app.get("/", (req, res) => {
  res.send("Hello from my api :D");
});

export { app };
