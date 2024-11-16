import express from "express";
import { getTransactions } from "../controllers/transactions-controller.js";

const transactionsRouter = express.Router();

transactionsRouter.get("/", getTransactions);

export { transactionsRouter };
