import StockTransaction from "../models/StockTransaction.js";

const getTransactions = async (req, res) => {
  const transactions = await StockTransaction.findAll({
    limit: 10,
  });
  res.send({ transactions: transactions });
};

export { getTransactions };
